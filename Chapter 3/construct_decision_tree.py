# source_code/3/construct_decision_tree.py
# Constructs a decision tree from data specified in a CSV file.
# Format of a CSV file:
# Each data item is written on one line, with its variables separated
# by a comma. The last variable is used as a decision variable to
# branch a node and construct the decision tree.

import math
# anytree module is used to visualize the decision tree constructed by
# this ID3 algorithm.
from anytree import Node, RenderTree
import sys
sys.path.append('C:/Users/snehah/Desktop/DataScienceAlgorithmsinaWeek_Code/Chapter01/common')
import common
import decision_tree

# Program start
csv_file_name = sys.argv[1]
verbose = int(sys.argv[2])  # verbosity level, 0 - only decision tree

# Define the enquired column to be the last one.
# I.e. a column defining the decision variable.
(heading, complete_data, incomplete_data,
 enquired_column) = common.csv_file_to_ordered_data(csv_file_name)

tree = decision_tree.constuct_decision_tree(
    verbose, heading, complete_data, enquired_column)
decision_tree.display_tree(tree)
