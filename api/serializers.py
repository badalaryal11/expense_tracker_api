from django.contrib.auth.models import User
from rest_framework import serializers
from .models import ExpenseIncome

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # Creates and returns a new user with a hashed password.
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user


class ExpenseIncomeSerializer(serializers.ModelSerializer):
    # The `total` property from the model is automatically included as a read-only field.
    class Meta:
        model = ExpenseIncome
        fields = [
            'id', 'title', 'description', 'amount', 'transaction_type',
            'tax', 'tax_type', 'total', 'created_at', 'updated_at'
        ]
        # The user is set automatically in the view based on the request.
        read_only_fields = ('user',)