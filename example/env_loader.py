from easy_dotenv import EnvConfig

class Env(EnvConfig):
    port: int
    api_key: str

env = Env()

# Export env variable
__all__ = ['env']