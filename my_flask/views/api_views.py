import pickle
import json
from urllib.parse import urlparse
from flask import Blueprint, render_template, request
from my_flask import PKL_FILEPATH

api_bp = Blueprint('api', __name__)

@api_bp.route('/')
def index():
    host = urlparse(request.base_url).hostname
    return render_template('api_index.html', host=host), 200

@api_bp.route('/pred')
def pred():
    args_dict = request.args.to_dict()

    if args_dict.get('Education') == None:
        return 'Education Required!', 400
    if args_dict.get('Education') not in ['Graduation', 'PhD', 'Master', 'Basic', '2n Cycle']:
        return 'Education value is not available!'
    if args_dict.get('Marital_Status') == None:
        return 'Marital_Status Required!', 400
    if args_dict.get('Marital_Status') not in ['Single', 'Together', 'Married', 'Divorced', 'Widow', 'Alone', 'Absurd', 'YOLO']:
        return 'Marital_Status value is not available!'

    model = None
    with open(PKL_FILEPATH, 'rb') as pickle_file:
        model = pickle.load(pickle_file)

    X_data = [{'Year_Birth': args_dict.get('Year_Birth'), 'Education': args_dict.get('Education'), 'Marital_Status': args_dict.get('Marital_Status'),
                'Income': args_dict.get('Income'), 'Kidhome': args_dict.get('Kidhome'), 'Teenhome': args_dict.get('Teenhome')}]
    pred = round(model.predict(X_data)[0], 2)
    data = {'predict': pred}
    json_data = json.dumps(data)
    
    return json_data, 200