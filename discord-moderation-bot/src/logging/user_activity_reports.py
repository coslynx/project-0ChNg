import pandas as pd

class UserActivityReports:
    def __init__(self):
        self.user_activity_data = pd.DataFrame(columns=['user_id', 'action', 'timestamp'])

    def log_moderation_action(self, user_id, action, timestamp):
        self.user_activity_data = self.user_activity_data.append({'user_id': user_id, 'action': action, 'timestamp': timestamp}, ignore_index=True)

    def generate_user_activity_report(self):
        return self.user_activity_data

    def generate_warnings_report(self):
        warnings_data = self.user_activity_data[self.user_activity_data['action'].str.contains('warning', case=False)]
        return warnings_data

    def generate_kicks_report(self):
        kicks_data = self.user_activity_data[self.user_activity_data['action'].str.contains('kick', case=False)]
        return kicks_data

    def generate_bans_report(self):
        bans_data = self.user_activity_data[self.user_activity_data['action'].str.contains('ban', case=False)]
        return bans_data

    def clear_user_activity_data(self):
        self.user_activity_data = pd.DataFrame(columns=['user_id', 'action', 'timestamp'])

# Instantiate the UserActivityReports class
user_activity_reports = UserActivityReports()