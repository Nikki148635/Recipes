# # Base image
# FROM python:3.9

# # Create work directory
# WORKDIR /app

# # Copy requirements file
# COPY requirements.txt ./

# # Install dependencies
# RUN pip install -r requirements.txt

# # Copy application files
# COPY . .

# # Set environment variable for recipe data path
# ENV RECIPE_DATA_PATH /app/recipes.json

# # Expose Flask port
# EXPOSE 5000

# # Run Flask application
# CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]












    # {% comment %} <ul>
    #     {% for recipe in recipes %}
    #         <li>
    #             <h2>{{ recipe.title }}</h2>
    #             <p>{{ recipe.ingredients }}</p>
    #             <a href="/recommend?recipe_id={{ recipe.id }}">Recommend Similar</a>
    #         </li>
    #     {% endfor %}
    # </ul> {% endcomment %}