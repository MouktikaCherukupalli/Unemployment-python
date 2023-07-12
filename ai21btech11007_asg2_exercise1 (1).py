import pandas as pd
import re
import matplotlib.pyplot as plt
import numpy as np

#part 1 to add a column containing mean of all month's unemployment rate

df = pd.read_csv('USUnemployment.csv')
#print(df)
#to assign a new column Avg_Unemployment_Rate
df = df.assign(Avg_Unemployment_Rate=lambda x: (x.Jan+x.Feb+x.Mar+x.Apr+x.May+x.Jun+x.Jul+x.Aug+x.Sep+x.Oct+x.Nov+x.Dec) / 12)
#print(df)
#to arrange them in descending order
test = df.sort_values(['Avg_Unemployment_Rate'], ascending=[False])
#to drop all the extra columns and to print a dataframe of 5 rows and 2 columns
df_sort=test.drop(['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'], axis=1)
#print(df_sort)
#resetting index
df_sort=df_sort.reset_index()
#print(df_sort)
#deleting previous index column
df_sort=df_sort.drop(['index'],axis=1)
#to print only first 5 rows in this dataframe
df_first_5 = df_sort[['Year','Avg_Unemployment_Rate']].head(5)
print(df_first_5)

#part-2 

#function to print unemployement status from avg unemployment rate
def function(Avg_Unemployment_Rate):
   if(Avg_Unemployment_Rate<4):
    print('Low')
   elif(Avg_Unemployment_Rate<6 and Avg_Unemployment_Rate>=4):
    print('Medium')
   elif(Avg_Unemployment_Rate>=6):
    print('High')
    
#to add a new column of unemployment status 
for i in range(72):
   if(df.loc[i,'Avg_Unemployment_Rate']<4):
    df.loc[i,'Unemployment_Status']='Low'
   elif(df.loc[i,'Avg_Unemployment_Rate']<6 and df.loc[i,'Avg_Unemployment_Rate']>=4 ):
     df.loc[i,'Unemployment_Status']='Medium'
   elif(df.loc[i,'Avg_Unemployment_Rate']>=6):
    df.loc[i,'Unemployment_Status']='High'
#print(df)
# to calculate percentages of high low and medium occured in dataframe to plot pie chart
k=0
m=0
l=0
for i in range(72):
    if(df.loc[i,'Unemployment_Status']=='High'):
        k=k+1
high=(k*100)/72
#print(high)
for j in range(72):
    if(df.loc[j,'Unemployment_Status']=='Medium'):
        m=m+1
medium=(m*100)/72
#print(medium)
for n in range(72):
    if(df.loc[n,'Unemployment_Status']=='Low'):
        l=l+1
low=(l*100)/72
#print(low)
#to plot pie chart
y = np.array([high,medium,low])
mylabels = ["High", "Medium", "Low"]
plt.pie(y, labels = mylabels,autopct='%1.2f%%',startangle=90)
plt.legend(title='Unemployment_Status')
plt.show()

#part-3 
#to add a column decade
for i in range(72):
     df.loc[i,'Decade']=str((df.loc[i,'Year']//10)*10)
df['Decade'] =  df['Decade'].astype(str) +'s'
#to drop other columns
df_decade=df.drop(['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec','Avg_Unemployment_Rate'], axis=1)
#print(df_decade)
#to print each row of deacde
count=1940
for i in range(72):
     a=df.loc[i,'Decade']
     b=int(a[0:4])
     if( b==count):
        print(df.iloc[[i]])
        count=count+10
     


#part-4
#to add seasons-columns to dataframe  
for i in range(72):
    df.loc[i,'Winter']=(df.loc[i,'Dec']+df.loc[i,'Jan']+df.loc[i,'Feb'])/3
for i in range(72):
    df.loc[i,'Spring']=(df.loc[i,'Mar']+df.loc[i,'Apr']+df.loc[i,'May'])/3
for i in range(72):
    df.loc[i,'Summer']=(df.loc[i,'Jun']+df.loc[i,'Jul']+df.loc[i,'Aug'])/3
for i in range(72):
    df.loc[i,'Autumn']=(df.loc[i,'Sep']+df.loc[i,'Oct']+df.loc[i,'Nov'])/3
#to drop all other columns 
df_new=df.drop(['Year','Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec','Avg_Unemployment_Rate','Unemployment_Status','Decade'], axis=1)
#print(df_new)
#to plot line graph from year 1990 to 2005
df_1990to2005 = df.copy()
#to delete other rows from dataframe
for i in range(72):
    if(df_1990to2005.loc[i,'Year']<1990 or df_1990to2005.loc[i,'Year']>2005):
      df_1990to2005.drop([i],axis=0,inplace=True)
#print(df_1990to2005)
#plotting all four in same graph
plt.plot(df_1990to2005['Year'], df_1990to2005["Winter"],label='Winter')
plt.plot(df_1990to2005['Year'], df_1990to2005["Summer"],label='Summer')
plt.plot(df_1990to2005['Year'], df_1990to2005["Spring"],label='Spring')
plt.plot(df_1990to2005['Year'], df_1990to2005["Autumn"],label='Autumn')
plt.legend()
plt.show()

#part-5
#to add winter scale column by calculating previous year's average
for i in range(72):
    if(i>3):
        df_new.loc[i,'Winter_scale']=(df_new.loc[i,'Winter']+df_new.loc[i-1,'Winter']+df_new.loc[i-2,'Winter']+df_new.loc[i-3,'Winter']+df_new.loc[i-4,'Winter'])/5
     #same value for first 4 rows   
    else:
        df_new.loc[i,'Winter_scale']=df_new.loc[i,'Winter']
#similarly for spring
for i in range(72):
    if(i>3):
        df_new.loc[i,'Spring_scale']=(df_new.loc[i,'Spring']+df_new.loc[i-1,'Spring']+df_new.loc[i-2,'Spring']+df_new.loc[i-3,'Spring']+df_new.loc[i-4,'Spring'])/5
    else:
        df_new.loc[i,'Spring_scale']=df_new.loc[i,'Spring']
#similarly for summer
for i in range(72):
    if(i>3):
        df_new.loc[i,'Summer_scale']=(df_new.loc[i,'Summer']+df_new.loc[i-1,'Summer']+df_new.loc[i-2,'Summer']+df_new.loc[i-3,'Summer']+df_new.loc[i-4,'Summer'])/5
    else:
        df_new.loc[i,'Summer_scale']=df_new.loc[i,'Summer']
#similarly for autumn
for i in range(72):
    if(i>3):
        df_new.loc[i,'Autumn_scale']=(df_new.loc[i,'Autumn']+df_new.loc[i-1,'Autumn']+df_new.loc[i-2,'Autumn']+df_new.loc[i-3,'Autumn']+df_new.loc[i-4,'Autumn'])/5
    else:
        df_new.loc[i,'Autumn_scale']=df_new.loc[i,'Autumn']
#print(df_new)
#to print rows with given years 
#the index will be 'given year -1948'
#print(df_new.iloc[[1950-1948]])
#print(df_new.iloc[[1960-1948]])
#print(df_new.iloc[[1970-1948]])
#print(df_new.iloc[[1980-1948]])
#print(df_new.iloc[[1990-1948]])
#print(df_new.iloc[[2000-1948]])














