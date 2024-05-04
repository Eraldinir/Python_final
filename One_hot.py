import random
import pandas
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pandas.DataFrame({'whoAmI':lst})
print(data.head())