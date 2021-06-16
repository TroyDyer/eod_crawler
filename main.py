import pywinmacro as pw
import time


location1 = (268, 54)   # 주소창
location2 = (269, 167)  # 검색창
location3 = (386, 650)  # Historical data
location4 = (604, 880)  # Download

stocks = ["FB", "MSFT", "RIOT", "MARA", "TSLA", "AAPL"]


# 히스토리 데이터 다운로드하는 함수
def price(ticker):
    # 검색창 클릭
    pw.click(location2)
    time.sleep(3)
    # 티커코드 입력
    pw.type_in(ticker)
    time.sleep(3)
    # 엔터
    pw.key_press_once("enter")
    time.sleep(3)
    # Historical Data 클릭
    pw.click(location3)
    time.sleep(3)
    # Download 클릭
    pw.click(location4)
    time.sleep(3)


# stocks 리스트에 저장된 종목 데이터 반복 다운로드
def get_price_data(stocks):
    for stock in stocks:
        price(stock)
        time.sleep(4)


# 크롬이 열려 있는 상황에서 Yahoo Finance 이동하는 함수
def go_to_yfinance():
    pw.click(location1)
    time.sleep(1)
    pw.type_in("https://finance.yahoo.com")
    time.sleep(1)
    pw.key_press_once("enter")


# 야후파이낸스 접속
go_to_yfinance()

# 주가 검색하는 작업
get_price_data(stocks)