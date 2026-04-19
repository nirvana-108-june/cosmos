import requests

BASE_URL = "https://openapi.ls-sec.co.kr:8080"  # 실제 LS OpenAPI 베이스 URL 확인 필요

APP_KEY = "222"
APP_SECRET = "111"



def get_access_token():
    url = f"{BASE_URL}/oauth2/token"   # 실제 경로는 LS 문서 확인
    headers = {"Content-Type": "application/json"}
    body = {
        "appkey": APP_KEY,
        "appsecret": APP_SECRET,
        "grant_type": "client_credentials"
    }

    resp = requests.post(url, headers=headers, json=body)
    resp.raise_for_status()
    data = resp.json()
    return data["access_token"]

def get_futures_price(access_token, focode: str):
    """
    focode: 선물 코드 (예: '101T6000' 등)
    """
    url = f"{BASE_URL}/futures/price/tXXXX"  # 실제 TR URL로 교체
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}",
        "appkey": APP_KEY,
        "appsecret": APP_SECRET,
        # 필요시 tr_id, custtype 등 추가
    }
    body = {
        "tXXXXInBlock": {
            "focode": focode
        }
    }

    resp = requests.post(url, headers=headers, json=body)
    resp.raise_for_status()
    data = resp.json()

    # LS에서 내려주는 Output Block 명 확인 필요
    out_block = data["tXXXXOutBlock"]  # 예시
    cur_price = float(out_block["price"])  # 실제 필드명 확인 필요

    return cur_price, out_block
