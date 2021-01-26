import pandas as pd

data = pd.read_csv('data_analytics.csv')
payment_per_subscription = 9.99
apple_percent = 0.3

data['Pay'] = data['Subscription Offer Type'] != 'Free Trial'
subscriptions = data[['Subscriber ID', 'Pay']]
subscriptions_per_subscriber = subscriptions.groupby('Subscriber ID')
subscribers = len(subscriptions_per_subscriber)
money_per_subscriber = (subscriptions_per_subscriber.sum()) * payment_per_subscription
ltv = money_per_subscriber.mean() * (1 - apple_percent)
print('LTV: {}'.format(ltv.item()))
