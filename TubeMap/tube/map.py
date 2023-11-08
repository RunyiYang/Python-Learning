import json
from tube.components import Station, Line, Connection
    
class TubeMap:
    """
    Task 1: Complete the definition of the TubeMap class by:
    - completing the "import_from_json()" method

    Don't hesitate to divide your code into several sub-methods, if needed.

    As a minimum, the TubeMap class must contain these three member attributes:
    - stations: a dictionary that indexes Station instances by their id 
      (key=id (str), value=Station)
    - lines: a dictionary that indexes Line instances by their id 
      (key=id, value=Line)
    - connections: a list of Connection instances for the TubeMap 
      (list of Connections)
    """

    def __init__(self):
        self.stations = {}  # key: id (str), value: Station instance
        self.lines = {}  # key: id (str), value: Line instance
        self.connections = []  # list of Connection instances
    def load_data(self, data):
        """_summary_

        Args:
            time: int
            line: Line
            stations: set[Station]
            id: str
            name: str
        """
        # Load stations
        for station_data in data["stations"]:
            zone_float = float(station_data["zone"])
            if zone_float.is_integer():
                zones = {int(zone_float)}
            else:
                zone_int = int(zone_float)
                zones = {zone_int, zone_int + 1}
            station = Station(station_data["id"], station_data["name"], zones)
            self.stations[station.id] = station

        # Load lines
        for line_data in data["lines"]:
            line = Line(line_data["line"], line_data["name"])
            self.lines[line.id] = line

        # Load connections
        for connection_data in data["connections"]:
            station1 = self.stations[connection_data["station1"]]
            station2 = self.stations[connection_data["station2"]]
            line = self.lines[connection_data["line"]]
            time = int(connection_data["time"])
            connection = Connection({station1, station2}, line, time)
            self.connections.append(connection)

    def import_from_json(self, filename):
        """ Import tube map information from a JSON file.
        
        During the import process, the `stations`, `lines` and `connections` 
        attributes should be updated.

        You can use the `json` python package to easily load the JSON file at 
        `filepath`

        Note: when the indicated zone is not an integer (for instance: "2.5"), 
            it means that the station belongs to two zones. 
            For example, if the zone of a station is "2.5", 
            it means that the station is in both zones 2 and 3.

        Args:
            filepath (str) : relative or absolute path to the JSON file 
                containing all the information about the tube map graph to 
                import. If filepath is invalid, no attribute should be updated, 
                and no error should be raised.

        Returns:
            None
        """
        with open(filename, 'r') as file:
            data = json.load(file)
        self.load_data(data)

    def __repr__(self):
        return f"TubeMap with {len(self.stations)} stations, {len(self.lines)} lines, and {len(self.connections)} connections."



def test_import():
    tubemap = TubeMap()
    tubemap.import_from_json("data/london.json")
    
    # view one example Station
    print(tubemap.stations[list(tubemap.stations)[0]])
    
    # view one example Line
    print(tubemap.lines[list(tubemap.lines)[0]])
    
    # view the first Connection
    print(tubemap.connections[0])
    
    # view stations for the first Connection
    print([station for station in tubemap.connections[0].stations])


if __name__ == "__main__":
    test_import()
