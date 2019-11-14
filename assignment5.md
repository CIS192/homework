# Assignment 5: Bringing Tumblr Back
> Due November 14th at 11:59 PM. Start early and make use of office hours. This assignment will take an estimated 4 hours.

## Preface
In this assignment, we will be building a blog using Django. The blog will support markdown formatting, as well as SQL database support. As we found out in class, this is actually not too difficult! Refer to and recreate the code given in lecture today as it will help tremendously for this assignment - not only as a boilerplate but also to gain understanding as to how Django works.

For the HTML sections of this assignment, feel free to refer to Piazza, the shared 19x lecture or online documentation. Well designed assignments will receive extra credit!

## Project Layout
Feel free to write all the functionality into a single app within your project. You will design a database model to store blog posts. You must include at least 5 fields in the model for your posts (the specifics of which are up to you). Think about how the information stored in actual blogs for inspiration!

### Splash Page
The splash page is the entry point to your blog, feel free to spice it up! This page should be accessible at the empty route `/` and should have a short blurb about yourself, as well as an image using a `img` tag (feel free to use image hosting such as imgur.com to make your life easier). 

### Post Page
The post page renders markdown into HTML for a given blog post. This page should be accessible at the route `/post/<id>`, where `<id>` is the unique identifier for a blog post. For example, `/post/helloworld` should render the blog post pertaining to `helloworld`.

#### Sub Routes
Retrieving the sub-route for a given route can be specified as follows in the `urls.py` file: 

```python
path('post/<str:id>', post, name='post')
```

Subsequently, in `views.py`, we can retrieve this `id` value by creating an additional parameter in the view method:

```python
def post_view(request, id):
```

By the way, querying for a specific instance of data can be done using something like: 

```python
object = Model.objects.get(field=value)
```

This should be enough logic to get started!

#### Rendering Markdown
An example markdown post would be something like:

```md
# Hello World
> This is a blog post!

Hey guys, it's Arun here. Today, we're gonna be talking about
Django. Blah blah blah, insert animal fact and youtube video here.
```

Converting the markdown content into HTML content can be done using the [markdown2](https://github.com/trentm/python-markdown2) package. Refer to the documentation to get started (should only be one or two lines of code to render). 

Finally, we can render the HTML as HTML (and not as a string of HTML code) by passing the HTML content to our template and calling `{{ something|safe }}` in the template itself.

### Blog Page
This page should be accessible at the route `/blog` and should list every blog post in the database. Each listing should include a link to the actual post using a `<a>` tag with a `href="link/to/post"` property.

## Submission
This assignment should be uploaded to Gradescope as a `.zip` file, which include a `README.md` file containing all the necessary code and instructions to run your project. If we can’t run your code from the instructions outlined in `README.md`, the assignment will yield a 0. 

We also require an actual blog post about a topic of your choosing for credit. Be creative and have fun!
