from processdata import CSVData
from utils.normalize import NormalizeWord


def main():
    # path to data"
    path_data = "data/dictionary.csv"
    # Load data from csv
    csv = CSVData()
    english_words = csv.load_data(path_data)
    # strip() for all column in dict
    nm = NormalizeWord()
    english_words = nm.trim_all_column(english_words)

    print english_words.head(3)


if __name__ == "__main__":
    main()
