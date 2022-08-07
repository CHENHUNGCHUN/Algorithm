from gettext import find


graph = {}
graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2

graph['a'] = {}
graph['a']['fin'] = 1

graph['b'] = {}
graph['b']['a'] = 3
graph['b']['fin'] = 5

graph['fin'] = {}

#成本
infinity = float('inf')
costs = {}
costs['a'] = 6
costs['b'] = 2
costs['fin'] = infinity

#父節點
parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['fin'] = None

processed = []

def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_node = None
    for i in costs:
        if costs[i] < lowest_cost and i not in processed:
            lowest_cost = costs[i]
            lowest_node = i
    return lowest_node

node = find_lowest_cost_node(costs)

while node is not None:
    cost = costs[node]   #cost = 2  node = b
    neighbors = graph[node]    
    for n in neighbors.keys():   #n = a ,fin
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost: 
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)
    
print(costs)
