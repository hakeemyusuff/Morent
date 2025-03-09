from django.core.management.base import BaseCommand
from car_rental.models import Car

car_data = car_data = [
    {
        "brand": "Suzuki",
        "model": "Vitara",
        "year": 2019,
        "color": "Dark Gray/Slate",
        "description": "The Suzuki Vitara is a compact SUV that combines practicality with a touch of ruggedness. This model features Suzuki's reliable engineering with good ground clearance and lightweight construction for improved fuel efficiency. The Vitara offers a comfortable ride quality, responsive handling, and modern safety features like autonomous emergency braking and adaptive cruise control in higher trim levels.",
        "car_type": "SUV",
        "seat_capacity": 5,
        "transmission_type": "AUTO",
        "fuel_tank_capacity": 47,
        "price_per_day": 45.00,
        "is_available": True,
    },
    {
        "brand": "Volkswagen",
        "model": "Touareg",
        "year": 2020,
        "color": "Brown/Bronze",
        "description": "The Volkswagen Touareg is a premium midsize SUV that blends sophisticated styling with advanced technology and capable performance. This third-generation model features a plush, well-appointed interior with high-quality materials and the impressive Innovision Cockpit system. The Touareg delivers a comfortable yet engaging driving experience with its adaptive air suspension and powerful engine options.",
        "car_type": "SUV",
        "seat_capacity": 5,
        "transmission_type": "AUTO",
        "fuel_tank_capacity": 75,
        "price_per_day": 85.00,
        "is_available": True,
    },
    {
        "brand": "Suzuki",
        "model": "SX4 S-Cross",
        "year": 2019,
        "color": "Dark Gray/Slate",
        "description": "The Suzuki SX4 S-Cross is a practical compact crossover offering an excellent balance of space, features, and value. This model combines city-friendly dimensions with a versatile interior and Suzuki's reliable engineering. The S-Cross provides good fuel economy, comfortable ride quality, and light, predictable handling, making it an ideal vehicle for daily commuting and weekend adventures.",
        "car_type": "SUV",
        "seat_capacity": 5,
        "transmission_type": "AUTO",
        "fuel_tank_capacity": 47,
        "price_per_day": 40.00,
        "is_available": True,
    },
    {
        "brand": "Hyundai",
        "model": "Santa Fe",
        "year": 2021,
        "color": "Black",
        "description": "The Hyundai Santa Fe is a midsize SUV that offers a compelling combination of comfort, technology, and practicality. This fourth-generation model features a bold exterior design with Hyundai's signature cascading grille and distinctive split headlight arrangement. The Santa Fe provides a spacious, well-built interior with premium materials, comprehensive safety features, and efficient powertrain options including hybrid variants.",
        "car_type": "SUV",
        "seat_capacity": 5,
        "transmission_type": "AUTO",
        "fuel_tank_capacity": 67,
        "price_per_day": 65.00,
        "is_available": True,
    },
    {
        "brand": "MG",
        "model": "ZS",
        "year": 2021,
        "color": "Light Blue/Teal",
        "description": "The MG ZS is a stylish compact crossover that delivers excellent value with its combination of attractive design, practical interior, and comprehensive feature set. This model showcases MG's modern design language with a distinctive front grille and contemporary profile. The ZS offers good interior space, user-friendly technology, and a comfortable ride quality, making it an appealing option for budget-conscious families.",
        "car_type": "SUV",
        "seat_capacity": 5,
        "transmission_type": "AUTO",
        "fuel_tank_capacity": 48,
        "price_per_day": 35.00,
        "is_available": True,
    },
    {
        "brand": "MG",
        "model": "HS",
        "year": 2022,
        "color": "Silver/White",
        "description": "The MG HS is a midsize SUV that represents the brand's move upmarket with more premium features and refined design. This model features a distinctive exterior with an assertive front fascia and clean, European-inspired styling. The HS provides a spacious, well-appointed interior with soft-touch materials, a comprehensive infotainment system, and advanced driver assistance features that rival more expensive competitors.",
        "car_type": "SUV",
        "seat_capacity": 5,
        "transmission_type": "AUTO",
        "fuel_tank_capacity": 55,
        "price_per_day": 50.00,
        "is_available": True,
    },
]

class Command(BaseCommand):
    help = "Populate the database with car data"

    def handle(self, *args, **kwargs):
        car_objects = [Car(**data) for data in car_data]
        Car.objects.bulk_create(car_objects)
        self.stdout.write(self.style.SUCCESS("Successfully inserted car data!"))
