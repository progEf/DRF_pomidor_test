from rest_framework import serializers

from services.models import Subscription, Plan


class PlanSerializers(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = ('__all__')


class SubscriptionSerializers(serializers.ModelSerializer):
    plan = PlanSerializers()
    client_name = serializers.CharField(source='client.company_name')
    email = serializers.CharField(source='client.user.email')

    class Meta:
        model = Subscription
        fields = ('id', 'plan_id', 'client_name', 'email', 'plan')

