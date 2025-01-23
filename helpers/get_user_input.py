import sys

def get_user_input() -> str:
    """
    Get user input from command line arguments.
    Returns the first argument passed or a default message if none provided.
    """
    default_message = "Say something!"
    if len(sys.argv) <= 1:
        print(f"\n⚠️  No input provided. Using default: '{default_message}'\n")
        return default_message
    user_input = " ".join(sys.argv[1:])
    print(f"\n🔍 Processing query: '{user_input}'\n")
    return user_input