class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    API_ID = "11450167"
    API_HASH = "d0d147646f5c54e7d2324ddc873bc90c"

    CASH_API_KEY = "1T4JPU6WMF1DG7EI"  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = "postgres://ofgdlqfx:rsEOX2dcqxnYhLIR1g6mLWXuvVhiWg7V@mel.db.elephantsql.com/ofgdlqfx"  # A sql database url from elephantsql.com

    EVENT_LOGS = "-1001762139427"  # Event logs channel to note down important bot level events

    MONGO_DB_URI = "mongodb+srv://Nimoop:nimo69@cluster0.bsftute.mongodb.net/?retryWrites=true&w=majority"  # Get ths value from cloud.mongodb.com

    # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://te.legra.ph/file/538c2560d0dfb51e8bfe8.jpg"

    SUPPORT_CHAT = "timepassxdman"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = "5624877035:AAELcGVsrE9jrH0ah_ySojn2pj0RUXGimB8"  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = "0N223Q4G64B4"  # Get this value from https://timezonedb.com/api

    OWNER_ID = "5222353449"  # User id of your telegram account (Must be integer)

    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = [5733263480]  # User id of sudo users
    DEV_USERS = []  # User id of dev users
    DEMONS = [5021231683]  # User id of support users
    TIGERS = [5021231683]  # User id of tiger users
    WOLVES = [5021231683]  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
