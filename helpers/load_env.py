def load_env():
    import os
    from dotenv import load_dotenv

    print("\n🔧 Loading environment variables...")
    load_dotenv(override=True)

    credentials_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
    if credentials_path:
        print(f"✅ Google credentials found at: {credentials_path}")
    else:
        print("❌ Warning: GOOGLE_APPLICATION_CREDENTIALS not set!")

    print("✨ Environment setup complete\n")


if __name__ == "__main__":
    load_env()
