# В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. 
# Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?

import random
import pandas
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pandas.DataFrame({'whoAmI':lst})
print(data)

#-------------------------------------------------------
# тут я проверяю, а как собственно работает get_dummies. Ну - работает.

table = pandas.get_dummies(data)
table = table.rename(columns= {"whoAmI_human":"Human","whoAmI_robot":"Robot"})
#print(table)

#-------------------------------------------------------
# теперь надо попробовать обойтись без него.

def findhuman(x):
    if x == "human":
        return 1
    else:
        return 0
    
def findrobot(x):
    if x == "robot":
        return 1
    else:
        return 0

data['Human'] = data['whoAmI'].apply(findhuman)
data['Robot'] = data['whoAmI'].apply(findrobot)
#data1 = data.drop('whoAmI', axis= 1 , inplace= True)
res = data.loc[:, data.columns !='whoAmI']
print(res)