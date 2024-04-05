import numpy as np
import pandas as pd
import random 
import xlsxwriter

SP500_Excel_file = 'S&P 500 Companies (Standard and Poor 500).xlsx'
workbook = xlsxwriter.Workbook("Companies Data.xlsx", {'nan_inf_to_errors': True})
worksheet = workbook.add_worksheet("FirstSheet")

# EIN Generation 
# This function should generate a random number of 9 digits. We can get 1,000,000,000 different numbers of 9 digits
# n is the row count variable 

#Special type of data :
#EIN, Headquearets location, foundation year, Date added to SP&500, sector

def EIN_generator(n):

    #variable Nº 1
    added_numbers = set()
    EIN = []
    while len(EIN) < n:
        number = str(np.random.randint(1,101)) + "-" + str(np.random.randint(1000000,9999999))
        if number not in added_numbers:
            EIN.append(number)
            added_numbers.add(number)
    return EIN
def list_generator(data_dict):
    data = []
    for key,value in data_dict.items():
        for i in range(value):
            data.append(key)
    random.shuffle(data)
    return data
def read_locations():
    # gets a sample of headquaters locations for S&P500 companies
    df = pd.read_excel('Stock Screener_2024-03-21 (1).xlsx', usecols=['Location']) 
    new_dict = df.to_dict()
    locations = new_dict['Location']
    location = list(locations.values())
    states= []
    for i in range(len(location)):
        var = str(location[i])
        a = var.find(",")
        states.append(var[a+2:])
    return states
def numeric_assignation(data_list):
    # Assigns a numeric value for each different state 
    data_numbers = {}
    numeric_assignations,data = data_list[:-1],data_list[:-1]
    cnt = 0
    for i in range(len(data)):
        if data[i] not in data_numbers.values():
            cnt +=1
            data_numbers[cnt] = data[i]
    for i in range(len(numeric_assignations)): 
        a = [key for key, value in data_numbers.items() if value == numeric_assignations[i]]
        numeric_assignations[i] = a[0]
    return numeric_assignations,data_numbers
def locations_generator(n):
    #variable Nº 2
    # i'll use a multinomial distribution so i need the occurrence probability of each state 
    locations_list = read_locations()
    numeric_states, states_numbers = numeric_assignation(locations_list)
    probabilities = {}
    cnter = 0
    for key,value in states_numbers.items():
        cnter +=1
        probabilities[cnter] = numeric_states.count(key)/len(numeric_states)
    probabilities_list = [value for key, value in probabilities.items()]
    #data generation
    data = np.random.multinomial(n, probabilities_list)
    data_with_years = {values: keys for keys,values in states_numbers.items()}
    i = -1
    for key,values in data_with_years.items():
        i +=1
        data_with_years[key] = data[i]
    data = list_generator(data_with_years)
    return data
def read_sector():
    # gets a sample of headquaters locations for S&P500 companies
    df = pd.read_excel('Stock Screener_2024-03-21 (1).xlsx', usecols=['Sector']) 
    new_dict = df.to_dict()
    sector = new_dict['Sector']
    sector = list(sector.values())
    return sector[:-1]
def sector_generator(n):
    #variable Nº 3
    # i'll use a multinomial distribution so i need the occurrence probability of each state 
    sectors_list = read_sector()
    numeric_sectors, sectors_numbers = numeric_assignation(sectors_list)
    probabilities = {}
    cnter = 0
    for key,value in sectors_numbers.items():
        cnter +=1
        probabilities[cnter] = numeric_sectors.count(key)/len(numeric_sectors)
    probabilities_list = [value for key, value in probabilities.items()]
    #print(probabilities_list)
    #data generation
    data = np.random.multinomial(n, probabilities_list)
    data_with_years = {values: keys for keys,values in sectors_numbers.items()}
    i = -1
    for key,values in data_with_years.items():
        i +=1
        data_with_years[key] = data[i]
    data = list_generator(data_with_years)
    return data
def read_founded_year():
    df = pd.read_excel('Stock Screener_2024-03-21 (1).xlsx', usecols=['Founded'])
    new_dict = df.to_dict()
    founded_year = list(new_dict['Founded'].values())
    return founded_year[:-1]
def founded_year_generator(n):
    #variable Nº 4
    # i'll use a multinomial distribution so i need the occurrence probability of each founded year 
    founded_year = read_founded_year()
    probabilities = {}
    for i in founded_year:
        if i not in probabilities.keys():
            probabilities[i] = founded_year.count(i)/len(founded_year)
    data = np.random.multinomial(n,list(probabilities.values()))
    data_with_years = dict(probabilities)
    i = -1
    for key,values in data_with_years.items():
        i +=1
        data_with_years[key] = data[i]
    data = list_generator(data_with_years)
    return data
def read_added_to_SP500_year():
    df = pd.read_excel('Stock Screener_2024-03-21 (1).xlsx', usecols=['Date added to S&P500'])
    new_dict = df.to_dict()
    added_year = list(new_dict['Date added to S&P500'].values())
    return added_year[:-1]
def added_to_SP500_year_generator(n):
    #variable Nº 5
    # i'll use a multinomial distribution so i need the occurrence probability of each added year to SP&500 index
    added_year = read_founded_year()
    probabilities = {}
    for i in added_year:
        if i not in probabilities.keys():
            probabilities[i] = added_year.count(i)/len(added_year)
    data = np.random.multinomial(n,list(probabilities.values()))
    data_with_years = dict(probabilities)
    i = -1
    for key,values in data_with_years.items():
        i +=1
        data_with_years[key] = data[i]
    data = list_generator(data_with_years)
    return data


#Other type of data :

#Market cap, Dividen Yield, EPS diluted, Trailing 12 months, EPS diluted growth %, TTM YoY, price y otros indicadores 
#la idea es crear una funcion que reciba el tipo de dato y retorne la lista de tamaño n con los datos aplicando una distribucion normal 
#luego en la funcion principal donde se van a llamar a todas las funciones generadoras, crear cada una de las listas para market cap, dividen yield, etc
#Falta buscar más datos economicos de la empresas, buscarlos en tradingview. 

def read_other_data(column):
    df = pd.read_excel('Stock Screener_2024-03-21 (1).xlsx', usecols = [column])
    new_dict = df.to_dict()
    read_dict = new_dict[column]
    read_list = list(read_dict.values())
    read_list_filtered = list(filter(lambda x: not np.isnan(x), read_list))
    return read_list_filtered
def generate_other_data_lognormal(column, n):
    read_list = read_other_data(column)
    read_list_log = np.log(read_list)
    mean = np.mean(read_list_log)
    sigma = np.std(read_list_log)
    data = np.random.lognormal(mean,sigma,n)
    data_round = list(np.round(data,decimals = 3))
    np.set_printoptions(suppress=True)
    return data_round
def generate_other_data_normal_nonegativos(column, n):
    read_list = read_other_data(column)
    mean = np.mean(read_list)
    std_dev = np.std(read_list)
    data = np.random.normal(mean,std_dev,n)
    data_nonegativos = np.clip(data, a_min=0, a_max=None)
    data_round = list(np.round(data_nonegativos,decimals= 3))
    np.set_printoptions(suppress=True)
    return data_round




final_data_dict = {}
data_lognormal = ["Market capitalization (Billions)",
        "Price","Volume 1 day", "Relative Volume 1 day",
        "Price to earnings ratio","Volume 1 day", 
        "Relative Volume 1 day","Volatility 1 month",
        "Volatility 1 week","Price to sales ratio",
        "Price to book ratio","Price to cash flow ratio", 
        "Price to cash ratio","Price to free cash flow ratio",
        "Enterprise value to revenue ratio, Trailing 12 months", "Enterprise value to EBITDA ratio, Trailing 12 months",
        "Enterprise value to EBIT ratio, Trailing 12 months","Operating margin %, Annual", "Gross margin %, Annual",
        "Number of shareholders, Annual", "Revenue per employee, Annual  (Millions)", "Cash to debt ratio, Annual",
        "Total liabilities, Annual (Billions)","Total assets, Quarterly (Billions)"]
    
data_normal_nonegativos = ["Dividend yield %, Trailing 12 months",
                                "Dividends per share, Annual",
                                 "Dividends per share, Quarterly"]
    
def final_data(n):
        final_data_dict["EIN Number"]= EIN_generator(n)
        final_data_dict["Headquaters location"] = locations_generator(n)
        final_data_dict["Sector"] = sector_generator(n)
        final_data_dict["Date added to SP500"] = added_to_SP500_year_generator(n)
        final_data_dict["Year founded"] = founded_year_generator(n)
        for i in data_lognormal:
            data_list_lognormal = generate_other_data_lognormal(i,n)
            final_data_dict[i] = data_list_lognormal
        for j in data_normal_nonegativos:
            data_list_nonegativos = generate_other_data_normal_nonegativos(j,n)
            final_data_dict[j] = data_list_nonegativos
        
        i = 0
        for key,value in final_data_dict.items():
            worksheet.write(0,i,key)
            i +=1 
        j = 0
        for key,value in final_data_dict.items():
            #a = list(value)
            for i in range(n):
                worksheet.write(i+1,j,value[i])
            j += 1
        workbook.close()
        return final_data_dict


#print(final_data(10))
   
    