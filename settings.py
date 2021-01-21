import os

if os.getenv('ENVIRONMENT') is None:
    from dotenv import load_dotenv
    load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")


if __name__ == '__main__':
    print(f'BOT_TOKEN: {BOT_TOKEN}')
