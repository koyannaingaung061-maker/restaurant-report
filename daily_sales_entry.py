date=input("Enter date (YYYY-MM-DD):")
total_sales=0
total_orders=0
while True:
    sale=input("Enter sale:").strip().lower()
    if sale=="done":
        break
    sale=int(sale)
    total_sales=total_sales+sale
    total_orders=total_orders+1
average=total_sales/total_orders
print("====== DIALY SALES REPORT ======")
print("Date:",date)
print("Total_sales:",total_sales)
print("Total_orders:",total_orders)
print("Average Sale Per Order:",average)
file=open("daily_report.txt","a")
file.write("Date:"+date+"\n")
file.write("Total Sales:"+str(total_sales)+"\n")
file.write("Total Orders:"+str(total_orders)+"\n")
file.write("Average Sale Per Orders:"+str(average)+"\n")
file.close()
print("Report saved successfully.")
file=open("daily_report.txt","r")
print(file.read())
file.close()

