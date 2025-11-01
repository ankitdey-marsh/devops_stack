import os
import sys

# ensure this file's directory is on sys.path so the local "app" package resolves
sys.path.insert(0, os.path.dirname(__file__))

from app import create_app
import config

app = create_app()

def main():
    app.run(host=config.HOST, port=config.PORT, debug=config.DEBUG)

if __name__ == "__main__":
    main()
