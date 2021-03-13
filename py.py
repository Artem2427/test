import csv
with open("acme_worksheet.csv", newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    next(reader)
    count = 0
    name = []
    array = []
    date = []
    for row in reader:
        array.append(row)
        if row[1] in date:
            date.remove(row[1])
        date.append(row[1])
        if row[0] in name:
            continue
        name.append(row[0])
    print(array, "\n")
    print(name, "\n")
    print(date, "\n")
    with open("new_file.csv", 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=",")
        writer.writerow(["Name / Date", "2020-06-29", "2020-06-30", "2020-07-01",
                        "2020-07-02", "2020-07-03", "2020-07-04", "2020-07-05"])
        i = 0
        j = 0
        l= 0
        for j in range(len(name)):
            k = 0
            ours = []
            hol = []
            print("k ==", k, "j ===", j, "i ===", i)
            for i in range(len(array)):
                for k in range(len(date)):
                    print("k ==", k, "j ===", j, "i ===", i)
                    if date[k] and name[j] in array[i]:
                        ours.append(array[i][2])
                        hol.append(date[k])
                p = 0
                for p in range(len(date)):
                    if date[p] in hol:
                        continue
                    else:
                        print(p)
                        ours.insert(p, '0')
                print(ours)
                writer.writerow([name[j], ours[0], ours[1], ours[2],
                                ours[3], ours[4], ours[5], ours[6]])
                ours = []
                hol = []











