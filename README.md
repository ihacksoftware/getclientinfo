# Client Information Collector

A simple FastAPI application that collects and displays client information including:
- User Agent
- IP Address
- Local IP Address (using WebRTC)
- Screen Resolution
- Browser Language
- Platform

## Setup

1. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python main.py
```

4. Open your browser and navigate to:
```
http://localhost:8000
```

## Features

- Collects server-side information (IP, User Agent)
- Uses WebRTC to detect local IP addresses
- Displays client-side information (screen resolution, language, platform)
- Modern, responsive UI
- Real-time information display

## Note

The local IP detection using WebRTC might not work in all browsers or might be blocked by certain security settings. 