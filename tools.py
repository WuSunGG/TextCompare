import json

res = {
    "code": "NotFound",
    "message": "services \"hadoop-service\" not found",
    "status": 404,
    "type": "error"
}


def buildErrorResponse(msg):
    res['type'] = 'error'
    res['status'] = 500
    res['message'] = msg
    res['code'] = "出错了"
    return res


def buildSuccessResponse(data):
    res['type'] = 'success'
    res['status'] = 200
    res['message'] = "成功"
    res['code'] = "成功"
    res['data'] = data
    return res


def bldPrs(msg, code=0, progress=0):
    """
    构建进度消息
    :param msg: 提示消息
    :param code: 状态码，-1：错误，0：正确
    :param progress: 进度消息，有效范围[0,100]
    :return:
    """
    return json.dumps(({"code": code, "msg": msg, "progress": progress}))
