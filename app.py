from flask import Flask, render_template, request
from src.providers.TubManger import YoutubeManager

app = Flask(__name__)


@app.route("/")
def index():
    print("Start")
    return render_template('index.html', Haserreur = False, path =True)


@app.route("/download",  methods=['POST'])
def download():
    url = request.form.get('url')
    quality = request.form.get('quality')
    print(url)
    print(quality)
    path = YoutubeManager.DownloadVideo(url,quality)
    if path == False:
        return render_template('index.html', Haserreur = True)
    else:
        download = request.url_root+path
        return render_template('index.html', Haserreur = False, path =download )
        
    pass
if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=5000)