# pypostblog
A personal blog written in Python with the Django framework and using PostgreSQL as a database.

Initial commit 18.11.2023
The initial pypostblog commit. I made a post model, a post form, some view and urls to access them.

Creation and Deletion commit 23.11.2023
Created a view to create and a view to delete posts. After creation, deletion or updating a post, you get redirected to the post_list page.

Posts list page update commit 23.11.2023
Updated the posts list, adding a paginator and limiting the number of posts that can be on a page at a given time.
Added an account app with a user model for authentication.