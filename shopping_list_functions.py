class ShoppingListFunctions:

    def __init__(self):
        self.list_of_vars = []
        self.shopping_list = {}
        self.week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        self.meals = ["Breakfast", "Dinner", "Supper", "Snack"]

    def make_shopping_list(self, data):
        # If value of checkboxes is equal 1 (True) -> add appropriate products to shopping list
        for var in range(len(self.list_of_vars)):
            if self.list_of_vars[var].get() == 1:
                # Calculate day and meal based on index
                chosen_day = self.week_days[int(var / 8)]
                chosen_meal = self.meals[int((var % 8) / 2)]

                for k, v in data[chosen_day][chosen_meal].items():
                    if k not in self.shopping_list:
                        self.shopping_list[k] = v
                    else:
                        self.shopping_list[k] = self.shopping_list[k] + v

        all_products = ""
        for k, v in self.shopping_list.items():
            all_products += f"{k}: {v} \n"

        return all_products
