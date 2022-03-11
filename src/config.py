from pydantic import BaseSettings

class Settings(BaseSettings):
    class Config: 
        env_file = '.env'

    DATABASE_URL: str

    db_host: str
    db_port: int = 5432
    db_user: str
    db_password: str
    db_db: str

    debug: bool = False
    ADMIN_TOKEN: str = None
    
TORTOISE_ORM = {
    'connections': {
        # Dict format for connection
        # 'default': {
        #     'engine': 'tortoise.backends.asyncpg',
        #     'credentials': {
        #         'host': Settings().db_host,
        #         'port': Settings().db_port,
        #         'user': Settings().db_user,
        #         'password': Settings().db_password,
        #         'database': Settings().db_db,
        #     }
        # },
        # Using a DB_URL string
        'default': Settings().DATABASE_URL
    },
    'apps': {
        'models': {
            'models': ['src.models', 'aerich.models'],
            # If no default_connection specified, defaults to 'default'
            'default_connection': 'default',
        }
    }
}