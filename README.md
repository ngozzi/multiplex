# Multiplex Dependency Structure of S&P500 Stocks
[multiplex.png]

## Introduction
The aim of this work is to analyze dependencies and correlations between S&P500 stocks using a multiplex approach. To do so I considered different types of correlations (Pearson, Kendall and Spearman) between historical prices of stocks.

## Build the Network
For each of the three correlation considered, I evaluated correlation matrices between historical log-returns of stocks. Then I filtered these matrices using the Planar Maximally Filtered Graph algorithm (PMFG). A python version of this algorithm that I wrote for this project is included in the notebooks folder. 
These preprocessing activity yields 3 filtered, weighted, undirected networks that, cosidered together, form a 3-layer multiplex network. 

## Multiplex Analysis 
I considered a few multiplex metrics to analyze the multiplex stocks network: 
- Overlapping Degree, to check the global importance of nodes; 
- Multiplex Participation Coefficient (MPC), to analyze the distribution of the activity of a node among layers; 
- Multiplex Cartography; 
- Similarity between layers;

## References
- A tool for filtering information in complex systems , M. Tumminello, T. Aste, T. Di Matteo and R. N. Mantegna PNAS July 26, 2005. 102 (30) 10421-10426;  https://doi.org/10.1073/pnas.0500298102;
- The new challenges of multiplex networks: Measures and model, F. Battiston, V. Nicosia and V. Latora. Eur. Phys. J. Special Topics 226, 401–416 (2017);
- The multiplex dependency structure of financial markets, N. Musumeci, V. Nicosia, T. Aste, T. Di Matteo, V. Latora. Jun 15, 2016; https://arxiv.org/abs/1606.04872v1
- Scrape list of current S&P500 components: https://gist.github.com/johncoughlan/39ad681ce03b1c246441d0c775cda45a.

