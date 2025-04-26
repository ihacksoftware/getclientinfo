# Client Information Collector

A simple FastAPI application that collects and displays client information including:
- User Agent
- IP Address
- Local IP Address (using WebRTC)
- Screen Resolution
- Browser Language
- Platform

## Setup

### Option 1: Local Setup

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

### Option 2: Docker Setup

1. Build the Docker image:
```bash
docker build -t client-info-collector .
```

2. Run the container:
```bash
docker run -p 8000:8000 client-info-collector
```

3. Open your browser and navigate to:
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