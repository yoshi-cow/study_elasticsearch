from flask import Flask, render_template, request
from elasticsearch import Elasticsearch

app = Flask(__name__)

es = Elasticsearch("http://elasticsearch:9200")

categories = ["dokujo", "it_life", "kaden", "livedoor", "movie", "peachy", "smax", "sports", "topic"]

@app.route("/", methods=["GET", "POST"])
def index():
    results =[]
    if request.method == "POST":
        start_date = request.form.get("start_date")
        end_date = request.form.get("end_date")
        category = request.form.get("category")
        keyword = request.form.get("keyword")

        # 検索クエリ構築
        query = {
            "bool": {
                "must": [],
                "filter": []
            }
        }

        # 検索キーワード
        if keyword:
            # 複数キーワードの場合、それらすべてのキーワードが含まれる文章を検索する。
            keywords = keyword.split() # キーワードをスペースで分割
            for k in keywords:
                query["bool"]["must"].append({
                    "match": {
                        "content": k
                    }
                })

        # 発表日の範囲指定
        if start_date and end_date:
            # 両方の範囲指定
            query["bool"]["filter"].append({
                "range": {
                    "published_at": {
                        "gte": start_date,
                        "lte": end_date
                    }
                }
            })
        elif start_date:
            # 開始日のみ指定　→ 開始日と同じ日の記事を抽出
            query["bool"]["filter"].append({
                "range": {
                    "published_at": {
                        "gte": start_date,
                        "lte": start_date
                    }
                }
            })
        elif end_date:
            query["bool"]["filter"].append({
                "range": {
                    "published_at": {
                        "gte": end_date,
                        "lte": end_date
                    }
                }
            })

        # カテゴリの絞り込み
        if category and category in categories:
            query["bool"]["filter"].append({
                "term": {
                    "category": category
                }
            })

        
        response = es.search(index="news_articles", body={"query": query})

        results = response["hits"]["hits"]

    return render_template("index.html", results=results, categories=categories)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
