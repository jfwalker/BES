# BES
Branch Estimation Synthesizer

This is a program designed to do concordance informed branch length. In short this means that given a set of gene trees and a species tree to map to, the program will identify edges that are concordant with the species tree and use a variety of stats behind the edges to calculate what the branch lengths should be. This provides an extremely fast way to add branch lengths to a species tree, and makes sure that the only thing informing the species tree branch lengths is concordant relationships. Both species tree and gene trees must be unrooted! Currently this is under active development but to run:

```BES.py -m SpeciesTree -t FileOfGeneTrees -s [optional support value] -o [optional outfile]```


The name comes from an exhibit I saw in the British natural history museum on the egyptian god [Bes](https://en.wikipedia.org/wiki/Bes), credit to Robyn Phillips for pointing it out. Having never seen a picture of Bes before I thought it was necessary to draw some attention to the coolest looking egyptian god of all. If you search Bes you'll probably just find things related to the utility company so google searches need to be specific.
