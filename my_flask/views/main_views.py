from flask import Blueprint, request
from urllib.parse import urlparse

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    host = urlparse(request.base_url).hostname
    url = f'http://{host}:3000/public/dashboard/1e49d05a-b978-4b3b-9c01-22faaa1aeaca'
    iframe = f'<iframe src="{url}" frameborder="0" width="100%" height="100%" allowtransparency></iframe>'
    return iframe, 200