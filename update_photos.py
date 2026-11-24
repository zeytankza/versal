import json

with open('/home/dev/sites/versal/real_verified_photos.json', 'r', encoding='utf-8') as f:
    photos = json.load(f)

# Re-assign to categories
photo_map = {
    "hero_bg": photos[0],
    "hero_card": photos[1],
    "hall_grand": photos[2],
    "hall_table_setting": photos[3],
    "hall_vip": photos[4],
    "hall_stage": photos[5],
    "food_mangal": photos[6],
    "food_cold_appetizers": photos[7],
    "food_hot_dish": photos[8],
    "food_salad": photos[9],
    "food_dessert": photos[10],
    "atmosphere_wedding": photos[11],
    "atmosphere_dance": photos[12],
    "atmosphere_toast": photos[13],
    "welcome_zone": photos[14],
    "exterior": photos[15]
}

with open('/home/dev/sites/versal/photo_map.json', 'w', encoding='utf-8') as f:
    json.dump(photo_map, f, indent=2)

print("Updated photo_map.json with verified 200 OK URLs!")
