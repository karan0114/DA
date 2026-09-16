import pandas as pd

orders = pd.read_csv("orders.csv", parse_dates = ["order_date"])
customers = pd.read_csv("customers.csv", parse_dates = ["signup_date"])
products = pd.read_csv("products.csv")

## (rows, columns)
#print(f'{orders.shape} \n {customers.shape}\n{products.shape}') 

#print(f'---TOP 5 ORDERS---\n {orders.head(5)}')
#print(f'---LAST 5 ORDERS---\n {orders.tail(5)}')

#orders.info()
#print(orders[["category", "city"]].describe())
print(f'{orders[["city", "order_date"]].head(5)}')
print(f'---Specific rows and columns---\n{orders[orders["price"] > 5000].head(3)}')

