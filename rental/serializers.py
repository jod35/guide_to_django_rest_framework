from rest_framework import serializers
from . import models


class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        fields =["id","name"]
        model=models.Friend



class BelongingSerializer(serializers.ModelSerializer):
    class Meta:
        fields =["id","name"]
        model=models.Belonging


class BorrowedSerializer(serializers.ModelSerializer):
    class Meta:
        fields =["id","what","to_who","when"]
        model=models.Borrowed