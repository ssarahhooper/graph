# CECS 427 Assignment: Graphs
Due date: 9/16/225
By: Sarah Hooper

## Usage Instructions
` python ./graph.py --input "a_graph.gml" --multi_BFS a b c --analyze --plot`

`python ./graph.py --create_random_graph n c 
seed --multi_BFS a b c --analyze --plot --output "output_graph.gml"`
* must create a random graph or input .gml file
* random graph takes parameters n, c, seed
* multi_BFS must accept at least 1 integer

## Implementation
### File handling and Graph
* the first 3 functions are dedicated to file handling and 
graph creation.
* I used mapping to ensure all the variables are strings
* I calculated p using the given function and then used the library networkx to create the graph
### BFS
* I created two functions, one to calculate the BFS of a 
given node and a second to handle multiple roots given.
* The BFS function follows a general algorithm:
  * Start with the root node and marked as visited, put in queue and add to bfs tree with distance of 0
  * process nodes in order by taking first node out of queue
  * check each neighbor, if haven't visited, mark as visited and add to graph, put neighbor in queue
  * repeat until no more nodes are in queue
  * return bfs tree
* Multi_BFS then uses this function to repeat this process given the different roots
### Analysis
* The analysis mainly uses Networkx to return the connected
components, cycles, isolated nodes, graph density, and average shortest path
### Plot
* plot graph initially gave me some issues with ensuring the edges of the BFS lined up with the edges of the original graph.
* but using pos=pos in both the original and bfs ensured the edges lined up

## Examples

`python ./graph.py --input "output_graph.gml" --multi_BFS 3 6 --analyze --plot`
* given this command, the expected terminal output should look like this:
* {
  "num_components": 1,
  "cycle_detection": [
    [
      "0",
      "1"
    ],
    [
      "1",
      "2"
    ],
    [
      "2",
      "7"
    ],
    [
      "7",
      "0"
    ]
  ],
  "isolated_nodes": [],
  "density": 0.37777777777777777,
  "average_shortest_path": 1.7555555555555555
}
* Two graphs will be shown, one for each root.
## Name and ID
* Sarah Hooper: 032031049
* I did not realize we were supposed to be in pairs until it was too late.


