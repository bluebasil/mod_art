#!/bin/python3

import math
import os
import random
import re
import sys
import copy


#
# Complete the 'findMinComplexity' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY complexity
#  2. INTEGER days
#


class Node:
    parent = None
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right
        self.id = random.random()

def create_tree(complexity):
    if len(complexity) == 0:
        return None
    i = complexity.index(max(complexity))
    new_node = Node(max(complexity), create_tree(complexity[:i]), create_tree(complexity[i+1:]))
    if new_node.right is not None:
        new_node.right.parent = new_node
    if new_node.left is not None:
        new_node.left.parent = new_node
    return new_node

# def get_minimum_outer_node(tree):
#     t1 = _get_minimum_outer_left_node(tree.left)
#     t2 = _get_minimum_outer_right_node(tree.right)
#     return _decide_better_tree(t1, t2)

def _get_minimum_outer_left_node(tree):
    if tree is None:
        return None
    t = _get_minimum_outer_left_node(tree.left)
    return _decide_better_tree(tree,t)

def _get_minimum_outer_right_node(tree):
    if tree is None:
        return None
    t = _get_minimum_outer_right_node(tree.right)
    return _decide_better_tree(tree,t)

# return the non-None, or otherwise min value between the two nodes given
def _decide_better_tree(t1, t2):
    if t1 is None:
        return t2
    if t2 is None:
        return t1
    if t1.value <= t2.value:
        return t1
    else:
        return t2

# Gets the minimum node and makes it a new root
def get_next_root(root_trees):
    new_root_candidate = None
    candidate_is_left = False
    min_val = math.inf
    for t in root_trees:

        # check outer left
        proposed_new_root = _get_minimum_outer_left_node(t.left)
        if proposed_new_root is not None and proposed_new_root.value < min_val:
            min_val = proposed_new_root.value
            new_root_candidate = proposed_new_root
            candidate_is_left = True

        # check outer right
        proposed_new_root = _get_minimum_outer_right_node(t.right)
        if proposed_new_root is not None and proposed_new_root.value < min_val:
            min_val = proposed_new_root.value
            new_root_candidate = proposed_new_root
            candidate_is_left = False

    # Trim this root so that it wont get counted in the future
    if candidate_is_left:
        new_root_candidate.parent.left = None
    else:
        new_root_candidate.parent.right = None
    new_root_candidate.parent = None

    return new_root_candidate


# alwasy gets the minimum outer node
def findMinComplexity2(complexity, days):
    # just for optimization
    if days == len(complexity):
        return sum(complexity)
    # have to have at least 1 task per day
    if days > len(complexity):
        return math.inf
    if days == 1:
        return max(complexity)

    root_trees = [create_tree(complexity)]
    for d in range(days-1):
        root_trees.append(get_next_root(root_trees))


    return sum([t.value for t in root_trees])



def _get_outer_nodes_left(root_node):
    if root_node is None:
        return []
    return [root_node] + _get_outer_nodes_left(root_node.left)

def _get_outer_nodes_right(root_node):
    if root_node is None:
        return []
    return [root_node] + _get_outer_nodes_left(root_node.right)



def test_roots(root_trees_src, days):
    root_trees = copy.deepcopy(root_trees_src)
    if days == 1:
        return sum([t.value for t in root_trees])

    potential_nodes = []
    for t in root_trees:
        potential_nodes += _get_outer_nodes_left(t.left) + _get_outer_nodes_right(t.right)

    min_value = math.inf
    for n in potential_nodes:
        if n not in root_trees:
            result = test_roots(root_trees + [n], days-1)
            if result < min_value:
                min_value = result
    return min_value





def findMinComplexity3(complexity, days):
    # just for optimization
    if days == len(complexity):
        return sum(complexity)
    # have to have at least 1 task per day
    if days > len(complexity):
        return math.inf
    if days == 1:
        return max(complexity)

    root_trees = [create_tree(complexity)]
    min_value = test_roots(root_trees,days)


    return min_value


def findMinComplexity(complexity, days):
    # just for optimization
    if days == len(complexity):
        return sum(complexity)
    # have to have at least 1 task per day
    if days > len(complexity):
        return math.inf
    if days == 1:
        return max(complexity)


    min_total = math.inf
    last_value = math.inf

    for count, value in enumerate(complexity):
        if count == 0:
            continue


        day1 = findMinComplexity(complexity[:count], 1)
        if day1 != math.inf:
            day2 = findMinComplexity(complexity[count:], days - 1)
            check_total = day1 + day2
            if check_total <= min_total:
                min_total = check_total

    return min_total


if __name__ == '__main__':
    #out = findMinComplexity([20,0,10,4,5,2,8,1,4,3],5) # should be 35
    # out = findMinComplexity3([20,0,10,4,5,2,8,1,4,3],5)

    out = findMinComplexity3(
        [78190, 22747, 10702, 64721, 38053, 34618, 86319, 72425, 2690, 29316, 22482, 24790, 16217, 85234, 24809, 46690,
         48555, 90212, 50168, 13812, 37118, 84880, 57021, 85942, 14941, 42226, 4387, 45393, 10079, 52548, 73960, 78087,
         57431, 11040, 81402, 63046, 66405, 20893, 29339, 16343, 10710, 75285, 48976, 69130, 87223, 12514, 76060, 30247,
         2784, 18428, 14593, 44089, 3019, 79746, 1355, 55577, 24875, 36768, 43280, 6205, 15136, 28479, 33696, 5194,
         87620, 71145, 59761, 20748, 85383, 41687, 28232, 48377, 91642, 37565, 60044, 73515, 17152, 94833, 56855], 47)
    print(out)