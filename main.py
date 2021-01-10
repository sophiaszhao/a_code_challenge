from flask import Flask, jsonify
import os
import psycopg2
from psycopg2.extras import RealDictCursor
import simplejson as json
app = Flask(__name__)

connection = psycopg2.connect(host='localhost', user=os.getenv('POSTGRES_USER'), password=os.getenv('POSTGRES_PASSWORD'))

@app.route('/')
def starships_by_rating():
    cursor = connection.cursor(cursor_factory=RealDictCursor)
    cursor.execute("SELECT * FROM starships ORDER BY rating ASC")
    starships = cursor.fetchall()
    cursor.close()
    return jsonify(starships)

if __name__ == '__main__':
    app.run(debug=True)