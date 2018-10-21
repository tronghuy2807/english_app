import pandas as pd

class CSVData:
    def load_data(self,path):
        try:
            return pd.read_csv(path, encoding='utf-8',sep = '|', dtype=str)
        except Exception,e:
            print ("Can not load file in path: ", path)
            print e
    def insert_data(self,data,path):
        print 'TODO'
    def update_data(self,data,path):
        print 'TODO'
    def delete_data(self, data,path):
        print 'TODO'
    def query_data(self,data,condition):
        print 'TODO'