from flask import Blueprint, jsonify, request, abort
from flask.views import MethodView 
from my_app import app, db
from my_app.my_module.models import ExampleModelClass

import json

home = Blueprint('home', __name__)

@home.route('/')
@home.route('/home')
def index():
    return 'Wellcome to the homepage!'

class ExampleRESTClassModelView(MethodView):
    
    def get(self, id=None):
        if not id:
            # find and return the first 10 objects, if no gived an id
            example_items = ExampleModelClass.query.paginate(1, 10).items
            result = {item.id: {'name': item.name} for item in example_items}
        else:
            # find and return a gived id object
            example_item = ExampleModelClass.query.filter_by(id=id).first()
            if not example_item:
                abort(404, 'Item não existe')
            result = {'name': example_item.name}
        return jsonify(result), 200
    
    def post(self):
        # create an object and save the data
        name = json.loads(request.data.decode()).get('name')
        example_item = ExampleModelClass(name)

        db.session.add(example_item)
        db.session.commit()

        return jsonify({
            example_item.id: {
                'name': example_item.name
            }
        })

example_view = ExampleRESTClassModelView.as_view('example_view')
app.add_url_rule('/example/', view_func=example_view, methods=['GET', 'POST'])
app.add_url_rule('/example/<int:id>', view_func=example_view, methods=['GET'])

