
import random


#function generate a graph with 1000 peaks and 15000 edges 
def generate_graph():
    graph = {}
    for i in range(1000):
        graph[i] = []
    for i in range(15000):
        a = random.randint(0, 999)
        b = random.randint(0, 999)
        if a != b and b not in graph[a]:
            graph[a].append(b)
            graph[b].append(a)
    return graph


#function find a single dominating set in the graph
def find_dominating_set(graph):
    dominating_set = []
    for i in range(1000):
        if i not in dominating_set:
            dominating_set.append(i)
            print("The peak", i, "is added to the dominating set")
            for j in graph[i]:
                if j not in dominating_set:
                    dominating_set.append(j)
                    print("The peak", j, "is added to the dominating set")
                else:
                    print("The peak", j, "is already in the dominating set")
        else:
            print("The peak", i, "is already in the dominating set")
    return dominating_set



#print graph in a file
def print_graph(graph):
    f = open("graph.txt", "w")
    f.write(str(graph))
    print("The graph is written in the file graph.txt")
    f.close()


#print the result in a file
def print_result(dominating_set):
    f = open("dominating_set.txt", "w")
    f.write(str(dominating_set))
    print("The dominating set is written in the file dominating_set.txt")
    f.close()

graph = generate_graph()
dominating_set = find_dominating_set(graph)
print(find_dominating_set(generate_graph()))
print_graph(graph)
print_result(dominating_set)
