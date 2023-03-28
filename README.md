1) No users in the application yet so created a mock user (in routes)
2) Used HTML to create HTML page (updated so no longer visable in code)
3) Created a seperate folder called templates so that when layout of the applcations is changed the HTML from every page does not need to altered
4) View function is simplified because HTML code is in a seperate HTML index file (template--HTML=rendering)
5) Fake users created in (routes.py) these are preserved as much possible until needed to implement real posts. Fake users are created because logged users would likely want to see posts of people they're connected with
6) index.HTML updated to show recent posts
7) Create a template inheritance feature for navigation bar (created "base template" for this)
