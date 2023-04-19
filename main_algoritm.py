import osmnx as ox
import networkx as nx
from geopy.geocoders import Nominatim
import webbrowser
import os
ox.use_cache = False
ox.log_console = False

loc = Nominatim(user_agent="none")

print("Откуда")
adress_1 = input()#Чапаева 8а Киров или любой другой мне нужны баги, мои дорогие тестеры
getLoc = loc.geocode(adress_1)
start_x = getLoc.longitude
start_y = getLoc.latitude

print("Куда")
adress_2 = input()#Карла Маркса 84 Киров или любой другой мне нужны баги, мои дорогие тестеры
location = loc.geocode(adress_2)
end_x = location.longitude
end_y = location.latitude

place = 'Kirov,Kirov Oblast,Volga Federal District,Russia'
mode = 'drive'#,'walk'
optimizer = 'time'

graph = ox.graph_from_place(place, network_type = mode)

orig_node = ox.nearest_nodes(graph, start_x, start_y)

dest_node = ox.nearest_nodes(graph, end_x, end_y)

shortest_route = nx.shortest_path(graph, orig_node, dest_node,
                                  weight=optimizer)
shortest_route_map = ox.plot_route_folium(graph, shortest_route,
                                          tiles='openstreetmap')
shortest_route_map.save('map.html')
webbrowser.open('file://' + os.path.realpath('map.html'))