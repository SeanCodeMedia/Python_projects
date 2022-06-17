
hotel = 140 

charlotte = 183 

Tampa = 220 

Pirrsburgh = 222 

Los_Angeles = 475

price = 40

cost = None 

discount = None 


def hotel_cost (nights):
    
    return hotel*nights 
    

def plane_ride_cost( city ):
    
    if city == "Charlotte": 
        
        return charlotte
    if city == "Tampa": 
        
        return Tampa
        
    if city == "Pittsburgh":
        
        return Pirrsburgh
    if city == "Los Angeles": 
        
        return Los_Angeles
        
        

plane_ride_cost("Charlette")

#################TRANSPORTATION################

def rental_car_cost (days): 
    
    if days >= 7: 
        
       discount = price*days
        
       cost = discount - 50
        
       print cost 
        
       return cost 
        
    elif days >= 3:
        
      discount = price*days 
      cost = discount - 20
      print cost 
      return cost

    elif days < 3:
        cost = price*days 
        print cost

    	return cost

rental_car_cost(1) 

    
