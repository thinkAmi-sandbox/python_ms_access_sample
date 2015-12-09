import pypyodbc
import config

def main():
    conn = pypyodbc.win_connect_mdb(config.PATH_MDB)
    # accdbは開けず、以下のエラーとなる
    # conn = pypyodbc.win_connect_mdb(config.PATH_ACCDB)
    # pypyodbc.Error: ('HY000', "[HY000] [Microsoft][ODBC Microsoft Access Driver] 
    # データベース '(不明)' を開くことができません。アプリケーションで認識できないデータベースであるか、
    # またはファイルが破損しています。 ")
    
    cur = conn.cursor()
    cur.execute("select item_name from item")
    
    for c in cur.fetchall():
        print(c[0]) #=> `hoge`, `fuga`
        
    cur.close()
    conn.close()
    
if __name__ == '__main__':
    main()