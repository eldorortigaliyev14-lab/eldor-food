from django.shortcuts import render


PRODUCTS = [
    ("Eldor burger", "Shirali mol go'shti, cheddar va maxsus sous", 42000, "burger", "Bestseller"),
    ("Double smash", "Ikki qavat mol go'shti va ikki karra cheddar", 55000, "burger", "To'yimli"),
    ("Crispy chicken", "Qarsildoq tovuq, yangi salat va sous", 36000, "chicken", "Qarsildoq"),
    ("Pepperoni pizza", "Pepperoni, mozzarella va pomidor sousi", 68000, "pizza", "Yangi"),
    ("Street fries", "Oltinrang fri, paprika va maxsus dip", 19000, "snack", "Yengil tamaddi"),
    ("Fresh lemonade", "Limon, yalpiz va muzdek kayfiyat", 16000, "drink", "Muzdek"),
    ("Cheeseburger classic", "Mol go'shti kotleti, cheddar va uy sousi", 39000, "burger", "Klassik"),
    ("BBQ burger", "Barbekyu sousi, qarsildoq piyoz va mol go'shti", 46000, "burger", "BBQ"),
    ("Mushroom burger", "Qo'ziqorin, eritilgan pishloq va shirali kotlet", 44000, "burger", "Yumshoq ta'm"),
    ("Spicy burger", "Achchiq sous, jalapeno va cheddar", 43000, "burger", "Achchiq"),
    ("Chicken burger", "Qarsildoq tovuq filesi va maxsus sous", 35000, "burger", "Sevimli"),
    ("Mini burger set", "Ikki mini burger va fri kartoshkasi", 49000, "burger", "Set"),
    ("BBQ double burger", "Ikki kotlet, dudlangan pishloq va BBQ", 57000, "burger", "To'yimli"),
    ("Cheese bomb burger", "Uch xil pishloq va yumshoq bulochka", 48000, "burger", "Pishloqli"),
    ("Texas burger", "Mol go'shti, dudlama va BBQ", 51000, "burger", "Texas"),
    ("Green burger", "Yangi salat, avokado sousi va mol go'shti", 47000, "burger", "Yangi"),
    ("Chicken strips", "Ziravorli qarsildoq tovuq bo'laklari", 32000, "chicken", "Qarsildoq"),
    ("Hot wings", "Achchiq glazurdagi tovuq qanotlari", 39000, "chicken", "Achchiq"),
    ("Chicken bites", "Yumshoq tovuq bo'laklari va dip sous", 29000, "chicken", "Yengil"),
    ("Chicken wrap", "Tovuq, salat va sarimsoqli sous lavashda", 33000, "chicken", "O'rama"),
    ("Chicken nuggets", "Oltinrang nuggets, 6 dona", 27000, "chicken", "Bolalarbop"),
    ("Honey chicken", "Asal sousidagi tovuq va kunjut", 38000, "chicken", "Maxsus"),
    ("Chicken steak", "Grilda pishgan tovuq filesi va ko'katlar", 41000, "chicken", "Grilda"),
    ("Buffalo wings", "Buffalo sousi va dip bilan qanotchalar", 40000, "chicken", "Bestseller"),
    ("Margarita pizza", "Mozzarella, pomidor va xushbo'y rayhon", 58000, "pizza", "Klassik"),
    ("Four cheese pizza", "Mozzarella, cheddar, parmesan va dorblu", 74000, "pizza", "Pishloqli"),
    ("BBQ chicken pizza", "Tovuq, BBQ sousi va qizil piyoz", 69000, "pizza", "Bestseller"),
    ("Vegetarian pizza", "Qalampir, zaytun va qo'ziqorin", 62000, "pizza", "Yengil"),
    ("Meat lovers pizza", "Mol go'shti, tovuq va pepperoni", 79000, "pizza", "To'yimli"),
    ("Mushroom pizza", "Qo'ziqorin, mozzarella va maxsus sous", 65000, "pizza", "Yangi"),
    ("Spicy salami pizza", "Achchiq salami, qalampir va mozzarella", 70000, "pizza", "Achchiq"),
    ("Chicken ranch pizza", "Tovuq, ranch sousi va ko'katlar", 68000, "pizza", "Yangi"),
    ("Onion rings", "Qarsildoq piyoz halqalari, 8 dona", 22000, "snack", "Qarsildoq"),
    ("Cheese sticks", "Cho'ziluvchan pishloq tayoqchalari", 28000, "snack", "Pishloqli"),
    ("Loaded fries", "Fri, cheddar sousi va ko'katlar", 31000, "snack", "Bestseller"),
    ("Potato wedges", "Ziravorli pech kartoshkasi va dip", 23000, "snack", "Yumshoq"),
    ("Nachos cheese", "Nachos chipslari va pishloqli salsa", 26000, "snack", "Qarsildoq"),
    ("Caesar salad", "Tovuq, parmesan, salat bargi va sous", 37000, "snack", "Yengil"),
    ("Coleslaw salad", "Yangi karam va sabzili salat", 17000, "snack", "Yangi"),
    ("Garlic bread", "Sarimsoqli sous va pishloqli non", 21000, "snack", "Issiq"),
    ("Classic cola", "Muzdek gazlangan ichimlik, 0.5 l", 12000, "drink", "Muzdek"),
    ("Orange fizz", "Apelsinli gazlangan ichimlik", 15000, "drink", "Mevali"),
    ("Berry milkshake", "Qulupnay va rezavorli quyuq kokteyl", 24000, "drink", "Shirin"),
    ("Chocolate milkshake", "Kakao bilan sutli kokteyl", 25000, "drink", "Shirin"),
    ("Iced coffee", "Muz, sut va yangi damlangan qahva", 22000, "drink", "Sovuq qahva"),
    ("Mango smoothie", "Mango va yogurtli mevali smuzi", 26000, "drink", "Mevali"),
    ("Peach iced tea", "Shaftolili muzdek choy", 16000, "drink", "Yozgi"),
    ("Mineral water", "Gazlangan yoki gazlanmagan suv, 0.5 l", 7000, "drink", "Yengil"),
]

CATEGORY_IMAGES = {
    "burger": [
        "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?auto=format&fit=crop&w=900&q=85",
        "https://images.unsplash.com/photo-1553979459-d2229ba7433a?auto=format&fit=crop&w=900&q=85",
    ],
    "chicken": [
        "https://images.unsplash.com/photo-1626082927389-6cd097cdc6ec?auto=format&fit=crop&w=900&q=85",
        "https://images.unsplash.com/photo-1562967914-608f82629710?auto=format&fit=crop&w=900&q=85",
    ],
    "pizza": [
        "https://images.unsplash.com/photo-1628840042765-356cda07504e?auto=format&fit=crop&w=900&q=85",
        "https://images.unsplash.com/photo-1579751626657-72bc17010498?auto=format&fit=crop&w=900&q=85",
    ],
    "snack": [
        "https://images.unsplash.com/photo-1573080496219-bb080dd4f877?auto=format&fit=crop&w=900&q=85",
        "https://images.unsplash.com/photo-1630384060421-cb20d0e0649d?auto=format&fit=crop&w=900&q=85",
    ],
    "drink": [
        "https://images.unsplash.com/photo-1513558161293-cdaf765edfd7?auto=format&fit=crop&w=900&q=85",
        "https://images.unsplash.com/photo-1517701604599-bb29b565090c?auto=format&fit=crop&w=900&q=85",
    ],
}

MENU_ITEMS = [
    {
        "name": name,
        "description": description,
        "price": price,
        "price_text": f"{price:,}".replace(",", " "),
        "category": category,
        "label": label,
        "image": CATEGORY_IMAGES[category][index % len(CATEGORY_IMAGES[category])],
    }
    for index, (name, description, price, category, label) in enumerate(PRODUCTS)
]


def home(request):
    return render(request, "menu/home.html", {"menu_items": MENU_ITEMS})