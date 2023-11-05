################################################################################
#     ____                          __     _                          _____
#    / __ \  __  __  ___    _____  / /_   (_)  ____    ____          |__  /
#   / / / / / / / / / _ \  / ___/ / __/  / /  / __ \  / __ \          /_ < 
#  / /_/ / / /_/ / /  __/ (__  ) / /_   / /  / /_/ / / / / /        ___/ / 
#  \___\_\ \__,_/  \___/ /____/  \__/  /_/   \____/ /_/ /_/        /____/  
#                                                                          
#  Question 3
################################################################################
#
# Instructions:
# Make a Python class for a magical oven that can combine ingredients at 
# different temperatures to craft special materials.
# 
# The oven class should have the methods:
# - add(item) to add an oven to be combined
# - freeze() to freeze the ingredients
# - boil() to boil the ingredients
# - wait() to combine the ingredients with no change in temperature
# - get_output() to get the result 
#
# You will need to change the `make_oven()` function to return a new instance
# of your oven.
#
# The `alchemy_combine()` function will use your oven. You can see the expected 
# formulas and their outputs in the test file, `question3_test.py`.

# A set of ingredients can be combined into more than one new ingredient
recipes = {
  'freeze': {
    ('water', 'air'): ('snow',)
  },
  'boil': {
    ('lead', 'mercury'): ('gold',),
    ('cheese', 'dough', 'tomato'): ('pizza',)
  },
  'wait': {  
  }
}

class Oven:
  def __init__(self):
    self.ingredients : list = []
  
  def add(self, item):
    self.ingredients.append(item)
  
  def freeze(self):
    self.combine_ingredients(recipes['freeze'])

  def boil(self):
    self.combine_ingredients(recipes['boil'])

  def wait(self):
    self.combine_ingredients(recipes['wait'])

  def combine_ingredients(self, possible_recipes):

    for recipe in possible_recipes:

      result = possible_recipes[recipe]

      # Check if current ingredients are present (they must be exactly the same)
      ingredients_present_count = 0
      for ingredient in self.ingredients:
        if ingredient in recipe:
          ingredients_present_count += 1
        else:
          break
      # Reassign ingredients if all ingredients are present
      if ingredients_present_count == len(self.ingredients):
        self.ingredients = result

        # Let's say we can only combine one recipe at a time
        break
  
  def get_output(self) -> str:
    return " ".join(self.ingredients)

# This function should return an oven instance!
def make_oven():
  return Oven()

def alchemy_combine(oven, ingredients, temperature):
  
  for item in ingredients:
    oven.add(item)

  if temperature < 0:
    oven.freeze()
  elif temperature >= 100:
    oven.boil()
  else:
    oven.wait()

  return oven.get_output()