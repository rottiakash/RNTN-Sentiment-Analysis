from sklearn.model_selection import train_test_split
train, test = [] , []

with open("processed_tree.txt") as f:
    lines = f.readlines()
    lines  = list(map(lambda x: x.rstrip("\n"),lines))
    train,test = train_test_split(lines,test_size=0.2)


with open("train.txt","w") as f:
     for line in train:
            f.write("%s\n"%(line.rstrip("\n")))


with open("test.txt","w") as f:
     for line in test:
            f.write("%s\n"%(line.rstrip("\n")))