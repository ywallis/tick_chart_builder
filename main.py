import redis
# import ccxt.pro as ccxt
import asyncio
import json
from ccxt_pg import export_to_sql, create_public_trades_table
from config import pg_config
from helpers import starter

watching = True


async def watch_ticker(client, ticker, redis_instance, table):
    while watching:
        try:
            trades = await client.watch_trades(ticker)
            # print(trades)
            # send_to_redis(redis_instance, trade)
            export_to_sql(trades, pg_config, table, False)

        except Exception as e:
            print(e)
            raise (e)


def send_to_redis(redis_instance, trade_item):
    redis_instance.lpush("orders_test", json.dumps(trade_item))
    redis_instance.ltrim("orders_test", 0, 99)

async def main():

    client, ticker = await starter()
    table_name = f"{client.name} | {ticker}"
    r = redis.Redis(host="localhost", port=6379, decode_responses=True)
    print(f"Starting, watching {ticker}.")
    create_public_trades_table(pg_config, table_name)
    await watch_ticker(client, ticker, r, table_name)
# client = ccxt.binance()
# ticker = "BTC/USDT"
# table_name = f"{client.name} | {ticker}"

if __name__ == "__main__":
    asyncio.run(main())
