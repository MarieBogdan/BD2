class View:

    def show_menu(self):
        self.show_message("\nChoose a table you want to edit or to make a request:")
        self.show_message("1. Author")
        self.show_message("2. Recipe")
        self.show_message("3. Ingredients")
        self.show_message("4. Category")

        return input("\nEnter your choice: ")

    def show_author_menu(self):
        self.show_message("\nChoose what you want to do:")
        self.show_message("1. Add author")
        self.show_message("2. Update author")
        self.show_message("3. Delete author")
        self.show_message("4. Quit")

        return input("\nEnter your choice: ")

    def show_recipe_menu(self):
        self.show_message("\nChoose what you want to do:")
        self.show_message("1. Add recipe")
        self.show_message("2. Update recipe")
        self.show_message("3. Delete recipe")
        self.show_message("4. Quit")

        return input("\nEnter your choice: ")

    def show_ingredients_menu(self):
        self.show_message("\nChoose what you want to do:")
        self.show_message("1. Add ingredient")
        self.show_message("2. Update ingredient")
        self.show_message("3. Delete ingredient")
        self.show_message("4. Quit")

        return input("\nEnter your choice: ")

    def show_category_menu(self):
        self.show_message("\nChoose what you want to do:")
        self.show_message("1. Add category")
        self.show_message("2. Update category")
        self.show_message("3. Delete category")
        self.show_message("4. Quit")

        return input("\nEnter your choice: ")

    def get_authors_input(self):
        name = input("Enter author`s name: ")
        password = input("Enter password: ")
        return name, password

    def get_recipe_input(self):
        login = input("Enter author's login: ")
        name = input("Enter recipes`s name: ")
        calories = input("Enter recipes`s calories: ")
        time = input("Enter recipes`s time: ")
        photos = input("Enter path to recipes`s photos: ")
        steps = input("Enter recipes`s steps: ")

        return login, name, calories, time, photos, steps

    def get_recipe_id(self):
        recipe_id = input("Enter recipe id: ")

        return recipe_id

    def get_login(self):
        login = input("Enter author's login: ")

        return login

    def get_number(self):
        number_of_data = input("Enter number of data to generate: ")

        return number_of_data
    def get_ingredient_input(self):
        name = input("Enter ingredient`s name: ")
        recipe_id = input("Enter recipe's id for which you need this ingredient: ")
        amount = input("Enter amount of the ingredient: ")
        measurement_unit = input("Enter measurement unit for this ingredient: ")
        temperature = input("Enter temperature of the ingredient: ")

        return name, recipe_id, amount, measurement_unit, temperature

    def get_ingredient_id(self):
        ingredient_id = input("Enter ingredient id: ")

        return ingredient_id

    def get_category_id(self):
        category_id = input("Enter category id: ")

        return category_id

    def get_difficulty_input(self):
        difficulty = input("Enter dish`s difficulty(Difficult, Medium, Easy): ")

        return difficulty

    def get_type_input(self):
        type_ = input("Enter dish`s type(Starter, Main course, Dessert): ")

        return type_

    def get_country_input(self):
        country = input("Enter dish`s country: ")

        return country

    def show_authors_login(self, login):
        print("Author's login is: ", login)

    def show_recipe_id(self, recipe_id):
        print("Recipe id is: ", recipe_id)

    def show_message(self, message):
        print(message)

    def display_author_table(self, authors):
        print("\nAuthor Table")

        headers = ["#", "Login", "Name", "Password"]

        authors_num = [[str(i + 1)] + list(author) for i, author in enumerate(authors)]

        all_data = [headers] + authors_num

        max_lengths = [max(map(len, column)) for column in zip(*all_data)]

        headers_formatted = [header.center(max_lengths[i]) for i, header in enumerate(headers)]
        print(" | ".join(headers_formatted))
        print("-" * sum(max_lengths + [3 * len(max_lengths)]))

        for author in authors_num:
            formatted_data = [str(value).center(max_lengths[i]) for i, value in enumerate(author)]
            print(" | ".join(formatted_data))

    def display_recipe_table(self, recipes):
        print("\nRecipe Table")

        headers = ["#", "Recipe_ID", "Author_login", "Name", "Calories", "Time", "Photos", "Steps"]

        recipes_num = [(i + 1,) + tuple(recipe) for i, recipe in enumerate(recipes)]

        all_data = [headers] + recipes_num

        max_lengths = [max(map(lambda x: len(str(x)), column)) for column in zip(*all_data)]

        headers_formatted = [header.center(max_lengths[i]) for i, header in enumerate(headers)]
        print(" | ".join(headers_formatted))
        print("-" * sum(max_lengths + [3 * len(max_lengths)]))

        for recipe in recipes_num:
            formatted_data = [str(value).center(max_lengths[i]) for i, value in enumerate(recipe)]
            print(" | ".join(formatted_data))

    def display_ingredients_table(self, ingredients):
        print("\nIngredients Table")

        headers = ["#", "Ingredients_ID", "Name"]

        ingredients_num = [(i + 1,) + tuple(ingredient) for i, ingredient in enumerate(ingredients)]

        all_data = [headers] + ingredients_num

        max_lengths = [max(map(lambda x: len(str(x)), column)) for column in zip(*all_data)]

        headers_formatted = [header.center(max_lengths[i]) for i, header in enumerate(headers)]
        print(" | ".join(headers_formatted))
        print("-" * sum(max_lengths + [3 * len(max_lengths)]))

        for ingredient in ingredients_num:
            formatted_data = [str(value).center(max_lengths[i]) for i, value in enumerate(ingredient)]
            print(" | ".join(formatted_data))

    def display_category_table(self, categories):
        print("\nCategory Table")

        headers = ["#", "Category_ID", "Difficulty", "Type", "Country"]

        categories_num = [(i + 1,) + tuple(category) for i, category in enumerate(categories)]

        all_data = [headers] + categories_num

        max_lengths = [max(map(lambda x: len(str(x)), column)) for column in zip(*all_data)]

        headers_formatted = [header.center(max_lengths[i]) for i, header in enumerate(headers)]
        print(" | ".join(headers_formatted))
        print("-" * sum(max_lengths + [3 * len(max_lengths)]))

        for category in categories_num:
            formatted_data = [str(value).center(max_lengths[i]) for i, value in enumerate(category)]
            print(" | ".join(formatted_data))

    def display_consists_table(self, consists_values):
        print("\nConsists Table")

        headers = ["Recipe_FK", "Ingredients_FK", "Amount", "Measurement unit", "Temperature"]

        all_data = [headers] + consists_values

        max_lengths = [max(map(lambda x: len(str(x)), column)) for column in zip(*all_data)]

        headers_formatted = [header.center(max_lengths[i]) for i, header in enumerate(headers)]
        print(" | ".join(headers_formatted))
        print("-" * sum(max_lengths + [3 * len(max_lengths)]))

        for consists_value in consists_values:
            formatted_data = [str(value).center(max_lengths[i]) for i, value in enumerate(consists_value)]
            print(" | ".join(formatted_data))

    def display_includes_table(self, includes_values):
        print("\nIncludes Table")

        headers = ["Recipe_FK", "Category_FK"]

        all_data = [headers] + includes_values

        max_lengths = [max(map(lambda x: len(str(x)), column)) for column in zip(*all_data)]

        headers_formatted = [header.center(max_lengths[i]) for i, header in enumerate(headers)]
        print(" | ".join(headers_formatted))
        print("-" * sum(max_lengths + [3 * len(max_lengths)]))

        for includes_value in includes_values:
            formatted_data = [str(value).center(max_lengths[i]) for i, value in enumerate(includes_value)]
            print(" | ".join(formatted_data))





