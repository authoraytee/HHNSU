from sqlalchemy import create_engine
 
engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost/hhnsu")
engine.connect()
print("Соединение прошло успешно")
