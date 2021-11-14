from sqlalchemy import create_engine
 
engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost/postgres")
engine.connect()
print("Соединение прошло успешно")
