from env_loader import base, telegram

if __name__ == "__main__":
    print("Base Environment Variables:")
    print(f"Port: {base.port}")
    print(f"API Key: {base.api_key}")
    print(f"Debug mode: {base.debug}")
    print(f"Workers: {base.workers}")

    print("\nTelegram Environment Variables:")
    print(f"Bot Token: {telegram.bot_token}")
    print(f"Chat ID: {telegram.chat_id}")
    print(f"Channel ID: {telegram.channel_id}")
