date=input("Enter date (YYYY-MM-DD):")
total_sales=0
total_orders=0
while True:
    sale=input("Enter sale:").strip().lower()
    if sale=="done":
        break
    try:
        sale=int(sale)
    except ValueError:
        print("Please enter a number or 'done'.")
        continue
    total_sales=total_sales+sale
    total_orders=total_orders+1
if total_orders>0:
    average=total_sales/total_orders
else:
    average=0
print("===== DAILY SALES REPORT =====")
print("Date:",date)
print("Total Sales:",total_sales)
print("Total Orders:",total_orders)
print("Average Sale Per Order:",average)
with open("daily_report.txt","a") as file:
    file.write("Date:"+date+"\n")
    file.write("Total Sales:"+str(total_sales)+"\n")
    file.write("Total Orders:"+str(total_orders)+"\n")
    file.write("Average Sale Per Order:"+str(average)+"\n")
print("Report Save Successfully")
      
        
        
        
    

