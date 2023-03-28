from flask import Flask

app = Flask(__name__)
#name is a predefined variable
from app import routes
#application importing routes (placed at the bottom to workaround circular imports)
