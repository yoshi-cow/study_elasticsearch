FROM docker.elastic.co/elasticsearch/elasticsearch:8.9.0

# Kuromojiプラグインをインストール
RUN elasticsearch-plugin install analysis-kuromoji

# Elasticsearchを起動
CMD ["elasticsearch"]
