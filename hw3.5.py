#HW3 Question 5

def course_schedule(n, prerequisites):
    flags = [0]*n
    #flags: 0 is unvisited
    #       1 is visiting
    #       2 is dealt_with
    incoming_edges = [[] for i in range(n)]
    outgoing_edges = [[] for i in range(n)]
    for c in prerequisites:
        to_take = c[0]
        you_need = c[1]
        incoming_edges[to_take].append(you_need)
        outgoing_edges[you_need].append(to_take)
    #thats the construction
    free_vertices = []
    added = 0
    for i in range(n):
        if len(incoming_edges[i]) == 0:
            free_vertices.append(i)
            added += 1
    #free_vertices is ready
    while len(free_vertices) != 0:
        current_vertex = free_vertices[0]
        nei = outgoing_edges[current_vertex]
        for v in nei:
            incoming_edges[v].remove(current_vertex)
            if len(incoming_edges[v]) == 0:
                free_vertices.append(v)
                added += 1
        free_vertices.remove(current_vertex)
    return added == n
