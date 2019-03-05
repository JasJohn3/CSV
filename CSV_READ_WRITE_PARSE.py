import csv
#read a csv file
with open('names.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file)
#Write a csv file
with open('new_names.csv','w') as new_file:
    csv_writer = csv.writer(new_file, delimeter = ',')
#reading into a dictionary file
with open('names.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

#writing to a dictionary file
with open('names.csv', 'r') as csv_file:
    fieldnames = ['first_name','last_name', 'email']
    csv_reader = csv.DictWriter(csv_file, fieldnames = fieldnames, delimiter = ',\t')
    #writes the field names of the csv file
    csv_writer.writeheader()
    for line in csv_reader:
        csv_writer.writerow(line)