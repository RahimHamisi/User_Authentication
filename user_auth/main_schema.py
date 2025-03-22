import graphene

from auth_app.schema import UserQuery
from auth_app.views import UserMutation


class Query(UserQuery,graphene.ObjectType):
    pass




class Mutation(UserMutation,graphene.ObjectType):
    pass




schema=graphene.Schema(query=   Query,mutation=Mutation)