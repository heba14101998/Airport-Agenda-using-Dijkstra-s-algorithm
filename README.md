# Airport Agenda using Dijkstra's algorithm
Reserving air flights can be a complex problem, especially between cities not connected by a direct flight. The goal of this project is to apply Dijkstraβs Algorithm to find the shortest path from starting airport to destination airport, such that minimizes the total travel distance to its destination.

# Tools

* Python json library.
* Python math library.
* Python system library.
* Python pandas library.
* Spyder IDE.

# Dataset
We are given a json file contains a list of airports with some geo-information like city, country and location (longitude, latitude) , airport id as well as airport specific designations (a list of destination airports) as shown below:

{{< figure src="/images/Projects/Project2 dataset.png" title="" >}}

# Delivables
## Application (main.py)
1. Take inputs from user and avoiding user error as shown
{{< figure src="/images/Projects/Project2 inputs.png" title="" >}}

2. Read and parse the json file.
3. Calling the immplemednted algorithm from its medule
4. Print airport agenda to user as shown:. 
{{< figure src="/images/Projects/Project2 outputs.png" title="" >}}


## Implementation Steps (dijkstrs.py)
1. Create a class called _π¨ππππππ_ takes the information of airport (π΄ππππππ‘ πΌπ· πΏπππππ‘π’ππ, πΏππ‘ππ‘π’ππ, π·ππ π‘ππππ‘ππππ ) as arguments of its constructor.
2. Create _π«πππππππ_ class that manages the whole process (e.g. it contains all the Airports in a list etc.,). Moreover, this class contains a function called ππππ_π‘βπ_π βπππ‘ππ π‘_πππ‘β(π ππ’πππ, πππ πππ‘ππ‘πππ)
	- I apply Euclidean distance formula as follows:
3. Store the distance between each airport with their destinations in Airport class.
4. Some airports are not existing so that I create a function in _**Graph**_ class to delete any missing airport ID from airport destination

