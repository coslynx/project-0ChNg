import pandas as pd

class ReputationSystem:
    def __init__(self):
        self.reputation_points = {}

    def assign_reputation_points(self, user_id, points):
        if user_id in self.reputation_points:
            self.reputation_points[user_id] += points
        else:
            self.reputation_points[user_id] = points

    def get_reputation_points(self, user_id):
        if user_id in self.reputation_points:
            return self.reputation_points[user_id]
        else:
            return 0

    def implement_rewards_penalties(self, user_id, action):
        if action == "reward":
            self.assign_reputation_points(user_id, 10)
        elif action == "penalty":
            self.assign_reputation_points(user_id, -5)
        else:
            print("Invalid action. Please choose 'reward' or 'penalty'.")

    def generate_report(self):
        df = pd.DataFrame(list(self.reputation_points.items()), columns=['User_ID', 'Reputation_Points'])
        return df

# Sample implementation
# reputation_system = ReputationSystem()
# reputation_system.assign_reputation_points("user123", 20)
# reputation_system.implement_rewards_penalties("user123", "penalty")
# print(reputation_system.get_reputation_points("user123"))
# print(reputation_system.generate_report())