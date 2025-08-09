
# Blog-Project

A simple blog web application built with Django.

## Features

- Create, read, update, and delete blog posts
- User authentication and authorization
- Responsive design for mobile and desktop
- Rich text editing for posts
- Pagination for blog lists
- Comments system (optional)

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/sameer9860/Blog-Project.git
   cd Blog-Project (if you are in another dir)
````

2. **Create and activate a virtual environment**

   ```bash
   python -m venv env
   .\env\Scripts\activate  # Windows PowerShell
   source env/bin/activate # macOS/Linux
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**

   ```bash
   python manage.py migrate
   ```

5. **Run the development server**

   ```bash
   python manage.py runserver
   ```

6. **Open your browser**

   Go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to see the blog in action.


## License

This project is licensed under the sameer9860 License. See the [LICENSE](LICENSE) file for details.
