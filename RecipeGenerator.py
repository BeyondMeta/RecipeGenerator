# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 11:28:04 2019

@author: Sophie
Recipe Generator
"""
import random
# =============================================================================
# from recipe_scrapers import scrape_me
# # give the url as a string, it can be url from any site listed below
# scraper = scrape_me('http://allrecipes.com/Recipe/Apple-Cake-Iv/Detail.aspx')
# 
# scraper.title()
# scraper.total_time()
# scraper.ingredients()
# scraper.instructions()
# scraper.links()
# =============================================================================


def RecipeGenerator():
    
    Ingredients = ["Pasta", "Lamb", "Chicken", "Pork", "Ground Beef", 
                   "Goose", "Cheddar", "Mozzerala", "Carrots", 
                   "Red Chili flakes", "Black pepercorns", "Coriander", 
                   "Fennel seeds", "Paprika", "Oregano", "Turmeric", 
                   "Nutmeg", "Bay Leaves", "Cayenne Pepper", "Thyme", "Cinnamon", 
                   "Panko bread crumbs", "Couscous", "Rice", "All-purpose flour",
                   "White sugar", "Brown sugar", "Powdered sugar", "Baking Powder", 
                   "Active dry yeast", "Chicken stock", "Beef stock", "Milk", "Butter", 
                   "Heave cream", "Eggs", "Parmesan", "Bacon", "Parsley", "Celery", "Carrots",
                   "Lemons", "Limes", "Orange juice", "Ketchup", "Mayonnaise", "Extra virgin olive oil",
                   "Vegetable oil", "Olive oil", "Vinegar", "Mustard", "Honey",
                   "Garlir", "Shallots", "Potatoes", "Onions", "Tomatoes", "Bubble Tea"               
                   ]    
    PreparationMethod = ["Cut", "Grate", "Mix", "Whip", "Bake", "Stir Fry", "Boil", "Cook"]
    Quantity =["Teaspoon", "Table spoon", "Cup", "Pinch", "Bucket", "To Taste"]
    Quantity2 = ["1/4", "1/2", "3/4", "1", "1 & 1/2", "2"]
    CookingTime = random.randint(1, 120)
    Temperature = random.randint(0, 450)
    
    
    numIngre = random.randint(1, len("Ingredients"))
    myIngredients = random.sample(Ingredients, numIngre)
    
    for i in myIngredients:
        print(Quantity2[random.randint(0,len(Quantity2) -1)], " of ", 
            Quantity[random.randint(0,len(Quantity) -1)], i)

    print(PreparationMethod[random.randint(0, len(PreparationMethod))],"the ingredients for ", CookingTime, " minutes  at ", Temperature , "°F")
    
    
    
    