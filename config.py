import os

CURR_NET = os.getenv("ZPUSH_NETWORK", "test")
PUSH_SERVER = {
    "test": {
        "root_url": "http://testapi.zebrablocklabs.com:5100/",
        "timeout": 10
    },
    "main": {
        "root_url": "http://dev.zebrablocklabs.com:5100/",
        "timeout": 10
    }
}


def get_config():
    return PUSH_SERVER[CURR_NET]
