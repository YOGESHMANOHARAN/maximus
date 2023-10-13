import wget
import pandas as pd


# date = list(pd.date_range('1995/07/28','2023/01/23',freq='1D'))
date = list(pd.date_range('2013/01/01','2021/01/01',freq='1YS'))
no_days = range(0,len(date))
date_string =[]

for i in no_days:
    cc = str(date[i])
    print (cc)
    date_string.append(cc[0:4]+cc[5:7]+cc[8:10])

for i in no_days:
    try:
        date_string[i]
        print(date_string[i])
        url= 'https://archive.arm.gov/orders/fileServer/orders/manoharany1/238308/sgparmbeatmC1.c1.'+date_string[i]+'.003000.nc'
        print(url)
        # url = 'https://archive.arm.gov/orders/fileServer/orders/manoharany1/238308/sgpbeflux1longC1.c1.'+date_string[i]+'.000000.cdf'
        wget.download(url,r"C:\Users\ymnharan\Documents\GitHub\github_repository\STOCHASTIC DATA\CDF2_files")
    except:
        if 0<<2:
            continue
