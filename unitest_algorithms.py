import unittest
import algorithms
import math 
n = 10
data_dict = {}
for i in range(n):
     data_dict[i] = i*10
estados_usa = ["Alabama","Alaska","Arizona","Arkansas","California","Colorado","Connecticut","Delaware","Florida","Georgia","Hawái","Idaho","Illinois","Indiana",
    "Iowa","Kansas","Kentucky","Luisiana","Maine","Maryland","Massachusetts","Míchigan","Minnesota","Misisipi","Misuri","Montana","Nebraska","Nevada","New Hampshire","Nueva Jersey"]
data_to_read = ["Market capitalization (Billions)",
        "Price","Volume 1 day", "Relative Volume 1 day",
        "Price to earnings ratio","Volume 1 day", 
        "Relative Volume 1 day","Volatility 1 month",
        "Volatility 1 week","Price to sales ratio",
        "Price to book ratio","Price to cash flow ratio",]
class AlgorithmsTests(unittest.TestCase):
    n = 10
    def test_EIN_generator(self):
            result = algorithms.EIN_generator(n)
            self.assertIsInstance(result, list)
    def test_list_generator(self):
            result = algorithms.list_generator(data_dict)
            self.assertIsInstance(result,list)
    def test_read_location(self):
            result = algorithms.read_locations()
            self.assertIsInstance(result,list)
            self.assertTrue(all((isinstance(x,str) for x in result )), "No todos los elementos son cadenas de texto")
    def test_numeric_assignation(self):
            result_list, result_dict = algorithms.numeric_assignation(estados_usa)
            self.assertIsInstance(result_list,list)
            self.assertTrue(all(isinstance(x,int) for x in result_list), "No todos los elementos en la lista son enteros")
            self.assertIsInstance(result_dict, dict)
    def test_locations_generator(self):
            result = algorithms.locations_generator(n)
            self.assertIsInstance(result,list)
            self.assertTrue(all(isinstance(x,str) for x in result), "No todos los elementos en la lista son cadenas de texto")
    def test_sector_generator(self):
            result = algorithms.sector_generator(n)
            self.assertIsInstance(result,list)
            self.assertTrue(all(isinstance(x,str) for x in result), "No todos los elementos en la lista son cadenas de texto")
    def test_read_sector(self):
            result = algorithms.read_sector()
            self.assertIsInstance(result,list)
            self.assertTrue(all(isinstance(x,str) for x in result), "No todos los elementos en la lista son cadenas de texto")
    def test_founded_year_generator(self):
            result = algorithms.founded_year_generator(n)
            self.assertIsInstance(result,list)
            self.assertTrue(all(isinstance(x,float) for x in result), "No todos los elementos en la lista son cadenas de texto")
    def test_added_year_SP500(self):
            result = algorithms.read_added_to_SP500_year()
            self.assertIsInstance(result,list)
            self.assertTrue(all(isinstance(x,float) for x in result), "No todos los elementos en la lista son cadenas de texto")
    def test_added_year_SP500_generator(self):
            result = algorithms.added_to_SP500_year_generator(n)
            self.assertIsInstance(result,list)
            self.assertTrue(all(isinstance(x,float) for x in result), "No todos los elementos en la lista son cadenas de texto")
    def test_read_other_data(self):
            for i in data_to_read:
                result = algorithms.read_other_data(i)
                self.assertIsInstance(result,list)
                self.assertFalse(any(math.isnan(x) for x in result), "La lista tiene valores no definidos")
    def test_lognormal_generator(self):
           for i in data_to_read:
                result = algorithms.generate_other_data_lognormal(i,n)
                self.assertIsInstance(result,list)
                self.assertFalse(any(math.isnan(x) for x in result), "La lista generada tiene valores no definidos")
    def test_normal_nonegativos_generator(self):
           for i in data_to_read:
                result = algorithms.generate_other_data_normal_nonegativos(i,n)
                self.assertIsInstance(result,list)
                self.assertFalse(any(math.isnan(x) for x in result), "La lista generada tiene valores no definidos")
    def test_final_data_generator(self):
           result = algorithms.final_data(n)
           self.assertIsInstance(result,dict)
    
if __name__ == "__main__":
   unittest.main()
