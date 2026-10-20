import os
from urllib.parse import quote_plus

class Config:
    DB_HOST: str = os.getenv(key="DB_HOST", default="localhost")  
    DB_PORT: int = os.getenv(key="DB_PORT", default=14441) 
    DB_USER: str = os.getenv(key="DB_USER", default="avnadmin") 
    DB_PASSWORD: str = os.getenv(key="DB_PASSWORD", default="") 
    DB_NAME: str = os.getenv(key="DB_NAME", default="") 
    DB_SSL_CA: str = os.getenv(key="DB_SSL_CA", default="CERTS/ca.pem") 

    @property
    def DATABASE_URL(self) -> str:
        user = quote_plus(self.DB_USER)
        password = quote_plus(self.DB_PASSWORD)
        database = quote_plus(self.DB_NAME)

        return (
            f"mysql+mysqlconnector://{user}:{password}"
            f"@{self.DB_HOST}:{self.DB_PORT}/{database}"
        )

config = Config()
