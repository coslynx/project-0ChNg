import pandas as pd

class ModerationLogs:
    def __init__(self):
        self.logs = pd.DataFrame(columns=['timestamp', 'action', 'user_id', 'reason'])

    def log_action(self, timestamp, action, user_id, reason):
        self.logs = self.logs.append({'timestamp': timestamp, 'action': action, 'user_id': user_id, 'reason': reason}, ignore_index=True)

    def get_logs(self):
        return self.logs

    def generate_report(self):
        report = self.logs.groupby('user_id').agg({'action': 'count'}).reset_index()
        return report

# Instantiate ModerationLogs object
moderation_logs = ModerationLogs()