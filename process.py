lines = []
with open("tree.txt") as f:
    lines = f.readlines()
import re
with open("processed_tree.txt","w") as f:
    for line in lines:
        if(re.match("^\(",line)):
            f.write("%s\n"%(line.rstrip("\n")))