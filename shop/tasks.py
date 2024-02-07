from django.db.models import Sum

from ecommerce_innovation.celery import app
from shop.models import Shop, Order, DailyData


@app.task(name="ecommerce_innovation.calculate_daily_data")
def calculate_daily_data():
    shops = Shop.objects.all()
    for shop in shops:
        print(shop)
        stats = Order.objects.filter(shop=shop).aggregate(Sum('total_amount'), Sum('total_quantity'))
        try:
            DailyData.objects.create(
                shop=shop,
                total_amount=stats.get('total_amount__sum'),
                total_quantity=stats.get('total_quantity__sum')
            )
        except Exception as e:
            print(e)
            pass
