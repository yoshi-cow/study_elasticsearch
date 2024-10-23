# study_elasticsearch

- news file を elasticsearch に保存し、全文検索でキーワード検索する web アプリの作成

studu_elasticsearch/
│
├── docker-compose.yml
├── elasticsearch/
│ └── Dockerfile
├── webapp/
│ ├── app.py # Flask アプリのメインコード
│ ├── requirements.txt # Flask と Elasticsearch パッケージ
│ ├── Dockerfile
│ └── templates/
│ └── index.html # 検索画面
├── news_data/ # ニュースコーパスファイル
