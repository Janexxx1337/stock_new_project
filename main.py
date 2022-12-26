import requests
import smtplib

my_email = 'krahs123@gmail.com'
my_password = 'jvcmypmwsyorapfw'

response = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=TSLA&apikey=Z4MNOVTV5MIBTJQ7').json()
before_yesterday = response['Time Series (Daily)']['2022-12-22']['4. close']
yesterday = response['Time Series (Daily)']['2022-12-23']['4. close']

difference = abs(float(yesterday) - float(before_yesterday))
dif_percent = ( difference / float(yesterday)) * 100
if dif_percent > 4:
    today_news = requests.get('https://newsapi.org/v2/everything?q=TSLA&from=2022-12-26&sortBy=popularity&apiKey=f937f961ee724e30b145e81cdc649e7a').json()
    articles = today_news['articles']
    three_articles = articles[:3]
    connection = smtplib.SMTP('smtp.gmail.com')
    connection.starttls()
    connection.login(my_email, my_password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=krahs123@mail.ru,
        msg=f'Subject: Stocks News\n\n {three_articles}'
    )
