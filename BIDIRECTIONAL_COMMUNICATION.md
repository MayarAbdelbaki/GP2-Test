# Bidirectional Communication Setup

This system enables two-way communication between your PC and the autocar.

## How It Works

1. **Autocar → PC**: Autocar sends images when faces are detected
2. **PC → Autocar**: PC sends person detection results back to autocar
3. **Autocar displays**: Messages from PC appear in autocar terminal

## Setup

### On Your PC

1. **Set Autocar IP Address**:
   ```bash
   # Windows PowerShell
   $env:AUTOCAR_IP="192.168.8.155"
   
   # Or set it in webhook_receiver.py directly:
   AUTOCAR_IP = "192.168.101.101"  # Your autocar's IP
   ```

2. **Start Webhook Receiver**:
   ```bash
   cd webhookPC
   python webhook_receiver.py
   ```

### On Autocar

1. **Copy message_receiver.py** to the autocar (same directory as face_capture.py)

2. **Run Face Detection**:
   ```bash
   python3 face_capture.py
   ```
   
   The message receiver will start automatically in the background.

## Message Flow

1. Autocar detects face → sends image to PC
2. PC receives image → sends to Hugging Face
3. Hugging Face returns result (e.g., "Person: unknown person")
4. PC parses result → sends message to autocar
5. Autocar displays message in terminal:
   ```
   [2026-01-14 01:19:13] Message from PC:
     Person: unknown person
   ```

## Configuration

### PC Configuration (webhook_receiver.py)

```python
AUTOCAR_IP = "192.168.101.101"  # Your autocar's IP address
AUTOCAR_MESSAGE_PORT = 5001    # Port for sending messages
ENABLE_AUTOCAR_MESSAGES = True # Enable/disable message sending
```

### Autocar Configuration

The message receiver runs automatically when you start `face_capture.py`. It listens on port 5001.

## Finding Autocar IP Address

On the autocar, run:
```bash
ifconfig
# or
ip addr
```

Look for the IP address (usually starts with 192.168.x.x or 172.x.x.x)

## Testing

1. **Test message receiver on autocar**:
   ```bash
   # On autocar, test if it's listening:
   curl http://localhost:5001/health
   ```

2. **Test from PC**:
   ```bash
   # Send a test message from PC:
   curl -X POST http://AUTOCAR_IP:5001/message \
     -H "Content-Type: application/json" \
     -d '{"message": "Person: test person", "source": "PC"}'
   ```

3. **Check autocar terminal** - you should see the message displayed.

## Troubleshooting

### Messages not appearing on autocar?

1. **Check autocar IP**: Make sure AUTOCAR_IP is set correctly on PC
2. **Check port**: Ensure port 5001 is not blocked by firewall
3. **Check message receiver**: Verify message_receiver.py is in the same directory as face_capture.py
4. **Check network**: Ensure PC and autocar are on the same network

### Port already in use?

If you see "Address already in use" error:
- Another instance might be running
- Change MESSAGE_PORT in message_receiver.py to a different port
- Update AUTOCAR_MESSAGE_PORT in webhook_receiver.py to match

## Example Output

**PC Terminal:**
```
✓ Image received: 15.jpg
  Sending to Hugging Face API...
✓ Image sent to Hugging Face API successfully
  Person: unknown person
✓ Message sent to autocar: Person: unknown person
```

**Autocar Terminal:**
```
[2026-01-14 01:19:13] Message from PC:
  Person: unknown person
```
