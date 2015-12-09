import sqlalchemy
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import config

Base = declarative_base()
class Item(Base):
	# テーブル名の指定が必要
	__tablename__ = 'item'
	
	item_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
	item_name = sqlalchemy.Column(sqlalchemy.String)
	
	# print()された時に表示する内容
	def __str__(self):
		return self.item_name

def main():
	# `access`dialectを使うため、sqlalchemy-accessパッケージが必要
	# formatで`{`を使うため、`{`を重ねることでエスケープ
	url = "access+pyodbc:///?Driver={{Microsoft Access Driver (*.mdb, *.accdb)}};Dbq={0};".format(config.PATH_ACCDB)
	
	engine = sqlalchemy.create_engine(url)
	Session = scoped_session(sessionmaker(autocommit=False,
										autoflush=False,
										bind=engine))
	session = Session()
	for item in session.query(Item):
		print(item) 

if __name__ == '__main__':
	main()
