#### БД ДЛЯ ОТЗЫВОВ

replies_db = [
    {
        "id": 1,
        "username": "Алекс Стейн",
        "cartype": "Hyundai Elantra",
        "date": "21-07-2022",
        "rating": 4,
        "image_url": "/avatars/user1.jpg",
        "text": "Отличная машина для города — экономичная и манёвренная. Удобный салон, тихая работа двигателя. Езжу уже 2 года — доволен."
    },
    {
        "id": 2,
        "username": "Марина Власова",
        "cartype": "Tesla Model S",
        "date": "10-03-2023",
        "rating": 5,
        "image_url": "/avatars/user1.jpg",
        "text": "Настоящее будущее на колёсах. Быстрая, бесшумная и с впечатляющим автопилотом. Заряжаю дома, и этого хватает на неделю."
    },
    {
        "id": 3,
        "username": "Олег Карпов",
        "cartype": "Volkswagen Golf",
        "date": "05-09-2022",
        "rating": 3,
        "image_url": "/avatars/user1.jpg",
        "text": "Неплохой вариант для повседневных поездок. Есть ощущение, что подвеска могла бы быть мягче. В остальном — надёжный авто."
    },
    {
        "id": 4,
        "username": "Ирина Смирнова",
        "cartype": "BMW X5",
        "date": "17-01-2023",
        "rating": 5,
        "image_url": "/avatars/user1.jpg",
        "text": "Мощный, комфортный, престижный. На трассе — зверь. Расход, конечно, не маленький, но удовольствия — масса."
    },
    {
        "id": 5,
        "username": "Дмитрий Сафронов",
        "cartype": "Toyota Corolla",
        "date": "29-11-2022",
        "rating": 4,
        "image_url": "/avatars/user1.jpg",
        "text": "Классическая рабочая лошадка. Очень надёжный авто. Обслуживание недорогое, в морозы заводится без проблем."
    }
]

######## БД ДЛЯ ПОКУПКИ И АРЕНДЫ АВТО
brands = {
    1: "Toyota", 2: "Nissan", 3: "BMW", 4: "Tesla", 5: "Ford",
    6: "Honda", 7: "Hyundai", 8: "Kia", 9: "Chevrolet", 10: "Mazda"
}

models = {
    1: "Corolla", 2: "Camry", 3: "GT-R", 4: "Model S", 5: "Mustang",
    6: "Civic", 7: "Accord", 8: "Tucson", 9: "Sportage", 10: "Cruze",
    11: "CX-5", 12: "Explorer", 13: "F-150", 14: "Altima", 15: "Elantra",
    16: "Rio", 17: "Impala", 18: "CX-9", 19: "Focus", 20: "Fusion"
}

bodies = {
    1: "Sedan",
    2: "Coupe",
    3: "SUV",
    4: "Hatchback"
}

transmissions = {
    1: "Manual",
    2: "Automatic"
}

engines = {
    1: "Petrol",
    2: "Diesel",
    3: "Hybrid",
    4: "Electric"
}

drives = {
    1: "FWD",
    2: "RWD",
    3: "AWD"
}

generations = ["2010–2014", "2015–2019", "2020+"]
fuel_options = ["50L", "60L", "70L", "80L", "90L", "100L"]
seat_options = ["2 People", "4 People", "5 People", "6 People", "7 People"]

# Возможные значения для генерации
brand_ids = list(range(1, 1 + len(brands)))  # допустим, 10 брендов
model_ids = list(range(1, 1 + len(models)))  # допустим, 20 моделей
body_ids = [1, 2, 3, 4]
transmission_ids = [1, 2]
engine_ids = [1, 2, 3, 4]
drive_ids = [1, 2, 3]

cars_db_sell = []
import random
# Генерация дополнительных записей
for i in range(1, 100):
    price = random.randint(700000, 5000000)
    cars_db_sell.append({
        "id": i,
        "image_url": "/cars/1.png",
        "brand_id": random.choice(brand_ids),
        "model_id": random.choice(model_ids),
        "generation": random.choice(generations),
        "body_id": random.choice(body_ids),
        "transmission_id": random.choice(transmission_ids),
        "engine_id": random.choice(engine_ids),
        "drive_id": random.choice(drive_ids),
        "volume": round(random.uniform(1.2, 6.0), 1),
        "year": random.randint(2010, 2024),
        "mileage": random.randint(10000, 200000),
        "price": price,
        "seats": random.choice(seat_options),
        "fuel": random.choice(fuel_options),
        "is_liked": random.choice([True, False]),
        "old_price": (None
                      if random.random() > 0.5
                      else price + random.randint(20000, 100000))
    })


def add_dict_values(d: list[dict]):
    ans = []
    for row in d:
        new_row = {
                **row,
                "brand": brands.get(row["brand_id"]),
                "model": models.get(row["model_id"]),
                "body": bodies.get(row["body_id"]),
                "transmission": transmissions.get(row["transmission_id"]),
                "engine": engines.get(row["engine_id"]),
                "drive": drives.get(row["drive_id"]),
            }
        ans.append(new_row)

    return ans



########### БД С ШИНАМИ
tire_brands = ["Torgo", "Michelin", "Pirelli", "Bridgestone", "Nokian"]
tire_models = ["MP47", "Energy Saver", "Ice Zero", "Turanza", "Nordman"]
tire_seasons = ["лето", "зима", "всесезон"]
tire_sizes = ["R14 175/65", "R15 185/65", "R16 195/60", "R17 205/55", "R18 225/45"]
tire_load_indexes = ["88T", "91H", "95V", "98W"]

tires_bd = []

for i in range(1, 101):
    tire_brand = random.choice(tire_brands)
    tire_model = random.choice(tire_models)
    tire_size = random.choice(tire_sizes)
    tire_index = random.choice(tire_load_indexes)
    tire_season = random.choice(tire_seasons)
    tire_name = f"Шина {tire_size} {tire_brand} {tire_model} {tire_index} {tire_season}"
    tire_price = random.randint(1000, 8000)
    tire_is_liked = random.choice([True, False])
    var1 = random.choice([1, 2, 3])
    var2 = random.choice([1, 2, 3])

    tires_bd.append({
        "image_url": "/parts/1.jpg",
        "name": tire_name,
        "price": tire_price,
        "is_liked": tire_is_liked,
        "var1": var1,
        "var2": var2
    })


#######
offers_bd = []

offers_names = [
    "Фильтр масляный HYUNDAI/KIA 26300–35505",
    "Фильтр масляный TOYOTA 90915-YZZE2",
    "Фильтр масляный NISSAN 15208-65F0A",
    "Фильтр масляный MANN W 914/2",
    "Фильтр масляный BOSCH 0 451 103 318",
    "Фильтр масляный LADA 2101-1012005-08",
    "Фильтр масляный RENAULT 7700274177"
]

for i, name in enumerate(offers_names, start=1):
    offers_bd.append({
        "image_url": "/parts/2.jpg",
        "id": i,
        "name": name,
        "price": random.randint(400, 900),
        "is_liked": random.choice([True, False])
    })
