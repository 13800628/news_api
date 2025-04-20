from fastapi import FastAPI, Query, HTTPException
from scraper.yahoo import fetch_yahoo_news
from scraper.nhk import fetch_nhk_news
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS設定を追加
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 全てのオリジンを許可（本番環境ではオリジンを制限するのが良い）
    allow_credentials=True,
    allow_methods=["*"],  # 全てのメソッドを許可
    allow_headers=["*"],  # 全てのヘッダーを許可
)

@app.get("/")
def root():
    return {"message": "ニューススクレイピングAPIへようこそ"}

@app.get("/news/")
def get_news(source: str = Query(..., description="ニュースサイト: Yahoo or NHK"),
             keyword: str = Query(None, description="検索キーワード（任意）")):
    try:
        if source == "Yahoo":
            news_data = fetch_yahoo_news(keyword)
        elif source == "NHK":
            news_data = fetch_nhk_news(keyword)
        else:
            raise HTTPException(status_code=400, detail="サポートされていないニュースサイトです")

        # データの整形（newsデータが空または無効な場合のチェック）
        if not news_data or not isinstance(news_data, list):
            raise HTTPException(status_code=500, detail="データの取得に失敗しました")

        return {"news": news_data}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"内部エラー: {str(e)}")