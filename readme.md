# A simple multi-vendor ecommerce backend, with functionalities:
- JWT Authentication
- Different user types
- Shop management
- Product management
- Cart management
- Order management
- Periodic task for generating daily statistics<br/>
There's also a frontend page with infinity scroll for showing product data.
# To run the project:
- Clone the repo and go to project root
- Create a .env file and copy the contents of .env.example file, assign values if necessary
- Both docker and virtualenv can be used to set up the interpreter
- To use venv
    ```python -m venv venv```(might be python3 for some), then activate the venv
- To use docker run ```docker compose up --build``` then create static_local directory, run ```python manage.py collectstatic```
- Install required packages ```pip install -r requirements.txt```
- For venv, run server with ```python manage.py runserver```
- A postman collection and sample fixture has been added to the repository