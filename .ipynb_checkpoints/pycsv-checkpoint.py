import pandas as pd

orders = pd.read_csv("orders.csv", parse_dates = ["order_date"])
customers = pd.read_csv("customers.csv", parse_dates = ["signup_date"])
products = pd.read_csv("products.csv")

## (rows, columns)
#print(f'{orders.shape} \n {customers.shape}\n{products.shape}') 

#print(f'---TOP 5 ORDERS---\n {orders.head(5)}')
#print(f'---LAST 5 ORDERS---\n {orders.tail(5)}')

#orders.info()
#describe()finds mean, median, standard deviation, average, etc
#print(orders.describe()) 
#print(f'{orders[["city", "order_date"]].head(5)}')
#print(f'---Specific rows and columns---\n{orders[orders["price"] > 5000].head(5)}')

#creating a derived column
orders["revenue"] = orders["price"]*orders["quantity"]
#print(f'Added new column "revenue" \n{orders[["order_id", "price", "quantity", "revenue"]].head(3)}')
filter = (orders["category"] == "Electronics") & \
       (orders["city"] == "Mumbai") & \
       (orders["revenue"] > 2000)

'''
print(f'filtered rows \n(orders["category"] == "Electronics") & \
       \n(orders["city"] == "Mumbai") & \
       \n(orders["revenue"] > 2000)')
print(orders[filter][["order_id", "brand", "revenue"]].head())
'''
metro = orders[orders["city"].isin(["Mumbai", "Delhi", "Bengaluru"])]
#print(f'{len(metro)} items ordered in the three biggest metros \n("Mumbai", "Delhi", "Bengaluru")')

# to show data relative to categories groupby(col)[measure].agg(...)
by_category =  (orders.groupby("category")["revenue"].sum().sort_values(ascending = False))

#print(f' ---REVENUE AS PER CATEGORY---\n{by_category}')
