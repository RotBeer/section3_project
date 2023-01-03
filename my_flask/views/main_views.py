from flask import Blueprint, request, render_template
from urllib.parse import urlparse
import os

main_bp = Blueprint('main', __name__)


@main_bp.route('/')
def index():
    metabase_url = os.getenv('metabase_url')
    print(metabase_url)
    return render_template('index.html', metabase_url=metabase_url), 200