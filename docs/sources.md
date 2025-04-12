---
title: Sources
nav_order: 4
---

{: .no_toc }
# Sources

<details open markdown="block">
{: .text-delta }
<summary>Table of contents</summary>
+ ToC
{: toc }
</details>

## Sources from structured libraries or documentation

These are sources I used to inform myself in general or for understanding the background of the code snippets I found:

+ [Flask documentation](https://flask.palletsprojects.com/en/stable/)
+ [Jinja2 documentation](https://jinja.palletsprojects.com/en/stable/templates/#)
+ [Library for CSS and html](https://www.w3schools.com/html/default.asp)
+ [Bootstrap component library](https://getbootstrap.com/docs/5.3/getting-started/introduction/)
+ [SQLite documentation](https://www.sqlite.org/)
+ [SQLAlchemy documentation](https://www.sqlalchemy.org/)
+ + [SQLAlchemy Deletes](https://docs.sqlalchemy.org/en/20/core/dml.html#sqlalchemy.sql.expression.delete) for the delete function for notes 
+ [WTForms documentation](https://wtforms.readthedocs.io/en/2.3.x/)
+ + [WTForms field definitions](https://wtforms.readthedocs.io/en/2.3.x/fields/) for the select field in the CategoryForm
+ [Datacamp Markdown formatting](https://www.datacamp.com/cheat-sheet/markdown-cheat-sheet-23)
+ [Course information from FSWD](https://hwrberlin.github.io/fswd/)

## Sources from forums, articles and other repositories for concrete challenges

These are sources I used to solve specific challenges. In difference to the direct code copy I adapted the logic onto my project or adapted the code to fit my project.

+ Challenge: Clearing the new category textfield after submitting 
+ + Solution:[Reddit](https://www.reddit.com/r/flask/comments/55320p/clear_valid_form_after_it_is_submitted/), [Stack overflow](https://stackoverflow.com/questions/31945329/clear-valid-form-after-it-is-submitted/31945712#31945712)
+ Challenge: Placing the container so that header, content and footer are shown vertical while sidebar and main are placed horizontal 
+ + Solution: [Bootstrap grid layout](https://getbootstrap.com/docs/4.0/layout/grid/), [Holy grail layout](https://blog.pixelfreestudio.com/creating-complex-layouts-with-css-flexbox/), [YouTube 'How to create RESPONSIVE Layouts with CSS GRID'](https://www.youtube.com/watch?v=S9OiWe5iBYo)
+ Challenge: Dynamic creation of cards including the notes 
+ + Solution: [Stack overflow](https://stackoverflow.com/a/9204987) (Later also used for category menu on the sidebar)
+ Challenge: Everytime when reloading the Dashboard the last added category was created again
+ + Solution: [Stack overflow](https://stackoverflow.com/a/31945712)
+ Challenge: Creating a dropdown menu with the list of existing categories
+ + Solution: [Stack overflow](https://stackoverflow.com/a/48236887), [WTForms field definitions](https://wtforms.readthedocs.io/en/2.3.x/fields/) for the select field in the CategoryForm
+ Challenge: Card on dashboard showed the categoryID instead of the category name (because the category name was stored in a separate table)
+ + Solution: [GitHub project Petmatch](https://github.com/SimoneHeinrich/PetMatch/blob/main/app.py) (app.py line 159-161) (Credits to my fellow students Simone Heinrich and Patryk Kujawski)
+ Challenge: Change color of Text when hovering over it
+ + Solution: [Stack overflow](https://stackoverflow.com/a/75193905)
+ Challenge: Creating a Navbar
+ + Solution: [YouTube 'Navbar CSS Tutorial: 3 Ways to Create a Navigation Bar with Flexbox'](https://www.youtube.com/watch?v=PwWHL3RyQgk)


## Sources from which content was directly copied 

These are sources from which many lines of code were copied exactly the same into this project.

+ Copied the code written in the video to setup the Dashboard, Login and Registration [YouTube 'Web Development mit Flask Tutorial - Flask & Jinja2 Basics'](https://www.youtube.com/watch?v=U5qrFwQreyg) [YouTube 'Web Development mit Flask - Full Stack App mit SQLAlchemy & Bootstrap'](https://www.youtube.com/watch?v=nC7vQn0jZXw) (Changed some elements in the further development)
+ Copied css and html elements from [Holy grail layout](https://blog.pixelfreestudio.com/creating-complex-layouts-with-css-flexbox/) (Section: 'Creating a Holy Grail Layout')
+ Copied Navbar elements [Bootstrap navbar](https://getbootstrap.com/docs/5.0/components/navbar/)
+ Copied Card elements [Bootstrap cards](https://getbootstrap.com/docs/5.3/components/card/)
+ Copied the whole file as a base for this documentation [GitHub project fswd-app](https://github.com/hwrberlin/fswd-app/tree/docs)
+ 
+ 

No LLMs (such as ChatGPT) or other AI tools (such als Copilot) were used for creating this project. 
