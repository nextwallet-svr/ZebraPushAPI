import os

CURR_NET = os.getenv("ZPUSH_NETWORK", "test")
PUSH_SERVER = {
    "test": {
        "root_url": "http://testdev.zebrablocklabs.com:5100/",
        "timeout": 10
    },
    "main": {
        "root_url": os.getenv("ZPUSH_URL", "http://dev.zebrablocklabs.com:5100/"),
        "timeout": 10
    }
}


def get_config():
    return PUSH_SERVER[CURR_NET]
