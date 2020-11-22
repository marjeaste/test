import sqlite3

conn = sqlite3.connect("servers.db")
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS servers
                  (number, server, server_port, port_ip)
               """)
servers = [('1', 'server_1', 'port_1', 'ip_port1'),
           ('2','server_1', 'port_2', 'ip_port2'),
           ('3','server_1', 'port_3', 'ip_port3'),
           ('4','server_2', 'port_1', 'ip_port1')]

cursor.executemany("INSERT INTO servers VALUES (?,?,?,?)", servers)
conn.commit()

tests = SELECT * FROM servers;
print(tests)

