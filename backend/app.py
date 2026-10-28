from flask import Flask, jsonify


def create_app(): # function
    app = Flask(__name__) # creates a Flask application instance

    @app.route("/") # defines the URL the backend responds to
    def home():
        return jsonify({ # returns a JSON response with a welcome message and status
            "message": "Welcome to CallBack API!",
            "status": "running"
        })

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)