import requests
from logging import debug, info

from tools import bldPrs


class progress:
    FAIL = "fail"
    OK = "ok"
    OFFLINE = "offline"
    userid = ""

    def __init__(self, userid):
        if len(userid) < 5:
            info("userid {} is to short".format(userid))
        else:
            debug("set userid  as {}".format(userid))

            self.userid = userid

    def putMsg(self, msg, progress, code=0):
        msg = bldPrs(msg, code, progress)
        url = "http://122.114.95.64:8221"
        payload = 'type=publish&to={}&content={}'.format(self.userid, msg)
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        res = response.text
        if res != self.OK:
            info("send msg to {} is failed,msg is {},status is {}".format(self.userid, msg, res))
        else:
            debug("send msg to {} is successful,msg is {},status is {}".format(self.userid, msg, res))
        return res == self.OK


if __name__ == "__main__":
    pr = progress("sunwutest")
    print(pr.putMsg("xxxxxx"))
