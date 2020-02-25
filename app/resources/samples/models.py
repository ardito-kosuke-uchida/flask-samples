from flask_restplus import fields


def sample_model(api):
    return api.model('Sample Model', model={
        'name': fields.String,
        'age': fields.Integer,
    })
