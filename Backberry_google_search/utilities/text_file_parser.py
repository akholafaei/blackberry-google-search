
"""
Blackberry Google search project by Ali Kholafaei
"""
class DataParser:

    def get_test_data(self):
        with open("C:\\Users\\Solmaz\\Documents\\Ali_backup\\Backberry_google_search\\utilities\\search_data.txt", "r") as filestream:
            dct = {}
            for line in filestream:
                (key, value) = line.strip().split(",")
                dct[key] = value
        return dct




