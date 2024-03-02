from flask import Flask, render_template, request
import json

# Load recipe data from JSON file
with open("recipes.json") as f:
    recipe_data = json.loads(f)
    print(recipe_data)

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/search")
def search_recipes():
    ingredient = request.args.get("ingredient")
    result = search_recipes_by_ingredient(ingredient, recipe_data)
    return render_template("search_results.html", searched_ingredient=result)

def search_recipes_by_ingredient(x, y):
    for objects in recipe_data: 
        mylist = objects["ingredients"]
        for z in mylist:
            if z == x:
                print(z, "ingredient match")
                return z

@app.route("/recommend")
def recommend_recipes(u, f):
    # Extract user preferences and dietary restrictions from request
    # ...
    get_user_preferences = request.get["preferences"] 
    restrictions = recipe_data["dietary_tags"]
    user_restrictions = []
    user_preferences = []
    for i in restrictions: 
        if i != ["vegan"] & ["vegetarian"]: 
            return i
        user_restrictions.append(i)
    else: 
        return i
        user_preferences.append(i)
        break
    recipes = recipe_data["title"]
    
    filtered_recipes = filter_recipes_by_dietary_restrictions(recipes, user_restrictions)
    recommended_recipes = recommend_recipes(user_preferences, filtered_recipes)
    return render_template("recommendations.html", recipes=recommended_recipes)
    
    
def filter_recipes_by_dietary_restrictions(a, b): 
    get_title = request.args.get["title"]
    for recipe in recipes:  
        if recipe == get_title:
            print(recipe, "recipe match")
            return recipe
            break


if __name__ == "__main__":
    app.run(debug=True)
