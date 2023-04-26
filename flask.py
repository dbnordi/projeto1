from flask import Flask, send_file

app = Flask(__name__)

@app.route('/download')
def download():
    return send_file('C:\Users\ti\Desktop\Docs Douglas\PI 2023\uploads', as_attachment=True)
