# YumYard

YumYard is a web application that allows users to explore, share, and discover a variety of food recipes. With a user-friendly interface and interactive features, YumYard aims to make the culinary journey enjoyable for everyone.

## Live Demo

Visit the live YumYard web application at [/](/) to experience the culinary world firsthand.

## Features

- **Recipe Posting**: Users can post their favorite recipes, complete with details such as name, description, ingredients, and steps.
- **YouTube Video Embedding**: Enhance your recipes by embedding YouTube videos to provide step-by-step visual instructions.
- **Recipe Details**: View detailed information about recipes, including steps, description, and ingredients.
- **User Authentication**: Secure user accounts with a robust authentication system, enabling users to log in and sign up.
- **CRUD Operations**: Users who have posted recipes can perform CRUD (Create, Read, Update, Delete) operations on their recipes.
- **Recipe Search**: Easily search for recipes based on names or ingredients, making it effortless to find your desired dishes.
- **Responsive Design**: A beautiful and responsive design ensures an enjoyable user experience on various devices.

## Technology Stack

- **Python**: Backend development is powered by the Python programming language.
- **Django**: The web application framework used for building the backend.
- **Bootstrap**: Frontend design and styling are crafted using the Bootstrap framework for a sleek and modern appearance.
- **HTML/CSS**: The foundation of the web pages is created with HTML for structure and CSS for styling.
- **JavaScript**: Client-side interactivity is enhanced with JavaScript.
- **Dropbox**: Storage of various assets for direct public URLs.

## How to Contribute

1. Fork the repository.
2. Clone the forked repository to your local machine.
3. Create a virtual environment and install dependencies.
   ```bash
   pip install -r requirements.txt
   ```
4. Make changes and test locally.
5. Submit a pull request with your changes.

## Get Started Locally

To run COOKies locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/devXpraAddy/YumYard.git
   cd cookies
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:

   ```bash
   python manage.py migrate
   ```

5. Run the development server:

   ```bash
   python manage.py runserver
   ```

6. Open your browser and visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to see COOKies in action.

Happy cooking! 🍪🍲
