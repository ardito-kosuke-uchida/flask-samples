from .samples import api as samples_api


def setup_resources(api):
    api.add_namespace(samples_api)
