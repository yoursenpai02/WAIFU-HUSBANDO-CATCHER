class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "5946409711"
    sudo_users = "5946409711", "5946409711"
    GROUP_ID = -1002087696194
    TOKEN = "6439354120:AAHArofBgfJTggFruyk7xaAXmDB8H9wmEhM"
    mongo_url = "mongodb+srv://teamdaxx123:teamdaxx123@cluster0.ysbpgcp.mongodb.net/?retryWrites=true&w=majority"
    PHOTO_URL = ["https://telegra.ph/file/b925c3985f0f325e62e17.jpg", "https://telegra.ph/file/4211fb191383d895dab9d.jpg"]
    SUPPORT_CHAT = "senpaibotmanagement"
    UPDATE_CHAT = "senpaibotmanagement"
    BOT_USERNAME = "Villan_Waifu_bot"
    CHARA_CHANNEL_ID = "-1002087696194"
    api_id = 26626068
    api_hash = "bf423698bcbe33cfd58b11c78c42caa2"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
