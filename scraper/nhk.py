import requests
from bs4 import BeautifulSoup

def fetch_nhk_news(keyword=None):
    """
    NHKニュースをスクレイピングして取得する関数
    keyword: 検索したいキーワード (オプション)
    """
    url = f"https://www3.nhk.or.jp/news/" if not keyword else f"https://www3.nhk.or.jp/news/search/?q={keyword}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")
        
        articles = []
        for item in soup.find_all('a', class_='content'):
            title = item.find('em', class_='title').get_text()  # 修正されたクラス名でタイトルを取得
            link = item['href']
            articles.append({'title': title, 'link': f"https://www3.nhk.or.jp{link}"})
        
        return articles
    
    except requests.RequestException as e:
        print(f"Error fetching NHK news: {e}")
        return []