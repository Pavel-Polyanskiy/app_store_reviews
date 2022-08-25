import pandas as pd
from app_store_scraper import AppStore
from langdetect import detect


#parsing reviews
crypto_apps = ['coinbase-buy-bitcoin-ether',
    'crypto-com-buy-bitcoin-eth',
    'binance-buy-bitcoin-crypto',
    'robinhood-investing-for-all',
    'kucoin-buy-bitcoin-ether',
    'coinmarketcap-crypto-tracker',
    'webull-investing-trading',
    'ftx-buy-sell-crypto',
    'coinbase-pro',
    'metamask-blockchain-wallet']

data = []
for app in crypto_apps:
    try:
        my_app = AppStore(
        country = 'us', 
        app_name = app
        ) 

        my_app.review(100)

        app_reviews = []
        for i in range(my_app.reviews_count):
            review = {}
            review['app_name'] = app
            review['user_name'] =  my_app.reviews[i]['userName']
            review['timestamp'] =  my_app.reviews[i]['date']
            review['review'] =  my_app.reviews[i]['review']
            review['rating'] =  my_app.reviews[i]['rating']

            app_reviews.append(review)

        data.append(app_reviews)

    except:
        print(f'Problems with {app}')


df = pd.concat([pd.DataFrame(data[i]) for i in range(10)], axis = 0)
df['marketplace'] = 'app_store'


#extracting the language
df['language'] = df['review'].apply(lambda language: detect(language))


#saving file
df.to_csv('data.csv')