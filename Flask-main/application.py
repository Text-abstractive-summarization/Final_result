from flask import Flask, request, jsonify
import re

from crawling import Crawling

crawl = Crawling('./ke-t5')

application = Flask(__name__)

@application.route("/")
def hello():
    return "서버 실행중"

@application.route("/politics", methods=['POST'])
def politics():
    pol = crawl.make_df('정치') #정치 부문 크롤링
    if len(pol) == 4: # 기사가 4개 or 3개 크롤링 되니까 경우의 수 2개

        image = []
        answer = []
        media = []

        for i in range(pol): # 신문사 이름에 맞춰서 신문사 로고 이미지 패스 설정
            if pol['media'][i] == '중앙일보':
                image[i] = './'
            elif pol['media'][i] == '조선일보':
                image[i] = './'
            elif pol['media'][i] == '동아일보':
                image[i] = './'
            elif pol['media'][i] == '경향신문':
                image[i] = './'
            elif pol['media'][i] == '한겨례':
                image[i] = './'
            elif pol['media'][i] == '한국일보':
                image[i] = './'
            else:
                image[i] = './'

        for i in range(pol): # 요약문
            answer[i] = pol['generated_text'][i]

        for i in range(pol): # 신문사
            media[i] = pol['media'][i]
        res = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleImage": {
                            'imageUrl': image[0],
                            "altText": '신문사 로고입니다.'
                        },
                        "simpleText": {
                            "text": media[0] + ""
                                               "" + answer[0]
                        }
                    },
                    {
                        "simpleImage": {
                            'imageUrl': image[1],
                            "altText": '신문사 로고입니다.'
                        },
                        "simpleText": {
                            "text": media[1] + ""
                                               "" + answer[1]
                        }
                    },
                    {
                        "simpleImage": {
                            'imageUrl': image[2],
                            "altText": '신문사 로고입니다.'
                        },
                        "simpleText": {
                            "text": media[2] + ""
                                               "" + answer[2]
                        }
                    },
                    {
                        "simpleImage": {
                            'imageUrl': image[3],
                            "altText": '신문사 로고입니다.'
                        },
                        "simpleText": {
                            "text": media[3] + ""
                                               "" + answer[3]
                        }
                    },
                ]
            }
        }

        # 답변 전송
        return jsonify(res)
    elif len(pol) == 3:
        image = []
        answer = []
        media = []

        for i in range(pol):
            if pol['media'][i] == '중앙일보':
                image[i] = './'
            elif pol['media'][i] == '조선일보':
                image[i] = './'
            elif pol['media'][i] == '동아일보':
                image[i] = './'
            elif pol['media'][i] == '경향신문':
                image[i] = './'
            elif pol['media'][i] == '한겨례':
                image[i] = './'
            elif pol['media'][i] == '한국일보':
                image[i] = './'
            else:
                image[i] = './'

        for i in range(pol):
            answer[i] = pol['generated_text'][i]

        for i in range(pol):
            media[i] = pol['media'][i]
        res = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleImage": {
                            'imageUrl': image[0],
                            "altText": '신문사 로고입니다.'
                        },
                        "simpleText": {
                            "text": media[0] + ""
                                               "" + answer[0]
                        }
                    },
                    {
                        "simpleImage": {
                            'imageUrl': image[1],
                            "altText": '신문사 로고입니다.'
                        },
                        "simpleText": {
                            "text": media[1] + ""
                                               "" + answer[1]
                        }
                    },
                    {
                        "simpleImage": {
                            'imageUrl': image[2],
                            "altText": '신문사 로고입니다.'
                        },
                        "simpleText": {
                            "text": media[2] + ""
                                               "" + answer[2]
                        }
                    }
                ]
            }
        }

        # 답변 전송
        return jsonify(res)


@application.route("/economy", methods=['POST'])
def economy():
    eco = crawl.make_df('경제')
    if len(eco) == 4:

        image = []
        answer = []
        media = []

        for i in range(eco):
            if eco['media'][i] == '중앙일보':
                image[i] = './'
            elif eco['media'][i] == '조선일보':
                image[i] = './'
            elif eco['media'][i] == '동아일보':
                image[i] = './'
            elif eco['media'][i] == '경향신문':
                image[i] = './'
            elif eco['media'][i] == '한겨례':
                image[i] = './'
            elif eco['media'][i] == '한국일보':
                image[i] = './'
            else:
                image[i] = './'

        for i in range(eco):
            answer[i] = eco['generated_text'][i]

        for i in range(eco):
            media[i] = eco['media'][i]
        res = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleImage": {
                            'imageUrl': image[0],
                            "altText": '신문사 로고입니다.'
                        },
                        "simpleText": {
                            "text": media[0] + ""
                                               "" + answer[0]
                        }
                    },
                    {
                        "simpleImage": {
                            'imageUrl': image[1],
                            "altText": '신문사 로고입니다.'
                        },
                        "simpleText": {
                            "text": media[1] + ""
                                               "" + answer[1]
                        }
                    },
                    {
                        "simpleImage": {
                            'imageUrl': image[2],
                            "altText": '신문사 로고입니다.'
                        },
                        "simpleText": {
                            "text": media[2] + ""
                                               "" + answer[2]
                        }
                    },
                    {
                        "simpleImage": {
                            'imageUrl': image[3],
                            "altText": '신문사 로고입니다.'
                        },
                        "simpleText": {
                            "text": media[3] + ""
                                               "" + answer[3]
                        }
                    },
                ]
            }
        }

        # 답변 전송
        return jsonify(res)
    elif len(eco) == 3:
        image = []
        answer = []
        media = []

        for i in range(soc):
            if eco['media'][i] == '중앙일보':
                image[i] = './'
            elif eco['media'][i] == '조선일보':
                image[i] = './'
            elif eco['media'][i] == '동아일보':
                image[i] = './'
            elif eco['media'][i] == '경향신문':
                image[i] = './'
            elif eco['media'][i] == '한겨례':
                image[i] = './'
            elif eco['media'][i] == '한국일보':
                image[i] = './'
            else:
                image[i] = './'

        for i in range(eco):
            answer[i] = eco['generated_text'][i]

        for i in range(eco):
            media[i] = eco['media'][i]
        res = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleImage": {
                            'imageUrl': image[0],
                            "altText": '신문사 로고입니다.'
                        },
                        "simpleText": {
                            "text": media[0] + ""
                                               "" + answer[0]
                        }
                    },
                    {
                        "simpleImage": {
                            'imageUrl': image[1],
                            "altText": '신문사 로고입니다.'
                        },
                        "simpleText": {
                            "text": media[1] + ""
                                               "" + answer[1]
                        }
                    },
                    {
                        "simpleImage": {
                            'imageUrl': image[2],
                            "altText": '신문사 로고입니다.'
                        },
                        "simpleText": {
                            "text": media[2] + ""
                                               "" + answer[2]
                        }
                    }
                ]
            }
        }

        # 답변 전송
        return jsonify(res)


@application.route("/society", methods=['POST'])
def society():
    soc = crawl.make_df('사회')
    if len(soc) == 4:

        image = []
        answer = []
        media = []

        for i in range(soc):
            if soc['media'][i] == '중앙일보':
                image[i] = './'
            elif soc['media'][i] == '조선일보':
                image[i] = './'
            elif soc['media'][i] == '동아일보':
                image[i] = './'
            elif soc['media'][i] == '경향신문':
                image[i] = './'
            elif soc['media'][i] == '한겨례':
                image[i] = './'
            elif soc['media'][i] == '한국일보':
                image[i] = './'
            else:
                image[i] = './'

        for i in range(soc):
            answer[i] = soc['generated_text'][i]

        for i in range(soc):
            media[i] = soc['media'][i]
        res = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleImage": {
                            'imageUrl': image[0],
                            "altText": '신문사 로고입니다.'
                        },
                        "simpleText": {
                            "text": media[0] + ""
                                               "" + answer[0]
                        }
                    },
                    {
                        "simpleImage": {
                            'imageUrl': image[1],
                            "altText": '신문사 로고입니다.'
                        },
                        "simpleText": {
                            "text": media[1] + ""
                                               "" + answer[1]
                        }
                    },
                    {
                        "simpleImage": {
                            'imageUrl': image[2],
                            "altText": '신문사 로고입니다.'
                        },
                        "simpleText": {
                            "text": media[2] + ""
                                               "" + answer[2]
                        }
                    },
                    {
                        "simpleImage": {
                            'imageUrl': image[3],
                            "altText": '신문사 로고입니다.'
                        },
                        "simpleText": {
                            "text": media[3] + ""
                                               "" + answer[3]
                        }
                    },
                ]
            }
        }

        # 답변 전송
        return jsonify(res)
    elif len(soc) == 3:
        image = []
        answer = []
        media = []

        for i in range(soc):
            if soc['media'][i] == '중앙일보':
                image[i] = './'
            elif soc['media'][i] == '조선일보':
                image[i] = './'
            elif soc['media'][i] == '동아일보':
                image[i] = './'
            elif soc['media'][i] == '경향신문':
                image[i] = './'
            elif soc['media'][i] == '한겨례':
                image[i] = './'
            elif soc['media'][i] == '한국일보':
                image[i] = './'
            else:
                image[i] = './'

        for i in range(soc):
            answer[i] = soc['generated_text'][i]

        for i in range(soc):
            media[i] = soc['media'][i]
        res = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleImage": {
                            'imageUrl': image[0],
                            "altText": '신문사 로고입니다.'
                        },
                        "simpleText": {
                            "text": media[0] + ""
                                               "" + answer[0]
                        }
                    },
                    {
                        "simpleImage": {
                            'imageUrl': image[1],
                            "altText": '신문사 로고입니다.'
                        },
                        "simpleText": {
                            "text": media[1] + ""
                                               "" + answer[1]
                        }
                    },
                    {
                        "simpleImage": {
                            'imageUrl': image[2],
                            "altText": '신문사 로고입니다.'
                        },
                        "simpleText": {
                            "text": media[2] + ""
                                               "" + answer[2]
                        }
                    }
                ]
            }
        }

        # 답변 전송
        return jsonify(res)


@application.route("/culture", methods=['POST'])
def living():
    liv = crawl.make_df('생활/문화')
    if len(liv) == 4:

        image = []
        answer = []
        media = []

        for i in range(liv):
            if liv['media'][i] == '중앙일보':
                image[i] = './'
            elif liv['media'][i] == '조선일보':
                image[i] = './'
            elif liv['media'][i] == '동아일보':
                image[i] = './'
            elif liv['media'][i] == '경향신문':
                image[i] = './'
            elif liv['media'][i] == '한겨례':
                image[i] = './'
            elif liv['media'][i] == '한국일보':
                image[i] = './'
            else:
                image[i] = './'

        for i in range(liv):
            answer[i] = liv['generated_text'][i]

        for i in range(liv):
            media[i] = liv['media'][i]
        res = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleImage": {
                            'imageUrl': image[0],
                            "altText": '신문사 로고입니다.'
                        },
                        "simpleText": {
                            "text": media[0] + ""
                                               "" + answer[0]
                        }
                    },
                    {
                        "simpleImage": {
                            'imageUrl': image[1],
                            "altText": '신문사 로고입니다.'
                        },
                        "simpleText": {
                            "text": media[1] + ""
                                               "" + answer[1]
                        }
                    },
                    {
                        "simpleImage": {
                            'imageUrl': image[2],
                            "altText": '신문사 로고입니다.'
                        },
                        "simpleText": {
                            "text": media[2] + ""
                                               "" + answer[2]
                        }
                    },
                    {
                        "simpleImage": {
                            'imageUrl': image[3],
                            "altText": '신문사 로고입니다.'
                        },
                        "simpleText": {
                            "text": media[3] + ""
                                               "" + answer[3]
                        }
                    },
                ]
            }
        }

        # 답변 전송
        return jsonify(res)
    elif len(liv) == 3:
        image = []
        answer = []
        media = []

        for i in range(liv):
            if liv['media'][i] == '중앙일보':
                image[i] = './'
            elif liv['media'][i] == '조선일보':
                image[i] = './'
            elif liv['media'][i] == '동아일보':
                image[i] = './'
            elif liv['media'][i] == '경향신문':
                image[i] = './'
            elif liv['media'][i] == '한겨례':
                image[i] = './'
            elif liv['media'][i] == '한국일보':
                image[i] = './'
            else:
                image[i] = './'

        for i in range(liv):
            answer[i] = liv['generated_text'][i]

        for i in range(liv):
            media[i] = liv['media'][i]
        res = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleImage": {
                            'imageUrl': image[0],
                            "altText": '신문사 로고입니다.'
                        },
                        "simpleText": {
                            "text": media[0] + ""
                                               "" + answer[0]
                        }
                    },
                    {
                        "simpleImage": {
                            'imageUrl': image[1],
                            "altText": '신문사 로고입니다.'
                        },
                        "simpleText": {
                            "text": media[1] + ""
                                               "" + answer[1]
                        }
                    },
                    {
                        "simpleImage": {
                            'imageUrl': image[2],
                            "altText": '신문사 로고입니다.'
                        },
                        "simpleText": {
                            "text": media[2] + ""
                                               "" + answer[2]
                        }
                    }
                ]
            }
        }

        # 답변 전송
        return jsonify(res)


@application.route("/sports", methods=['POST'])
def sport():
    spo = crawl.make_df('스포츠')
    if len(spo) == 4:

        image = []
        answer = []
        media = []

        for i in range(spo):
            if spo['media'][i] == '중앙일보':
                image[i] = './'
            elif spo['media'][i] == '조선일보':
                image[i] = './'
            elif spo['media'][i] == '동아일보':
                image[i] = './'
            elif spo['media'][i] == '경향신문':
                image[i] = './'
            elif spo['media'][i] == '한겨례':
                image[i] = './'
            elif spo['media'][i] == '한국일보':
                image[i] = './'
            else:
                image[i] = './'

        for i in range(spo):
            answer[i] = spo['generated_text'][i]

        for i in range(spo):
            media[i] = spo['media'][i]
        res = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleImage": {
                            'imageUrl': image[0],
                            "altText": '신문사 로고입니다.'
                        },
                        "simpleText": {
                            "text": media[0] + ""
                                               "" + answer[0]
                        }
                    },
                    {
                        "simpleImage": {
                            'imageUrl': image[1],
                            "altText": '신문사 로고입니다.'
                        },
                        "simpleText": {
                            "text": media[1] + ""
                                               "" + answer[1]
                        }
                    },
                    {
                        "simpleImage": {
                            'imageUrl': image[2],
                            "altText": '신문사 로고입니다.'
                        },
                        "simpleText": {
                            "text": media[2] + ""
                                               "" + answer[2]
                        }
                    },
                    {
                        "simpleImage": {
                            'imageUrl': image[3],
                            "altText": '신문사 로고입니다.'
                        },
                        "simpleText": {
                            "text": media[3] + ""
                                               "" + answer[3]
                        }
                    },
                ]
            }
        }

        # 답변 전송
        return jsonify(res)
    elif len(spo) == 3:
        image = []
        answer = []
        media = []

        for i in range(spo):
            if spo['media'][i] == '중앙일보':
                image[i] = './'
            elif spo['media'][i] == '조선일보':
                image[i] = './'
            elif spo['media'][i] == '동아일보':
                image[i] = './'
            elif spo['media'][i] == '경향신문':
                image[i] = './'
            elif spo['media'][i] == '한겨례':
                image[i] = './'
            elif spo['media'][i] == '한국일보':
                image[i] = './'
            else:
                image[i] = './'

        for i in range(spo):
            answer[i] = spo['generated_text'][i]

        for i in range(spo):
            media[i] = spo['media'][i]
        res = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleImage": {
                            'imageUrl': image[0],
                            "altText": '신문사 로고입니다.'
                        },
                        "simpleText": {
                            "text": media[0] + ""
                                               "" + answer[0]
                        }
                    },
                    {
                        "simpleImage": {
                            'imageUrl': image[1],
                            "altText": '신문사 로고입니다.'
                        },
                        "simpleText": {
                            "text": media[1] + ""
                                               "" + answer[1]
                        }
                    },
                    {
                        "simpleImage": {
                            'imageUrl': image[2],
                            "altText": '신문사 로고입니다.'
                        },
                        "simpleText": {
                            "text": media[2] + ""
                                               "" + answer[2]
                        }
                    }
                ]
            }
        }

        # 답변 전송
        return jsonify(res)


@application.route('/search', methods = ['POST'])
def text():
    text = req["action"]["detailParams"]["sys_text"]["origin"]
    answer = crawl.query(text)
    answer1 = answer['generated_text']

    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": answer1
                    }
                }
            ]
        }
    }
    return jsonify(res)

@application.route('/urlink', methods = ['POST'])
def urlink():
    url = req["action"]["detailParams"]["sys_url"]["origin"]
    if re.match('https://news.naver.com'):
        final_df = crawl.choice_url(url)
    else:
        answer = '네이버 뉴스 url를 입력해주세요'
    answer = final_df['generated_text']

    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": answer
                    }
                }
            ]
        }
    }
    return jsonify(res)

if __name__ == "__main__":
    application.run(host='0.0.0.0', port=5000, threaded=True)
