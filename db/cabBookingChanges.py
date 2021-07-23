def readCabCSV(destination,people,lugguage): 
        result = "Cabs are not available for your location and preferences.\n Please try changing your preferences."
        if people:
            people=people.lower()
        if(people in ["one people","two people","three people" ,"four people"]):
             maxpeople= 4 
        elif(people in ["five people","six people","seven people"]):
              maxpeople= 7
        elif(int(people) <=3):
             maxpeople =3
        elif(int(people) <=4):
             maxpeople =4
        elif(int(people) <=7):
             maxpeople =7
        else:
             maxpeople = int(people)
    
        if lugguage:
            lugguage=lugguage.lower() 
        if(lugguage in ["one bag","two bags"]):
            maxlugguage= 2 ;
        elif(lugguage in ["three bags"]):     
             maxlugguage=3;
        elif(lugguage in ["four bags","five bags","six bags","seven bags","seven bags"]):
             maxlugguage= 8 ;     
        elif(int(lugguage) <=2):
             maxlugguage =2
        elif(int(lugguage) <=3):
             maxlugguage =3
        elif(int(lugguage) <=8):
             maxlugguage =8
        else:
            maxlugguage=int(lugguage)
            
        print("maxlugguage=",maxlugguage)
        print("maxpeople=",maxpeople)
        data = pd.read_csv("db/cabsavailable.csv")

        #print("Initial data:\n",data)
        if(len(data.index) != 0):
            data = data.loc[data['location'] == ('madhapur')]
            print("After location filter:\n",data)
        else:
            return result
        if(len(data.index) != 0):
            data = data[data['maxnumber'] == maxpeople]
            print("After people filter:\n",data)
        else:
            return result
        if(len(data.index) != 0):
            data = data[data['maxluggage'] == maxlugguage]
            print("After lugguage filter:\n",data)
        else:
            return result
        result = ""
        if(len(data.index) != 0):
            result = "Cab booked :" + data.values[0][1]+" - "+data.values[0][4]    
        return result
def perform_action_cab_booking(attributes):
    result = readCabCSV(attributes['destination'],attributes['people'],attributes['luggage'])
    return result, IntentComplete()

