# import os
# from dotenv import load_dotenv

# load_dotenv()

# postgres_user = os.getenv('POSTGRES_USER')
# postgres_password = os.getenv('POSTGRES_PASSWORD')
# postgres_db = os.getenv('POSTGRES_DB')
# postgres_db = os.getenv('POSTGRES_DB')
# postgres_db = os.getenv('POSTGRES_DB')
#
# host = credentials['HOST']
# port = credentials['PORT']
from dotenv import dotenv_values

pg_config = dotenv_values('.env')
