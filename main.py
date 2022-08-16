# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import slack
import os
from pathlib import Path

from dotenv import load_dotenv

env_path = Path('.')/'.env'
load_dotenv(dotenv_path = env_path)

client = slack.WebClient(token=os.environ['SLACK_TOKEN'])

client.chat_postMessage(channel='#test-automation',text="hello world!")