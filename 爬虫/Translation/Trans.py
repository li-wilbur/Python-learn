# -*- conding:utf-8 -*-
# Auther : Li
# date : 2020-08-23
# role : Translation
import json
import requests

Trans_result = {}  # 字典用来存储翻译的结果，包含翻译源文本，翻译结果和翻译方式。


def Trans(trans_obj):
    # 翻译程序主函数，通过post向有道发起翻译请求，并将返回值存储到字典中。

    # 请求头部信息。
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0",
        "Referer": "http://fanyi.youdao.com/",
        "Connection": "keep-alive"
    }

    # POST请求数据，关键字："i"，即为要翻译的对象。
    post_trans = {
        "action": "FY_BY_REALTlME",
        "bv": "e2a78ed30c66e16a857c5b6486a1d326",
        "client": "fanyideskweb",
        "from": "AUTO",
        "i": post_object,
        "doctype": "json",
        "keyfrom": "fanyi.web",
        "lts": "1598163348219",
        "salt": "15981633482192",
        "sign": "69e857999ebdff6b1b5fae2016d14d19",
        "smartresult": "dict",
        "to": "AUTO",
        "version": "2.1"
    }
    url_trans = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
    # 发起翻译请求
    reponse = requests.post(url=url_trans, headers=headers, data=post_trans, timeout=15)
    trans_json = reponse.text
    # 通过json模块格式化信息。
    trans_dict = json.loads(trans_json)
    Trans_result["type"] = trans_dict["type"]
    Trans_result["src"] = trans_dict["translateResult"][0][0]["src"]
    Trans_result["text"] = trans_dict["translateResult"][0][0]["tgt"]
    return Trans_result


def Result(Trans_result):
    # 本函数将字典中的信息进行可视化格式并输出。
    if Trans_result["type"] == "EN2ZH_CN":
        print("英文转中文")
    elif Trans_result["type"] == "ZH_CN2EN":
        print("中文转英文")
    else:
        print("")
    print("翻译的源文本： {}".format(Trans_result["src"]))
    print("翻译结果为： {}".format(Trans_result["text"]))


# 循环翻译
while True:
    print("==========翻译小助手===========")
    post_object = input("请输入想要翻译的文字:\n(不输入任何字符回车即为退出。)\n:")
    if post_object == "":
        print("Goodbye!")
        break
    else:
        Trans(post_object)
        Result(Trans_result)
