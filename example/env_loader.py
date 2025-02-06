from easy_dotenv import EnvConfig

class BaseEnv(EnvConfig):
    port: int
    api_key: str
    debug: bool = False     # Optional with default value
    workers: int = 4    
    
class TelegramEnv(EnvConfig):
    bot_token: str
    chat_id: str
    channel_id: str = ''

base = BaseEnv('..')  # Look for .env file in project root
telegram = TelegramEnv('..')  # Look for .env file in project root

# Export environment variable
__all__ = ['base', 'telegram']