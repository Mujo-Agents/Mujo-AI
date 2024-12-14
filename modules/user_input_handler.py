class UserInputHandler:
    def collect_user_input(self):
        print("Enter your name:")
        user_name = input()
        print("Enter a culture you want represented:")
        culture = input()
        print("Enter aesthetic preferences (e.g., modern, minimal, bold):")
        preferences = input().split(", ")
        return {"user_name": user_name, "culture": culture, "preferences": preferences}
