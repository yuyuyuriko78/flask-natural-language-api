from flask import Flask, render_template, request
from google.cloud import language_v1

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/index', methods=['post'])
def post():

    # GCP接続情報
    client = language_v1.LanguageServiceClient()

    # 最終的にフロントエンドに返す配列
    results = []

    # APIに渡すテキストを整形
    text_for_analysis = request.form['text-for-analysis']
    document = {'content': text_for_analysis, 'type_': 'PLAIN_TEXT'}

    # APIを実行
    response = client.analyze_sentiment(request={'document': document})

    # 文章ごとに結果を取得
    for sentence in response.sentences:
        sentence_text = sentence.text.content
        sentence_sentiment_score = sentence.sentiment.score
        sentence_sentiment_magnitude = sentence.sentiment.magnitude
        item = {
            'sentence_text': sentence_text,
            'sentence_sentiment_score': sentence_sentiment_score,
            'sentence_sentiment_magnitude': sentence_sentiment_magnitude
        }
        results.append(item)

    # 結果をフロントエンドに返す
    return render_template('index.html', text=text_for_analysis, result=results)


@app.route("/apisample", methods=['GET', 'POST'])
def analyze_sentiment():

    # GCP接続情報
    client = language_v1.LanguageServiceClient()

    # APIに渡すテキストを整形
    text_for_analysis = request.get_json()
    document = {'content': text_for_analysis['text'], 'type_': 'PLAIN_TEXT'}

    # APIを実行
    response = client.analyze_sentiment(request={'document': document})

    # 最終的に返す配列
    results = []

    # 文章ごとに結果を取得
    for sentence in response.sentences:
        sentence_text = sentence.text.content
        sentence_sentiment_score = sentence.sentiment.score
        sentence_sentiment_magnitude = sentence.sentiment.magnitude
        item = {
            'テキスト': sentence_text,
            '感情のポジネガ': sentence_sentiment_score,
            '感情の強さ': sentence_sentiment_magnitude
        }
        results.append(item)

    return str(results)


if __name__ == '__main__':
    app.run(debug=True)
