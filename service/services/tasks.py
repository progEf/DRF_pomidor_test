import time

from celery import shared_task
from django.db.models import Prefetch, F, Sum
from celery_singleton import Singleton

@shared_task(base = Singleton)
def set_price(sur_id):
    from services.models import Subscription
    time.sleep(5)

    sur = Subscription.objects.filter(id=sur_id).annotate(annotate_price=F('service__full_price') -
                     F('service__full_price') * F('plan__discount_percent') / 100.00).first()

    sur.price = sur.annotate_price
    sur.save()