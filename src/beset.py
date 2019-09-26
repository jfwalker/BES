import Quartets


#transform the species tree into a set of nodes that can correspond to quartets
def prepare_sp_tree(sp_tree):
	sp_tree_quartets = {}
	q_to_n = {}
	for i in sp_tree.iternodes():
	
		i.data['q'] = Quartets.get_quartet(i,sp_tree)
		
		#tips are different so they won't have a corresponding quartet
		if i.istip:
			i.data['qln'] = []
			i.data['qlntrees'] = set()
		else:
			sp_tree_quartets[i.data['q']] = []
			q_to_n[i.data['q']] = []
		
	return sp_tree_quartets,q_to_n

def process_gene_trees(g_tree,sp_quartet_tree,sp_tree):
	print "here"