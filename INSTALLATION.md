# Installation Guide

## For AIot Autocar Prime (Python 3.6)

1. Install required dependencies:
```bash
pip3 install -r requirements_autocar.txt
```

This will install:
- `requests` - For sending HTTP requests to webhook
- `opencv-python` - For image processing (if not already installed)

2. Configure webhook URL:
```bash
export WEBHOOK_URL=http://YOUR_PC_IP:5000/webhook
```

Replace `YOUR_PC_IP` with your PC's IP address.

3. Run the face detection:
```bash
python3 face_capture.py
```

## For Your PC (Webhook Receiver)

1. Navigate to webhookPC folder:
```bash
cd webhookPC
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

This will install Flask 2.0.3 (compatible with Python 3.6+).

3. Run the webhook receiver:
```bash
python webhook_receiver.py
```

## Python Version Notes

- **Autocar**: Python 3.6 (required by hardware)
- **PC**: Python 3.6 or higher (Flask 2.0.3 supports Python 3.6+)
- All code uses f-strings which are available in Python 3.6+

