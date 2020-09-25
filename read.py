import numpy as np
from matplotlib import pyplot as plt
import operator

arr = np.arange(3)
max_idx, max_val = max(enumerate(arr), key=operator.itemgetter(1))

l = [0, 1, 2]
max_val = max(l)
max_idx = l.index(max_val)
print(max_idx, max_val)


# with open(filename, "r") as fp:
#     # Row dimension
#     nums = fp.readline().strip()
#     row = int(nums)

#     A = []
#     for i in range(row):
#         nums = fp.readline().rstrip().split()
#         A.append([float(num) for num in nums])
#     A = np.array(A)


def read_network(self, filename):
    """Read data from FILENAME and construct the network."""
    # open network file
    fp = open(filename, "r")

    # get first line
    ln = fp.readline().strip()
    while ln is not "":
        # node name
        ln2 = ln.split(",")
        from_node_name = ln2[0]
        arcs = ln2[1:]
        try:  # if node doesn't exist, add to network
            self.get_node(from_node_name)
        except NetworkError:
            self.add_node(from_node_name)

        ln = fp.readline().strip()  # get next line

    fp.close()


# BREADTH-FIRST SEARCH
def search(tree, search_value):
    # initialise the queue with head node only
    qu = LinkedList()
    qu.append(tree.head)
    # loop over when the list is not empty
    while qu.head != None:  # the whole queue/linked list cannot compare with None.
        nd = qu.head.value  # get the node in the linked list
        nd_value = qu.pop(
            0
        ).value  # pop the first node in the list and get the node value
        if nd_value == search_value:  # check the node value with the search value
            return nd.name
        else:
            for arc in nd.arcs_out:
                qu.append(arc.to_node)  # add the node's daughter nodes into the queue
    # if the search value is not found, return None
    return None


# INSERTION SORT
def insertion_sort(A):
    A3 = np.sort(A)  # sort the list using Python built-in function
    # - Use np.arange(**number**) to get a list of integers (for the index table).
    # - Your index table should be 0-indexed (this is Python after all) as opposed to
    #   the 1-indexed example in the notes.

    # create an index list, starting at 0. [0 1 2 3 4]
    ind = [k for k in range(len(A))]

    # pick the value from index 1 to the last
    for i in range(1, len(A)):
        # the index before the current pick
        j = i - 1
        # check the pick and element before the pick till the front of the list
        while j > -1:
            pick = A[i]
            # if pick is smaller than the element before it, swap the values
            if pick < A[j]:
                A[i], A[j] = A[j], A[i]
                # swap the index list simultaneously
                ind[i], ind[j] = ind[j], ind[i]
            else:
                break
            # shift pick and the value the pick is going to compare with both by one
            i = i - 1
            j = i - 1
    return ind


# for networks
class Node(object):
    def __init__(self):
        self.name = None
        self.value = None
        self.arcs_in = []
        self.arcs_out = []

    def __repr__(self):
        return "nd: {}".format(self.name)
