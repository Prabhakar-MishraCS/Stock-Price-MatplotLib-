import pandas_datareader as web
import matplotlib.pyplot as plt

plt.style.use('dark_background')
company = 'TSLA'
df = web.DataReader(company, data_source = 'yahoo', start ='2015-01-01', end ='2021-07-01')
#print(df.shape)

plt.figure(figsize=(14,6))
plt.title("Closing Price")
plt.plot(df['Close'])
plt.xlabel('Date',fontsize ='18')
plt.ylabel('Closing Price in $',fontsize = '18')
plt.show()

