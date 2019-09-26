import sys
import argparse
import Extras
import beset
import tree_stuff



'''
argparse crap
'''
def generate_argparser():

	parser = argparse.ArgumentParser(
        prog="BES.py",
        )
	parser.add_argument("-m", "--maptree", required=True, type=str, help="""
	UNROOTED tree to add branch lengths to""")
	parser.add_argument("-t", "--treeset", required=True, type=str, help="""
	UNROOTED trees to get branches from""")
	parser.add_argument("-s", "--support", required=False, type=str, help="""
	Support cutoff""")
	parser.add_argument("-o", "--outfile", type=str, help="""
	Output file""")
	return parser
	
def main(arguments=None):
	
	parser = generate_argparser()
	args = parser.parse_args(arguments)
	Extras.get_time("Run Starting", None)
	
	#turn the mapping tree into it's respective quartets
	m_tree = (open(args.maptree, "r").readline()).strip("\n\r")
	sp_tree = tree_stuff.build(m_tree)
	sp_quartet_tree,q_to_n = beset.prepare_sp_tree(sp_tree)
	
	
	g_tree = open(args.treeset, "r")
	beset.process_gene_trees(g_tree,sp_quartet_tree,sp_tree)
	
	
	
	Extras.get_time("Run Ending", None)
	
	
	
	
	
if __name__ == "__main__":
	main()