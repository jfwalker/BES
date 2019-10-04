import Quartets
import tree_stuff
import sys
import stats

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
		#It's not a tip but make sure it still contains info
		elif i.data['q'] != None:
			sp_tree_quartets[i.data['q']] = []
			q_to_n[i.data['q']] = []
		
	return sp_tree_quartets,q_to_n


#run through the gene trees, check if they match the species tree
def process_gene_trees(g_tree,sp_quartet_tree,sp_tree,supval):
	
	count = 0
	#i becomes each tree
	for gene in g_tree:
		
		tree = tree_stuff.build(gene)
		sys.stderr.write("processing gene " + str(count) + '\r')
		count += 1
		for i in sp_quartet_tree:
			
			for j in tree.iternodes():
				
				#Get the quartet from the bipartition
				gqu = Quartets.get_quartet(j,tree)
				
				#You'll get none for something that's a tip and for one internal
				if gqu != None:
					
					#Check to see if it matches
					if i.match(gqu):
					
						#There's a match add the length
						
						#Need to account for trees with no edge values
						if j.label == "":
							j.label = 0.0
						
						if supval <= float(j.label):
							sp_quartet_tree[i].append(j.length)
							check = set()
							keep = set()
							
							#Get left and right of the new quartet to check against the right
							#and the left of the species quartet
							for k in gqu.lefts:
								if len(k) == 1:
									check.add(list(k)[0])
							
							for k in gqu.rights:
								if len(k) == 1:
									check.add(list(k)[0])
							
							#Get the left and the right of the species quartet
							
							for k in i.lefts:
								if len(k) == 1 and len(check.intersection(k)) == 1:
									keep.add(list(k)[0])
							
							for k in i.rights:
								if len(k) == 1 and len(check.intersection(k)) == 1:
									keep.add(list(k)[0])
							
							for k in keep:
								ln = tree.get_tip(k).length
								st = sp_tree.get_tip(k)
								if tree not in st.data["qlntrees"]:
									st.data["qlntrees"].add(tree)
									st.data["qln"].append(ln)
	return sp_tree,sp_quartet_tree
	
def summarizer(sp_tree,sp_quartet_tree): 
	
	#Data stored on species tree
	for i in sp_tree.iternodes():
		if i == sp_tree:
			continue
		#No children means a tip
		if len(i.children) == 0:
			
			#verbose printing of all values
			#print i.label + "\t" + str(len(i.data["qln"]))
			holder = i.data["qln"]
			
		else:
			
			holder = sp_quartet_tree[i.data["q"]]
			#verbose printing of all values
			#print i.get_newick_repr(False) + "\t" + str(len(sp_quartet_tree[i.data["q"]]))
		
		#Make sure something has actually been concordant and met the cutoff
		if len(holder) == 0:
			continue
		
		mean = stats.mean(holder)	
		i.data["mean"] = mean
	print sp_tree.get_newick_otherlen("mean") + ";"
					
				
			
			
			