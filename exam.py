import socket
import itertools

def client_inputs(n):
    values = [0, 1, 2, 3]

    com = itertools.combinations_with_replacement(values, n)

    labels_list = []
    for val in com:
        labels_list = labels_list + list(set(itertools.permutations(list(val))))

    return(labels_list)
#print(client_inputs(2))

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_IP = "54.153.25.35"
server_port = 8865

client.connect((server_IP, server_port))

server_msg1 = client.recv(1024).decode('ascii')
server_msg1 = server_msg1[:len(server_msg1)-1]
print(server_msg1)

graph = {}
input_level = 1
count = 0

while count < len(client_inputs(input_level)):
    count = 0
    b = False
    for input in client_inputs(input_level):
        for client_ms in input:
            client_msg = str(client_ms).encode('ascii')
            client.send(client_msg)
            server_msg2 = client.recv(1024).decode('ascii')
            server_msg2 = server_msg2[:len(server_msg2) - 1]
            if server_msg1 == "END" and server_msg2 == "END":
                b = True
            else:
                key = "(" + server_msg1 + "," + server_msg2 + ")"
                graph.update({key: client_msg.decode("utf-8")})
                print(len(graph))
                print(graph)
                server_msg1 = server_msg2

        if b == True:
            count = count + 1
            #print(count)
        r = "RESET"
        rs = r.encode('ascii')
        client.send(rs)
        server_msg1 = client.recv(1024).decode('ascii')  # check one more time
        server_msg1 = server_msg1[:len(server_msg1) - 1]

    input_level = input_level + 1

print()
print(graph)

"""
#bonus
graph_list = []
for key in graph:
    graph_list.append(key)

import networkx as nx
digraph = nx.DiGraph()
digraph.add_edges_from(graph_list)

print(nx.shortest_path(graph, 'START', 'END'))

"""