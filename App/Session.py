import os
from datetime import datetime
from tkinter import messagebox

import DBconnection as DB
import SignIn as si

# Global variables to store session information
current_user = None
last_activity = None
check = None


def start_session(username):
    global current_user, last_activity
    current_user = username
    last_activity = datetime.now()


def end_session():
    global current_user, last_activity
    current_user = None
    last_activity = None


def update_last_activity():
    global last_activity
    last_activity = datetime.now()


def check_user_activity(max_inactive_duration):
    global current_user, last_activity
    if last_activity is None:
        # No active session
        return False
    inactive_duration = datetime.now() - last_activity
    return inactive_duration.total_seconds() > max_inactive_duration


# Update user's last activity timestamp on any user interaction (e.g., button clicks)
def on_user_interaction(root, frame):
    global current_user, last_activity
    if current_user:
        update_last_activity()
        frame.after(11000, lambda: check_activity_and_logout(root, frame))


def check_activity_and_logout(root, frame):
    global current_user, last_activity, check
    max_inactive_duration = 10
    print("hello")
    if current_user and check_user_activity(max_inactive_duration) and check is None:
        check = True
        messagebox.showinfo("Logout", "You have been logged out due to inactivity.")
        end_session()
        frame.destroy()
        si.SignIn(root)


def update_user_token(username, token):
    # Replace 'your_user_table', 'your_token_column' with your actual table and column names
    update_query = f"UPDATE users SET Token = '{token}' WHERE username = '{username}'"
    # Execute the update query
    DB.execute_query(update_query)


def log_user_connection(username, token):
    # Get the AppData directory path
    appdata_path = os.path.join(os.getenv('APPDATA'), 'FileCipher')

    # Create the AppData directory if it doesn't exist
    if not os.path.exists(appdata_path):
        os.makedirs(appdata_path)

    # Create a log file in the AppData directory
    log_file_path = os.path.join(appdata_path, 'user_log.txt')

    # Get the current date and time
    current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Log user connection information to the file
    with open(log_file_path, 'a') as log_file:
        log_file.write(f"Username: {username}, Date of Connection: {current_datetime}, Token: {token}\n")
