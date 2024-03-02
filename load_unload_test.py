#Robotic Forklift Load and Unload Test
#Benjamin A. Keller
#3/2/2022

'''
===============================================================================

In this example, the program commands a robotic forklift to load and 
unload accordingly depending on what task is being executed between. 
I start by implementing an action based on what input is needed, cuing
the user whether or not they want to load or unload an item from a shelf, 
with conditional booleans of 'load' and 'unload' set to false. Once an action 
is given the forklift will either load a product from receiving to put from 
the shelve, unload to go to shipping, or state an error of an invalid input. 
In addition, it will execute basic functions of a forklift to safelyoperate the 
tasks. Once either stocking or picking is complete, the boolean sets to true, 
and the forklift will retract with a decrementing loop. 

===============================================================================
'''

# action  is set as input, with booleans "load" and "unload" set to false as default: 

action = input("is task stocking or picking? ")
load = False 
unload = False

# initial feature of commanding a robot to load a product:

if action.lower() == "stocking": 
    print("product from receiving on forklift going to putaway")
    print()
    for ext in range (5):
        print("fork extending", ext)
    if ext == 4: 
        print("\nproduct stocked on shelve")
        load = True 
        
    if load == True:
        print("\nitem loaded")
        print() 
        ret = 5
        while ret > 0: 
            ret -= 1  
            print("fork retracting", ret)
            if ret == 0: 
                print("forklift retracted - safe to proceed with next task")

# feature if the user wants to unload product:            

elif action.lower() == "picking":
    print("forklift empty - set to pick an ordered product from shelf to go to shipping")
    print()
    for ext in range (5):
        print("fork extending", ext)
    if ext == 4:  
        print("\nproduct retreved from shelve")
        unload = True 
    
    if unload == True:
        print("\nitem on the fork ")
        print() 
        ret = 5 
        while ret > 0: 
            ret -= 1
            print("fork retracting", ret) 
            if ret == 0: 
                print("forklift retracted - safe to move product to shipping")

# result for inputing an invalad option: 
else:
    print("error: invalad option")
