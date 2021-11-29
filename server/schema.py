import graphene

import apps.graphql.schema
import apps.ask_codex.schema

class Query(
    apps.graphql.schema.Query,
    apps.ask_codex.schema.Query,
):
    pass

class Mutation(
    apps.graphql.schema.Mutation,
    apps.ask_codex.schema.Mutation,
):
    pass

context = {

}

schema = graphene.Schema(query=Query, mutation=Mutation)
