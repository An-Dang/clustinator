from sklearn.cluster import DBSCAN
import numpy as np
import datetime
import time

from input import Input
from markovchain import MarkovChain


states = ["INITIAL","login","View_Items","home","logout","View_Items_quantity","Add_to_Cart","shoppingcart",
          "remove","deferorder","purchasecart","inventory","sellinventory","clearcart","cancelorder","$"]

# Data imports
PATH = "../data/raw/"
sessions_file = (PATH+'sessions.dat')


class Clustering:
    def __init__(self, X):
        self.X = X

    def dbscan(self):

        return DBSCAN(eps=1.5, min_samples=10).fit(self.X)

    def uniqueLabels(self):
        labels = self.dbscan().labels_
        return np.unique(labels, return_counts=True)


# main-method
if __name__ == '__main__':
    # Input data
    input = Input(sessions_file)
    # Slice sessions @sessions(None, None)
    session = input.sessions(None, 200)
    
    print('load data done', datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))

    # Compute transition matrix
    mc = MarkovChain(session, states)
    mc = mc.transition_matrix()

    print('matrix done', datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))
    print('start clustering \n')

    # DBSCAN
    dbscan = Clustering(mc)
    clustering = dbscan.uniqueLabels()
    print(clustering)

    print("\nEnd clustering", datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))
