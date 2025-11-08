import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'techblog.settings')
django.setup()

from tech.models import Tutorial

def update_remaining_tutorials():
    """Update remaining tutorials with more complete content"""
    
    # Define more complete content for remaining tutorials
    tutorial_updates = {
        'Advanced Python Techniques': {
            'content': '''Advanced Python techniques can significantly improve your code's efficiency, readability, and maintainability. This tutorial covers decorators, generators, context managers, and other powerful features.

Decorators
----------

Decorators are a way to modify or enhance functions or classes without permanently modifying their code:

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        result = func(*args, **kwargs)
        print("Something is happening after the function is called.")
        return result
    return wrapper

@my_decorator
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Alice")
# Output:
# Something is happening before the function is called.
# Hello, Alice!
# Something is happening after the function is called.
```

You can also create decorators with parameters:

```python
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hi, {name}!")

greet("Bob")
# Output:
# Hi, Bob!
# Hi, Bob!
# Hi, Bob!
```

Generators
----------

Generators are a memory-efficient way to create iterators:

```python
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Using the generator
for num in fibonacci(10):
    print(num)

# Generator expression
squares = (x**2 for x in range(10))
print(list(squares))  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

Context Managers
----------------

Context managers ensure proper resource management using the 'with' statement:

```python
class MyContextManager:
    def __enter__(self):
        print("Entering context")
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting context")
        if exc_type is not None:
            print(f"Exception occurred: {exc_value}")
        return False  # Don't suppress exceptions

# Using the context manager
with MyContextManager() as cm:
    print("Inside context")

# Built-in context managers
with open('file.txt', 'w') as f:
    f.write('Hello, World!')
# File is automatically closed
```

List Comprehensions and Generator Expressions
--------------------------------------------

These provide concise ways to create lists and generators:

```python
# List comprehension
squares = [x**2 for x in range(10) if x % 2 == 0]
print(squares)  # [0, 4, 16, 36, 64]

# Nested list comprehension
matrix = [[i*j for j in range(3)] for i in range(3)]
print(matrix)  # [[0, 0, 0], [0, 1, 2], [0, 2, 4]]

# Set comprehension
unique_lengths = {len(word) for word in ['apple', 'banana', 'cherry', 'date']}
print(unique_lengths)  # {4, 5, 6}

# Dictionary comprehension
word_lengths = {word: len(word) for word in ['python', 'java', 'javascript']}
print(word_lengths)  # {'python': 6, 'java': 4, 'javascript': 10}
```

Lambda Functions
----------------

Lambda functions are small anonymous functions:

```python
# Simple lambda
add = lambda x, y: x + y
print(add(5, 3))  # 8

# Using with higher-order functions
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)  # [2, 4, 6, 8, 10]

# Filtering with lambda
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4]
```

Descriptors
-----------

Descriptors allow you to customize attribute access:

```python
class PositiveNumber:
    def __init__(self, value=0):
        self.value = value
    
    def __get__(self, obj, objtype=None):
        return self.value
    
    def __set__(self, obj, value):
        if value < 0:
            raise ValueError("Value must be positive")
        self.value = value
    
    def __delete__(self, obj):
        self.value = 0

class Product:
    price = PositiveNumber()
    
    def __init__(self, name, price):
        self.name = name
        self.price = price

product = Product("Laptop", 999.99)
print(product.price)  # 999.99
# product.price = -100  # Raises ValueError
```

Metaclasses
-----------

Metaclasses control class creation:

```python
class SingletonMeta(type):
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Database(metaclass=SingletonMeta):
    def __init__(self):
        self.connection = "Connected to database"

# Both instances are the same
db1 = Database()
db2 = Database()
print(db1 is db2)  # True
```

Conclusion
----------

Mastering these advanced Python techniques will make you a more effective Python developer. They allow you to write more elegant, efficient, and maintainable code. Practice these concepts to deepen your understanding and improve your Python skills.'''
        },
        'React.js Fundamentals': {
            'content': '''React.js is a popular JavaScript library for building user interfaces, particularly single-page applications. Developed by Facebook, React allows developers to create reusable UI components and manage application state efficiently.

Getting Started
---------------

To create a new React application, use Create React App:

```bash
npx create-react-app my-react-app
cd my-react-app
npm start
```

This sets up a development environment with hot reloading at http://localhost:3000/

Components
----------

React applications are built from components. Components can be functional or class-based:

```jsx
// Functional component
function Welcome(props) {
    return <h1>Hello, {props.name}!</h1>;
}

// Using arrow function
const Welcome = (props) => {
    return <h1>Hello, {props.name}!</h1>;
};

// Component with destructuring
const Welcome = ({ name }) => {
    return <h1>Hello, {name}!</h1>;
};

// Using the component
function App() {
    return (
        <div>
            <Welcome name="Alice" />
            <Welcome name="Bob" />
        </div>
    );
}
```

JSX
---

JSX is a syntax extension that allows you to write HTML-like code in JavaScript:

```jsx
const element = (
    <div>
        <h1>Hello, World!</h1>
        <p>This is JSX</p>
        <ul>
            <li>Item 1</li>
            <li>Item 2</li>
        </ul>
    </div>
);
```

Props
-----

Props (properties) are how components pass data to each other:

```jsx
function UserCard({ name, email, age }) {
    return (
        <div className="user-card">
            <h2>{name}</h2>
            <p>Email: {email}</p>
            <p>Age: {age}</p>
        </div>
    );
}

function App() {
    const user = {
        name: "Charlie",
        email: "charlie@example.com",
        age: 28
    };
    
    return (
        <div>
            <UserCard {...user} />
            {/* Or pass individually */}
            <UserCard name="Dave" email="dave@example.com" age={32} />
        </div>
    );
}
```

State
-----

State is used to manage data that changes over time within a component:

```jsx
import React, { useState } from 'react';

function Counter() {
    const [count, setCount] = useState(0);
    
    return (
        <div>
            <p>Count: {count}</p>
            <button onClick={() => setCount(count + 1)}>
                Increment
            </button>
            <button onClick={() => setCount(count - 1)}>
                Decrement
            </button>
            <button onClick={() => setCount(0)}>
                Reset
            </button>
        </div>
    );
}
```

useEffect Hook
--------------

The useEffect hook manages side effects in functional components:

```jsx
import React, { useState, useEffect } from 'react';

function Timer() {
    const [seconds, setSeconds] = useState(0);
    
    // Runs after every render
    useEffect(() => {
        const interval = setInterval(() => {
            setSeconds(seconds => seconds + 1);
        }, 1000);
        
        // Cleanup function
        return () => clearInterval(interval);
    }, []); // Empty dependency array means run once on mount
    
    return (
        <div>
            <h1>Timer: {seconds} seconds</h1>
        </div>
    );
}

function UserProfile({ userId }) {
    const [user, setUser] = useState(null);
    
    // Runs when userId changes
    useEffect(() => {
        fetchUser(userId).then(userData => {
            setUser(userData);
        });
    }, [userId]); // Dependency array
    
    if (!user) return <div>Loading...</div>;
    
    return (
        <div>
            <h1>{user.name}</h1>
            <p>{user.email}</p>
        </div>
    );
}
```

Conditional Rendering
---------------------

React allows you to conditionally render components:

```jsx
function Greeting({ isLoggedIn, username }) {
    if (isLoggedIn) {
        return <h1>Welcome back, {username}!</h1>;
    }
    return <h1>Please sign in.</h1>;
}

function App() {
    const [isLoggedIn, setIsLoggedIn] = useState(false);
    
    return (
        <div>
            {isLoggedIn ? (
                <Greeting isLoggedIn={true} username="Alice" />
            ) : (
                <Greeting isLoggedIn={false} />
            )}
            
            {/* Using && operator */}
            {isLoggedIn && <button>Logout</button>}
            
            {/* Using ternary operator */}
            <button onClick={() => setIsLoggedIn(!isLoggedIn)}>
                {isLoggedIn ? 'Logout' : 'Login'}
            </button>
        </div>
    );
}
```

Lists and Keys
--------------

Rendering lists in React requires a unique key for each item:

```jsx
function TodoList({ todos }) {
    return (
        <ul>
            {todos.map(todo => (
                <li key={todo.id}>
                    {todo.text}
                    <button onClick={() => deleteTodo(todo.id)}>
                        Delete
                    </button>
                </li>
            ))}
        </ul>
    );
}

function App() {
    const [todos, setTodos] = useState([
        { id: 1, text: 'Learn React' },
        { id: 2, text: 'Build an app' },
        { id: 3, text: 'Deploy to production' }
    ]);
    
    return (
        <div>
            <TodoList todos={todos} />
        </div>
    );
}
```

Forms
-----

Handling forms in React:

```jsx
import React, { useState } from 'react';

function ContactForm() {
    const [formData, setFormData] = useState({
        name: '',
        email: '',
        message: ''
    });
    
    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData(prev => ({
            ...prev,
            [name]: value
        }));
    };
    
    const handleSubmit = (e) => {
        e.preventDefault();
        console.log('Form submitted:', formData);
        // Process form data
    };
    
    return (
        <form onSubmit={handleSubmit}>
            <div>
                <label>Name:</label>
                <input
                    type="text"
                    name="name"
                    value={formData.name}
                    onChange={handleChange}
                />
            </div>
            <div>
                <label>Email:</label>
                <input
                    type="email"
                    name="email"
                    value={formData.email}
                    onChange={handleChange}
                />
            </div>
            <div>
                <label>Message:</label>
                <textarea
                    name="message"
                    value={formData.message}
                    onChange={handleChange}
                />
            </div>
            <button type="submit">Submit</button>
        </form>
    );
}
```

Conclusion
----------

React's component-based architecture, virtual DOM, and rich ecosystem make it one of the most popular choices for building modern web applications. Mastering these fundamentals provides a solid foundation for building complex, interactive user interfaces.'''
        },
        'Machine Learning with Python': {
            'content': '''Machine learning is a subset of artificial intelligence that enables computers to learn and make decisions from data without being explicitly programmed. Python has become the dominant language for machine learning due to its simplicity and rich ecosystem of libraries.

Getting Started
---------------

The essential libraries for machine learning in Python include:
- NumPy: Numerical computing
- Pandas: Data manipulation and analysis
- Matplotlib/Seaborn: Data visualization
- Scikit-learn: Machine learning algorithms
- TensorFlow/PyTorch: Deep learning frameworks

```bash
pip install numpy pandas matplotlib seaborn scikit-learn
```

Data Preparation
----------------

Data preparation is crucial for successful machine learning:

```python
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load data
df = pd.read_csv('data.csv')

# Explore data
print(df.head())
print(df.info())
print(df.describe())

# Handle missing values
df = df.dropna()  # Or df.fillna(method='mean')

# Feature selection
features = ['feature1', 'feature2', 'feature3']
X = df[features]
y = df['target']

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
```

Supervised Learning
------------------

Supervised learning uses labeled data to train models:

```python
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, mean_squared_error

# Regression example
model_reg = LinearRegression()
model_reg.fit(X_train_scaled, y_train)
predictions_reg = model_reg.predict(X_test_scaled)
mse = mean_squared_error(y_test, predictions_reg)
print(f"Mean Squared Error: {mse}")

# Classification example
model_clf = RandomForestClassifier(n_estimators=100)
model_clf.fit(X_train_scaled, y_train)
predictions_clf = model_clf.predict(X_test_scaled)
accuracy = accuracy_score(y_test, predictions_clf)
print(f"Accuracy: {accuracy}")

# Cross-validation
from sklearn.model_selection import cross_val_score
scores = cross_val_score(model_clf, X_train_scaled, y_train, cv=5)
print(f"Cross-validation scores: {scores}")
print(f"Average CV score: {scores.mean()}")
```

Unsupervised Learning
---------------------

Unsupervised learning finds patterns in unlabeled data:

```python
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

# Clustering
kmeans = KMeans(n_clusters=3)
clusters = kmeans.fit_predict(X_scaled)
df['cluster'] = clusters

# Principal Component Analysis (PCA)
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)
print(f"Explained variance ratio: {pca.explained_variance_ratio_}")

# Visualization
import matplotlib.pyplot as plt
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=clusters)
plt.xlabel('First Principal Component')
plt.ylabel('Second Principal Component')
plt.title('PCA Visualization')
plt.show()
```

Model Evaluation
----------------

Proper model evaluation is essential:

```python
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Classification metrics
print("Classification Report:")
print(classification_report(y_test, predictions_clf))

# Confusion matrix
cm = confusion_matrix(y_test, predictions_clf)
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.title('Confusion Matrix')
plt.ylabel('Actual')
plt.xlabel('Predicted')
plt.show()

# ROC Curve (for binary classification)
from sklearn.metrics import roc_curve, auc
y_prob = model_clf.predict_proba(X_test_scaled)[:, 1]
fpr, tpr, _ = roc_curve(y_test, y_prob)
roc_auc = auc(fpr, tpr)

plt.figure()
plt.plot(fpr, tpr, label=f'ROC curve (AUC = {roc_auc:.2f})')
plt.plot([0, 1], [0, 1], 'k--')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
plt.legend()
plt.show()
```

Deep Learning with TensorFlow/Keras
-----------------------------------

For more complex problems, deep learning can be very effective:

```python
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

# Simple neural network
model = keras.Sequential([
    layers.Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    layers.Dropout(0.2),
    layers.Dense(32, activation='relu'),
    layers.Dropout(0.2),
    layers.Dense(1, activation='sigmoid')  # For binary classification
])

model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

# Train model
history = model.fit(
    X_train_scaled, y_train,
    epochs=50,
    batch_size=32,
    validation_split=0.2,
    verbose=1
)

# Evaluate
test_loss, test_accuracy = model.evaluate(X_test_scaled, y_test, verbose=0)
print(f"Test accuracy: {test_accuracy}")

# Plot training history
plt.plot(history.history['accuracy'], label='Training Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.title('Model Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()
plt.show()
```

Best Practices
--------------

1. **Start Simple**: Begin with basic algorithms before moving to complex models
2. **Feature Engineering**: Create meaningful features from raw data
3. **Cross-Validation**: Use proper validation techniques
4. **Hyperparameter Tuning**: Optimize model parameters
5. **Avoid Overfitting**: Use regularization techniques

```python
from sklearn.model_selection import GridSearchCV

# Hyperparameter tuning
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [3, 5, 7, None],
    'min_samples_split': [2, 5, 10]
}

grid_search = GridSearchCV(
    RandomForestClassifier(),
    param_grid,
    cv=5,
    scoring='accuracy',
    n_jobs=-1
)

grid_search.fit(X_train_scaled, y_train)
print(f"Best parameters: {grid_search.best_params_}")
print(f"Best cross-validation score: {grid_search.best_score_}")
```

Conclusion
----------

Machine learning with Python opens up powerful possibilities for data analysis and predictive modeling. By mastering these fundamentals and continuously practicing with real-world datasets, you can build sophisticated models that extract valuable insights from data.'''
        },
        'CSS Grid Layout': {
            'content': '''CSS Grid Layout is a two-dimensional layout system that allows you to create complex web layouts with rows and columns. Unlike Flexbox, which is primarily one-dimensional, Grid excels at creating overall page layouts and complex component designs.

Basic Concepts
--------------

Grid layout involves a grid container and grid items:

```css
.grid-container {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr; /* Three equal columns */
    grid-template-rows: 100px 200px;    /* Two rows */
    gap: 10px;                         /* Gap between items */
}
```

```html
<div class="grid-container">
    <div class="grid-item">1</div>
    <div class="grid-item">2</div>
    <div class="grid-item">3</div>
    <div class="grid-item">4</div>
    <div class="grid-item">5</div>
    <div class="grid-item">6</div>
</div>
```

Grid Template Areas
------------------

You can define named grid areas for more intuitive layouts:

```css
.layout {
    display: grid;
    grid-template-areas: 
        "header header header"
        "sidebar main aside"
        "footer footer footer";
    grid-template-columns: 200px 1fr 150px;
    grid-template-rows: 80px 1fr 60px;
    gap: 10px;
    height: 100vh;
}

.header { grid-area: header; }
.sidebar { grid-area: sidebar; }
.main { grid-area: main; }
.aside { grid-area: aside; }
.footer { grid-area: footer; }
```

```html
<div class="layout">
    <header class="header">Header</header>
    <nav class="sidebar">Sidebar</nav>
    <main class="main">Main Content</main>
    <aside class="aside">Aside</aside>
    <footer class="footer">Footer</footer>
</div>
```

Fractional Units and Functions
-----------------------------

CSS Grid provides powerful units and functions:

```css
.grid-container {
    display: grid;
    /* Using fr units for flexible sizing */
    grid-template-columns: 1fr 2fr 1fr; /* Middle column twice as wide */
    
    /* Using minmax for responsive behavior */
    grid-template-columns: repeat(3, minmax(200px, 1fr));
    
    /* Using fit-content */
    grid-template-columns: fit-content(200px) 1fr fit-content(150px);
    
    /* Auto-fit and auto-fill */
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
}
```

Grid Item Placement
-------------------

Control individual grid items:

```css
.grid-container {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    grid-template-rows: repeat(3, 100px);
    gap: 10px;
}

.item1 {
    /* Place item in specific column/row */
    grid-column: 1 / 3;  /* Columns 1 to 3 */
    grid-row: 1 / 2;     /* Row 1 */
}

.item2 {
    /* Using line names */
    grid-column: span 2; /* Span 2 columns */
    grid-row: 2;         /* Start at row 2 */
}

.item3 {
    /* Using grid-area shorthand */
    grid-area: 2 / 3 / 4 / 5; /* row-start / column-start / row-end / column-end */
}
```

Responsive Grid Layouts
-----------------------

Create responsive layouts with Grid:

```css
.responsive-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 20px;
}

/* Media queries for more control */
@media (max-width: 768px) {
    .responsive-grid {
        grid-template-columns: 1fr;
        gap: 10px;
    }
}

@media (min-width: 769px) and (max-width: 1024px) {
    .responsive-grid {
        grid-template-columns: repeat(2, 1fr);
    }
}

@media (min-width: 1025px) {
    .responsive-grid {
        grid-template-columns: repeat(3, 1fr);
    }
}
```

Alignment and Justification
---------------------------

Control alignment within the grid:

```css
.grid-container {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    grid-template-rows: repeat(2, 200px);
    gap: 15px;
    
    /* Align grid items within cells */
    align-items: center;     /* Vertical alignment */
    justify-items: center;   /* Horizontal alignment */
    
    /* Align entire grid within container */
    align-content: center;   /* Vertical alignment of grid */
    justify-content: center; /* Horizontal alignment of grid */
}

.grid-item {
    /* Override container alignment for individual items */
    align-self: start;       /* Align this item to top */
    justify-self: end;       /* Align this item to right */
}
```

Practical Examples
------------------

1. **Card Layout**:

```css
.card-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 20px;
    padding: 20px;
}

.card {
    background: white;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    padding: 20px;
}
```

2. **Dashboard Layout**:

```css
.dashboard {
    display: grid;
    grid-template-areas: 
        "header header header"
        "nav main aside"
        "nav footer footer";
    grid-template-columns: 200px 1fr 200px;
    grid-template-rows: 60px 1fr 60px;
    gap: 10px;
    height: 100vh;
}

.dashboard-header { grid-area: header; }
.dashboard-nav { grid-area: nav; }
.dashboard-main { grid-area: main; }
.dashboard-aside { grid-area: aside; }
.dashboard-footer { grid-area: footer; }
```

3. **Image Gallery**:

```css
.gallery {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
    grid-auto-rows: 200px;
    gap: 15px;
}

.gallery-item {
    background-size: cover;
    background-position: center;
    border-radius: 8px;
}
```

Browser Support and Fallbacks
-----------------------------

Grid has excellent browser support, but for older browsers:

```css
.grid-container {
    /* Fallback for older browsers */
    display: flex;
    flex-wrap: wrap;
    
    /* Modern browsers */
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 20px;
}

.grid-item {
    /* Fallback styles */
    flex: 1 1 300px;
    margin: 10px;
    
    /* Grid styles */
    margin: 0; /* Reset for grid */
}
```

Conclusion
----------

CSS Grid Layout provides powerful tools for creating complex, responsive web layouts. Its two-dimensional nature makes it ideal for overall page structure, while its alignment and placement features offer precise control over design elements. Mastering Grid will significantly improve your ability to create modern, responsive web designs.'''
        },
        'Node.js Backend Development': {
            'content': '''Node.js is a JavaScript runtime built on Chrome's V8 JavaScript engine that allows you to run JavaScript on the server. It's known for its non-blocking I/O and event-driven architecture, making it excellent for building scalable network applications.

Getting Started
---------------

Install Node.js from nodejs.org or use a package manager:

```bash
# Using nvm (Node Version Manager)
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
nvm install node
nvm use node

# Create a new project
mkdir my-node-app
cd my-node-app
npm init -y
```

Basic HTTP Server
-----------------

Create a simple HTTP server with Node.js:

```javascript
// server.js
const http = require('http');

const server = http.createServer((req, res) => {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/plain');
    res.end('Hello, World!\n');
});

const PORT = process.env.PORT || 3000;
server.listen(PORT, () => {
    console.log(`Server running at http://localhost:${PORT}/`);
});
```

Express.js Framework
--------------------

Express is the most popular web framework for Node.js:

```bash
npm install express
```

```javascript
// app.js
const express = require('express');
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Routes
app.get('/', (req, res) => {
    res.send('Hello from Express!');
});

app.get('/users/:id', (req, res) => {
    const userId = req.params.id;
    res.json({ id: userId, name: `User ${userId}` });
});

app.post('/users', (req, res) => {
    const { name, email } = req.body;
    // Save user to database
    res.status(201).json({ id: 123, name, email });
});

app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});
```

Middleware
----------

Middleware functions have access to the request and response objects:

```javascript
// Custom middleware
const logger = (req, res, next) => {
    console.log(`${new Date().toISOString()} - ${req.method} ${req.path}`);
    next(); // Pass control to next middleware
};

const auth = (req, res, next) => {
    const token = req.headers.authorization;
    if (!token) {
        return res.status(401).json({ error: 'Unauthorized' });
    }
    // Verify token
    next();
};

app.use(logger); // Apply to all routes
app.use('/protected', auth); // Apply only to /protected routes

// Error handling middleware
app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).json({ error: 'Something went wrong!' });
});
```

Database Integration
--------------------

Connect to databases using drivers or ORMs:

```bash
npm install mongoose  # MongoDB
npm install pg        # PostgreSQL
npm install sequelize # ORM for multiple databases
```

```javascript
// MongoDB with Mongoose
const mongoose = require('mongoose');

mongoose.connect('mongodb://localhost:27017/myapp');

const userSchema = new mongoose.Schema({
    name: String,
    email: { type: String, unique: true },
    createdAt: { type: Date, default: Date.now }
});

const User = mongoose.model('User', userSchema);

// CRUD operations
app.get('/users', async (req, res) => {
    try {
        const users = await User.find();
        res.json(users);
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

app.post('/users', async (req, res) => {
    try {
        const user = new User(req.body);
        await user.save();
        res.status(201).json(user);
    } catch (error) {
        res.status(400).json({ error: error.message });
    }
});
```

RESTful API Design
------------------

Create a well-structured REST API:

```javascript
// routes/users.js
const express = require('express');
const router = express.Router();
const User = require('../models/User');

// GET /api/users - Get all users
router.get('/', async (req, res) => {
    try {
        const users = await User.find();
        res.json(users);
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

// GET /api/users/:id - Get user by ID
router.get('/:id', async (req, res) => {
    try {
        const user = await User.findById(req.params.id);
        if (!user) {
            return res.status(404).json({ error: 'User not found' });
        }
        res.json(user);
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

// POST /api/users - Create new user
router.post('/', async (req, res) => {
    try {
        const user = new User(req.body);
        await user.save();
        res.status(201).json(user);
    } catch (error) {
        res.status(400).json({ error: error.message });
    }
});

// PUT /api/users/:id - Update user
router.put('/:id', async (req, res) => {
    try {
        const user = await User.findByIdAndUpdate(
            req.params.id,
            req.body,
            { new: true, runValidators: true }
        );
        if (!user) {
            return res.status(404).json({ error: 'User not found' });
        }
        res.json(user);
    } catch (error) {
        res.status(400).json({ error: error.message });
    }
});

// DELETE /api/users/:id - Delete user
router.delete('/:id', async (req, res) => {
    try {
        const user = await User.findByIdAndDelete(req.params.id);
        if (!user) {
            return res.status(404).json({ error: 'User not found' });
        }
        res.json({ message: 'User deleted successfully' });
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

module.exports = router;
```

Authentication
--------------

Implement authentication with JWT:

```bash
npm install jsonwebtoken bcryptjs
```

```javascript
// auth.js
const jwt = require('jsonwebtoken');
const bcrypt = require('bcryptjs');

const JWT_SECRET = process.env.JWT_SECRET || 'your-secret-key';

// Generate JWT token
const generateToken = (user) => {
    return jwt.sign(
        { id: user.id, email: user.email },
        JWT_SECRET,
        { expiresIn: '7d' }
    );
};

// Register user
app.post('/register', async (req, res) => {
    try {
        const { name, email, password } = req.body;
        
        // Check if user exists
        const existingUser = await User.findOne({ email });
        if (existingUser) {
            return res.status(400).json({ error: 'User already exists' });
        }
        
        // Hash password
        const salt = await bcrypt.genSalt(10);
        const hashedPassword = await bcrypt.hash(password, salt);
        
        // Create user
        const user = new User({ name, email, password: hashedPassword });
        await user.save();
        
        // Generate token
        const token = generateToken(user);
        
        res.status(201).json({ user, token });
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

// Login user
app.post('/login', async (req, res) => {
    try {
        const { email, password } = req.body;
        
        // Find user
        const user = await User.findOne({ email });
        if (!user) {
            return res.status(400).json({ error: 'Invalid credentials' });
        }
        
        // Check password
        const isMatch = await bcrypt.compare(password, user.password);
        if (!isMatch) {
            return res.status(400).json({ error: 'Invalid credentials' });
        }
        
        // Generate token
        const token = generateToken(user);
        
        res.json({ user, token });
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});
```

Testing
-------

Test your API with Jest and Supertest:

```bash
npm install --save-dev jest supertest
```

```javascript
// tests/users.test.js
const request = require('supertest');
const app = require('../app');

describe('Users API', () => {
    it('should get all users', async () => {
        const res = await request(app)
            .get('/api/users')
            .expect(200);
        
        expect(Array.isArray(res.body)).toBe(true);
    });
    
    it('should create a new user', async () => {
        const userData = {
            name: 'Test User',
            email: 'test@example.com',
            password: 'password123'
        };
        
        const res = await request(app)
            .post('/api/users')
            .send(userData)
            .expect(201);
        
        expect(res.body.name).toBe(userData.name);
        expect(res.body.email).toBe(userData.email);
    });
});
```

Deployment
----------

Deploy your Node.js application:

```bash
# Using PM2 process manager
npm install -g pm2
pm2 start app.js --name "my-app"
pm2 startup  # Generate startup script
pm2 save     # Save current process list

# Using Docker
# Dockerfile
FROM node:16
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
EXPOSE 3000
CMD ["node", "app.js"]
```

Environment Variables
---------------------

Manage configuration with environment variables:

```javascript
// config.js
require('dotenv').config();

module.exports = {
    port: process.env.PORT || 3000,
    databaseUrl: process.env.DATABASE_URL || 'mongodb://localhost:27017/myapp',
    jwtSecret: process.env.JWT_SECRET || 'your-secret-key',
    nodeEnv: process.env.NODE_ENV || 'development'
};
```

```bash
# .env
PORT=3000
DATABASE_URL=mongodb://localhost:27017/myapp
JWT_SECRET=your-super-secret-jwt-key
NODE_ENV=development
```

Conclusion
----------

Node.js provides a powerful platform for building scalable backend applications. With its vast ecosystem of packages, non-blocking I/O model, and JavaScript's familiarity, it's an excellent choice for modern web development. Mastering these concepts will enable you to build robust, efficient backend services.'''
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
    update_remaining_tutorials()