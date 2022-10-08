# import email
# import pymongo #pip install pymongo,pip install "pymongo[srv]"

# client = pymongo.MongoClient("mongodb+srv://ineuron:Shashi14@cluster0.hteym.mongodb.net/?retryWrites=true&w=majority")

# # client = pymongo.MongoClient("mongodb+srv://ineuron:mongodb123@cluster0.goi2j.mongodb.net/?retryWrites=true&w=majority")
# db = client.test

# print(db)

# d={"name":"shashi",
# "email":"egashashikumar@gmail.com",
# "surname":"ega"
# }

# db1=client['mongotest']
# coll = db1['test']
# coll.insert_one(d)


import pymongo
client = pymongo.MongoClient("mongodb+srv://ineuron:Shashi14@cluster0.hteym.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name":"sudhanshu",
    "email" : "sudhanshu@ineuron.ai",
    "surname" : "kumar"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d )




# git 

# https://git-scm.com/downloads