# **Staff**
Staff accounting service
***

## API description

- **Employee:**
  + get a list of staff using pagination;
  + get an employee by id;
  + create a new employee.
  
- **JSON Web Token (JWT):**
  + get JWT;
  + update JWT;
  + verify JWT.
  
***

## Launch project (local)
1. Create a virtual environment.

`python3 -m venv venv`

`source venv/bin/activate`

2. Сreate a file `.env` and fill it.

Look `dot_env_example`

3. Install requirements.

`pip install -r requirements.txt`

4. Run project.

`python3 manage.py runserver`
