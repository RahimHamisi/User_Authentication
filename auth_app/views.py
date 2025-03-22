from django.shortcuts import render
import graphene

# Create your views here.
class LoginUserMutation(graphene.Mutation):
    pass



class RegisterUserMutation(graphene.Mutation):
    pass





class UserMutation(graphene.ObjectType):
    login_user=LoginUserMutation.Field()
    register_user=RegisterUserMutation.Field()