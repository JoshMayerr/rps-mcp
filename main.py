import os
import random
import dotenv
from mcp.server.fastmcp import FastMCP

dotenv.load_dotenv()

RPS_API_KEY = os.getenv("rpsApiKey")

if not RPS_API_KEY:
    raise ValueError("rpsApiKey is not set")

mcp = FastMCP("Rock Paper Scissors")


@mcp.tool()
def rock_paper_scissors(user_choice: str) -> str:
    """
    Play rock paper scissors with Josh.

    Args:
        user_choice: The choice of the user.

    Returns:
        The result of the game.
    """
    options = ["rock", "paper", "scissors"]
    if user_choice not in options:
        return "Invalid choice. Please choose from: rock, paper, scissors"
    computer_choice = random.choice(options)
    if user_choice == computer_choice:
        return "It's a tie!"
    if user_choice == "rock" and computer_choice == "scissors":
        return "You won!"
    if user_choice == "paper" and computer_choice == "rock":
        return "You won!"
    if user_choice == "scissors" and computer_choice == "paper":
        return "You won!"
    return "You lost!"


if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')
