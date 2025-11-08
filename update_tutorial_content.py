import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'techblog.settings')
django.setup()

from tech.models import Tutorial

def update_tutorial_content():
    """Update tutorials with more complete content"""
    
    # Define more complete content for each tutorial
    tutorial_updates = {
        'Getting Started with Python': {
            'content': '''Python is a high-level, interpreted programming language known for its simplicity and readability. It's widely used for web development, data analysis, artificial intelligence, and scientific computing.

Getting Started
---------------

To get started with Python, you'll need to install it on your system. Visit python.org to download the latest version. Python comes with an interactive interpreter that you can access by typing 'python' in your terminal.

Basic Syntax
------------

Python uses indentation to define code blocks instead of curly braces or keywords. This makes the code more readable:

```python
# This is a comment
print("Hello, World!")  # This prints text to the console

# Variables
name = "Alice"
age = 30
is_student = True

# Lists
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(f"I like {fruit}")

# Functions
def greet(name):
    return f"Hello, {name}!"

message = greet("Bob")
print(message)
```

Data Types
----------

Python has several built-in data types:
- Numbers: integers, floats, complex numbers
- Strings: text data
- Lists: ordered collections
- Tuples: immutable ordered collections
- Dictionaries: key-value pairs
- Sets: unordered collections of unique items

Control Flow
------------

Python supports standard control flow statements:

```python
# If statements
if age >= 18:
    print("You are an adult")
elif age >= 13:
    print("You are a teenager")
else:
    print("You are a child")

# Loops
for i in range(5):
    print(f"Count: {i}")

count = 0
while count < 5:
    print(f"While count: {count}")
    count += 1
```

Conclusion
----------

Python's simplicity and versatility make it an excellent choice for beginners and experts alike. Its extensive standard library and rich ecosystem of third-party packages make it suitable for almost any programming task.'''
        },
        'Django Web Development': {
            'content': '''Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. It follows the model-view-template (MVT) architectural pattern and includes an ORM, authentication, and admin interface out of the box.

Installation
------------

To install Django, use pip:

```bash
pip install django
```

Creating a Project
------------------

Create a new Django project with:

```bash
django-admin startproject myproject
cd myproject
python manage.py runserver
```

This starts the development server at http://127.0.0.1:8000/

Project Structure
-----------------

A typical Django project includes:
- manage.py: Command-line utility
- settings.py: Configuration settings
- urls.py: URL routing
- wsgi.py: WSGI compatibility
- asgi.py: ASGI compatibility

Creating Apps
-------------

Django projects are composed of apps:

```bash
python manage.py startapp myapp
```

Each app includes:
- models.py: Database models
- views.py: View functions
- urls.py: App-specific URLs
- templates/: HTML templates
- static/: Static files (CSS, JS, images)

Models
------

Define your data structure in models.py:

```python
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
```

Views
-----

Create views in views.py:

```python
from django.shortcuts import render, get_object_or_404
from .models import Post

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'posts/list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'posts/detail.html', {'post': post})
```

Templates
---------

Django uses its own template language:

```html
<!-- posts/list.html -->
<h1>Blog Posts</h1>
{% for post in posts %}
    <div>
        <h2><a href="{% url 'post_detail' post.pk %}">{{ post.title }}</a></h2>
        <p>{{ post.content|truncatewords:30 }}</p>
        <small>By {{ post.author }} on {{ post.created_at }}</small>
    </div>
{% endfor %}
```

Admin Interface
---------------

Django provides a powerful admin interface. Register your models in admin.py:

```python
from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_at']
    list_filter = ['created_at', 'author']
    search_fields = ['title', 'content']
```

Run migrations to create database tables:

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

Conclusion
----------

Django's "batteries-included" philosophy and extensive documentation make it one of the most popular web frameworks for Python developers. Its emphasis on reusability and "don't repeat yourself" (DRY) principles helps developers build robust web applications quickly.'''
        },
        'JavaScript Fundamentals': {
            'content': '''JavaScript is the programming language of the web, enabling interactive and dynamic web pages. Originally created by Netscape in 1995, it has evolved into a powerful language for both client-side and server-side development.

Variables and Data Types
------------------------

JavaScript is dynamically typed, meaning you don't need to declare variable types:

```javascript
// Variables
var name = "Alice";        // Function-scoped (old way)
let age = 30;              // Block-scoped (new way)
const isStudent = true;    // Block-scoped, immutable reference

// Data types
let number = 42;           // Number
let string = "Hello";      // String
let boolean = true;        // Boolean
let array = [1, 2, 3];     // Array (object)
let object = {             // Object
    name: "Bob",
    age: 25
};
let nothing = null;        // Null
let empty;                 // Undefined
```

Functions
---------

JavaScript functions are first-class citizens:

```javascript
// Function declaration
function greet(name) {
    return `Hello, ${name}!`;
}

// Function expression
const add = function(a, b) {
    return a + b;
};

// Arrow function
const multiply = (a, b) => a * b;

// Function with default parameters
function power(base, exponent = 2) {
    return base ** exponent;
}

console.log(greet("World"));        // "Hello, World!"
console.log(add(5, 3));             // 8
console.log(multiply(4, 3));        // 12
console.log(power(3));              // 9 (3^2)
console.log(power(3, 3));           // 27 (3^3)
```

Control Flow
------------

JavaScript supports standard control flow statements:

```javascript
// If statements
if (age >= 18) {
    console.log("You are an adult");
} else if (age >= 13) {
    console.log("You are a teenager");
} else {
    console.log("You are a child");
}

// Switch statement
switch (day) {
    case 'Monday':
        console.log("Start of the week");
        break;
    case 'Friday':
        console.log("Almost weekend");
        break;
    default:
        console.log("Regular day");
}

// Loops
for (let i = 0; i < 5; i++) {
    console.log(`Count: ${i}`);
}

const fruits = ["apple", "banana", "orange"];
for (const fruit of fruits) {
    console.log(`I like ${fruit}`);
}

let count = 0;
while (count < 5) {
    console.log(`While count: ${count}`);
    count++;
}
```

Arrays and Objects
------------------

JavaScript provides powerful methods for working with arrays and objects:

```javascript
// Arrays
const numbers = [1, 2, 3, 4, 5];

// Array methods
const doubled = numbers.map(n => n * 2);           // [2, 4, 6, 8, 10]
const evens = numbers.filter(n => n % 2 === 0);    // [2, 4]
const sum = numbers.reduce((acc, n) => acc + n, 0); // 15

// Objects
const person = {
    name: "Charlie",
    age: 28,
    hobbies: ["reading", "coding", "gaming"],
    
    // Method
    greet() {
        return `Hi, I'm ${this.name}`;
    }
};

console.log(person.greet()); // "Hi, I'm Charlie"
console.log(person["name"]); // "Charlie" (bracket notation)
```

DOM Manipulation
----------------

JavaScript can interact with HTML elements through the Document Object Model (DOM):

```javascript
// Selecting elements
const heading = document.querySelector('h1');
const buttons = document.querySelectorAll('.btn');

// Modifying elements
heading.textContent = "New Heading";
heading.style.color = "blue";

// Event handling
const button = document.getElementById('myButton');
button.addEventListener('click', function() {
    alert('Button clicked!');
});

// Creating elements
const newDiv = document.createElement('div');
newDiv.textContent = "This is a new div";
document.body.appendChild(newDiv);
```

Modern JavaScript (ES6+)
------------------------

ES6 introduced many new features:

```javascript
// Template literals
const message = `Hello, ${name}!`;

// Destructuring
const person = { name: "Dave", age: 35 };
const { name, age } = person;

const numbers = [1, 2, 3];
const [first, second] = numbers;

// Spread operator
const arr1 = [1, 2, 3];
const arr2 = [...arr1, 4, 5]; // [1, 2, 3, 4, 5]

const obj1 = { a: 1, b: 2 };
const obj2 = { ...obj1, c: 3 }; // { a: 1, b: 2, c: 3 }

// Promises and async/await
async function fetchData() {
    try {
        const response = await fetch('/api/data');
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error:', error);
    }
}
```

Conclusion
----------

JavaScript's versatility and the vast ecosystem of libraries and frameworks make it essential for modern web development. Understanding these fundamentals provides a solid foundation for building interactive web applications.'''
        }
    }
    
    # Update tutorials with more complete content
    updated_count = 0
    for title, updates in tutorial_updates.items():
        try:
            tutorial = Tutorial.objects.get(title=title)
            tutorial.content = updates['content']
            tutorial.save()
            print(f"Updated content for tutorial: {title}")
            updated_count += 1
        except Tutorial.DoesNotExist:
            print(f"Tutorial not found: {title}")
        except Exception as e:
            print(f"Error updating tutorial '{title}': {e}")
    
    print(f"\nUpdated {updated_count} tutorials with complete content!")

if __name__ == '__main__':
    update_tutorial_content()