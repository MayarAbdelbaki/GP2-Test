# Current Network Configuration

## IP Addresses

- **PC IPv4 Address**: `192.168.56.1`
- **Autocar IP Address**: `192.168.101.101`

## Configuration Summary

### PC Side (webhook_receiver.py)
- Webhook receiver listens on: `0.0.0.0:5000`
- Autocar IP configured: `192.168.101.101`
- Message port to autocar: `5001`

### Autocar Side (face_capture.py)
- Webhook URL: `http://192.168.56.1:5000/webhook`
- Message receiver listens on: `0.0.0.0:5001`

## Quick Test Commands

### From Autocar to PC:
```bash
# Test if PC webhook is reachable
curl http://192.168.56.1:5000/health
```

### From PC to Autocar:
```bash
# Test if autocar message receiver is reachable
curl http://192.168.101.101:5001/health

# Send a test message
curl -X POST http://192.168.101.101:5001/message \
  -H "Content-Type: application/json" \
  -d '{"message": "Person: test person", "source": "PC"}'
```

## Network Flow

1. **Autocar → PC**: 
   - Autocar sends images to: `http://192.168.56.1:5000/webhook`

2. **PC → Autocar**: 
   - PC sends messages to: `http://192.168.101.101:5001/message`

## Files Updated

- ✅ `webhookPC/webhook_receiver.py` - AUTOCAR_IP set to 192.168.101.101
- ✅ `face_capture.py` - Webhook URL set to http://192.168.56.1:5000/webhook
- ✅ All documentation files updated with correct IPs
