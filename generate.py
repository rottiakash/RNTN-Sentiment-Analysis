lines = []
with open("dataset.txt") as f:
    lines = f.readlines()
    lines = list(map(lambda x : x.strip()[:-1].strip(),lines))

with open("output.txt","w") as f:
    for line in lines:
        f.write("%s\n"%(line))