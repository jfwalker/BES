# BES
Branch Estimation Synthesizer

This is a program designed to do concordance informed branch length. In short this means that given a set of gene trees and a species tree to map to, the program will identify edges that are concordant with the species tree and use a variety of stats behind the edges to calculate what the branch lengths should be. This provides an extremely fast way to add branch lengths to a species tree, and makes sure that the only thing informing the species tree branch lengths is concordant relationships. Both species tree and gene trees must be unrooted! Currently this is under active development but to run:

```BES.py -m SpeciesTree -t FileOfGeneTrees -s [optional support value] -o [optional outfile]```

The output will either be printed to your screen in which case is will be 7 trees, or it will be printed to the file names you've specified in which case there will be a \*.tre file with the same 7 trees that would go to output and a \*.verbose.csv where all values of all concordant edges are printed. In the .tre file the trees are as follows:

Tree 1: The mean of the concordant branches
Tree 2: The median of the concordant branches
Tree 3: The minimum value of any concordant branch
Tree 4: The maximum value of any concordant branch
Tree 5: The lower limit of the 95% CI
Tree 6: The upper limit of the 95% CI
Tree 7: The number of edges that are concordant with a particular relationship


If you would like a speed up, [cython](https://cython.org/) has also been added. For the test dataset the computer I'm running it on takes about 8 seconds but if you switch to cython it's usually about 5, so it can save quite a bit of time on larger datasets.

Once you have installed cython on your computer you just enter the source folder and run: ```python conf.py build_ext --inplace```

After it has compiled open the file called "run_cython.py" and change the variable use_cython from False to True.





The name comes from an exhibit I saw in the British natural history museum on the egyptian god [Bes](https://en.wikipedia.org/wiki/Bes), credit to Robyn Phillips for pointing it out. Having never seen a picture of Bes before I thought it was necessary to draw some attention to the coolest looking egyptian god of all. If you search Bes you'll probably just find things related to the utility company so google searches need to be specific.
