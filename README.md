Django blog challenge

Step 1. Django blog challenge started on 17/06/16
- Created the project and the structure using PyCharm
- Created an app called blogApp
- Created a superuser for admin access
- Registered the blogApp in INSTALLED_APPS in settings.py
- Created the model for our Posts
- Unit testing the model
- Registered the Post model in admin.py
- Added blog posts through the admin page

Step 2. Django Blog challenge continued - 18/06/16
- Created a view for the Post model
- Added a urls.py file in the global project folder and added the routes for our blogApp
- Created a template page base.html
- Created a child template page blogposts.html
- Added static content in the static folder
- Loaded staticfiles in the base.html template
- Styled the base.html template using css and Bootstrap

Step 3.
- Styled the blogposts.html page
- Created a templates folder inside the blogApp and moved the blogposts.html file inside it
- Created another template postdetail.html to open the details of each post
- Created a view 'post_detail' that uses the post unique id to render the post in 'postdetail.html'
- Linked the 'Read More' and 'Back To Blog' buttons
- Truncated the posts to 30 words so the user clicks on the 'Read More' button
