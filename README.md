# venv_environment_setup
# Django-Powered Discussion Forum

## Overview
This project is a Django-powered discussion forum that allows users to create accounts, log in, create discussion posts, and comment on posts. The project is designed with beginners in mind, making it a great introduction to Django and Python.

## planning stage
[ERD](text_files\erd.txt)

[MVP-Scope](text_files\MVP_Scope.txt)

[potential-features](text_files\potential_features.txt)

[priority-features](text_files\priority_features.txt)

[purpose-and-target-audience](text_files\purpose_and_target_audience.txt)

[user-flow-and-diagram](text_files\User_Flow_and_diagram.txt)

[user-stories](text_files\user_stories.txt)

## MVP Scope
### User Registration and Authentication
- **User Registration**: Allow new users to create an account by providing a username, email, and password.
- **User Login**: Enable registered users to log in using their email and password.
- **Password Reset**: Implement a simple password reset functionality through email.

### User Profile Management
- **Profile Page**: Provide a basic profile page where users can view and update their information (username, email).

### Discussion Posts
- **Create New Post**: Allow logged-in users to create new discussion posts with a title and content.
- **View Posts**: Display a list of all discussion posts on the forum page, including the title, content, and author.
- **View Post Details**: Enable users to click on a post to view its details and comments.

### Comments
- **Add Comment**: Allow logged-in users to comment on discussion posts.
- **View Comments**: Display comments under the associated post, including the content and author.

### Basic Navigation and UI
- **Homepage**: Create a simple homepage with links to register, log in, and access the forum.
- **Forum Page**: Display a list of discussion posts and a link to create a new post.
- **Post Creation Page**: Provide a form for creating new posts.
- **Post Detail Page**: Show the details of a post and its comments, along with a form to add a comment.

## Future Enhancements
- **Advanced User Profiles**: Add profile pictures, bio, and other personalization options.
- **Likes and Reactions**: Enable users to like or react to posts and comments.
- **Categories and Tags**: Organize posts by categories or tags for easier navigation.
- **Notifications**: Notify users of new comments or replies to their posts.
- **Search Functionality**: Allow users to search for posts by keywords.


## Validation 
**HTML**
[HTML validation](images/html%20validation.png)

**CSS**
[CSS-validation](images/css%20validation.png)

**Am I Responsive**
[Mobile view](images/mobile%20view.png)
[Tablet view](images/tablet%20view.png)
[Web view](images/web%20view.png)

**Lighthouse**
[Lighthouse report](images/lighouse%20desktop.png)


## How to Run the Project
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/discussion-forum.git
Navigate to the project directory:

bash
cd discussion-forum
Create a virtual environment:

bash
python -m venv env
Activate the virtual environment:

bash
# On Windows
.\env\Scripts\activate

# On macOS and Linux
source env/bin/activate
Install the dependencies:

bash
pip install -r requirements.txt
Apply the migrations:

bash
python manage.py migrate
Create a superuser:

bash
python manage.py createsuperuser
Run the development server:

bash
python manage.py runserver
Open your web browser and navigate to http://127.0.0.1:8000 to access the discussion forum.

Contributing
Contributions are welcome! Please read the CONTRIBUTING.md file for guidelines on how to contribute to this project.

License
This project is licensed under the MIT License. See the LICENSE file for more details.