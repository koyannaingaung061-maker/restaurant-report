date=input("Enter date (YYYY-MM-DD:)")
total_sales=0
total_orders=0
while True:
    sale=input("Enter sale").strip().lower()
    if sale=="done":
        break
    sale=int(sale)
    total_sales=total_sales+sale
    total_orders=total_orders+1
average=total_sales/total_orders
print("===== DAILY SALES REPORT =====")
print("Date:",date)
print("Total Sales:",total_sales)
print("Total Orders:",total_orders)
print("Average Sale Per Order:",average)
