from flask_restplus import Namespace, Resource
from ...utils.auth import auth
from ...repositories import SamplesRepository
from .models import sample_model


api = Namespace('samples')


@api.route('')
class SamplesResource(Resource):

    @auth(api)
    @api.marshal_with(sample_model(api), as_list=True)
    def get(self):
        return SamplesRepository.getlist()

@api.route('/<int:id>')
class SamplesResource(Resource):

    @auth(api)
    @api.marshal_with(sample_model(api))
    def get(self, id):
        return SamplesRepository.getitem(id)
