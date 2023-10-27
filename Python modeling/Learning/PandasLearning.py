import pandas as pd
import numpy as np

data = ["USA", "Ukraine", "Russia", "Poland"]
indexes = [3,4,5,6]
ser = pd.Series(data,index=indexes) # - таблиця з одною колонкою (одновимірний масив по суті)
print(ser)



dataFrameData = {
"Country":data,
"Nationality":["american", "ukrainian", "russian", "polish"],
"Population":[400,35,100,30],
"Regions" : [["Ohio","Virginia","LA"],
             ["Ohio","Virginia","LA"],
             ["Ohio","Virginia","LA"],
             ["Ohio","Virginia","LA"],]}
dataFrame = pd.DataFrame(dataFrameData,index=["USA","Ukraine","Russia","Poland"]) # - таблиця, що складається з багатьох колонок Series та індексів
print(dataFrame)

print(dataFrame.Nationality.USA)
print(dataFrame.loc["USA","Nationality"]) # - три види, як можна здобути інформацію з таблиці pandas 
print(dataFrame.iloc[0,1])

dataFrame.loc["USA","Nationality"] = "nigerian" # - а так - змінити 
print(dataFrame.loc["USA","Nationality"])

print(dataFrame.loc[dataFrame.Population > 100]) # - фільтрування інформації, спершу аналізується колонка "Population" і повертається масив булів (True - якщо справджується умова; False - якщо ні)
# - по ньому вже .loc веде пошук рядків, що задовольнили умову

#--------------Multi indexing ------------------------
print("\n","-----------------Multi Indexing-------------------------")
multiIndexIndex = pd.MultiIndex.from_tuples([("USA","Ohio"),("USA","LA"),("USA","San Francisco"),
                                             ("Ukraine","Podilla"),("Ukraine","Volun"),("Ukraine","Kyiv")])
colIndexes = ["Nationality","Population","GDP"]
dataMultiIndex = [["ohioan",30,30],
        ["american",40,40],
        ["mexican",15,20],
        ["ukrainian",5,100],
        ["ukrainian",10,90],
        ["ukrainian",20,30]]

dataFrameMultiIndex = pd.DataFrame(data=dataMultiIndex,columns=colIndexes,index=multiIndexIndex)
print(dataFrameMultiIndex)

#---------------------Date time Index----------------
print("\n","-----------------Date time Index-------------------------")

dateTimeIndexObj = pd.DatetimeIndex(pd.date_range("2023-10-20","2023-10-25",freq='D'))

timeFrame = pd.DataFrame(index=dateTimeIndexObj,columns=["Take a shit","Eat","Make a breakfast"],data=np.eye(6,3))

print(timeFrame)



#--------------- Window functions -----------------------
print("\n","----------------- Window functions -------------------------")
stock_list = [100, 98, 95, 96, 99, 102, 103, 105, 105, 108]

stockFrame = pd.DataFrame(data=stock_list, index=range(1,len(stock_list)+1),columns=["price"])
stockFrame["prev_price"] = stockFrame.shift(1)

stockFrame["rolling_sum_3"] = stockFrame["price"].rolling(window=3).sum() # - window - це к-сть попередніх колонок, значення яких ми включаємо в обрахункову операцію
# - тип rolling означає, що до кожної операції  береться цей елемент і ще 2 попередніх 

stockFrame["expanding_sum_2"] = stockFrame["price"].expanding(2).sum() # - тип expanding означає, що якась операція виконується, враховуючи всі попередні елементи, включаючи теперішній 

weights = [0.1, 0.2, 0.3, 0.2, 0.1]
stockFrame['weighted_avg'] = stockFrame['price'].rolling(5).apply(lambda x: np.sum(x * weights)) # - apply() - функція, що застосовує функцію в дужках для кожного значення 

stockFrame['ewm_mean'] = stockFrame['price'].ewm(span=3).mean() # - mean() - середнє арифметичне

print(stockFrame)


#-------------------------Agregation--------------------------
print(dataFrameMultiIndex.groupby(["Nationality"])["Population"].sum()) # - пошук ведеться виключно по колонках, отже змінювати індекси на інфу, котра може знадобитися - не можна
print(dataFrameMultiIndex.groupby(["Nationality"]).agg({
    "Population":"sum",
    "GDP":"mean"
}))
