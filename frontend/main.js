// ニュース取得ボタンがクリックされたときの処理
document.getElementById("fetch-news").addEventListener("click", async () => {
    const source = document.getElementById("source").value;
    const url = `https://news-api-run5.onrender.com/news/?source=${source}`;
  
    try {
        // API呼び出し
        const response = await fetch(url);
  
        // HTTPステータスコードが200でない場合にエラーを投げる
        if (!response.ok) {
            throw new Error(`HTTPエラー: ${response.status}`);
        }
  
        // レスポンスのJSONデータを取得
        const data = await response.json();
  
        // ニュースデータを表示
        displayNews(data);
    } catch (error) {
        console.error("Error fetching news:", error);
        alert(`ニュースの取得に失敗しました: ${error.message}`);
    }
  });
  
  // 検索機能ボタンがクリックされたときの処理
  document.getElementById("search-news").addEventListener("click", async () => {
    const source = document.getElementById("source").value;
    const keyword = document.getElementById("keyword").value;
    const url = `https://news-api-run5.onrender.com/news/?source=${source}&keyword=${keyword}`;
  
    try {
        // API呼び出し
        const response = await fetch(url);
  
        // HTTPステータスコードが200でない場合にエラーを投げる
        if (!response.ok) {
            throw new Error(`HTTPエラー: ${response.status}`);
        }
  
        // レスポンスのJSONデータを取得
        const data = await response.json();
  
        // ニュースデータを表示
        displayNews(data);
    } catch (error) {
        console.error("Error fetching news:", error);
        alert(`ニュースの取得に失敗しました: ${error.message}`);
    }
  });
  
  // ニュースデータを画面に表示する関数
  function displayNews(newsData) {
    const container = document.getElementById("news-container");
    container.innerHTML = "";  // 既存のニュースをリセット
  
    // レスポンスの形式をチェック
    if (newsData && Array.isArray(newsData.news)) {
        if (newsData.news.length > 0) {
            newsData.news.forEach(article => {
                const div = document.createElement("div");
                div.innerHTML = `
                    <h3>${article.title}</h3>
                    <a href="${article.link}" target="_blank">リンク</a>
                `;
                container.appendChild(div);
            });
        } else {
            container.innerHTML = "<p>該当するニュースはありませんでした。</p>";
        }
    } else {
        container.innerHTML = "<p>予期しないデータ形式が返されました。</p>";
    }
  }
