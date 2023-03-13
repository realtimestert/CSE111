from datetime import datetime

current_date_and_time = datetime.now()
day_of_week = current_date_and_time.weekday()

print(day_of_week)

subtotal = float(input("Please enter the subtotal: "))

if subtotal >= 50 and (day_of_week == 1 or day_of_week ==2):
    pre_discount = subtotal*.1
    discount = subtotal-pre_discount
    new_sales_tax = discount*.06
    new_total = new_sales_tax + discount
    print (f"Discount amount: ${pre_discount:.2f}")
    print (f"Sales tax amount: ${new_sales_tax:.2f}")
    print (f"Total: ${new_total:.2f}")
    
else:
    sales_tax = subtotal*.06
    total = sales_tax + subtotal
    print (f"Sales tax amount: ${sales_tax:.2f}")
    print (f"Total: ${total:.2f}")

