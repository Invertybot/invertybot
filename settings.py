import os

if os.getenv('IS_LOCAL') is None:
    from dotenv import load_dotenv
    load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
SERVER_URL = os.getenv("SERVER_URL")
MONGO_USER = os.getenv("MONGO_USER")
MONGO_PASS = os.getenv("MONGO_PASSWORD")

PORT = os.getenv("PORT")
SECRET_SALT = os.getenv("SECRET_SALT")


if __name__ == '__main__':
    print(f'BOT_TOKEN: {BOT_TOKEN}')
    print(f'MONGO_USER: {MONGO_USER}')
    print(f'MONGO_PASS: {MONGO_PASS}')
    print(f'SERVER_URL: {SERVER_URL}')
    print(f'PORT: {PORT}')
