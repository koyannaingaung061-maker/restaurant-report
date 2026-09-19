def calculate_orders(records):
    total_orders=0
    for record in records:
        total_orders=total_orders+record["orders"]
    return total_orders
def calculate_sales(records):
    total_sales=0
    for record in records:
        total_sales=total_sales+record["sales"]
    return total_sales
def calculate_expense(records):
    total_expense=0
    for record in records:
        total_expense=total_expense+record["expense"]
    return total_expense
def calculate_profit(sales,expense):
    profit=sales-expense
    return profit
def calculate_average(sales,orders):
    average=sales/orders
    return average
records=[{"day":"Tursday","orders":32,"sales":640000,"expense":370000},{"day":"Friday","orders":45,"sales":900000,"expense":510000},{"day":"Saturday","orders":58,"sales":1160000,"expense":650000},{"day":"Sunday","orders":50,"sales":1000000,"expense":580000}]
orders=calculate_orders(records)
sales=calculate_sales(records)
expense=calculate_expense(records)
profit=calculate_profit(sales,expense)
average=calculate_average(sales,orders)
print("Total Orders:",orders)
print("Total Sales:",sales)
print("Total Expense:",expense)
print("Profit:",profit)
print("Average Sales per Orders:",average)

    
