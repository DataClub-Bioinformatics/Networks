# Networks
Cytoplots and network visualization in python and cytoscape.js

When browsing a network, we want to be able to get a nodes (genes) nearest 
neighbors and retrieve GO information and pathway information about selected 
nodes alongside our own information we have about the node. Previously cytoscape
has been used for this task but it is a clumpsy java app and we would like
a smaller more responsive app and cytoscape.js seems to be the right choice.

Here we have a regular index.html file that loads the js script and render
the visualisation. We can later edit this file for style and functionality
but thats for later. 

We want to write a backend in python that serves the index.html file with
the network node and edge information, and that fetches GO and pathway data for
a list of nodes.

We will start of by having a small set of 20 genes and RNA-seq data. Calculate 
the correlation matrix and then graph the nodes and the edges of a correlation
higher than some number and put that information into a json file.

Then we want to write something that fetches GO data for a list of genes
and handle the data that comes of it. Depending on architecture we might later 
put stuff into a database but thats a later problem. 

