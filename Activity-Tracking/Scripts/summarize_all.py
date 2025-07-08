import os
import re
from collections import defaultdict

# Path to your log files
log_paths = {
    'general': 'Daily-WorkLog/general.md',
    'learning': 'Daily-WorkLog/Learning-of-the-Day.md',
    'myhealthActions': 'Daily-WorkLog/Health-Activities.md',
    'office_projects': 'Daily-WorkLog/office-projects/',
    'personal_projects': 'Daily-WorkLog/personal-projects/'
}


# Function to extract data from a log file
def extract_data(file_path, patterns):
    with open(file_path, 'r') as file:
        content = file.read()

    # Extract data
    data = {key: re.findall(pattern, content) for key, pattern in patterns.items()}

    return data


# Function to generate summary
def generate_summary(data):
    summary = defaultdict(list)

    num_entries = len(next(iter(data.values())))
    for i in range(num_entries):
        for key in data:
            summary[key].append(data[key][i].strip())

    return summary


# Function to write summary to a Markdown file
def write_summary_to_md(summary, output_file_path, title):
    with open(output_file_path, 'w') as file:
        file.write(f'# Summary of {title}\n')

        num_entries = len(summary[next(iter(summary.keys()))])
        for i in range(num_entries):
            file.write(f"\n## {summary['Dates'][i]}\n")
            for key in summary:
                if key != 'Dates':
                    file.write(f"### {key}\n- {summary[key][i]}\n")


# Function to summarize general logs
def summarize_general():
    patterns = {
        'Dates': r'## \[(.*?)\]',
        'Activities': r'### Activities\n- (.*?)\n',
        'Important Notes': r'### Important Notes\n- (.*?)\n'
    }
    data = extract_data(log_paths['general'], patterns)
    summary = generate_summary(data)
    write_summary_to_md(summary, 'summary_general.md', 'General Logs')


# Function to summarize learning logs
def summarize_learning():
    patterns = {
        'Dates': r'## \[(.*?)\]',
        'Topics Learned': r'### Topics Learned\n- (.*?)\n',
        'Key Takeaways': r'### Key Takeaways\n- (.*?)\n'
    }
    data = extract_data(log_paths['learning'], patterns)
    summary = generate_summary(data)
    write_summary_to_md(summary, 'summary_learning.md', 'Learning Logs')


# Function to summarize myhealthActions logs
def summarize_myhealthActions():
    patterns = {
        'Dates': r'## \[(.*?)\]',
        'Actions Taken': r'### Actions Taken\n- (.*?)\n',
        'Duration': r'### Duration\n- (.*?)\n',
        'Notes': r'### Notes\n- (.*?)\n'
    }
    data = extract_data(log_paths['myhealthActions'], patterns)
    summary = generate_summary(data)
    write_summary_to_md(summary, 'summary_myhealthActions.md', 'My Health Actions Logs')


# Function to summarize project logs (office or personal)
def summarize_projects(directory, output_file, title):
    patterns = {
        'Dates': r'## \[(.*?)\]',
        'Planned Tasks': r'### Planned Tasks\n- (.*?)\n',
        'Actual Tasks': r'### Actual Tasks\n- (.*?)\n',
        'Hours Worked': r'### Hours Worked\n- (.*?)\n',
        'Learnings': r'### Learnings\n- (.*?)\n',
        'Important Contributions': r'### Important Contributions\n- (.*?)\n'
    }

    all_data = defaultdict(list)

    for filename in os.listdir(directory):
        if filename.endswith('.md'):
            file_path = os.path.join(directory, filename)
            data = extract_data(file_path, patterns)
            for key in data:
                all_data[key].extend(data[key])

    summary = generate_summary(all_data)
    write_summary_to_md(summary, output_file, title)


def main():
    print("Choose an area to summarize:")
    print("1. General")
    print("2. Learning")
    print("3. My Health Actions")
    print("4. Office Projects")
    print("5. Personal Projects")
    print("6. All")

    choice = input("Enter the number corresponding to your choice: ")

    if choice == '1':
        summarize_general()
    elif choice == '2':
        summarize_learning()
    elif choice == '3':
        summarize_myhealthActions()
    elif choice == '4':
        summarize_projects(log_paths['office_projects'], 'summary_office_projects.md', 'Office Project Logs')
    elif choice == '5':
        summarize_projects(log_paths['personal_projects'], 'summary_personal_projects.md', 'Personal Project Logs')
    elif choice == '6':
        summarize_general()
        summarize_learning()
        summarize_myhealthActions()
        summarize_projects(log_paths['office_projects'], 'summary_office_projects.md', 'Office Project Logs')
        summarize_projects(log_paths['personal_projects'], 'summary_personal_projects.md', 'Personal Project Logs')
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()
