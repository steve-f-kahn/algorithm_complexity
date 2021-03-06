import csv
import os.path
import numpy as np
import time

class Timer():

    def populate_array(self):
        
        list_of_arrays = []
        i = 1
        while i <= 10:
            array = []
            j = 0
            while j < i*5000 :
                array.append(j)
                j+= 1
            i += 1
            list_of_arrays.append(array)
        return list_of_arrays


    def start(self, function):
        arrays = self.populate_array()
        results = []
        for array in arrays:
            first = time.time()
            function(array)
            second = time.time()
            results.append(second - first)

        self.write_to_file(results, function)
        
        
    def function_version(self, function):
        i = 1
        while True:
            if os.path.exists(f'{function.__name__}_v{i}.csv'):
                i += 1
            else :
                return i
    
    def write_to_file(self, results, function):
        version = self.function_version(function)
        with open(f'{function.__name__}_v{version}.csv', 'w') as csvfile:
            file = csv.writer(csvfile)
            i = 1
            file.writerow(["Array Size", "Time"])
            for result in results:
                file.writerow([5000*i,result])
                i += 1


        
