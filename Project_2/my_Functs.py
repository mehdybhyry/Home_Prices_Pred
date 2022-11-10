#Calculating the percentage of nan_values

def null_vals_prct(data):
    import pandas as pd
    nan_p = []
    columns = data.columns
    for i in columns:
        prcnt = len(data[i][data[i].isna() == True]) / len(data[i])*100
        nan_p.append(prcnt)
    Nan_values = pd.DataFrame({'Features' : columns, 'NaN_Prcnt': nan_p}).sort_values(by = 'NaN_Prcnt', ascending = False)
    Nan_values = Nan_values[Nan_values.NaN_Prcnt > 1]
    return(Nan_values)


def mehdy(data):
    import pandas as pd
    data = pd.read_csv("data/train.csv")
    return(data.head(3))


#Identifies null columns
def null_columns(data):
    print('<No of null rows in each column>\n', 'Columns\t No\t Type\n', '--------\t ----    -----')
    for i in data.columns:
        if data[i].isnull().sum() != 0:
           print(i, '  \t', data[i].isnull().sum(), '\t', data[i].dtype)
    print('\nTotal rows:',len(data))


#Identifies columns_type       
def columns_type(raw_data, typ):
    columns = []
    s = 0
    for i in raw_data.columns:
        if str(raw_data[i].dtypes) == str(typ):
            if s==0:
                print('<', typ, 'columns>')
                print('#\t   Column\t')
                print('-\t  -------\t')
            s+=1 
            print(s,'\t', i)
            columns.append(i)
    return(columns)


#unique columns count and values function
def unique_columns(raw_data, typ):
    s = 0
    for i in raw_data.columns:
        if str(raw_data[i].dtypes) == str(typ):
            if s==0:
                print('<Unique variables of', typ, 'features>')
                print('#\t   Column\t       Count\t     variables')
                print('-\t  -------\t      ------\t    ----------\n')
            s+=1 
            print(s,'\t', i,' \t\t', len(raw_data[i].unique()),' \t', raw_data[i].unique())