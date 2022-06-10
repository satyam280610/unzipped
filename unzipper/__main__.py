# Copyright (c) 2022 rdx28806

import os

from pyrogram import idle
from . import unzipperbot
from .helpers.unzip_help import check_logs
from config import Config

if __name__ == "__main__" :
    if not os.path.isdir(Config.DOWNLOAD_LOCATION):
        os.makedirs(Config.DOWNLOAD_LOCATION)
    unzipperbot.start()
    print("Checking Log channel…")
    check_logs()
    print("Bot is running now ! Join @rdx28806")
    idle()
