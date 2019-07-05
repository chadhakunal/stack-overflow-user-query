import pandas as pd
import pickle

topTags = pd.read_csv("TopTags.csv")
dataset = pd.read_pickle("finalDF")

print(dataset.shape)
tagDict = {}
for i in topTags["tags"]:
    tagDict[i] = 0

print(dataset.tail())
todrop = []
for cnt,i in enumerate(dataset["Tags"]):
    if cnt%100000 == 0:
        print("Iteration ",cnt)
    flag = True
    for j in i:
        if j in tagDict.keys():
            #if tagDict[j]<50:
            tagDict[j] += 1
            flag = False
    if flag:
        todrop.append(cnt)
#dataset.drop(todrop)
#print(dataset.shape)

tags0_10 = []
tags10_20 = []
tags20_30 = []
tags30_40 = []
tags40_50 = []
tags50_more = []
for i in tagDict.keys():
    if tagDict[i]>=0 and tagDict[i]<=10:
        tags0_10.append(i)
    elif tagDict[i]>10 and tagDict[i]<=20:
        tags10_20.append(i)
    elif tagDict[i]>20 and tagDict[i]<=30:
        tags20_30.append(i)
    elif tagDict[i]>30 and tagDict[i]<=40:
        tags30_40.append(i)
    elif tagDict[i]>40 and tagDict[i]<=50:
        tags40_50.append(i)
    else:
        tags50_more.append(i)       
    

print("Tags 0-10: ",len(tags0_10))
print("Tags 10-20: ",len(tags10_20))
print("Tags 20-30: ",len(tags20_30))
print("Tags 30-40: ",len(tags30_40))
print("Tags 40-50: ",len(tags40_50))
print("Tags >50: ",len(tags50_more))

#print(tagDict)

tagset1 = tags0_10 + tags10_20
tagset2 = tags20_30

pickle_out = open("tags1.pickle","wb")
pickle.dump(tagset1, pickle_out)
pickle_out.close()

pickle_out = open("tags2.pickle","wb")
pickle.dump(tagset2, pickle_out)
pickle_out.close()

