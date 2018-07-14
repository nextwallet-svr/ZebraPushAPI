import os

CURR_NET = os.getenv("NETWORK", "test")


PUSH_SERVER = {
    "test": {
        #"root_url": "http://localhost:5100/",
        "root_url": "http://101.132.189.59:5100/",
        "timeout": 10
    },
    "main": {
        "root_url": "http://localhost:5100/",
        "timeout": 10
    }
}

def get_config():
    return PUSH_SERVER[CURR_NET]
