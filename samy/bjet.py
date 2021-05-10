

#global imports

from base import *

#forward slash path styles

folder = Path("csv")
csvpath =  folder / "AlephBtag_MC_small_v2.csv"

#file specific imports

from sklearn.model_selection import train_test_split

from sklearn.neighbors import KNeighborsClassifier

#number of neighbours seems to have diminishing returns. from 3-10 seems to be the sweet spot
knn = KNeighborsClassifier(n_neighbors = 11)

#quark data
data = np.genfromtxt(csvpath, names=True)

#add whichever columns you want in here
columns = [
data['prob_b'],
data['bqvjet'],
#data['multip'],
#data['phi'],
data['pt2rel'],
#data['cTheta'] 
]

isb = data['isb']

#stacking cols into larger nparray
prob_combined = np.column_stack(columns)

pb_train, pb_test, isb_train, isb_test = train_test_split(prob_combined, isb, train_size = 0.01)

knn.fit(pb_train, isb_train)

print("Test set predictions: {}".format(knn.predict(pb_test)))
print("Test set accuracy: {}".format(knn.score(pb_test,isb_test)))