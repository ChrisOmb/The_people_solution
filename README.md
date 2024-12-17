# The People Project

**The People Project** is a simple Django application for creating and managing polls. Users can view polls, vote on them, and see the results. This project demonstrates the basic functionality of Django views, models, and templates.

## Features

- **Display a list of all polls**: Shows all available polls on the homepage.
- **View poll details**: Displays poll questions and voting options.
- **Vote on polls**: Users can vote for a choice in a poll.
- **See poll results**: Displays the number of votes each choice has received after voting.

## Tech Stack

- **Backend**: Django
- **Database**: SQLite (default for Django)
- **Frontend**: HTML, CSS (for styling)

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/the_people_project.git
   cd the_people_project

 2. Create a virtual environment
  
        python -m venv env
        source env/bin/activate  # On Windows: env\Scripts\activate

3.Install the required packages:

       pip install -r requirements.txt

4.Apply migrations:
      
      python manage.py migrate

5.Create a superuser (to access the Django admin interface):
    
       python manage.py createsuperuser

6.Run the development server:

       python manage.py runserver




