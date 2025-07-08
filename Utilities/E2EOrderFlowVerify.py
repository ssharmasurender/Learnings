import asyncio
import threading
from time import sleep

import websockets
import requests
import json
import time

from src.run_books.common.config import AUTH_TOKEN
#
# APP_API_SERVER=""
# APP_WEB_SOCKET_SERVER=""
AUTH_TOKEN="eyJhbGciOiJIUzI1NiJ9.eyJleHAiOjQ4OTU2MjgwMTksInNlc3Npb25JZCI6ImJlMGQ5N2FlLTE1N2ItNDcwZC1hNWJhLWU1MDMzNDg4NjcxMSIsImNvaW5kY3hfaWQiOiI0NmI4M2IyNC1lZTllLTExZWYtODk4ZC03Mzk1MzNlNmIzNGEiLCJ1c2VyX2lkIjoiNDZiODNiMjQtZWU5ZS0xMWVmLTg5OGQtNzM5NTMzZTZiMzRhIiwicyI6IndlYiIsInVzZXJBZ2VudCI6Ik1vemlsbGEvNS4wIChNYWNpbnRvc2g7IEludGVsIE1hYyBPUyBYIDExXzJfMykgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzg5LjAuNDM4OS4xMjggU2FmYXJpLzUzNy4zNiJ9.Iz7g1LW4Qr7XALPWcD0f6WsEbOO4TA5f6TTz-IRJsYo"
X_MBX_API_KEY="performance_binance_future_account_2"
MOCK_NEW_ORDER_ID="perf_141"

MOCK_WS_FUTURES_PRIVATE_HOST="wss://stream-perf-mock-ws-testnet-publisher-private-futures.dcxstage.com"
MOCK_WS_FUTURES_PUBLIC_HOST="wss://stream-perf-mock-ws-testnet-publisher-private-futures.dcxstage.com"
APP_API_HOST="https://performance-api.dcxstage.com"
MOCK_API_HOST="https://performance-mock-exchange.dcxstage.com"
APP_WSS_HOST="wss://stream-performance.dcxstage.com"

APP_ORDER_CREATE_API = {
    "url": f"{APP_API_HOST}/api/v1/derivatives/futures/orders",
    "ConnectMessage": "Connecting to APP_ORDER_CREATE_API",
    "Headers": {'X-Source': 'flutter_ios',
  'Content-Type': 'application/json',
  'Authorization': f'{AUTH_TOKEN}'},
    "Body": {
    "order": {
        "side": "buy",
        "pair": "B-BTC_USDT",
        "leverage": 3,
        "total_quantity": 3,
        "position_margin_type": "isolated",
        "margin_currency_short_name": "USDT",
        "order_type": "market_order"
    }
}
}

MOCK_ORDER_CREATE_API = {
    "url": f"{MOCK_API_HOST}/fapi/v1/order",
    "ConnectMessage": "Connecting to MOCK_ORDER_CREATE_API",
    "Headers": {'X-MBX-APIKEY': f'{X_MBX_API_KEY}',
  'Content-Type': 'application/json'},
    "Body": {
    "symbol": "ETHUSDT",
    "side": "BUY",
    "type": "MARKET",
    "quantity": 0.1,
    "newClientOrderId": f"{MOCK_NEW_ORDER_ID}"
}
}

MOCK_GET_ORDER_API = {
    "url": f"{MOCK_API_HOST}/fapi/v1/order?origClientOrderId={MOCK_NEW_ORDER_ID}",
    "ConnectMessage": "Connecting to MOCK_GET_ORDER_API",
    "Headers": {'X-MBX-APIKEY': f'{X_MBX_API_KEY}'},
    "Body": {}
}

MOCK_FUTURES_POST_LISTEN_KEY_API = {
    "url": f"{MOCK_API_HOST}/fapi/v1/listenKey",
    "ConnectMessage": "Connecting to MOCK_FUTURES_GET_LISTEN_KEY_API",
    "Headers": {'X-MBX-APIKEY': f'{X_MBX_API_KEY}'},
    "Body": {}
}

APP_ORDER_STATUS_API = {
    "url": f"{APP_API_HOST}/api/v1/derivatives/futures/orders?page=1&size=1",
    "ConnectMessage": "Connecting to APP_ORDER_STATUS_API",
    "Headers": {'X-Source': 'flutter_ios',
  'Content-Type': 'application/json',
  'Authorization': f'{AUTH_TOKEN}'},
    "Body": {}
}

APP_WEBSOCKET = {
    "url": f"{APP_WSS_HOST}/socket.io/?transport=websocket&EIO=10",
    "ConnectMessage": '42["join",{"channelName":"coindcx", "authHeader": "'+AUTH_TOKEN+'"},{"x-source":"web"}]',
    "Headers": {},
    "Body": {}
}

MOCK_FUTURES_PRIVATE_EVENTS_WEBSOCKET = {
    "url": f"{MOCK_WS_FUTURES_PRIVATE_HOST}/binanceFuturesWs/<KEY>",
    "ConnectMessage": "Connecting to MOCK_FUTURES_PRIVATE_EVENTS_WEBSOCKET_URL",
    "Headers": {},
    "Body": {}
}

# Global counters
websocket1_trade_count = 0
listenkey_trade_count = 0


async def connect_websocket_app( trade_counter=0, timeout=15):
    """Connects to a WebSocket and counts received messages."""
    async with websockets.connect(APP_WEBSOCKET.get('url')) as ws:
        # start_time = time.time()
        print("Connect to "+ APP_WEBSOCKET.get('url'))
        await ws.send(APP_WEBSOCKET.get('ConnectMessage'))
        print("Sent Message "+ APP_WEBSOCKET.get('ConnectMessage'))

        start_time = asyncio.get_event_loop().time()

        while True:
            # Check if the stop time has been reached
            if asyncio.get_event_loop().time() - start_time > timeout:
                print(f"Stopping WebSocket connection after {timeout} seconds")
                print(f"Total trades on WebSocket 1: {trade_counter}")
                break

            try:
                # Receive message from server
                # print("waiting for message read AppSockets")
                response = await asyncio.wait_for(ws.recv(), timeout=5)
                trade_counter=trade_counter+1
                print(f'received: {response}')
                # logging.info(f"Received: {response}")
            except asyncio.TimeoutError:
                # Handle cases where no message is received within timeout
                print("No message received within 5 seconds")
                # break
            except websockets.exceptions.ConnectionClosedError:
                # print("Connection Closed")
                print(f"Closing WebSocket APP websockets, Total Trades: {trade_counter}")
                break

async def connect_websocket(url, trade_counter=0, timeout=15):
    """Connects to a WebSocket and counts received messages."""
    async with websockets.connect(url) as ws:
        start_time = asyncio.get_event_loop().time()
        while True:
            if asyncio.get_event_loop().time() - start_time > timeout:
                print(f"Stopping WebSocket connection after {timeout} seconds")
                # print(f"Total trades on WebSocket 1: {trade_counter[0]}")
                print(f"Total trades on ListenKey WebSocket: {trade_counter}")
                break
            try:
                # print("waiting for message read :"+url)
                msg = await asyncio.wait_for(ws.recv(), timeout=5)
                print(f"Received message on {msg}")
                trade_counter = trade_counter + 1
            except asyncio.TimeoutError:
                print("No message received within 5 seconds")
                # break
                # break  # Stop if no new messages for 1 second
            except websockets.exceptions.ConnectionClosedError:
                print(f"Closing WebSocket APP websockets, Total Trades: {trade_counter}")
                break

def place_order_on_app():
    """Places an order and returns the order ID."""
    payload = APP_ORDER_CREATE_API.get("Body")
    response = requests.post(APP_ORDER_CREATE_API.get("url"), json=payload,headers=APP_ORDER_CREATE_API.get("Headers"))
    response.raise_for_status()
    order_id = response.json()[0].get("id")
    print(f"Order placed: {order_id}")
    return order_id


def check_order_status_on_mock(order_id):
    """Checks if the order is present on mock."""
    url = MOCK_GET_ORDER_API.get('url').replace(MOCK_NEW_ORDER_ID, order_id)
    print(url)
    response = requests.get(url, headers=MOCK_GET_ORDER_API.get("Headers"))
    print(MOCK_GET_ORDER_API.get("Headers"))
    response.raise_for_status()
    status = response.json().get("o").get("x")
    if status in ["FILLED", "PARTIALLY_FILLED"]:
        print(f"Order {order_id} found on mock with status: {status}")
        return status
        # time.sleep(2)  # Poll every 2 seconds


def get_mock_listen_key():
    """Retrieves a listen key for WebSocket subscription."""
    response = requests.post(MOCK_FUTURES_POST_LISTEN_KEY_API.get("url"), headers=MOCK_FUTURES_POST_LISTEN_KEY_API.get("Headers"))
    response.raise_for_status()
    listen_key = response.json().get("listenKey")
    print(f"Listen Key received: {listen_key}")
    return listen_key


def check_order_status_on_app(order_id):
    """Checks if the order is marked as filled in the app."""
    url = f"{APP_ORDER_STATUS_API.get('url')}"
    # while True:
    response = requests.get(url, headers=APP_ORDER_STATUS_API.get("Headers"))
    response.raise_for_status()
    status = response.json()[0].get("status")
    if status == "filled":
        print(f"Order {order_id} is FILLED in the app.")
        return
    time.sleep(2)


async def main():
    global websocket1_trade_count, listenkey_trade_count

    # Step 1: Connect to WebSocket 1
    websocket1_counter = [0]
    task1 = await asyncio.create_task(connect_websocket_app( websocket1_counter))
    listen_key = get_mock_listen_key()

    # Step 2: Connect to ListenKey WebSocket
    listenkey_counter = [0]
    listen_websocket_url = MOCK_FUTURES_PRIVATE_EVENTS_WEBSOCKET.get('url').replace("<KEY>", listen_key)
    task2 = await asyncio.create_task(connect_websocket(listen_websocket_url, listenkey_counter))
    # Step 2: Place order
    sleep(2)
    order_id = place_order_on_app()
    sleep(3)
    # Step 3: Check order on Mock
    check_order_status_on_mock(order_id)

    # Step 4: Get Listen Key
    # Step 6: Check order status on App
    check_order_status_on_app(order_id)

    # Wait for both WebSockets to complete
    await asyncio.gather(task1, task2)

    # Print trade counts
    print(f"Total trades on WebSocket 1: {websocket1_counter[0]}")
    print(f"Total trades on ListenKey WebSocket: {listenkey_counter[0]}")

def run_websocket_app():
    asyncio.run(connect_websocket_app(0))


def run_websocket_listenkey(url):
    asyncio.run(connect_websocket(url, 0))

def main_2():
    listen_key = get_mock_listen_key()
    listen_websocket_url = MOCK_FUTURES_PRIVATE_EVENTS_WEBSOCKET.get('url').replace("<KEY>", listen_key)

    thread1 = threading.Thread(target=run_websocket_app)
    thread2 = threading.Thread(target=run_websocket_listenkey, args=(listen_websocket_url,))

    thread1.start()
    thread2.start()
    sleep(2)
    order_id = place_order_on_app()
    sleep(3)
    # Step 3: Check order on Mock
    check_order_status_on_mock(order_id)

    # Step 4: Get Listen Key
    # Step 6: Check order status on App
    check_order_status_on_app(order_id)
    thread1.join()
    thread2.join()

    # sleep(3)
    # check_order_status_on_mock()
    # sleep(3)
    # check_order_status_on_app()

if __name__ == "__main__":
    # asyncio.run(main())
    main_2()
