import os
from flask import Flask, render_template, url_for, request, redirect
import random

app = Flask(__name__)

projects = ['Project 1', 'Project 2', 'Project 3']

@app.route('/')
def index():
    # Get a list of all the image files in the "emoji" folder
    image_files = os.listdir("static/emoji")
    # Choose a random image from the list
    random_image = random.choice(image_files)
    # Add the chosen image to the index.html template
    return render_template("index.html", image=random_image)


@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Get the form data submitted by the user
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        
        # Store the form data in a file named 'contact.txt'
        with open('contact.txt', 'a') as file:
            file.write(f'Name: {name}\nEmail: {email}\nMessage: {message}\n\n')
        
        # Redirect the user to the thank you page
        return render_template('thank_you.html')
    else:
        # Render the contact.html template
        return render_template('contact.html')

@app.route('/thank_you')
def thank_you():
    # Render the thank_you.html template
    return render_template('thank_you.html')


if __name__ == '__main__':
    app.run(debug=True)

