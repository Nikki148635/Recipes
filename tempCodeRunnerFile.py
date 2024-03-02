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
                return z