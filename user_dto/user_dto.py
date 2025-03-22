import graphene



class UserInputObject(graphene.InputObjectType):
    username=graphene.String(required=True)
    email=graphene.String()
    phone_number=graphene.String()
    password=graphene.String(required=True)
    first_name=graphene.String()
    last_name=graphene.String()

class UserOutputObject(graphene.ObjectType):
    id=graphene.String()
    username=graphene.String()
    phone_number=graphene.String()
    is_verified=graphene.Boolean()

class TokenOutputObject(graphene.ObjectType):
    access_token=graphene.String()
    refresh_token=graphene.String()
