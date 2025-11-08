import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'techblog.settings')
django.setup()

from tech.models import Article

def update_article_content():
    """Update articles with more complete content"""
    
    # Define more complete content for each article
    article_updates = {
        'The Future of Web Development': {
            'content': '''Web development is constantly evolving, with new technologies and frameworks emerging regularly. Understanding the trends shaping the future of web development can help developers stay ahead of the curve and build better applications.

Progressive Web Apps (PWAs)
---------------------------

Progressive Web Apps combine the best of web and mobile applications. They're reliable, fast, and engaging, working seamlessly across different devices and network conditions. PWAs can work offline, send push notifications, and be installed on users' home screens.

Key features of PWAs:
- Responsive design that works on any device
- Offline functionality through service workers
- App-like interactions with smooth animations
- Safe and secure with HTTPS
- Discoverable through search engines
- Installable like native apps
- Fresh content with automatic updates

WebAssembly (WASM)
------------------

WebAssembly is a binary instruction format that allows code written in multiple languages to run at near-native speed in web browsers. It opens up web development to languages like C, C++, Rust, and others, enabling performance-critical applications like games, video editing, and scientific computing to run in the browser.

Benefits of WebAssembly:
- Near-native performance
- Language diversity beyond JavaScript
- Better security through sandboxing
- Smaller file sizes than JavaScript
- Faster parsing and compilation

Serverless Architecture
-----------------------

Serverless computing allows developers to build and run applications without managing servers. Cloud providers handle the infrastructure, automatically scaling applications based on demand.

Advantages of serverless:
- Reduced operational overhead
- Automatic scaling
- Pay-per-execution pricing model
- Faster time to market
- Built-in high availability

Micro Frontends
---------------

Similar to microservices for the backend, micro frontends break down large frontend applications into smaller, independent pieces. Different teams can work on separate parts of the application using different technologies.

Benefits of micro frontends:
- Team autonomy and independence
- Technology diversity
- Easier maintenance and updates
- Better fault isolation
- Independent deployment

Artificial Intelligence Integration
-----------------------------------

AI is increasingly being integrated into web development tools and processes:
- AI-powered code completion and suggestions
- Automated testing and debugging
- Smart UI/UX design assistance
- Personalized user experiences
- Chatbots and virtual assistants

Static Site Generators and JAMstack
-----------------------------------

The JAMstack (JavaScript, APIs, Markup) architecture is gaining popularity for its performance, security, and scalability benefits. Static site generators like Next.js, Gatsby, and Nuxt.js pre-render pages at build time.

Advantages of JAMstack:
- Improved performance and speed
- Better security with no server-side processing
- Lower hosting costs
- Better developer experience
- Easier scaling

Edge Computing
--------------

Edge computing brings computation and data storage closer to users, reducing latency and improving performance. Content delivery networks (CDNs) are evolving to include edge computing capabilities.

Benefits of edge computing:
- Reduced latency
- Improved user experience
- Better handling of traffic spikes
- Enhanced security
- Compliance with data residency requirements

Web Components and Component Libraries
--------------------------------------

Web Components provide a standardized way to create reusable custom elements. Framework-agnostic component libraries are becoming more popular, allowing teams to share UI components across projects.

Future Technologies to Watch
----------------------------

1. **WebGPU**: Next-generation graphics API for the web
2. **WebXR**: Extended reality on the web (VR/AR)
3. **HTTP/3**: Next version of the HTTP protocol
4. **Container Queries**: Responsive design based on container size
5. **Native File System API**: Direct file system access in browsers

Conclusion
----------

The future of web development is exciting, with technologies focused on improving performance, developer experience, and user experience. Staying informed about these trends and continuously learning new technologies will help developers build better web applications and remain competitive in the field.

As we move forward, the emphasis will continue to be on creating faster, more secure, and more accessible web experiences for users worldwide. The key is to balance adopting new technologies with maintaining compatibility and performance across different devices and browsers.''',
            'tags': 'web-development future trends'
        },
        'Best Practices for Code Quality': {
            'content': '''Writing clean, maintainable code is essential for long-term project success. Good code quality improves collaboration, reduces bugs, and makes future modifications easier. Here are the key best practices for maintaining high code quality.

Code Readability
----------------

Readable code is maintainable code. Focus on writing code that others (and future you) can easily understand:

1. **Use meaningful names**: Variable, function, and class names should clearly express their purpose.
   ```javascript
   // Bad
   const d = new Date();
   const elapsed = t2 - t1;
   
   // Good
   const currentDate = new Date();
   const elapsedTimeInMs = endTime - startTime;
   ```

2. **Write self-documenting code**: The code itself should tell a story.
   ```python
   # Bad
   def calc(x, y, z):
       return x * y * z
   
   # Good
   def calculate_volume(length, width, height):
       return length * width * height
   ```

3. **Keep functions small**: Functions should do one thing and do it well.
   ```javascript
   // Bad - function doing multiple things
   function processUserOrder(order) {
       // Validate order
       // Calculate total
       // Apply discounts
       // Save to database
       // Send confirmation email
   }
   
   // Good - small, focused functions
   function validateOrder(order) { /* ... */ }
   function calculateTotal(order) { /* ... */ }
   function applyDiscounts(order) { /* ... */ }
   function saveOrder(order) { /* ... */ }
   function sendConfirmationEmail(order) { /* ... */ }
   ```

Consistent Coding Standards
---------------------------

Establish and follow consistent coding standards across your team:

1. **Style guides**: Adopt established style guides (like PEP 8 for Python, Airbnb for JavaScript)
2. **Naming conventions**: Consistently use camelCase, snake_case, or PascalCase
3. **File organization**: Maintain consistent directory structures
4. **Commenting practices**: Comment why, not what

Code Reviews
------------

Code reviews are crucial for maintaining quality and knowledge sharing:

1. **Review checklists**: Create standard checklists for common issues
2. **Automated tools**: Use linters and static analysis tools
3. **Constructive feedback**: Focus on the code, not the person
4. **Knowledge sharing**: Use reviews as learning opportunities

Testing Practices
-----------------

Comprehensive testing ensures code reliability:

1. **Test-driven development (TDD)**: Write tests before code
2. **Unit tests**: Test individual functions and components
3. **Integration tests**: Test how components work together
4. **End-to-end tests**: Test complete user workflows
5. **Test coverage**: Maintain high test coverage percentages

```javascript
// Example of well-tested function
function calculateDiscount(price, discountPercent) {
    if (price < 0) throw new Error('Price cannot be negative');
    if (discountPercent < 0 || discountPercent > 100) {
        throw new Error('Discount percent must be between 0 and 100');
    }
    
    return price * (discountPercent / 100);
}

// Tests
describe('calculateDiscount', () => {
    test('calculates correct discount', () => {
        expect(calculateDiscount(100, 20)).toBe(20);
    });
    
    test('throws error for negative price', () => {
        expect(() => calculateDiscount(-10, 20)).toThrow('Price cannot be negative');
    });
    
    test('throws error for invalid discount percent', () => {
        expect(() => calculateDiscount(100, 150)).toThrow('Discount percent must be between 0 and 100');
    });
});
```

Documentation
-------------

Good documentation is as important as good code:

1. **API documentation**: Document all public APIs
2. **Inline comments**: Explain complex logic
3. **README files**: Provide project setup and usage instructions
4. **Architecture diagrams**: Visual representations of system design

Error Handling
--------------

Proper error handling prevents crashes and improves user experience:

```python
# Good error handling pattern
def read_user_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        logger.error(f"User file not found: {filename}")
        return None
    except PermissionError:
        logger.error(f"Permission denied reading file: {filename}")
        raise  # Re-raise if it's a critical error
    except Exception as e:
        logger.error(f"Unexpected error reading file {filename}: {e}")
        return None
```

Performance Optimization
-----------------------

Write efficient code without sacrificing readability:

1. **Algorithm efficiency**: Choose appropriate data structures and algorithms
2. **Avoid premature optimization**: Profile first, optimize bottlenecks
3. **Memory management**: Be mindful of memory usage
4. **Caching**: Use caching for expensive operations

Security Best Practices
-----------------------

Security should be built into the development process:

1. **Input validation**: Always validate and sanitize user input
2. **Authentication and authorization**: Implement proper access controls
3. **Secure dependencies**: Keep dependencies updated
4. **Security testing**: Include security in your testing process

Refactoring
-----------

Regular refactoring keeps code clean and maintainable:

1. **Technical debt**: Track and address technical debt
2. **Boy Scout Rule**: Leave code better than you found it
3. **Refactoring patterns**: Learn common refactoring patterns
4. **Automated refactoring**: Use IDE tools for safe refactoring

Version Control Best Practices
------------------------------

Effective use of version control improves collaboration:

1. **Meaningful commit messages**: Explain what and why, not how
2. **Small, focused commits**: Make small, logical changes
3. **Branching strategies**: Use appropriate branching models
4. **Pull requests**: Use PRs for code review and discussion

Continuous Integration/Continuous Deployment (CI/CD)
----------------------------------------------------

Automate quality checks and deployment:

1. **Automated testing**: Run tests on every commit
2. **Code quality checks**: Integrate linters and static analysis
3. **Security scanning**: Include security checks in pipelines
4. **Automated deployment**: Reduce human error in deployments

Monitoring and Logging
----------------------

Proper monitoring helps identify issues early:

1. **Application logging**: Log important events and errors
2. **Performance monitoring**: Track application performance
3. **Error tracking**: Monitor and alert on errors
4. **User analytics**: Understand how users interact with your application

Conclusion
----------

Maintaining code quality is an ongoing process that requires commitment from the entire development team. By following these best practices, you can create code that is not only functional but also maintainable, secure, and efficient.

Remember that code quality is not just about following rules—it's about creating software that serves its users well and can be easily maintained and extended over time. The investment in quality upfront pays dividends in reduced maintenance costs and improved developer satisfaction throughout the life of the project.''',
            'tags': 'coding best-practices quality'
        },
        'Understanding RESTful APIs': {
            'content': '''REST (Representational State Transfer) is an architectural style for designing networked applications. RESTful APIs have become the standard for web services, providing a consistent and scalable way to expose application functionality over HTTP.

What is REST?
-------------

REST is an architectural style that defines a set of constraints and properties based on HTTP. A RESTful system typically uses HTTP verbs (GET, POST, PUT, DELETE) to perform operations on resources identified by URLs.

Key Principles of REST
----------------------

1. **Client-Server Architecture**: Separation of concerns between client and server
2. **Statelessness**: Each request from client to server must contain all the information needed to understand and process the request
3. **Cacheability**: Responses must define themselves as cacheable or not
4. **Uniform Interface**: Simplifies and decouples architecture
5. **Layered System**: Client cannot tell whether it's connected directly to the server or to an intermediary
6. **Code on Demand (optional)**: Servers can temporarily extend client functionality

HTTP Methods (Verbs)
--------------------

REST APIs use standard HTTP methods to perform CRUD operations:

- **GET**: Retrieve a resource or collection of resources
- **POST**: Create a new resource
- **PUT**: Update an existing resource (complete replacement)
- **PATCH**: Partially update an existing resource
- **DELETE**: Remove a resource

```http
GET /api/users/123        # Get user with ID 123
POST /api/users           # Create a new user
PUT /api/users/123        # Update user with ID 123 (full replacement)
PATCH /api/users/123      # Partially update user with ID 123
DELETE /api/users/123     # Delete user with ID 123
```

Resource Naming Conventions
---------------------------

Use nouns for resource names, not verbs:

```http
# Good
GET /api/users
GET /api/users/123
POST /api/users
PUT /api/users/123

# Bad
GET /api/getUsers
GET /api/deleteUser/123
POST /api/createUser
```

Use plural nouns for collections:

```http
# Good
GET /api/users
GET /api/users/123

# Avoid
GET /api/user
GET /api/user/123
```

HTTP Status Codes
-----------------

Use appropriate HTTP status codes to indicate the result of operations:

**2xx Success**
- 200 OK: General success
- 201 Created: Resource successfully created
- 204 No Content: Successful operation with no response body

**4xx Client Errors**
- 400 Bad Request: Invalid request data
- 401 Unauthorized: Authentication required
- 403 Forbidden: Authenticated but no permission
- 404 Not Found: Resource doesn't exist
- 409 Conflict: Resource conflict (e.g., duplicate)

**5xx Server Errors**
- 500 Internal Server Error: Generic server error
- 503 Service Unavailable: Temporarily unavailable

Request and Response Format
---------------------------

Use JSON for request and response bodies:

```http
POST /api/users HTTP/1.1
Content-Type: application/json
Accept: application/json

{
    "name": "John Doe",
    "email": "john@example.com",
    "age": 30
}
```

```http
HTTP/1.1 201 Created
Content-Type: application/json

{
    "id": 123,
    "name": "John Doe",
    "email": "john@example.com",
    "age": 30,
    "createdAt": "2023-01-01T00:00:00Z"
}
```

Versioning
----------

API versioning ensures backward compatibility:

1. **URL Versioning**: `/api/v1/users`
2. **Header Versioning**: `Accept: application/vnd.myapi.v1+json`
3. **Query Parameter**: `/api/users?version=1`

Filtering, Sorting, and Pagination
----------------------------------

Provide mechanisms for clients to control data retrieval:

```http
# Filtering
GET /api/users?status=active&role=admin

# Sorting
GET /api/users?sort=name,-createdAt

# Pagination
GET /api/users?page=2&limit=20

# Combining
GET /api/users?status=active&sort=-createdAt&page=1&limit=10
```

Error Handling
--------------

Return consistent error responses:

```json
{
    "error": {
        "code": "VALIDATION_ERROR",
        "message": "Invalid input data",
        "details": [
            {
                "field": "email",
                "message": "Email is required"
            },
            {
                "field": "age",
                "message": "Age must be a positive number"
            }
        ]
    }
}
```

Rate Limiting
-------------

Implement rate limiting to prevent abuse:

```http
HTTP/1.1 429 Too Many Requests
Retry-After: 3600

{
    "error": {
        "code": "RATE_LIMIT_EXCEEDED",
        "message": "Rate limit exceeded. Try again in 1 hour."
    }
}
```

Headers for Rate Limiting:
```http
X-RateLimit-Limit: 1000
X-RateLimit-Remaining: 999
X-RateLimit-Reset: 1610000000
```

Authentication and Authorization
--------------------------------

Secure your APIs properly:

1. **API Keys**: Simple authentication for public APIs
2. **OAuth 2.0**: Industry standard for authorization
3. **JWT (JSON Web Tokens)**: Stateless authentication
4. **Bearer Tokens**: Standard HTTP authentication scheme

```http
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

Documentation
-------------

Provide comprehensive API documentation:

1. **OpenAPI/Swagger**: Standard specification for REST APIs
2. **Interactive documentation**: Tools like Swagger UI
3. **Examples**: Provide request/response examples
4. **SDKs**: Client libraries for popular languages

CORS (Cross-Origin Resource Sharing)
------------------------------------

Handle CORS properly for web clients:

```http
Access-Control-Allow-Origin: https://myapp.com
Access-Control-Allow-Methods: GET, POST, PUT, DELETE
Access-Control-Allow-Headers: Content-Type, Authorization
```

Security Best Practices
-----------------------

1. **HTTPS**: Always use HTTPS in production
2. **Input Validation**: Validate and sanitize all inputs
3. **SQL Injection Prevention**: Use parameterized queries
4. **CSRF Protection**: Implement CSRF tokens for state-changing operations
5. **Security Headers**: Set appropriate security headers

HATEOAS (Hypermedia as the Engine of Application State)
-------------------------------------------------------

Include links in responses to guide clients:

```json
{
    "id": 123,
    "name": "John Doe",
    "email": "john@example.com",
    "links": {
        "self": "/api/users/123",
        "update": "/api/users/123",
        "delete": "/api/users/123",
        "orders": "/api/users/123/orders"
    }
}
```

API Design Tools
----------------

Use tools to design and test your APIs:

1. **Postman**: API testing and development
2. **Insomnia**: REST client with advanced features
3. **Swagger Editor**: Design APIs with OpenAPI specification
4. **Mock servers**: Create mock APIs for development

Testing REST APIs
-----------------

Comprehensive testing ensures API reliability:

1. **Unit tests**: Test individual endpoints
2. **Integration tests**: Test API workflows
3. **Load testing**: Test performance under load
4. **Security testing**: Test for vulnerabilities

Example Implementation
----------------------

Here's a simple example of a RESTful API implementation using Express.js:

```javascript
const express = require('express');
const app = express();

app.use(express.json());

// In-memory data store (in real apps, use a database)
let users = [
    { id: 1, name: 'John Doe', email: 'john@example.com' },
    { id: 2, name: 'Jane Smith', email: 'jane@example.com' }
];

// GET /api/users - Get all users
app.get('/api/users', (req, res) => {
    const { page = 1, limit = 10 } = req.query;
    const startIndex = (page - 1) * limit;
    const endIndex = page * limit;
    
    const paginatedUsers = users.slice(startIndex, endIndex);
    
    res.json({
        data: paginatedUsers,
        pagination: {
            page: parseInt(page),
            limit: parseInt(limit),
            total: users.length
        }
    });
});

// GET /api/users/:id - Get user by ID
app.get('/api/users/:id', (req, res) => {
    const user = users.find(u => u.id === parseInt(req.params.id));
    if (!user) {
        return res.status(404).json({
            error: {
                code: 'USER_NOT_FOUND',
                message: 'User not found'
            }
        });
    }
    res.json(user);
});

// POST /api/users - Create new user
app.post('/api/users', (req, res) => {
    const { name, email } = req.body;
    
    // Validation
    if (!name || !email) {
        return res.status(400).json({
            error: {
                code: 'VALIDATION_ERROR',
                message: 'Name and email are required'
            }
        });
    }
    
    // Create user
    const newUser = {
        id: users.length + 1,
        name,
        email
    };
    
    users.push(newUser);
    res.status(201).json(newUser);
});

// PUT /api/users/:id - Update user
app.put('/api/users/:id', (req, res) => {
    const userIndex = users.findIndex(u => u.id === parseInt(req.params.id));
    if (userIndex === -1) {
        return res.status(404).json({
            error: {
                code: 'USER_NOT_FOUND',
                message: 'User not found'
            }
        });
    }
    
    const { name, email } = req.body;
    if (!name || !email) {
        return res.status(400).json({
            error: {
                code: 'VALIDATION_ERROR',
                message: 'Name and email are required'
            }
        });
    }
    
    users[userIndex] = {
        id: parseInt(req.params.id),
        name,
        email
    };
    
    res.json(users[userIndex]);
});

// DELETE /api/users/:id - Delete user
app.delete('/api/users/:id', (req, res) => {
    const userIndex = users.findIndex(u => u.id === parseInt(req.params.id));
    if (userIndex === -1) {
        return res.status(404).json({
            error: {
                code: 'USER_NOT_FOUND',
                message: 'User not found'
            }
        });
    }
    
    users.splice(userIndex, 1);
    res.status(204).send();
});

app.listen(3000, () => {
    console.log('API server running on port 3000');
});
```

Conclusion
----------

RESTful APIs provide a standardized way to build web services that are scalable, maintainable, and interoperable. By following REST principles and best practices, you can create APIs that are easy to use, understand, and integrate with.

The key to successful REST API design is consistency, proper use of HTTP standards, comprehensive documentation, and thorough testing. As you develop your APIs, keep the end users in mind and strive to create interfaces that are intuitive and reliable.''',
            'tags': 'api rest web-services'
        }
    }
    
    # Update articles with more complete content
    updated_count = 0
    for title, updates in article_updates.items():
        try:
            article = Article.objects.get(title=title)
            article.content = updates['content']
            article.tags = updates['tags']
            article.save()
            print(f"Updated content for article: {title}")
            updated_count += 1
        except Article.DoesNotExist:
            print(f"Article not found: {title}")
        except Exception as e:
            print(f"Error updating article '{title}': {e}")
    
    print(f"\nUpdated {updated_count} articles with complete content!")

if __name__ == '__main__':
    update_article_content()