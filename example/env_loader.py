from easy_dotenv import EnvConfig

class Env(EnvConfig):
    port: int
    api_key: str
    debug: bool = False  # Optional with default value
    workers: int = 4     # Optional with default value

env = Env('..')  # Look for .env file in project root

# Export environment variable