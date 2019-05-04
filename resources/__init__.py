from sanic.response import json
from sanic.views import HTTPMethodView


class SmokeResources(HTTPMethodView):

    async def get(self, *args, **kwargs):
        return json({"200": "Data Push"})
