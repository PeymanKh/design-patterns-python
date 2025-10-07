"""
1. Single-Response Principle:
This principle states that each class should have only one responsibility.

Scenario:
The Scenario
You're building an API endpoint that:

    1. Receives a user query
    2. Calls an LLM (OpenAI/Anthropic/whatever)
    3. Saves the prompt and response to MongoDB
    4. Logs the token usage for billing
    5. Returns the response to the user
"""
class Agent:
    """Handles communication with LLM provider"""

    def generate_response(self, query):
        """Generates a response to the user's query"""
        pass


class DatabaseService:
    """Handles communication with MongoDB"""

    def save_prompt_and_response(self, prompt, response):
        """Saves the prompt and response to MongoDB"""
        pass


class UsageLogger:
    """Handles logging of token usage and billing"""

    def log_usage(self, tokens: int, timestamp: str):
        """Logs the token usage for billing"""
        pass


class QueryHandler:
    """Orchestrates the workflow - uses the services above"""

    def __init__(self, agent, db_service, logger):
        self.llm_service = agent
        self.db_service = db_service
        self.logger = logger
        pass

    def process_query(self, user_query: str) -> str:
        # Coordinate between services and return the final response
        pass


if __name__ == "__main__":
    agent = Agent()
    db_service = DatabaseService()
    logger = UsageLogger()
    query_handler = QueryHandler(agent, db_service, logger)
    query_handler.process_query("What is the meaning of life?")
