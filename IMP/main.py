import math
import sys
import os
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(ROOT_DIR)


import matplotlib.pyplot as plt
from IMP import fb_loc, twitter_loc, SD_loc, Pokec_loc, Gplus_loc,  yt_loc, dblp_loc, Epinions_loc, ca_cit_loc, HR_loc, twitch_loc, wiki_loc, reddit_loc,flickr_loc, brightkite_loc, lastfm_loc

from IMP.Simulation import *
from IMP.averaging import *
if __name__ == "__main__":
    #dict_counter_measure = {'id':COUNTER_MEASURE_COMMUNITY_DETECTION, 'p_orange_h': 0.05, 'p_orange_r':0.1}
    dict_counter_measure = {'id':COUNTER_MEASURE_FACTCHECKING, 'num_green':1, 'start_time':4, 'green_spreading_ratio':0.5,
                            'p_orange_h':0.05, 'p_orange_r':0.1, 'p_coinflip':0.7, 'frac_green':0.1, 'threshold_detection':0.05,
                            'threshold_block':0.05}
    dict_args = {"degree_of_supernodes":150, "number_of_supernodes": 1000, "nodes_in_clique": 16}



    list_gray = BigSimulation(num_runs=3, graph_loc=Gplus_loc, type_graph='SN', num_red=1, k=5, dict_args=dict_args,dict_counter_measure=dict_counter_measure)
