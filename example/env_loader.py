from easy_dotenv import EnvLoader

# Initialize environment variables once
env = EnvLoader.load(
    port=int,
    api_key=str
)

# Export env variable
__all__ = ['env']