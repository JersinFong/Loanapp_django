# Public Access
List veiw for all apps: https://nameless-dusk-76109.herokuapp.com/api/status/

Retrieve an app with it's id: https://nameless-dusk-76109.herokuapp.com/api/status/<:id>/

Post a new app: https://nameless-dusk-76109.herokuapp.com/api/loanapp/


# Teach Stack

django + djangorestframwork + docker + heroku

# Task Summary

1. Build a Restful API wit djanogrestframework for loanapp that supports CRUD operations
   a. Create/POST: 
      endpoint: api/loanapp/
      accepts valid json file
   b. Retrieve/Update/Delete(GET, PUT, DELETE)
      endipoint: api/status/<:id>/
      this id is automatically created by database, starts from 1.
   c. when user post duplicate app, update the old one instead of posting a new one
      based on limited information I had, I simply assumed the CFRequestId inside RequestHeader is unique for each app, so I used this    value to check is duplicates occur
      
2. Write unit test suites for all methods
   this is done inside django test file: app/stauts/test.py to test CRUD methods and duplicate posts, use this command to run it 
   ```
   $python manage.py test
   ```
   
3. wrap the app with docker container and deployed it to heroku
   
   
      
