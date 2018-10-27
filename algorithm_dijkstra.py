graph = {}
graph['start'] = {'a': 6, 'b': 2}
graph['a'] = {'fin': 1}
graph['b'] = {'fin': 5, 'a': 3}
graph['fin'] = {}

infinity = float('inf')
costs = {'a': 6, 'b': 2, 'fin': infinity}

parents = {'a': 'start', 'b': 'start', 'fin': None}

processed = []


def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


def find_lowest_way():
    node = find_lowest_cost_node(costs)
    while node is not None:
        cost = costs[node]
        nieghbors = graph[node]
        for n in nieghbors.keys():
            new_cost = cost + nieghbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node(costs)


find_lowest_way()
print(parents)
