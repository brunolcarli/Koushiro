from koushiro.settings import TOKEN
from src.commands import client
from src.keep_alive import keep_alive


if __name__ == '__main__':
    keep_alive()
    client.run(TOKEN)
