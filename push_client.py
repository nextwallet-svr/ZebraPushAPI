import logging
import json
from . import config

from simple_rest_client.api import API
from simple_rest_client.resource import Resource


class PushServiceResource(Resource):
    actions = {
        "send_mail": {"method": "POST", 'url': 'commonmail'},
        "send_sms": {"method": "POST", "url": "commonsms"},
        "send_notice": {"method": "POST", "url": "commonmsg"}
    }

class InternalServiceCall:
    def __init__(self, config):
        self.config = config
        self.push_service_api = self.get_push_api()

    def get_push_api(self):
        root_url = self.config.get("root_url")
        timeout = self.config.get('timeout')
        api = API(
            api_root_url = root_url,
            timeout=timeout,
            append_slash=False
        )
        api.add_resource(resource_name='push',
            resource_class=PushServiceResource
        )
        return api

    def send_mail(self, mail_info):
        """
        receive a dict of the mail info and send it to
        the ZebraPush server to send
        """
        mail_str = json.dumps(mail_info)
        try:
            body = {
                "mail_info": mail_str
            }
            response = self.push_service_api.push.send_mail(
                body=body, params={}, headers={}
            )
        except Exception as e:
            logging.error("send mail failed with error"+str(e))
            return {"retcode": -1, "message": "internal server error"}
        return response.body

    def send_sms(self, sms_info):
        """
        receive a dict of SMS info, and send it to
        the ZebraPush server to send
        """
        sms_str = json.dumps(sms_info)
        try:
            body = {
                "sms_info": sms_str
            }
            response = self.push_service_api.push.send_sms(
                body=body, params={}, headers={}
            )
        except Exception as e:
            logging.error("send SMS failed with error"+str(e))
            return {"retcode": -1, "message": "internal server error"}
        return response.body

    def send_notice(self, push_info):
        """
        receive a dict of notice info, and send it to
        the ZebraPush server to send
        """
        push_str = json.dumps(push_info)
        try:
            body = {
                "push_message": push_str
            }
            response = self.push_service_api.push.send_notice(
                body=body, params={}, headers={}
            )
        except Exception as e:
            logging.error("send SMS failed with error"+str(e))
            return {"retcode": -1, "message": "internal server error"}
        return response.body

# initiate the object
concrete_config = config.get_config()
zpush = InternalServiceCall(concrete_config)
