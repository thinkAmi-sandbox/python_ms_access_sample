import adodbapi
import config

def main():
    con_str = 'Provider=Microsoft.ACE.OLEDB.12.0;Data Source={0};'.format(config.PATH_ACCDB)
    conn = adodbapi.connect(con_str)
    cur = conn.cursor()
    cur.execute("select item_name from item")
    
    for c in cur.fetchall():
        print(c[0]) #=> `ringo`, `みかん
        
    cur.close()
    conn.close()
    
if __name__ == '__main__':
    main()