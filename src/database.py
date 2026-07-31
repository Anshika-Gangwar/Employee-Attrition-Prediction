from sqlalchemy import create_engine
from urllib.parse import quote_plus
from config import *

# Encode special characters in the password
encoded_password = quote_plus(DB_PASSWORD)

connection_string = (
    f"mysql+pymysql://{DB_USER}:{encoded_password}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

engine = create_engine(connection_string)

print("Database connected successfully!")
