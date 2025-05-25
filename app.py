from flask import Flask, request, jsonify
from tasks import process_video, transcribe_audio, score_segment

app = Flask(__name__)

@app.route('/api/submit-video', methods=['POST'])
def submit_video():
    data = request.get_json()
    video_url = data.get('video_url')
    if not video_url:
        return jsonify({'error': 'Missing video URL'}), 400
    task_id = process_video(video_url)
    return jsonify({'status': 'processing', 'task_id': task_id})

@app.route('/api/transcribe', methods=['POST'])
def transcribe():
    data = request.get_json()
    video_path = data.get('video_path')
    if not video_path:
        return jsonify({'error': 'Missing video path'}), 400
    transcript = transcribe_audio(video_path)
    return jsonify({'transcript': transcript})

@app.route('/api/score', methods=['POST'])
def score():
    data = request.get_json()
    text = data.get('text')
    if not text:
        return jsonify({'error': 'Missing text to score'}), 400
    score = score_segment(text)
    return jsonify({'score': score})

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/')
def index():
    return "Court Stream API is live!"
