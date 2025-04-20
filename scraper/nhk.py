import requests
from bs4 import BeautifulSoup

def fetch_nhk_news(keyword=None):
    url = "https://www3.nhk.or.jp/news/" if not keyword else f"https://www3.nhk.or.jp/news/search/?q={keyword}"
    
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, "html.parser")
        articles = []

        items = soup.find_all('a', class_='content')
        print(f"記事の候補数: {len(items)}")  # デバッグ用出力

        for item in items:
            title_elem = item.find('em', class_='title')
            if title_elem is None:
                print("タイトルが見つからない記事をスキップ")
                continue  # タイトルが見つからない場合スキップ

            title = title_elem.get_text(strip=True)
            link = item.get('href')

            if link:
                if not link.startswith("http"):
                    link = f"https://www3.nhk.or.jp{link}"
                articles.append({'title': title, 'link': link})
        
        print(f"取得できた記事数: {len(articles)}")
        return articles

    except requests.RequestException as e:
        print(f"リクエストエラー: {e}")
        return []

    except Exception as e:
        print(f"パースエラー: {e}")
        return []
