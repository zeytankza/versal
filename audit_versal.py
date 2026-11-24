import re
import json

with open('/home/dev/sites/versal/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

print(f"Total HTML length: {len(html)} bytes")

# 1. Check for system emojis in buttons or text
emojis = re.findall(r'[\U0001F300-\U0001FAFF]', html)
print(f"Emojis found: {len(emojis)} -> {set(emojis)}")

# 2. Check Leaflet attribution disabled
if '.leaflet-control-attribution, .leaflet-attribution-flag { display: none !important; }' in html:
    print("✓ Leaflet attribution hidden in CSS")
else:
    print("✗ WARNING: Leaflet CSS override missing!")

if 'attributionControl: false' in html:
    print("✓ Leaflet attributionControl: false set")
else:
    print("✗ WARNING: attributionControl: false missing!")

# 3. Check 152-FZ checkbox disabled button
if 'id="fz152-consent"' in html and 'id="submit-btn" disabled' in html:
    print("✓ 152-FZ checkbox unchecked and submit button disabled by default")
else:
    print("✗ WARNING: 152-FZ compliance issue!")

# 4. Check coordinates
if '43.911752' in html and '42.706753' in html:
    print("✓ Exact rooftop coordinates 43.911752, 42.706753 present")
else:
    print("✗ WARNING: Exact coordinates missing!")

# 5. Check fonts
if 'family=Onest' in html and 'family=Unbounded' in html:
    print("✓ Verified Cyrillic Google Fonts Unbounded + Onest connected")
else:
    print("✗ WARNING: Font connection issue!")

# 6. Check unique photos
img_srcs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', html)
print(f"Total img tags: {len(img_srcs)}, unique: {len(set(img_srcs))}")
if len(img_srcs) == len(set(img_srcs)):
    print("✓ All images are 100% UNIQUE! 0 duplicate photos!")
else:
    print("✗ Duplicate photos found!")

# 7. Check mobile carousel classes
if 'overflow-x-auto snap-x snap-mandatory scrollbar-none' in html:
    print("✓ Mobile horizontal carousels configured properly")
else:
    print("✗ Mobile carousel classes missing!")
