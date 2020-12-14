# GameReviewPredictor
#### Prequisites

- Python
- pip
- Heroku CLI
- Git

#### Deploying Flask App on Heroku

* Create a virtual environment with pipenv and install Flask and Gunicorn .

  ```
  $ pipenv install flask gunicorn 
  ```

* Create a "Procfile" and write the following code.

  ```
  $ touch Procfile 
  ```

  ```
  web: gunicorn app:app
  ```

* Create "runtime.txt" and write the following code.

  ```
  $ touch runtime.txt 
  ```

  ```
  python-3.8.3
  ```

* Update the requirements file by running :

  ```
  $ pip freeze > requirements.txt
  ```

 *  Initialize an empty repository, add the files in the repository and commit all the changes.

   ```
   $ git init 
   $ git add .
   $ git commit -m "My First Web Application"
   ```

* Login to heroku CLI using :

  ```
  heroku login
  ```

 * Now, Create a unique name for your Web app.

   ```
   $ heroku create your-first-heroku-app --buildpack heroku/python
   For example: 
   $ heroku create gamereviewpredictor --buildpack heroku/python
   ```

* Push the code from your local master branch to heroku’s master branch.

  ```
  $ git push heroku master
  ```

 * Now got to the web application using below link:

   https://gamereviewpredictor.herokuapp.com/
