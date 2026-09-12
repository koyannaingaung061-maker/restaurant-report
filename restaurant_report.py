def restarurant_report(records):
    total_sales=0
    total_expense=0
    for record in records:
        total_sales=total_sales+record["sales"]
        total_expense=total_expense+record["expense"]
    profit=total_sales-total_expense
    return total_sales,total_expense,profit
records=[{"day":"Monday","sales":350000,"expense":210000},{"day":"Tuesday","sales":280000,"expense":170000},{"day":"Wednesday","sales":420000,"expense":250000},{"day":"Thursday","sales":310000,"expense":190000}]
sales,expense,profit=restarurant_report(records)
print(sales)
print(expense)
print(profit)

    
    