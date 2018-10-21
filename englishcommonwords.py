from processdata import CSVData

def main():
    #path to data"
    path_data = "data/dictionary.csv"
    #Load data from csv
    csv = CSVData()
    english_words = csv.load_data(path_data)
    print 'xxx'
if __name__ == "__main__":
    print main()