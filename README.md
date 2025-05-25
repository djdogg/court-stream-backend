# Flask Backend for Court Stream App

## Features

- Submit a video for processing
- Transcribe audio
- Score transcript for vibe and viral potential

## Endpoints

- POST `/api/submit-video` — `{ "video_url": "https://..." }`
- POST `/api/transcribe` — `{ "video_path": "/path/to/video.mp4" }`
- POST `/api/score` — `{ "text": "Transcript..." }`

## To Run

```bash
pip install -r requirements.txt
python app.py
```