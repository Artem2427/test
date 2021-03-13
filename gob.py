import csv

with open("acme_worksheet.csv", newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    next(reader)

    grouped_data = dict()
    for row in reader:
        name, date, points = row
        if name not in grouped_data.keys():
            grouped_data[name] = {'Jun 29 2020': '0', 'Jun 30 2020': '0', 'Jul 01 2020': '0',
                                  'Jul 02 2020': '0', 'Jul 03 2020': '0', 'Jul 04 2020': '0',
                                  'Jul 05 2020': '0'}

        grouped_data[name][date] = points

    with open("new_file.csv", 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=",")
        writer.writerow(["Name / Date", "2020-06-29", "2020-06-30", "2020-07-01",
                         "2020-07-02", "2020-07-03", "2020-07-04", "2020-07-05"])

        for key, value in grouped_data.items():
            row = [key]
            for pair in value.values():
                row.append(pair)
            writer.writerow(row)