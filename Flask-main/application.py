from flask import Flask, request, jsonify
import re
from .crawling import Crawling


crawl = 

application = Flask(__name__)

@application.route("/")
def hello():
    return "서버 실행중"

@application.route("/politics",methods=['POST'])
def politics():

    answer1 = 0# 정치요약 1
    answer2 = 0# 정치요약 2
    answer3 = 0# 정치요약 3
    answer4 = 0# 정치요약 4
    answer5 = 0# 정치요약 5
    
    # 답변 텍스트 설정
    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": answer1
                    }
                },
                {
                    "simpleText": {
                        "text": answer2
                    }
                },
                {
                    "simpleText": {
                        "text": answer3
                    }
                },
                {
                    "simpleText": {
                        "text": answer4
                    }
                },
                {
                    "simpleText": {
                        "text": answer5
                    }
                }
            ]
        }
    }

    # 답변 전송
    return jsonify(res)
@application.route("/economy",methods=['POST'])
def economy():

    answer1 = 0# 경제요약 1
    answer2 = 0# 경제요약 2
    answer3 = 0# 경제요약 3
    answer4 = 0# 경제요약 4
    answer5 = 0# 경제요약 5
    
    # 답변 텍스트 설정
    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": answer1
                    }
                },
                {
                    "simpleText": {
                        "text": answer2
                    }
                },
                {
                    "simpleText": {
                        "text": answer3
                    }
                },
                {
                    "simpleText": {
                        "text": answer4
                    }
                },
                {
                    "simpleText": {
                        "text": answer5
                    }
                }
            ]
        }
    }

    # 답변 전송
    return jsonify(res)
@application.route("/society",methods=['POST'])
def society():

    answer1 = 0# 사회요약 1
    answer2 = 0# 사회요약 2
    answer3 = 0# 사회요약 3
    answer4 = 0# 사회요약 4
    answer5 = 0# 사회요약 5
    
    # 답변 텍스트 설정
    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": answer1
                    }
                },
                {
                    "simpleText": {
                        "text": answer2
                    }
                },
                {
                    "simpleText": {
                        "text": answer3
                    }
                },
                {
                    "simpleText": {
                        "text": answer4
                    }
                },
                {
                    "simpleText": {
                        "text": answer5
                    }
                }
            ]
        }
    }

    # 답변 전송
    return jsonify(res)
@application.route("/culture",methods=['POST'])
def living():

    answer1 = 0# 생/문요약 1
    answer2 = 0# 생/문요약 2
    answer3 = 0# 생/문요약 3
    answer4 = 0# 생/문요약 4
    answer5 = 0# 생/문요약 5
    
    # 답변 텍스트 설정
    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": answer1
                    }
                },
                {
                    "simpleText": {
                        "text": answer2
                    }
                },
                {
                    "simpleText": {
                        "text": answer3
                    }
                },
                {
                    "simpleText": {
                        "text": answer4
                    }
                },
                {
                    "simpleText": {
                        "text": answer5
                    }
                }
            ]
        }
    }

    # 답변 전송
    return jsonify(res)
@application.route("/sports",methods=['POST'])
def sport():

    answer1 = 0# 스포츠요약 1
    answer2 = 0# 스포츠요약 2
    answer3 = 0# 스포츠요약 3
    answer4 = 0# 스포츠요약 4
    answer5 = 0# 스포츠요약 5
    
    # 답변 텍스트 설정
    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": answer1
                    }
                },
                {
                    "simpleText": {
                        "text": answer2
                    }
                },
                {
                    "simpleText": {
                        "text": answer3
                    }
                },
                {
                    "simpleText": {
                        "text": answer4
                    }
                },
                {
                    "simpleText": {
                        "text": answer5
                    }
                }
            ]
        }
    }

    # 답변 전송
    return jsonify(res)

# @application.route('sys_text', methods = ['POST'])
# def search():
#     # text = req["action"]["detailParams"]["sys_text"]["origin"]
#     #answer =  크롤링/요약 함수( 텍스트 받은 값)
    
#     res = {
#         "version": "2.0",
#         "template": {
#             "outputs": [
#                 {
#                     "simpleText": {
#                         "text": answer
#                     }
#                 }
#             ]
#         }
#     }
#     return jsonify(res)

# @application.route('/urlink', methods = ['POST'])
# def urlink():
#     #url = req["action"]["detailParams"]["sys_url"]["origin"]
#     #if re.match('https://news.naver.com'):
#         #answer = 크롤링/요약함수 (url 받아오기)
#     #else:
#         #answer = '네이버 뉴스 url를 입력해주세요'
    
#     res = {
#         "version": "2.0",
#         "template": {
#             "outputs": [
#                 {
#                     "simpleText": {
#                         "text": answer
#                     }
#                 }
#             ]
#         }
#     }
#     return jsonify(res)

if __name__ == "__main__":
    application.run(host='0.0.0.0', port=5000, threaded=True)