# Simple recommendation system using Python's built-in dictionary (hash table)

class RecommendationSystem:
    def __init__(self):
        self.user_recommendations = {}
    def add_recommendations(self, user_id, recommendations):
        self.user_recommendations[user_id] = recommendations
    def get_recommendations(self, user_id):
        return self.user_recommendations.get(user_id, ["No recommendations available."])
    def show_all_users(self):
        for user_id, recs in self.user_recommendations.items():
            print(f"User {user_id}: {recs}")

if __name__ == "__main__":
    recommender = RecommendationSystem()
    recommender.add_recommendations("alice", ["Travel blog", "Music playlist", "New movie"])
    recommender.add_recommendations("bob", ["Tech news", "Sports update"])
    recommender.add_recommendations("carol", ["Cooking show", "Fashion tips"])
    print("Recommendations for Bob:")
    print(recommender.get_recommendations("bob"))
    print("\nRecommendations for Carol:")
    print(recommender.get_recommendations("carol"))
    print("\nAll users and recommendations:")
    recommender.show_all_users()
