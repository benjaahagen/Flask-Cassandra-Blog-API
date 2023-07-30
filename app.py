from flask import Flask, request, jsonify
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import uuid
from datetime import datetime

app = Flask(__name__)

cluster = Cluster(['127.0.0.1']) 
session = cluster.connect('blog')  


@app.route('/post', methods=['POST'])
def create_post():
    id = uuid.uuid4()
    title = request.json.get('title')
    content = request.json.get('content')
    author = request.json.get('author')
    timestamp = datetime.now()

    session.execute(
        """
        INSERT INTO posts (id, title, content, author, timestamp)
        VALUES (%s, %s, %s, %s, %s)
        """,
        (id, title, content, author, timestamp)
    )

    return jsonify({'id': id}), 201


@app.route('/post/<string:id>', methods=['GET'])
def get_post(id):
    rows = session.execute('SELECT * FROM posts WHERE id = %s', (uuid.UUID(id),))

    for row in rows:
        return jsonify({'id': str(row.id), 'title': row.title, 'content': row.content, 'author': row.author, 'timestamp': row.timestamp})

    return jsonify({'error': 'Post not found'}), 404


@app.route('/post/<string:id>', methods=['PUT'])
def update_post(id):
    title = request.json.get('title')
    content = request.json.get('content')
    author = request.json.get('author')

    session.execute(
        """
        UPDATE posts
        SET title = %s, content = %s, author = %s
        WHERE id = %s
        """,
        (title, content, author, uuid.UUID(id))
    )

    return jsonify({'message': 'Post updated'}), 200


@app.route('/post/<string:id>', methods=['DELETE'])
def delete_post(id):
    session.execute('DELETE FROM posts WHERE id = %s', (uuid.UUID(id),))

    return jsonify({'message': 'Post deleted'}), 200


@app.route('/posts', methods=['GET'])
def get_all_posts():
    rows = session.execute('SELECT * FROM posts')

    posts = []
    for row in rows:
        posts.append({'id': str(row.id), 'title': row.title, 'content': row.content, 'author': row.author, 'timestamp': row.timestamp})

    return jsonify(posts), 200


if __name__ == '__main__':
    app.run(debug=True)
