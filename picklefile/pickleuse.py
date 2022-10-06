#To Dump into pickle file
L=[1,2,3,...............................................]
import pickle
with open("filename.pickle",'wb') as data:
   pickle.dump(l,data)


#To load the pickle file
import pickle
DATA = pickle.load(open('filename.pickle', 'rb'))
 
                   or
 
with open('filename.pkl','rb') as fi:
   any_var_name = pickle.load(fi)
