from env_loader import env

if __name__ == "__main__":
    print(f"Port: {env.port}")
    print(f"API Key: {env.api_key}")
    print(f"Debug mode: {env.debug}")
    print(f"Workers: {env.workers}")
