from my_app import db

class ExampleModelClass(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))

    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return '<ExampleModelClass %d>' % self.id