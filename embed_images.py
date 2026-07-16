#!/usr/bin/env python3
"""Embeds remaining external city images. Run once from the vacations folder."""
import re, urllib.request, base64, subprocess, os, tempfile

FILE = 'moving_tracker.html'
with open(FILE) as f:
    html = f.read()

# Case-insensitive match, skip script tags
pattern = re.compile(r'src="(https://[^"]+\.(?:jpg|jpeg|png|webp|gif))"', re.IGNORECASE)
matches = [m for m in pattern.finditer(html)
           if not html[max(0,m.start()-10):m.start()].endswith('script')]

print(f"Found {len(matches)} external image(s) to embed")

HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'}

for m in matches:
    url = m.group(1)
    print(f"Fetching: {url[:90]}...")
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=20) as resp:
            raw = resp.read()
        suffix = '.png' if url.lower().endswith('.png') else '.jpg'
        with tempfile.NamedTemporaryFile(suffix=suffix, delete=False) as tmp:
            tmp.write(raw); tmp_path = tmp.name
        out = tmp_path + '_out.jpg'
        subprocess.run(['sips', '-Z', '960', '-s', 'format', 'jpeg',
                        '-s', 'formatOptions', '78', tmp_path, '--out', out],
                       capture_output=True)
        os.unlink(tmp_path)
        with open(out, 'rb') as f2:
            b64 = base64.b64encode(f2.read()).decode()
        os.unlink(out)
        html = html.replace(f'src="{url}"', f'src="data:image/jpeg;base64,{b64}"', 1)
        print(f"  → {len(b64)//1024}KB embedded ✓")
    except Exception as e:
        print(f"  ✗ Failed: {e}")

with open(FILE, 'w') as f:
    f.write(html)

remaining = len([m for m in re.finditer(r'<img[^>]+src="https://', html)])
print(f"\nDone. Remaining external <img> srcs: {remaining}")
print(f"File: {len(html)//1024}KB")
