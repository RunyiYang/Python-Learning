from network.graph import NeighbourGraphBuilder

class PathFinder:
    """
    Task 3: Complete the definition of the PathFinder class by:
    - completing the definition of the __init__() method (if needed)
    - completing the "get_shortest_path()" method (don't hesitate to divide 
      your code into several sub-methods)
    """

    def __init__(self, tubemap):
        """
        Args:
            tubemap (TubeMap) : The TubeMap to use.
        """
        self.tubemap = tubemap

        graph_builder = NeighbourGraphBuilder()
        self.graph = graph_builder.build(self.tubemap)
        
        # Feel free to add anything else needed here.
        
        
    def get_shortest_path(self, start_station_name, end_station_name):
        """ Find ONE shortest path from start_station_name to end_station_name.
        
        The shortest path is the path that takes the least amount of time.

        For instance, get_shortest_path('Stockwell', 'South Kensington') 
        should return the list:
        [Station(245, Stockwell, {2}), 
         Station(272, Vauxhall, {1, 2}), 
         Station(198, Pimlico, {1}), 
         Station(273, Victoria, {1}), 
         Station(229, Sloane Square, {1}), 
         Station(236, South Kensington, {1})
        ]

        If start_station_name or end_station_name does not exist, return None.
        
        You can use the Dijkstra algorithm to find the shortest path from
        start_station_name to end_station_name.

        Find a tutorial on YouTube to understand how the algorithm works, 
        e.g. https://www.youtube.com/watch?v=GazC3A4OQTE
        
        Alternatively, find the pseudocode on Wikipedia: https://en.wikipedia.org/wiki/Dijkstra's_algorithm#Pseudocode

        Args:
            start_station_name (str): name of the starting station
            end_station_name (str): name of the ending station

        Returns:
            list[Station] : list of Station objects corresponding to ONE 
                shortest path from start_station_name to end_station_name.
                Returns None if start_station_name or end_station_name does not 
                exist.
                Returns a list with one Station object (the station itself) if 
                start_station_name and end_station_name are the same.
        """
        """
        Dijkstra's algorithm pseudocode:
        1:	function Dijkstra(Graph, source):
        2:	for each vertex v in Graph:	// Initialization
        3:	dist[v] := infinity	// initial distance from source to vertex v is set to infinite
        4:	previous[v] := undefined	// Previous node in optimal path from source
        5:	dist[source] := 0	// Distance from source to source
        6:	Q := the set of all nodes in Graph	// all nodes in the graph are unoptimized - thus are in Q
        7:	while Q is not empty:	// main loop
        8:	u := node in Q with smallest dist[ ]
        9:	remove u from Q
        10:	for each neighbor v of u:	// where v has not yet been removed from Q.
        11:	alt := dist[u] + dist_between(u, v)
        12:	if alt < dist[v]	// Relax (u,v)
        13:	dist[v] := alt
        14:	previous[v] := u
        15:	return previous[ ]
        """
        """
        Implementation in PathFinder:
        
        The get_shortest_path() method initializes the shortest paths for all stations with a distance of infinity, except for the starting station which is initialized with a distance of zero.
        The method then iterates through unvisited stations, updating the shortest paths based on the connections and their durations.
        
        The nested dictionary graph represents the stations as nodes and the connections (and their durations) as edges, facilitating the application of Dijkstra's algorithm.
        
        The algorithm continues to explore the graph until the destination station is reached or all stations have been visited.
        
        Finally, the shortest path is reconstructed by backtracking from the destination station using the shortest paths data.
        """
        # Initialization variables
        # shortest_paths is a dictionary of the form {station_id: (duration, previous_station_id)}
        # unvisited_stations is a list of station ids
        # current_station_id is a string of number
        shortest_paths = {station: (float('infinity'), None) for station in self.tubemap.stations.keys()}  # {station_id: (duration, previous_station_id)}
        unvisited_stations = list(self.tubemap.stations.keys())
        current_station_id = None

        # Find start station id
        for station_id, station in self.tubemap.stations.items():
            if station.name == start_station_name:
                current_station_id = station_id
                break
        
        # If start or end station names don't exist in the graph, return None
        if not current_station_id or end_station_name not in [station.name for station in self.tubemap.stations.values()]:
            return None

        # Starting station has a duration of 0 to itself
        shortest_paths[current_station_id] = (0, None)

        # Iterate through unvisited stations, if current station has a shorter duration than the current shortest duration, update the shortest duration until the destination station is reached or all stations have been visited
        while current_station_id:
            current_duration = shortest_paths[current_station_id][0]
            # For every path from the current station
            for neighbour, connections in self.graph[current_station_id].items():
                # Calculate the shortest duration among all connections between the two stations
                min_duration = min([int(connection.time) for connection in connections])  # Ensure time is treated as an integer
                duration_through_current = current_duration + min_duration
                if duration_through_current < shortest_paths[neighbour][0]:
                    shortest_paths[neighbour] = (duration_through_current, current_station_id)
            # Delete visited stations from the unvisited stations list
            unvisited_stations.remove(current_station_id)
            # Re init and update id. If the all ides are visited, while loop will end
            current_station_id = None
            shortest_duration = float('infinity')
            for station_id in unvisited_stations:
                if shortest_paths[station_id][0] < shortest_duration:
                    shortest_duration = shortest_paths[station_id][0]
                    current_station_id = station_id

        # Construct the path
        # id : name
        # name: [station]
        path = []
        while end_station_name:
            for station_id, station in self.tubemap.stations.items():
                if station.name == end_station_name:
                    path.append(station)
                    end_station_name = None
                    next_station_id = shortest_paths[station_id][1]
                    if next_station_id:
                        end_station_name = self.tubemap.stations[next_station_id].name
                    break

        return path[::-1]



def test_shortest_path():
    from tube.map import TubeMap
    tubemap = TubeMap()
    tubemap.import_from_json("data/london.json")
    
    path_finder = PathFinder(tubemap)
    stations = path_finder.get_shortest_path("Covent Garden", "Covent Garden")
    print(stations)
    
    station_names = [station.name for station in stations]
    expected = ["Covent Garden", "Leicester Square", "Piccadilly Circus", 
                "Green Park"]
    assert station_names == expected


if __name__ == "__main__":
    test_shortest_path()
