#!/bin/bash
# Double-click this file in Finder to host all planners on your local network.
# Your iPhone/iPad must be on the same WiFi network.

PORT=8080
DIR="$(cd "$(dirname "$0")" && pwd)"

# Get local IP
IP=$(ipconfig getifaddr en0 2>/dev/null || ipconfig getifaddr en1 2>/dev/null || echo "unknown")

echo ""
echo "================================================"
echo "  Addison's Planner — Local Network Server"
echo "================================================"
echo ""
echo "  Open on your iPhone/iPad (same WiFi):"
echo ""
echo "  🏠 Home:          http://$IP:$PORT/index.html"
echo "  🌺 Moorea Trip:   http://$IP:$PORT/moorea.html"
echo "  🏔️  Seattle Guide: http://$IP:$PORT/moving_tracker.html"
echo ""
echo "  Press Ctrl+C to stop the server."
echo ""
echo "================================================"
echo ""

cd "$DIR"
python3 -m http.server $PORT
