import pandas as pd

def keepOnlyNeededColumnsInTable(csv, column_to_keep):
    f = pd.read_csv(csv, sep=",")
    keep_col = column_to_keep
    new_f = f[keep_col]
    new_f.to_csv(csv, index=False)
    print(new_f)
    print("deleted not needed columns in the table ")


def rename_column_names(csv):
    f = pd.read_csv(csv, sep=",")
    f.rename(columns={"timeStamp": "time"},inplace=True)
    f.to_csv(csv)


def add_two_hours(csv):
    data =pd.read_csv(csv,sep=",")
    print(data)
    data['time']=pd.to_datetime(data['time']) + pd.DateOffset(hours=2)
    data.to_csv(csv)


def joinTwoTables(csv1, csv2, csv_out):
    d_one = pd.read_csv(csv1, sep=",")
    d_two = pd.read_csv(csv2, sep=",")
    d_three = pd.merge(d_one, d_two, on='time', how='outer')
    d_three.to_csv(csv_out)
    print(d_three)


def sortByDate(csv_out):
    data = pd.read_csv(csv_out)
    print(data)
    data = data.sort_values(['time'])
    print(data)
    data.to_csv(csv_out)


def delteRowWithSpecificValueInColumnX(csv_in, csv_out):
    data = pd.read_csv(csv_in)
    print(data)
    data.drop(data[data[column_name] != value_to_not_delete].index, inplace=True)
    data.to_csv(csv_out)
    print(data)
    print("deleted value not needed")


def keepOnlyNeededColumnsInTable(csv, column_to_keep):
    f = pd.read_csv(csv, sep=",")
    keep_col = column_to_keep
    new_f = f[keep_col]
    new_f.to_csv(csv, index=False)
    print(new_f)
    print("deleted not needed columns in the table ")


def substractValueInRow(csv):
    data = pd.read_csv(csv, sep=",")
    data['totalCount'] = data['totalCount'].apply(lambda x: x - 2)
    data.to_csv(csv)
    print(data)


def joinTwoTables(csv1, csv2, csv_out):
    d_one = pd.read_csv(csv1, sep=",")
    d_two = pd.read_csv(csv2, sep=",")
    d_three = pd.merge(d_one, d_two, on='time', how='outer')
    d_three.to_csv(csv_out)
    print(d_three)


def sortByDate(csv_out):
    data = pd.read_csv(csv_out)
    print(data)
    data = data.sort_values(['time'])
    print(data)
    data.to_csv(csv_out)


def fillValueFromPreviousRow(csv):
    data = pd.read_csv(csv, sep=',')
    print(data)
    data[column_name_with_data].fillna(method="ffill", inplace=True)
    print(data)
    data.to_csv(csv)


def delteRowWithSpecificValue(csv):
    data = pd.read_csv(csv)
    print(data)
    data.drop(data[data['state'] == "RUNNING"].index, inplace=True)
    data.drop(data[data['state'] == "ERROR"].index, inplace=True)
    data.to_csv(csv)
    print(data)


def convert_date(csv):
    mydateparser = lambda x: pd.datetime.datetime.strptime(x,"%Y-%m-%dT%H:%M:%S.%fZ")
    data = pd.read_csv(csv, sep=",", parse_dates=['time'], dtype=object, date_parser=mydateparser)
    print(data)
    data.to_csv(csv)




