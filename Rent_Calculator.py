
# 🏠 Smart Rent Management System – Python Project (2025 Edition)
# 🎯 Objective
''' A Python-based system that helps landlords and tenants calculate, 
                     track, and manage rent with automation, AI features, and modern add-ons.'''
# 📋 Features
''' 1. Rent Calculator: Calculate monthly rent based on various parameters.
    2. Payment Tracker: Track rent payments and due dates.'''

#                                                rent calculator                                                          #

base_rent=int(input("enter your base rent :"))
no_of_tenents=int(input("enter how tenents live :"))
maintanance=int(input("enter maintainance charge per month :"))

# #utility
eletricity_usage=int(input("enter how many units eletricity used :"))
charge_per_unit=int(input("enter eletricity charge per unit in  ₹ :"))
water_usage=int(input("enter how many kiloliters(Kl) water used :"))
charge_per_kiloliters=int(input("enter water charge per kiloliter(kl) in ₹ :"))



# #calculations
grand_total=base_rent+maintanance+(eletricity_usage*charge_per_unit)+(water_usage*charge_per_kiloliters)
print("your total expenses including rent and maintanance is ",grand_total,"₹")
print("each tenet have to give :",(grand_total/no_of_tenents),"₹")

#                                                payment tracker                                                         #

from datetime import datetime

due_date=input("enter due date like (dd-mm-yyyy) :")
payment_day=input("enter payment date like (dd-mm-yyyy) :")

due_date = datetime.strptime(due_date, "%d-%m-%Y")
payment_day = datetime.strptime(payment_day, "%d-%m-%Y")


late_day=(payment_day-due_date).days

late_fee=0

if late_day>0:
    late_fee=late_day*20
    print("you have to pay late fee of ",late_fee,"₹")
else:
        print("no late fee payment on time !")






