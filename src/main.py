import time

from functions import *

from display_graph import display_graph
from readfile import readfile
from printing import printing, printingPenalty
from northwest import NorthWest


def menu():
    print("Hello, welcome to our Operations Research project! \n")
    print("This program has been written by Paul HU, Oscar BYRNE, Issey BOULET-TONGIER and Romain FERIGO.\n")
    time.sleep(2)

    while True:
        i=0
        while i==0:
            print("What do you want to do?")
            print("1. Test an existing file")
            print("2. Generate a random one")

            k=int(input("Type your choice: "))
            if k==1:
                print("\nWhich file do you want to test?")
                a=str(input("Type the number of the file (from 1 to 14): "))
                a += ".txt"
                data=readfile(a)
                if data!=None:
                    i=1
            elif k==2:
                print("Which size do you want to chose?")
                size=int(input("Type the size of your choice: "))
                data=randTable(size)
                i=1
    
        i=0
        while i!="2" and i!="1":
            print("\nWhich method do you want to use?")
            print("1. North-West\n2. Balas-Hammer")
            i=str(input("Type your choice: "))

        print("\nThe data is the following:")
    
        (datalist,order,provision)=data
        printing(datalist,order,provision) 
        if i=="1":   
            (transportdata,transportorder,transportprovision)=NorthWest(datalist, order, provision)
        else:
            (transportdata,transportorder,transportprovision)=BalasHammer(datalist,order,provision,datalist)
        a=0
        printing(transportdata,transportorder,transportprovision)
        g=display_graph(transportdata)
        best_improvement=None
        err=0
        precost=Costculation(transportdata,datalist,p=False)
        while a==0 :
        
            print("\n Starting the test:")
            test=testcircular(g,p=True)
            if can_reach_all_nodes(g)==False:
                print("The graph is degenerate.")
            while test!=1 or can_reach_all_nodes(g)==False:
            
                if test!=1:
                    (transportdata,g)=rectifCircular(test,transportdata, g,order,provision,best_improvement)
                if can_reach_all_nodes(g)==False:
                    g=testContinuity(g,datalist)

                test=testcircular(g)
            print("Test finished")
            potentials = calculate_potentials(g, datalist)
        
            display_potentials(potentials)
            potential_costs = calculate_potential_costs(transportdata, potentials)
            marginal_costs = calculate_marginal_costs(datalist, potential_costs)
            print('The potential costs is: ')
            print(tabulate(potential_costs, tablefmt="grid"))
            print('The marginal costs is: ')
            print(tabulate(marginal_costs, tablefmt="grid"))
            best_improvement=detect_best_improvement(marginal_costs,transportdata)
            if best_improvement is not None:
                # Ici, vous pouvez ajouter du code pour effectuer les modifications nécessaires dans votre réseau de transport
                # Par exemple, augmenter la capacité de l'arête identifiée comme amélioration potentielle
            
                if (err==10):
                    print("No possible improvement has been detected.")
                    a=1
                    cost=0
                    printingMarginal(marginal_costs)
                    for i in range(len(transportdata)):
                        for j in range(len(transportdata[i])):
                            cost+=transportdata[i][j]*datalist[i][j]
                    print(cost)
                    break 
                else:
                
                    print(tabulate(marginal_costs, tablefmt="grid"))
                    print("Best improvement detected: ", best_improvement)
                    print("The current cost is ")
                    postcost=Costculation(transportdata,datalist)
                    g.add_edge("P"+str(best_improvement[1]+1),"C"+str(best_improvement[0]+1))
                    if precost==postcost:
                        err+=1
                    else:
                        err=1
                    precost=postcost
                
                #printing(transportdata,transportorder,transportprovision)
            else:
                print("No potential improvement has been detected.")
                a=1
                cost=0
                for i in range(len(transportdata)):
                    for j in range(len(transportdata[i])):
                        cost+=transportdata[i][j]*datalist[i][j]
                print(cost)
                printing(transportdata,order,provision)
        z=None
        while z!="1" and z!="2":
            print("Do you want to continue?")
            print("1. Yes")
            pritn("2. No")
            z=str(input())
        if z=="2":
            break


if __name__ == "__main__":
    menu()