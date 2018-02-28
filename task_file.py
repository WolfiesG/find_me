p_name = (input("Enter Parcel name, or 'X' to Exit"))
tot_parcels = 0
am_parcels_acc = 0
tot_weight = 0
tot_price = 0
price = 0
consign = {}
while(p_name!='X'):
    length = float(input("Please enter Parcel Length (in cm)"))
    width = float(input("Please enter Parcel Width (in cm)"))
    breadth = float(input("Please enter Parcel Beadth (in cm)"))
    weight = float(input("Please enter Parcel Weight (in Kg)"))
    tot_parcels += 1
    if weight<1:
        print("Parcel too light")
    elif weight>10:
        print("Parcel too heavy")
    elif length>80 or width>80 or breadth>80 or length+width+breadth>200:
        print ("Parcel too large")
    else:
        print("Parcel "+p_name+" Okay")
        am_parcels_acc +=1
        tot_weight += weight
        if weight < 5:
            price = 10
        elif weight >= 5 and weight<=10:
            price = 10 + (weight-5)
        tot_price += price
        consign[p_name]= price
        

    p_name = (input("Enter Parcel name, or 'X' to Exit"))
print("Parcels Accepted: "+str(am_parcels_acc))
print("Parcels Rejected: "+str(tot_parcels - am_parcels_acc))
print("Consignment Weight: "+str(tot_weight)+" Kg")
print (consign)
