from .models import CarListing

def load_data():

    data_list = [
        {
        "company": "Toyota",
        "category": "Japanese",
        "looking_for": "High Quality Car for commute, Best in class quality car with high gas mileage, Very Safe Car",
        "specifications": "30 miles per gallon mpg, #1 in Quality, 5 star crash rating",
        "car_type": "Family Sedan, Small Suv",
        "ppc_score": 80
    },
    {
        "company": "Jeep",
        "category": "American",
        "looking_for": "Vehicle that is good on highway, Vehicle that is good for offroading, Vehicle with high brand value",
        "specifications": "Mac Suspension, 50 mm of ground clearance",
        "car_type": "Large SUV",
        "ppc_score": 90
    },
    {
        "company": "Tesla",
        "category": "American",
        "looking_for": "I want the best electric car, Electric car less than 60,000 us dollars, Electric car with high technology, Electric car with auto driving mode",
        "specifications": "200 miles range between charge, 58000 usd price, Autonomous driving",
        "car_type": "Family Sedan, Fully Electric",
        "ppc_score": 95
    },
    {
        "company": "Ford",
        "category": "American",
        "looking_for": "I want a semi pickup truck which is electric, I want a truck which is reliable",
        "specifications": "200 miles range between charge, First Time Quality",
        "car_type": "Semi Pickup Electric Truck",
        "ppc_score": 85
    },
    {
        "company": "Gladiator",
        "category": "American",
        "looking_for": "I want a semi pickup truck which is reliable",
        "specifications": "10 year warranty",
        "car_type": "Semi Pickup Truck",
        "ppc_score": 80
    },
    {
        "company": "Kia",
        "category": "Korean",
        "looking_for": "Family electric car which is less than 40,000 us dollars",
        "specifications": "38000 usd",
        "car_type": "family 4 door electric",
        "ppc_score": 80
    },
    {
        "company": "Honda",
        "category": "Japanese",
        "looking_for": "I want a sports car that goes from 0 to 60 mph in less than 5 seconds",
        "specifications": "0 to 60 in < 5 seconds",
        "car_type": "2 door sports car",
        "ppc_score": 50
    },
    {
        "company": "Hyundai",
        "category": "Korean",
        "looking_for": "Looking for a budget car that is safe",
        "specifications": "5 star safety rating, less than 25,000 us dollars",
        "car_type": "family sedan, budget",
        "ppc_score": 80
    }
    ]
    CarListing.objects.bulk_create([CarListing(**data) for data in data_list])


