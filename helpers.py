import ccxt.pro as ccxt

def pick_exchange():
    while True:
        try:
            exchange_id = input('Enter exchange id: ')
        except AttributeError:
            print('Wrong exchange id, please try again')
        else:
            return exchange_id

async def pick_currency(client):

    await client.load_markets()
    
    while True:
        currency = input('Enter currency in CCXT-format: ')
        if currency in client.markets:
            print('Market found')
            return currency
        else:
            print('Market not found, try again.')


async def starter():

    eid = pick_exchange() 

    taker_client = getattr(ccxt, eid)()

    print(taker_client.name)
    currency = await pick_currency(taker_client)
    return taker_client, currency
