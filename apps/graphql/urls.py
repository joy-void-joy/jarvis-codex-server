import re
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView

import importlib
from server.settings import GRAPHENE
schema = importlib.import_module('.'.join(GRAPHENE['SCHEMA'].split('.')[:-1]))

class GraphiQLView(GraphQLView):
    context = {}

    def __init__(self, graphiql_template=None, context={}, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.context = context

        if graphiql_template is not None:
            self.graphiql_template = graphiql_template

graphql_view = GraphiQLView.as_view(
        graphiql_template='graphql/graphql.html',
        graphiql=True,
        context=schema.context
    )

urlpatterns = [
    path("", csrf_exempt(graphql_view)),
]