import csv

def find_wrong_line():
    with open('../data/dictionary.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='|')
        line_count = 0
        try:
            for row in csv_reader:
                line_count += 1
                print line_count
                print row[2]
        except:
            print "-----------"

if __name__ == "__main__":
    find_wrong_line()