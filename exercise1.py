import pandas as pd
data = pd.read_csv("exercise1_data.csv") #loading the data from the CSV file into a pandas DataFrame

print(data.head()) #displaying the first 5 rows of the DataFrame
print(data.info()) #displaying the summary information of the DataFrame
print(data.describe()) #displaying the statistical summary of the DataFrame
print(data.tail()) #displaying the last 5 rows of the DataFrame
print(data.columns) #displaying the column names of the DataFrame
print(data.index) #displaying the index of the DataFrame
print(data.shape) #displaying the shape of the DataFrame (number of rows and columns)
