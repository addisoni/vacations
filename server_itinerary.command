#!/bin/bash
# Double-click this file in Finder to host the itinerary on your local network.
# Your iPhone/iPad must be on the same WiFi network.

PORT=8080
DIR="$(cd "$(dirname "$0")" && pwd)"

# Get local IP
IP=$(ipconfig getifaddr en0 2>/dev/null || ipconfig getifaddr en1 2>/dev/null || echo "unknown")

echo ""
echo "================================================"
echo "  Moorea Itinerary — Local Network Server"
echo "================================================"
echo ""
echo "  Open this on your iPhone/iPad:"
echo ""
echo "    http://$IP:$PORT/itinerary.html"
echo ""
echo "  Make sure your iPhone is on the same WiFi."
echo "  Press Ctrl+C to stop the server."
echo ""
echo "================================================"
echo ""

cd "$DIR"
python3 -m http.server $PORT
