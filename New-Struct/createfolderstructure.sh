#!/bin/bash

# Create directories
mkdir -p Activity-Tracking/Daily-WorkLog/work-projects
mkdir -p Activity-Tracking/Daily-WorkLog/personal-projects
mkdir -p Activity-Tracking/scripts

# Create files and write contents
# General Journal Thoughts
cat <<EOF > Activity-Tracking/Daily-WorkLog/general-journal-thoughts.md
# General Journal Thoughts

## Sample Record

### Date: YYYY-MM-DD

#### Thoughts:
- Reflective notes on the day's events and feelings.

#### Learnings:
- Key insights or lessons learned.

#### Challenges:
- Difficulties encountered and thoughts on overcoming them.
EOF

# Work Projects
cat <<EOF > Activity-Tracking/Daily-WorkLog/work-projects/project1.md
# Project 1 Log

## Sample Record

### Date: YYYY-MM-DD

#### Tasks Accomplished:
- Task 1: Description of task and progress made.
- Task 2: Description of task and progress made.

#### Next Steps:
- Tasks planned for the next day or week.

#### Insights:
- Any new ideas or discoveries related to Project 1.
EOF

cat <<EOF > Activity-Tracking/Daily-WorkLog/work-projects/project2.md
# Project 2 Log

## Sample Record

### Date: YYYY-MM-DD

#### Tasks Accomplished:
- Task 1: Description of task and progress made.
- Task 2: Description of task and progress made.

#### Next Steps:
- Tasks planned for the next day or week.

#### Insights:
- Any new ideas or discoveries related to Project 2.
EOF

cat <<EOF > Activity-Tracking/Daily-WorkLog/work-projects/project3.md
# Project 3 Log

## Sample Record

### Date: YYYY-MM-DD

#### Tasks Accomplished:
- Task 1: Description of task and progress made.
- Task 2: Description of task and progress made.

#### Next Steps:
- Tasks planned for the next day or week.

#### Insights:
- Any new ideas or discoveries related to Project 3.
EOF

cat <<EOF > Activity-Tracking/Daily-WorkLog/work-projects/general-work.md
# General Work Log

## Sample Record

### Date: YYYY-MM-DD

#### Activities:
- Meetings attended, emails responded to, etc.

#### Achievements:
- Major accomplishments or contributions.

#### Challenges:
- Issues faced and how they were addressed.

#### Plans:
- Goals or tasks for the upcoming days.
EOF

cat <<EOF > Activity-Tracking/Daily-WorkLog/work-projects/growth-TODO.md
# Growth TODO

## Sample Record

### TODO Items

- [ ] Task 1: Description with follow-up date (YYYY-MM-DD).
- [ ] Task 2: Description with follow-up date (YYYY-MM-DD).
EOF

# Personal Projects
cat <<EOF > Activity-Tracking/Daily-WorkLog/personal-projects/health-activities.md
# Health Activities Log

## Sample Record

### Date: YYYY-MM-DD

#### Activities:
- Exercise: Type and duration.
- Diet: What was consumed.
- Sleep: Quality and duration.
- Vitals: Any noteworthy measurements (e.g., weight, blood pressure).

#### Notes:
- Any unusual feelings or observations about health.
EOF

cat <<EOF > Activity-Tracking/Daily-WorkLog/personal-projects/Learning-of-the-day.md
# Learning of the Day

## Sample Record

### Date: YYYY-MM-DD

#### Topic:
- Key subject or skill learned.

#### Details:
- Summary of what was learned and its significance.

#### Application:
- How this learning can be applied in work or personal life.
EOF

cat <<EOF > Activity-Tracking/Daily-WorkLog/personal-projects/personal-TODO.md
# Personal TODO

## Sample Record

### TODO Items

- [ ] Task 1: Description with follow-up date (YYYY-MM-DD).
- [ ] Task 2: Description with follow-up date (YYYY-MM-DD).
EOF

# Script file
cat <<EOF > Activity-Tracking/scripts/summarize.py
# Script to summarize logs

# Placeholder for script functionality
EOF

# Make the script executable
chmod +x create_activity_tracking.sh

echo "Activity tracking folder structure and files created successfully."
