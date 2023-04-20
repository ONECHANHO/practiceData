import requests #URL 요청 보내는 모듈
import json #클라이언트-서버가 통신하는 규율, 규격

def send_slack_message(message):
    bot_url = 'https://hooks.slack.com/services/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'
    payload = {
        "text" : message
    }

    response = requests.post(
        bot_url,
        data=json.dumps(payload),
        headers={"Content-Type":"application/json"}
    )

    print(response)

send_slack_message("안녕하세요")
