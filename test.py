# 猴子补丁
from gevent import monkey
# monkey.patch_all()
from zhihu_crawler import *
import requests

# if __name__ == '__main__':
#     # 设置代理; 如采集量较大，建议每次请求都切换代理
#     set_proxy({'http': 'http://127.0.0.1:631', 'https': 'http://127.0.0.1:631'})

#     # 设置cookie
#     set_cookie({'d_c0': 'AIBfvRMxmhSPTk1AffR--QLwm-gDM5V5scE=|1646725014'})

    # 搜索采集使用案例:
    # for info in search_crawl(key_word='天空', count=10):
    #     print(info)

    # # 可传入data_type 指定搜索类型
    # for info in search_crawl(key_word='天空', count=10, data_type='answer'):
    #     print(info)

    # # 用户信息回答列表使用案例(采集该用户信息及50条回答信息,每条回答包含50条评论):
    # for info in user_crawler('wo-men-de-tai-kong',
    #                          answer_count=50,
    #                          comment_count=50
    #                          ):
    #     print(info)

    # # 用户信息提问列表使用案例(采集该用户信息及10条问题信息,每条问题包含10条回答，每条回答包含50条评论):
    # for info in user_crawler('wo-men-de-tai-kong',
    #                          question_count=10,
    #                          drill_down_count=10,
    #                          comment_count=50
    #                          ):
    #     print(info)

    # # 热点问题采集使用案例
    # # 采集 前10个问题, 每个问题采集10条回答
    # for info in hot_questions_crawl(question_count=10, drill_down_count=10):
    #     print(info)

    # 可传入period 指定热榜性质。如小时榜、日榜、周榜、月榜
    # 传入domains 采集指定主题的问题
    # for info in hot_questions_crawler(question_count=10, period='day', domains=['1001', 1003]):
    #     print(info)



def get_proxy():
    return requests.get("http://127.0.0.1:5010/get/").json()

def delete_proxy(proxy):
    requests.get("http://127.0.0.1:5010/delete/?proxy={}".format(proxy))

if __name__ == '__main__':
    proxy = get_proxy().get("proxy")
    proxies = {'http': 'http://{}'.format(proxy), 'https': 'http://{}'.format(proxy)}
    set_proxy(get_proxy())
    set_cookie({'d_c0': 'AvAQDHN4mxSPTtVyJn9kQSMi43V1kPWH_qc=|1646810832'})
    for info in search_crawler(key_word='滴普', nums=3, agree_users=True):
        # print(info)
        pass