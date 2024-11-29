import os, json, shutil, datetime, csv

dir = input("Directory: ")
goaldir = os.path.join(dir, "..", os.path.basename(dir) + "new")

if os.path.exists(goaldir):
    shutil.rmtree(goaldir)
os.mkdir(goaldir)


#lastseen = [0] * 10
#currentdate = (datetime.datetime.utcnow() - datetime.datetime(1970,1,1)).days
taglist = set()
dataarray = []
goodtaglist = set()
for filename in os.listdir(dir):
    f = os.path.join(dir, filename)
    if os.path.isfile(f):
        print("Reading " + f, end="\r")
        file = open(f)
        data = json.load(file)
        file.close()
        DailyVersion = data.get('FirstPlayed', 0)
        taglist.update(data.keys())
        if (DailyVersion > 17000):
            goodtaglist.update([tag for tag in data.keys() if data[tag] != 0])
            shutil.copyfile(f, os.path.join(goaldir, filename))
            dataarray.append(data)
            #lastseen[int((currentdate - DailyVersion) / 365.25)] += 1

#for index in range(len(lastseen)):
#    print(lastseen[index], "players seen in range", index, index+1)
#print("Good tags:", goodtaglist)
print("Unused tags:", taglist - goodtaglist)

goalcsvfile = os.path.join(goaldir, "csv.csv")
csvf = open(goalcsvfile, 'w')
csvwriter = csv.writer(csvf)

csvwriter.writerow(taglist)
[csvwriter.writerow([data.get(key, None) for key in goodtaglist]) for data in dataarray]

csvf.close()

print("Rows:", len(dataarray), "Columns:", len(goodtaglist))
