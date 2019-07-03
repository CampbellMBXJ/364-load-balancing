# 364-load-balancing
given a number of source nodes (greater then 3), transit nodes (greater then 2) and destination nodes (greater then 3) this will produce a lp where all loads from a source node to a destination node will be split evenly over exactly two transit nodes.
All transit nodes are assumed to be connected to all other nodes.
####Running
python 3 only.
`main.py` takes the number of nodes as 3 cl paramaters and sends output to stdout
`runner.sh` given a fourth cl paramater, the location of a cplex installation, will automaticly pipe the output into cplex.

