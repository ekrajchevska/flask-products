from app import init_app

app = init_app()

if __name__ == '__main__':      # i bez main kje raboti bidejki od bash skriptata go povikuva wsgi:app object
    app.run(host='0.0.0.0', debug=True, port=5000)