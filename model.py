import random
import uuid
from models import Base, Author, Recipe, Ingredients, Category, Includes, Consists, s
from sqlalchemy.sql import exists

starter = ["Tomato Soup", "Minestrone", "Clam Chowder", "Butternut Squash Soup", "French Onion Soup",
           "Chicken Noodle Soup",
           "Gazpacho", "Lentil Soup", "Split Pea Soup", "Potato Leek Soup", "Cream of Mushroom Soup", "Miso Soup",
           "Chicken and Rice Soup", "Beef Stew", "Goulash", "Chili", "Tortilla Soup", "Corn Chowder",
           "Cabbage Soup",
           "Borscht", "Wonton Soup", "Hot and Sour Soup", "Egg Drop Soup", "Pho", "Ramen", "Chow Mein", "Udon Soup",
           "Vichyssoise", "Gazpacho Andaluz", "Avgolemono Soup", "Chicken and Dumplings", "Matzo Ball Soup",
           "Beef Barley Soup", "New England Clam Chowder", "Lobster Bisque", "Oyster Stew", "Tom Yum Soup",
           "Tom Kha Gai", "Beef Noodle Soup", "Beef and Vegetable Soup", "Minced Beef Soup", "Meatball Soup",
           "Chicken Gumbo", "Jambalaya", "Crawfish Etouffee", "Shrimp and Corn Chowder",
           "Chicken and Sausage Gumbo",
           "Seafood Bisque", "Chicken Tortilla Soup", "Chicken Posole", "Cheddar Broccoli Soup", "Pumpkin Soup",
           "Carrot Ginger Soup", "Broccoli Cheddar Soup", "Mushroom Bisque", "Spinach Soup", "Leek and Potato Soup",
           "Chicken and Wild Rice Soup", "Cream of Asparagus Soup", "Cream of Artichoke Soup",
           "Roasted Red Pepper Soup",
           "Avocado Soup", "Asparagus and Pea Soup", "Beet Soup", "Sweet Potato Soup", "Cream of Celery Soup",
           "Spinach and Lentil Soup", "Potato Corn Chowder", "Cream of Spinach Soup", "Onion and Garlic Soup",
           "Cream of Tomato Soup", "Italian Wedding Soup", "Bok Choy Soup", "Roasted Butternut Squash Soup",
           "Navy Bean Soup", "Wild Mushroom Soup", "Tuscan Bean Soup", "Chickpea Soup", "Moroccan Lentil Soup",
           "Pea and Ham Soup", "Cream of Chicken Soup", "Cream of Turkey Soup", "Chicken and Leek Soup",
           "Chicken Mulligatawny",
           "Chicken and Rice Soup with Saffron", "Cream of Chicken and Mushroom Soup",
           "Cream of Chicken and Rice Soup",
           "Chicken and Lentil Soup", "Chicken and Barley Soup", "Chicken and Black Bean Soup",
           "Chicken and Couscous Soup",
           "Chicken and Chickpea Soup", "Chicken and Sweet Potato Soup", "Chicken and Corn Soup",
           "Chicken and Potato Soup",
           "Chicken and Mushroom Soup with Thyme", "Chicken and Rice Soup with Curry", "Chicken and Vegetable Soup",
           "Chicken and Rice Soup with Lemon", "Chicken and Rice Soup with Cilantro"]
main_course = ["Spaghetti Carbonara", "Beef Stroganoff", "Chicken Alfredo", "Chicken Parmesan", "Shrimp Scampi",
               "Pad Thai", "Beef and Broccoli",
               "Lobster Bisque", "Lamb Kebabs", "Chicken Fajitas", "Garlic Butter Shrimp",
               "Beef and Mushroom Stir-Fry",
               "Honey Glazed Salmon", "Lemon Garlic Butter Shrimp", "Sesame Chicken", "Cajun Jambalaya",
               "Mushroom Risotto",
               "Chicken Tikka Masala", "Baked Ziti", "Crispy Pork Belly", "Lemon Butter Garlic Shrimp",
               "Chicken Marsala",
               "Sweet and Sour Chicken", "Tandoori Chicken", "Coconut Curry Chicken", "Chicken and Rice Casserole",
               "Honey Garlic Shrimp", "Pork Chops with Apples", "Chicken Stroganoff", "Beef and Noodles",
               "Honey Mustard Salmon",
               "Lemon Pepper Chicken", "Mongolian Beef", "Teriyaki Chicken", "Creamy Garlic Shrimp",
               "Garlic Parmesan Shrimp",
               "Beef with Broccoli", "Lemon Herb Roast Chicken", "Shrimp and Grits", "Pineapple Teriyaki Chicken",
               "Garlic Parmesan Chicken", "Orange Chicken", "Chicken Cacciatore", "Peppered Steak",
               "Shrimp Fettuccine Alfredo",
               "Chicken Coconut Curry", "Beef Stir-Fry", "Lemon Pepper Salmon", "Beef and Vegetable Stir-Fry",
               "Pork Tenderloin with Apples", "Chicken Fried Rice", "Garlic Butter Shrimp Pasta", "Shrimp Stir-Fry",
               "Beef and Green Bean Stir-Fry", "Chicken and Mushroom Risotto", "Lemon Herb Roast Salmon",
               "Chicken Florentine",
               "Honey Mustard Chicken", "Chicken Gumbo", "Teriyaki Beef", "Pork and Apple Stir-Fry",
               "Creamy Garlic Shrimp Pasta",
               "Garlic Parmesan Shrimp Pasta", "Beef and Asparagus Stir-Fry", "Shrimp Alfredo",
               "Chicken and Leek Risotto",
               "Lemon Herb Roast Pork", "Beef and Snow Pea Stir-Fry", "Chicken Enchiladas", "Miso Salmon",
               "Chicken and Artichoke Risotto",
               "Garlic Butter Shrimp and Broccoli", "Chicken and Spinach Risotto", "Beef and Carrot Stir-Fry",
               "Orange Shrimp",
               "Chicken and Sun-Dried Tomato Risotto", "Teriyaki Chicken and Pineapple",
               "Beef and Bok Choy Stir-Fry",
               "Pork and Pear Stir-Fry", "Chicken and Mango Risotto", "Shrimp Scampi Linguine",
               "Garlic Butter Shrimp and Asparagus",
               "Chicken and Red Pepper Risotto", "Lemon Herb Roast Lamb", "Beef and Red Pepper Stir-Fry",
               "Garlic Parmesan Shrimp and Broccoli", "Teriyaki Beef and Broccoli", "Chicken and Zucchini Risotto",
               "Honey Mustard Chicken and Potatoes", "Creamy Garlic Shrimp and Spinach",
               "Beef and Eggplant Stir-Fry",
               "Garlic Butter Shrimp and Spinach", "Chicken and Asparagus Risotto",
               "Lemon Herb Roast Chicken and Potatoes",
               "Mongolian Beef and Broccoli", "Chicken and Mushroom Risotto", "Lemon Pepper Salmon and Asparagus",
               "Beef and Snow Pea Stir-Fry", "Pork and Brussels Sprouts Stir-Fry",
               "Garlic Parmesan Shrimp and Spinach",
               "Chicken and Butternut Squash Risotto"]
dessert = ["Chocolate Cake", "Apple Pie", "Cheesecake", "Strawberry Shortcake",
           "Tiramisu", "Brownies", "Red Velvet Cake", "Ice Cream Sundae", "Lemon Bars", "Pumpkin Pie",
           "Chocolate Chip Cookies",
           "Key Lime Pie", "Banana Split", "Carrot Cake", "Cupcakes", "Rice Pudding", "Blueberry Muffins",
           "Peach Cobbler",
           "Fruit Salad", "Panna Cotta", "Chocolate Mousse", "Lava Cake", "Coconut Macaroons", "Bread Pudding",
           "Cherry Pie",
           "Peanut Butter Cookies", "Caramel Flan", "Strawberry Cheesecake", "Chocolate Brownies", "Apple Crisp",
           "Pecan Pie",
           "Lemon Meringue Pie", "Oatmeal Cookies", "Chocolate Fondue", "Vanilla Ice Cream", "Lemon Sorbet",
           "Fudge Brownies",
           "Chocolate Eclairs", "Creme Brulee", "Raspberry Sorbet", "Chocolate Souffle", "Butter Pecan Ice Cream",
           "Tropical Fruit Salad", "Fruit Tart", "Cheese Danish", "Molten Chocolate Cake",
           "Chocolate Covered Strawberries",
           "Cannoli", "Peach Melba", "Chocolate Pudding", "Gelato", "Cherry Cheesecake", "Cinnamon Rolls",
           "Pineapple Upside-Down Cake", "Mango Sorbet", "Caramel Apple", "Strawberry Shortcake",
           "Chocolate Lava Cake",
           "White Chocolate Mousse", "Pumpkin Cheesecake", "Pistachio Ice Cream", "Cherry Pie", "Oreo Cookies",
           "Key Lime Pie",
           "Fruit Sorbet", "Chocolate Tiramisu", "Caramel Flan", "Lemon Bars", "Chocolate Muffins", "Rhubarb Pie",
           "Snickerdoodle Cookies", "Banana Cream Pie", "Toasted Marshmallows", "Berry Parfait",
           "Ricotta Cheesecake",
           "Pineapple Cake", "Lemon Tarts", "Coconut Cream Pie", "Peanut Butter Brownies", "Chocolate Crepes",
           "Mint Chocolate Chip Ice Cream", "Peach Cobbler", "Lemon Cake", "Blueberry Pie",
           "Chocolate Creme Brulee",
           "Red Velvet Cupcakes", "Butterscotch Pudding", "Apple Turnovers", "Pumpkin Muffins", "Cinnamon Bread",
           "Berry Trifle", "Vanilla Panna Cotta", "Mango Sorbet", "Cheese Blintzes", "Chocolate Lava Cake",
           "Chocolate Cherry Trifle", "Caramel Popcorn", "Raspberry Mousse", "Butter Pecan Cake", "Kiwi Sorbet",
           "Pineapple Upside-Down Cake", "Ricotta Cannoli", "Peach Melba", "Lemon Meringue Pie"]
category_type = ["Starter", "Main course", "Dessert"]
category_difficulty = ["Difficult", "Medium", "Easy"]
country = ["Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda", "Argentina", "Armenia",
           "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belgium",
           "Belize", "Benin", "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", "Brunei", "Bulgaria",
           "Burkina Faso", "Burundi", "Cabo Verde", "Cambodia", "Cameroon", "Canada", "Central African Republic",
           "Chad", "Chile", "Colombia", "Comoros", "Congo (Congo-Brazzaville)", "Costa Rica", "Croatia",
           "Cuba", "Cyprus", "Czechia (Czech Republic)", "Democratic Republic of the Congo (Congo-Kinshasa)",
           "Denmark", "Djibouti", "Dominica", "Dominican Republic", "East Timor", "Ecuador", "Egypt", "El Salvador",
           "Equatorial Guinea", "Eritrea", "Estonia", "Eswatini", "Ethiopia", "Fiji", "Finland", "France", "Gabon",
           "Gambia", "Georgia", "Germany", "Ghana", "Greece", "Grenada", "Guatemala", "Guinea", "Guinea-Bissau",
           "Guyana", "Haiti", "Honduras", "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland",
           "Israel", "Italy", "Ivory Coast", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati",
           "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein",
           "Lithuania"]
ingredients = ["Salt", "Pepper", "Garlic", "Onion", "Olive oil", "Lemon", "Basil", "Parsley", "Thyme", "Rosemary",
               "Sage", "Oregano", "Cumin", "Coriander", "Cilantro", "Paprika", "Cayenne pepper", "Ginger", "Turmeric",
               "Cinnamon", "Nutmeg", "Cloves", "Bay leaves", "Mustard seeds", "Soy sauce", "Worcestershire sauce",
               "Vinegar", "Ketchup", "Mayonnaise", "Mustard", "Honey", "Brown sugar", "White sugar", "Maple syrup",
               "Molasses", "Peanut butter", "Almond butter", "Sesame seeds", "Coconut milk", "Sour cream", "Yogurt",
               "Milk", "Cream", "Butter", "Cheese", "Eggs", "Flour", "Cornstarch", "Baking powder", "Baking soda",
               "Cocoa powder", "Vanilla extract", "Almond extract", "Lime zest", "Orange zest", "Pecans", "Walnuts",
               "Cashews", "Hazelnuts", "Macadamia nuts", "Pistachios", "Sunflower seeds", "Pumpkin seeds", "Quinoa",
               "Rice", "Pasta", "Bread", "Couscous", "Barley", "Bulgur", "Lentils", "Chickpeas", "Black beans",
               "Kidney beans", "Cannellini beans", "Lima beans", "Green peas", "Carrots", "Celery", "Bell peppers",
               "Cucumbers", "Tomatoes", "Zucchini", "Mushrooms", "Spinach", "Kale", "Lettuce", "Cabbage", "Broccoli",
               "Cauliflower", "Eggplant", "Asparagus", "Green beans", "Radishes", "Beets", "Sweet potatoes", "Potatoes",
               "White cabbage"]


class Model:
    def __init__(self):

        self.create_tables()


    def create_tables(self):

        if not s.query(Author).first():
            Base.metadata.create_all(s.get_bind())

        s.commit()

    def generate_login(self):
        login = (
                chr(random.randint(65, 114)) +
                chr(random.randint(65, 90)) +
                chr(random.randint(65, 90)) +
                chr(random.randint(65, 90))
        )
        return login

    def generate_id(self):
        return str(uuid.uuid4())

    def add_author(self, name, password):
        login = self.generate_login()
        author = Author(Login=login, Name=name, Password=password)
        s.add(author)
        s.commit()
        return author.Login

    def add_recipe(self, login, name, calories, cooking_time, photos, steps, difficulty, type_, recipe_country):

        recipe_id = self.generate_id()

        author = s.query(Author).filter_by(Login=login).first()
        if not author:
            raise ValueError("Author with this login was not found.")

        category = s.query(Category).filter_by(Difficulty=difficulty, Type=type_, Country=recipe_country).first()
        if not category:
            category_id = self.add_category(difficulty, type_, recipe_country)
        else:
            category_id = category.Category_ID

        recipe = Recipe(
            Recipe_ID=recipe_id,
            Author_login=author.Login,
            Name=name,
            Calories=calories,
            Time=cooking_time,
            Photos=photos,
            Steps=steps
        )

        s.add(recipe)
        s.commit()

        includes = Includes(Recipe_FK=recipe_id, Category_FK=category_id)
        s.add(includes)
        s.commit()

        return recipe.Recipe_ID

    def add_ingredient(self, name, recipe_id, amount, measurement_unit, temperature):
        ingredient_id = self.generate_id()
        ingredient = Ingredients(Ingredients_ID=ingredient_id, Name=name)
        s.add(ingredient)
        s.commit()

        consists = Consists(
            Recipe_FK=recipe_id,
            Ingredients_FK=ingredient.Ingredients_ID,
            Amount=amount,
            Measurement_unit=measurement_unit,
            Temperature=temperature
        )
        s.add(consists)
        s.commit()

        return ingredient.Ingredients_ID

    def add_category(self, difficulty, type_, recipe_country):
        category_id = self.generate_id()
        category = Category(Category_ID=category_id, Difficulty=difficulty, Type=type_, Country=recipe_country)
        s.add(category)
        s.commit()
        return category.Category_ID

    def update_author(self, login, name, password):
        author = s.query(Author).filter_by(Login=login).first()

        if author:
            author.Name = name
            author.Password = password
            s.commit()
        else:
            print(f"Author with this login was not found.")

    def update_recipe(self, recipe_id, author_login, name, calories, cooking_time, photos, steps, difficulty, type_, recipe_country):
        recipe = s.query(Recipe).filter_by(Recipe_ID=recipe_id).first()

        if recipe:
            recipe.Author_login = author_login
            recipe.Name = name
            recipe.Calories = calories
            recipe.Time = cooking_time
            recipe.Photos = photos
            recipe.Steps = steps

            category = s.query(Category).filter_by(Difficulty=difficulty, Type=type_, Country=recipe_country).first()

            if not category:
                category = self.add_category(difficulty, type_, recipe_country)

            includes = s.query(Includes).filter_by(Recipe_FK=recipe_id).first()

            if includes:
                includes.Category_FK = category.Category_ID

            s.commit()
        else:
            print(f"Recipe with this ID was not found.")

    def update_ingredient(self, ingredient_id, name, recipe_id, amount, measurement_unit, temperature):
        ingredient = s.query(Ingredients).filter_by(Ingredients_ID=ingredient_id).first()

        if ingredient:
            ingredient.Name = name
            ingredient.Recipe_id = recipe_id

            consists = s.query(Consists).filter_by(Ingredients_FK=ingredient_id, Recipe_FK=recipe_id).first()
            if consists:
                consists.Amount = amount
                consists.Measurement_unit = measurement_unit
                consists.Temperature = temperature
                s.commit()
        else:
            print(f"Ingredient with this ID was not found.")

    def update_category(self, category_id, difficulty, type_, recipe_country):
        category = s.query(Category).filter_by(Category_ID=category_id).first()
        if category:
            category.Difficulty = difficulty
            category.Type = type_
            category.Country = recipe_country
            s.commit()
        else:
            print(f"Category with this ID was not found.")

    def delete_author(self, login):
        author = s.query(Author).filter_by(Login=login).first()

        if not author:
            print(f"Author with this ID was not found.")
            return

        recipes = s.query(Recipe).filter_by(Author_login=login).all()

        if recipes:
            raise ValueError("Cannot delete author with existing recipes.")

        s.delete(author)
        s.commit()

    def delete_recipe(self, recipe_id):
        recipe = s.query(Recipe).filter_by(Recipe_ID=recipe_id).first()

        if not recipe:
            print(f"Recipe with this ID was not found.")
            return

        s.query(Consists).filter_by(Recipe_FK=recipe_id).delete()
        s.query(Includes).filter_by(Recipe_FK=recipe_id).delete()
        s.delete(recipe)
        s.commit()

    def delete_ingredient(self, ingredient_id):
        ingredient = s.query(Ingredients).filter_by(Ingredients_ID=ingredient_id).first()

        if not ingredient:
            print(f"Ingredient with this ID was not found.")
            return

        consists = s.query(Consists).filter_by(Ingredients_FK=ingredient_id).all()

        if consists:
            raise ValueError("Cannot delete ingredient which consists in recipe.")

        s.delete(ingredient)
        s.commit()

    def delete_category(self, category_id):
        category = s.query(Category).filter_by(Category_ID=category_id).first()

        if not category:
            print(f"Category with this ID was not found.")
            return

        includes = s.query(Includes).filter_by(Category_FK=category_id).all()

        if includes:
            raise ValueError("Cannot delete category which includes recipe.")

        s.delete(category)
        s.commit()


    def generate_dish(self, dish_type):
        if dish_type == "starter":
            dish = random.choice(starter)
        elif dish_type == "main course":
            dish = random.choice(main_course)
        else:
            dish = random.choice(dessert)

        return dish

    def get_authors(self):
        authors = s.query(Author.Login, Author.Name, Author.Password).all()
        return authors

    def get_recipes(self):
        recipes = s.query(
            Recipe.Recipe_ID, Recipe.Author_login, Recipe.Name,
            Recipe.Calories, Recipe.Time, Recipe.Photos, Recipe.Steps
        ).all()
        return recipes

    def get_ingredients(self):
        ingredients = s.query(Ingredients.Ingredients_ID, Ingredients.Name).all()
        return ingredients

    def get_categories(self):
        categories = s.query(Category.Category_ID, Category.Difficulty, Category.Type, Category.Country).all()
        return categories

    def get_includes(self):
        includes = s.query(Includes.Recipe_FK, Includes.Category_FK).all()
        return includes

    def get_consists(self):
        consists = s.query(
            Consists.Recipe_FK, Consists.Ingredients_FK,
            Consists.Amount, Consists.Measurement_unit, Consists.Temperature
        ).all()
        return consists

    def author_exists(self, login):
        return bool(s.query(exists().where(Author.Login == login)).scalar())

    def recipe_exists(self, recipe_id):
        return bool(s.query(exists().where(Recipe.Recipe_ID == recipe_id)).scalar())

    def ingredient_exists(self, ingredient_id):
        return bool(s.query(exists().where(Ingredients.Ingredients_ID == ingredient_id)).scalar())

    def category_id_exists(self, category_id):
        return bool(s.query(exists().where(Category.Category_ID == category_id)).scalar())

    def category_param_exists(self, difficulty, type_, recipe_country):
        return bool(s.query(exists().where(Category.Difficulty == difficulty, Category.Type == type_, Category.Country == recipe_country)).scalar())

