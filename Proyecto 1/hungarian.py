import networkx as nx
import numpy as np


def make_cost_matrix(profit_matrix):
    """
    Converts a profit matrix into a cost matrix.
    Expects NumPy objects as input.
    """
    # subtract profit matrix from a matrix made of the max value of the profit matrix
    matrix_shape = profit_matrix.shape
    offset_matrix = np.ones(matrix_shape, dtype=int) * profit_matrix.max()
    cost_matrix = offset_matrix - profit_matrix
    return cost_matrix


def cover_all_zeros(my_matrix, matrix):
    result_matrix = my_matrix.copy()
    total_covered = 0
    max_matching = {}
    while total_covered < min(len(my_matrix), len(my_matrix[0])):
        # Find minimum number of lines to cover all zeros in the matrix and find total covered rows and columns.
        max_matching, covered_rows, covered_columns = cover_zeros(
            result_matrix, matrix)
        total_covered = len(covered_rows) + len(covered_columns)
        # Step 4: if the total covered rows+columns is not equal to the matrix size then adjust it by min uncovered num (m).
        if total_covered < min(len(my_matrix), len(my_matrix[0])):
            result_matrix = adjust_matrix_by_min_uncovered_num(
                result_matrix, covered_rows, covered_columns)
    return max_matching


def adjust_matrix_by_min_uncovered_num(result_matrix, covered_rows, covered_columns):
    """Subtract m from every uncovered number and add m to every element covered with two lines."""
    # Calculate minimum uncovered number (m)
    elements = []
    for row_index, row in enumerate(result_matrix):
        if row_index not in covered_rows:
            for index, element in enumerate(row):
                if index not in covered_columns:
                    elements.append(element)
    min_uncovered_num = min(elements)

    # Add m to every covered element
    adjusted_matrix = result_matrix
    for row in covered_rows:
        adjusted_matrix[row] += min_uncovered_num
    for column in covered_columns:
        adjusted_matrix[:, column] += min_uncovered_num

    # Subtract m from every element
    m_matrix = np.ones(result_matrix.shape, dtype=int) * min_uncovered_num
    adjusted_matrix -= m_matrix

    return adjusted_matrix


def substract_row(my_matrix):
    for index, row in enumerate(my_matrix):
        my_matrix[index] -= row.min()


def substract_col(my_matrix):
    for index, column in enumerate(my_matrix.T):
        my_matrix[:, index] -= column.min()


def hungarian(matrix):
    """Runs the Hungarian algorithm on a given matrix and returns the results."""
    results1 = []
    results2 = []
    # First rows first:
    my_matrix = make_cost_matrix(np.array(matrix))

    # Step 1: Subtract row mins from each row.
    substract_row(my_matrix)
    # Step 2: Subtract column mins from each column.
    substract_col(my_matrix)

    # Step 3: Use minimum number of lines to cover all zeros in the matrix.
    # If the total covered rows+columns is not equal to the matrix size then adjust matrix and repeat.
    max_matching = cover_all_zeros(my_matrix, matrix)

    for i in max_matching.keys():
        if i < len(my_matrix):
            results1.append((i, max_matching[i]-len(my_matrix)))
        else:
            results1.append((max_matching[i], i-len(my_matrix)))
    # Calculate total potential
    value1 = 0
    for row, column in results1:
        value1 += matrix[row][column]

    # Second columns first
    my_matrix = make_cost_matrix(np.array(matrix))

    # Step 1: Subtract column mins from each column.
    substract_col(my_matrix)

    # Step 2: Subtract row mins from each row.
    substract_row(my_matrix)
    # Step 3: Use minimum number of lines to cover all zeros in the matrix.
    # If the total covered rows+columns is not equal to the matrix size then adjust matrix and repeat.
    max_matching = cover_all_zeros(my_matrix, matrix)

    for i in max_matching.keys():
        if i < len(my_matrix):
            results2.append((i, max_matching[i]-len(my_matrix)))
        else:
            results2.append((max_matching[i], i-len(my_matrix)))
    # Calculate total potential
    value2 = 0
    for row, column in results2:
        value2 += matrix[row][column]

    if value1 >= value2:
        return value1, results1
    return value2, results2


def cover_zeros(matrix, origin_matrix):
    """bipartite graph matching"""
    rows, cols = np.matrix(matrix).shape
    G = nx.Graph()

    # add nodes to row and column
    G.add_nodes_from(range(rows), bipartite=0)  # row nodes
    G.add_nodes_from(range(rows, rows + cols),
                     bipartite=1)  # column nodes

    # add edges between row and column with zero
    zero_indices = []
    for row_i in range(rows):
        for col_i in range(cols):
            if matrix[row_i][col_i] == 0:
                zero_indices.append((row_i, col_i))
    edges = []
    for row, col in zero_indices:
        edges.append((row, col+rows, origin_matrix[row][col]))
    G.add_weighted_edges_from(edges)

    if not nx.is_bipartite(G):
        G = nx.Graph(G)

    max_matching = {}
    # Check if the graph is connected
    if not nx.is_connected(G):
        components = list(nx.connected_components(G))
        for i in components:
            # Compute the maximum matching
            max_matching.update(nx.max_weight_matching(
                nx.Graph(G.subgraph(i))))

            # for l in i:
            #     if l < rows:
            #         for r in i:
            #             if r >= rows:
            #                 if r not in max_matching.values():
            #                     for j in G.edges:
            #                         if j == (l, r):
            #                             max_matching[l] = r
            # #                             break
            # max_matching.update(nx.bipartite.maximum_matching(G.subgraph(i)))
    else:
       # Compute the maximum matching
        max_matching.update(
            nx.max_weight_matching(G))

        # for l in range(rows):
        #     for r in range(rows, rows+cols):
        #         if r not in max_matching.values():
        #             for i in G.edges:
        #                 if i == (l, r):
        #                     max_matching[l] = r
        # #                     break
        # max_matching.update(nx.bipartite.maximum_matching(G))
    # max_matching = max_matching if len(max_matching) >= len(
    #     second_matching) else second_matching
    covered_rows = []
    covered_cols = []
    degrees = []
    count = 0
    for i in G.degree:
        degrees.append(i)
    for i in max_matching.keys():
        if i < rows:
            count += 1
            if degrees[i][1] >= degrees[max_matching[i]][1]:
                covered_rows.append(i)
                degrees[i] = (i, 0)
                for j in range(rows, cols+rows):
                    if matrix[i, j-rows] == 0:
                        degrees[j] = (
                            j, max(0, degrees[j][1]-1))
            else:
                covered_cols.append(max_matching[i] - rows)
                degrees[max_matching[i]] = (max_matching[i], 0)
                for j in range(rows):
                    if matrix[j, max_matching[i]-rows] == 0:
                        degrees[j] = (
                            j, max(0, degrees[j][1]-1))

        else:
            if degrees[max_matching[i]][1] >= degrees[i][1]:
                covered_rows.append(max_matching[i])
                degrees[max_matching[i]] = (max_matching[i], 0)
                for j in range(rows, cols+rows):
                    if matrix[max_matching[i], j-rows] == 0:
                        degrees[j] = (
                            j, max(0, degrees[j][1]-1))

            else:
                covered_cols.append(i-rows)
                degrees[i] = (i, 0)
                for j in range(rows):
                    if matrix[j, i-rows] == 0:
                        degrees[j] = (
                            j, max(0, degrees[j][1]-1))
    # add_other_zeros(matrix, cols, rows, max_matching,
    #                 covered_rows, covered_cols, degrees)

    return max_matching, set(covered_rows), set(covered_cols)
