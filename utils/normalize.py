import csv

class Manual:
    def find_wrong_line(self):
        with open('../data/dictionary.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter='|')
            line_count = 0
            for row in csv_reader:
                try:
                    line_count += 1
                    r = row[2]
                except:
                    print line_count
                    print "-----------"

if __name__ == "__main__":
    manual = Manual()
    manual.find_wrong_line()