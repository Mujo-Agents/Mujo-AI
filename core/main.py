from modules.user_input_handler import UserInputHandler
from modules.agent_generator import AgentGenerator
from utils.logger import Logger

def main():
    Logger.log("Starting CulturaAI...")

    # Collect user input
    user_handler = UserInputHandler()
    user_data = user_handler.collect_user_input()

    # Generate a cultural agent
    generator = AgentGenerator()
    agent = generator.generate_agent(user_data)

    Logger.log(f"Agent generated successfully: {agent}")

if __name__ == "__main__":
    main()
