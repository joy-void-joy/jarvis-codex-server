from __future__ import annotations

import graphene
from graphql_auth import mutations as auth_mutations

class Query(graphene.ObjectType):
    _pass = graphene.Boolean()

class Mutation(graphene.ObjectType):
    token_auth = auth_mutations.ObtainJSONWebToken.Field()
    verify_token = auth_mutations.VerifyToken.Field()
    refresh_token = auth_mutations.RefreshToken.Field()
    revoke_token = auth_mutations.RevokeToken.Field()
