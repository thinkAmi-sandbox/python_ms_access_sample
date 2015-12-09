import pypyodbc
import config

def main():
    # formatで`{`を使うため、`{`を重ねることでエスケープ
    conn = pypyodbc.connect("Driver={{Microsoft Access Driver (*.mdb, *.accdb)}};Dbq={0};".format(config.PATH_ACCDB))
    cur = conn.cursor()
    cur.execute("select item_name from item")
    
    for c in cur.fetchall():
        print(c[0]) #=> `ringo`, `みかん
    
    cur.close()
    conn.close()
    
if __name__ == '__main__':
    main()