from AMMusic.core.bot import AMMusicBot
from AMMusic.core.dir import dirr
from AMMusic.core.git import git
from AMMusic.core.userbot import Userbot
from AMMusic.misc import dbb, heroku, sudo

from .logging import LOGGER


dirr()

git()

dbb()

heroku()

sudo()

# Clients
app = AMMusicBot()
userbot = Userbot()


from .platforms import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()
