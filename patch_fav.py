import re

with open('/home/dev/sites/versal/index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Replace favicon
c = c.replace(
    '<link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>👑</text></svg>">',
    '<link rel="icon" href="data:image/svg+xml,<svg xmlns=\'http://www.w3.org/2000/svg\' viewBox=\'0 0 24 24\' fill=\'none\' stroke=\'%23D4AF37\' stroke-width=\'2\' stroke-linecap=\'round\' stroke-linejoin=\'round\'><path d=\'m2 4 3 12h14l3-12-6 7-4-7-4 7-6-7zm3 16h14\'/></svg>">'
)

with open('/home/dev/sites/versal/index.html', 'w', encoding='utf-8') as f:
    f.write(c)

print("Favicon replaced with pure SVG vector!")
