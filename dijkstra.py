# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 06:31:49 2021

@author: Heba Mohamed
"""
import json
import math as mt
import sys
import pandas as pd

class Airport:
    
    
    '''
    PARAMETERS
    ----------
    data = {'airport id': {
                            'Longitude': float num,
                            'Latitude': float num,
                            'destinations': [other airports ids]
                            }
    }
    '''
    def __init__(self, all_nodes: list, data: dict):
        
        self.airport_dict = data
        self.airport_graph = self.calc_euclidean_distance(all_nodes,data)     
        
    def calc_euclidean_distance(self,all_nodes,data):
    
        '''
        RETURN 
        ----------
        airport_graph ={
                        'airport id1': {'airport id2': euclidean distance between the 2 airports,
                                        'airport id3': euclidean distance between the 2 airports,
                                        ...},
                        
                        'airport id2': {'airport id3': euclidean distance between the 2 airports,
                                        'airport id4': euclidean distance between the 2 airports,
                                        ...}
                            }
        
        Euclidean Equation
        -------
            distance = sqrt[ (x2– x1)^2 + (y2 – y1)^2].
        '''
        airport_graph = {}

        for node in all_nodes:
            # select a node, then measure the distance between this node and the neighbours (in te destination list)
            airport_graph[node]={}
            
            # measure distance between airport = node and all the other neighbour airports
            for neighbour in self.airport_dict[node]['destinations']:
                lng1 = self.airport_dict[node]['Longitude']
                lat1 = self.airport_dict[node]['Latitude']
                try:
                    # if the destenation node (airport) doesn't exist skip
                    lng2 = self.airport_dict[neighbour]['Longitude']
                    lat2 = self.airport_dict[neighbour]['Latitude']
                    
                    d_lng = (lng1 - lng2)**2
                    d_lat = (lat1 - lat2)**2
                    distance = round(mt.sqrt(d_lng + d_lat),2)
                    
                    # displaying the distance during calculation
                    # print("The distance between '{:4s}' and '{:4s}' is-> {:4.2f}".format(node, neighbour,distance))
                    airport_graph[node][neighbour] = distance
                except:
                    continue
        
        return airport_graph
            
    def get_graph_nodes(self,airport_graph):
        '''Returns the airport geaph with Euclidean distances'''
        return self.airport_graph

###############################################################################
###############################################################################        
class Graph(object):
    '''
    First, we’ll create the Graph class. 
    but it will make the implementation of the algorithm more succinct. 
    '''
    def __init__(self, nodes, init_graph):
        self.nodes = nodes
        self.graph = self.construct_graph(nodes, init_graph)
        
    def construct_graph(self, nodes, init_graph):
        '''
        This method makes sure that the graph is symmetrical. 
        In other words, if there's a path from node A to B with a value V, 
        there needs to be a path from node B to node A with a value V.
        '''
        graph = {}
        for node in nodes:
            graph[node] = {}
        
        graph.update(init_graph)
        
        for node, edges in graph.items():
            for adjacent_node, value in edges.items():
                if graph[adjacent_node].get(node, False) == False:
                    graph[adjacent_node][node] = value
                                        
        return graph
    
    def get_nodes(self):
        ''''Returns the nodes of the graph.'''
        return self.nodes
    
    def get_outgoing_edges(self, node):
        '''Returns the neighbors of a node.'''
        connections = []
        for out_node in self.nodes:
            if self.graph[node].get(out_node, False) != False:
                connections.append(out_node)
        return connections
    
    def get_distance(self, node1, node2):
        '''Returns the distance between any 2 nodes'''
        return round(self.graph[node1][node2],2)
    
###############################################################################
###############################################################################
class Dijkstra:  
    def __init__(self, graph, start_node):
        self.graph = graph
        self.start_node = start_node
    
    def dijkstra_algorithm(self,graph, start_node):
        unvisited_nodes = list(graph.get_nodes())
     
        # We'll use this dict to save the cost of visiting each node and update it as we move along the graph   
        shortest_path = {}    
        # We'll use this dict to save the shortest known path to a node found so far
        previous_nodes = {}    
        # We'll use max_value to initialize the "infinity" value of the unvisited nodes   
        max_value = sys.maxsize
        for node in unvisited_nodes:
            shortest_path[node] = max_value
        # However, we initialize the starting node's value with 0   
        shortest_path[start_node] = 0
        
        # The algorithm executes until we visit all nodes
        while unvisited_nodes:
            # The code block below finds the node with the lowest score
            current_min_node = None
            for node in unvisited_nodes: # Iterate over the nodes
                if current_min_node == None:
                    current_min_node = node
                elif shortest_path[node] < shortest_path[current_min_node]:
                    current_min_node = node
                    
            # The code block below retrieves the current node's neighbors and updates their distances
            neighbors = graph.get_outgoing_edges(current_min_node)
            for neighbor in neighbors:
                tentative_value = shortest_path[current_min_node] + graph.get_distance(current_min_node, neighbor)
                if tentative_value < shortest_path[neighbor]:
                    shortest_path[neighbor] = tentative_value
                    # We also update the best path to the current node
                    previous_nodes[neighbor] = current_min_node
     
            # After visiting its neighbors, we mark the node as "visited"
            unvisited_nodes.remove(current_min_node)
        return previous_nodes, shortest_path

    def find_shortest_path(self, source, dest):
        previous_nodes, shortest_path = self.dijkstra_algorithm(self.graph, source)
        path = []
        node = dest
        while node != source:
            path.append(node)
            node = previous_nodes[node]
        # Add the start node manually
        path.append(source)
        return shortest_path[dest], path

###############################################################################
###############################################################################
######## Read and parse the json file in pandas datframe ########

def parse_json(json_path):
    with open(json_path) as file:
        data = json.load(file)
        
    # Keep only the usefull information and store it in a new dictionay
    '''airport_dict ={'airport id': {
                                'Longitude': float num,
                                'Latitude': float num,
                                'destinations': [other airports ids]
                                }
        }
    '''
    airport_dict = dict()
    for i in data:
        airport_dict[ i['Airport ID'] ]= {}
        airport_dict[ i['Airport ID'] ]['Longitude'] = float(i['Longitude']) 
        airport_dict[ i['Airport ID'] ]['Latitude'] = float(i['Latitude']) 
        airport_dict[ i['Airport ID'] ]['destinations'] = i['destinations'] 
    
    nodes = list(airport_dict.keys())
    
    airport = Airport(nodes, airport_dict)
    init_graph = airport.airport_graph
    
    graph = Graph(nodes,init_graph)
    
    return init_graph, airport_dict, graph, data
###############################################################################
###############################################################################
