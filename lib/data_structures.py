spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]


def get_names(spicy_foods):
    return [food_name["name"] for food_name in spicy_foods]


print(get_names(spicy_foods))


def get_spiciest_foods(spicy_foods):
    return [
        spiciest_food
        for spiciest_food in spicy_foods
        if spiciest_food["heat_level"] > 5
    ]


print(get_spiciest_foods(spicy_foods))


def print_spicy_foods(spicy_foods):
    for spicy_food in spicy_foods:
        heat_level = "🌶" * spicy_food["heat_level"]
        print(
            f"{spicy_food['name']} ({spicy_food['cuisine']}) | Heat Level: {heat_level}"
        )


print_spicy_foods(spicy_foods)


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for spicy_food_by_cuisine in spicy_foods:
        if spicy_food_by_cuisine["cuisine"] == cuisine:
            return spicy_food_by_cuisine
    return None


print("Food by cuisine is: ", get_spicy_food_by_cuisine(spicy_foods, "American"))


def print_spiciest_foods(spicy_foods):
    for spiciest_foods in spicy_foods:
        if spiciest_foods["heat_level"] >= 5:
            heat_level = "🌶" * spiciest_foods["heat_level"]
            print(
                f"{spiciest_foods['name']} ({spiciest_foods['cuisine']}) | Heat Level: {heat_level}"
            )


print_spiciest_foods(spicy_foods)


def get_average_heat_level(spicy_foods):
    total_heat = sum([food_heat_level["heat_level"] for food_heat_level in spicy_foods])
    average_heat = total_heat / len(spicy_foods)
    return round(average_heat, 2)


print("average heat level is:", get_average_heat_level(spicy_foods))


def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods


spicy_food = {"name": "Vindaloo", "cuisine": "Indian", "heat_level": 8}


print(create_spicy_food(spicy_foods, spicy_food))
