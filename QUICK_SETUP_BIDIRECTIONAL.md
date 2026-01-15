# Quick Setup: Bidirectional Communication

## Step 1: Find Autocar IP Address

On the autocar, run:
```bash
ifconfig
```
Note the IP address (e.g., `192.168.8.155`)

## Step 2: Configure PC

### Option A: Set Environment Variable
```bash
# Windows PowerShell
$env:AUTOCAR_IP="192.168.101.101"

# Then start webhook receiver
cd webhookPC
python webhook_receiver.py
```

### Option B: Edit webhook_receiver.py
Open `webhookPC/webhook_receiver.py` and set:
```python
AUTOCAR_IP = "192.168.101.101"  # Your autocar's IP
```

## Step 3: Copy message_receiver.py to Autocar

Copy `message_receiver.py` to the autocar (same directory as `face_capture.py`)

## Step 4: Run on Autocar

```bash
python3 face_capture.py
```

The message receiver will start automatically!

## Step 5: Test

When a face is detected:
- Autocar sends image to PC
- PC processes with Hugging Face
- PC sends result back to autocar
- **You'll see "Person: unknown person" in autocar terminal!**

## That's it! 🎉

Messages from PC will now appear in your autocar terminal automatically.
