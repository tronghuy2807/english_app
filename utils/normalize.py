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

class NormalizeWord:
    def trim_all_column(self,df):
        """
        Trim whitespace from ends of each value across all series in dataframe
        """
        trim_string = lambda x: x.strip() if type(x) is str else x
        return df.applymap(trim_string)


if __name__ == "__main__":
    manual = Manual()
    manual.find_wrong_line()