from math import sqrt
import heapq

def shortest_path(M, source, destination):
    intersections = M.intersections
    roads = M.roads

    # direct distance of each node to destination
    direct_distance = get_direct_distance(
        intersections, intersections[destination])

    '''
    tuple(total_distance, distance, node)
    - total_distance: total distance combine shortest from node and direct_distance to destination (for pop/push in heapq of python)
    - distance: shortest distance from source to current node
    - node: node name
    '''
    p_queue: list[(int, int, int)] = []
    visited = [False] * len(intersections.keys())
    
    # Save shortest distance and last node
    previous = {}
    result = []

    # init source
    heapq.heappush(p_queue, (direct_distance[source], direct_distance[source], source))
    previous[source] = {"distance": 0, 'last_node': None}

    while len(p_queue) > 0:
        current_pop_node = heapq.heappop(p_queue)
        # current_total_distance unused cause sorting in heapq only
        (current_total_distance, current_distance, current_node) = current_pop_node

        if current_node == destination:
            break
        
        neighbors = roads[current_node]
        visited[current_node] = True
        neighbors = list(filter(lambda x: visited[x] == False, neighbors))

        for neighbor in neighbors:
            temp_distance = calculate_distance(intersections[current_node], intersections[neighbor])
            temp_shortest_distance = current_distance + temp_distance
            temp_total_distance = temp_shortest_distance + direct_distance[neighbor]

            # if new neighbor total distance is shorter -> add to heap and regis to previos[]
            if ((neighbor in previous) and (temp_total_distance >= previous[neighbor]['distance'])) is False:
                previous[neighbor] = { "distance": temp_total_distance, 'last_node': current_node }
                heapq.heappush(p_queue, (temp_total_distance, temp_shortest_distance, neighbor))

    # traverse through previos[] from destination to source to get result[]
    curr = destination
    while(curr != source):
        result.append(curr)
        curr = previous[curr]['last_node']
    result.append(source)
    result.reverse()
    return result

# get direct distance from each node to destination
def get_direct_distance(intersections, destination):
    direct_distance = {}
    for vert, cord in intersections.items():
        direct_distance[vert] = calculate_distance(cord, destination)
    return direct_distance

# calculate distance of 2 points
def calculate_distance(source, destination):
    return sqrt((source[0] - destination[0]) ** 2 + (source[1] - destination[1]) ** 2)
