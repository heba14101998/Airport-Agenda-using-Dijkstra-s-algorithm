# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 22:30:32 2021

@author: Heba Mohamed
"""
import dijkstra as dk 

json_path = 'Airports.json'
init_graph, airport_dict, graph, data = dk.parse_json(json_path)

######## User inputs 
print('\n#### Welcome to Airport Agenda System! Enter your source airport index (◒‿◒) ####')
src_idx = input("(a number netween 0 and {}): ".format(len(init_graph)).upper()) 

while src_idx:
    try:
        src_idx = int(src_idx)
        src=list(airport_dict.keys())[src_idx]    
        break
    except:
        src_idx = input("Invalid input please enter a number netween 0 and {}  (◒‿◒): ".format(len(init_graph))) 
        continue

dest_idx = input("Enter your destination airport index (◒‿◒)(a number netween 0 and {}): ".format(len(init_graph))) 
while dest_idx:
    try :
        dest_idx = int(dest_idx)
        dest=list(airport_dict.keys())[dest_idx]    
        break
    except:
        dest_idx = input("Invalid airport index please enter a number netween 0 and {}  (◒‿◒): ".format(len(init_graph))) 
        continue
        
######## clalling algoithm and measure the path     
print("Praparing your agenda (◒‿◒)")
DA = dk.Dijkstra(graph, src)
shortest_val, path = DA.find_shortest_path(src, dest)

######## Display Path by airports names and ids ########  
''' names is a dictionary keys = airports ides and values is airports names'''
names = dict()
for i in data:
    names[ i['Airport ID'] ]= {}
    names[ i['Airport ID'] ]['Name'] = i['Name'] 

path_list = list(names[i]['Name'] for i in path)
 
print('\n#################### final report ####################\n\nWe found that the best path between:\n'.upper())
print("You have to  [{}] and [{}] has a distance value of = {}.".format(src,dest,round(shortest_val,2)))
print("""\n"{}" is the source airport name to reach your destination in the "{}" airport.""".format(names[src]['Name'], names[dest]['Name']))
print ('\nyour agenda (shortest path):\n'.upper())
print(" -> ".join(reversed(path)))
print("\n")
print(" -> ".join(reversed(path_list)))
print('\n#################### happy trip (◒‿◒) ####################\n'.upper())



