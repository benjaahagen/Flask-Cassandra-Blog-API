# Flask-Cassandra-Blog-API
This project is a RESTful API for a blog application. It's built with Flask and uses Apache Cassandra for data storage. The API allows for creating, reading, updating, and deleting blog posts.


## Usage
The server will start on localhost port 5000. You can make requests to the following endpoints:

- `POST /post`: Create a new post. The request body should be a JSON object with "title", "content", and "author" fields.
- `GET /post/<id>`: Get a specific post.
- `PUT /post/<id>`: Update a specific post. The request body should be a JSON object with the fields you want to update.
- `DELETE /post/<id>`: Delete a specific post.
- `GET /posts`: Get all posts.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
