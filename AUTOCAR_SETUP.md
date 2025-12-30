# Autocar Setup Instructions

## Quick Setup

Your PC's IP address: **172.23.150.8**

### Option 1: Using Environment Variable (Recommended)

On the autocar, run:
```bash
export WEBHOOK_URL=http://172.23.150.8:5000/webhook
python3 face_capture.py
```

### Option 2: Using Setup Script

1. Make the script executable:
```bash
chmod +x webhookPC/SETUP_AUTOCAR.sh
```

2. Run the setup script:
```bash
source webhookPC/SETUP_AUTOCAR.sh
python3 face_capture.py
```

### Option 3: Make it Permanent

Add to your `~/.bashrc` file:
```bash
echo 'export WEBHOOK_URL=http://172.23.150.8:5000/webhook' >> ~/.bashrc
source ~/.bashrc
```

## Verify Connection

Before running face detection, make sure:
1. Your PC webhook receiver is running (`python webhook_receiver.py` in webhookPC folder)
2. Test connection from autocar:
```bash
curl http://172.23.150.8:5000/health
```

You should see a JSON response with status "healthy".

## Run Face Detection

Once configured, simply run:
```bash
python3 face_capture.py
```

The system will:
- Detect human faces
- Capture images every 5 seconds when face is detected
- Send images to your PC at 172.23.150.8:5000/webhook
- Save images locally on autocar in `captured_faces/` folder
- Save images on PC in `webhookPC/received_images/` folder

