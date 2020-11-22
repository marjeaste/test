server = "ID-сервера"
port1,port2, portn = "MAC1", "MAC2", "MACn"
ip1, ipn = "IP1", "IPn"
#  print(server + "      " + port1 + "      " + ip1)
#  print(server + "      " + port1 + "      " + ipn)
#  print(server + "      " + port2 + "      " + ip1)
#  print(server + "      " + port2 + "      " + ipn)
#  print(server + "      " + portn + "      " + ip1)
#  print(server + "      " + portn + "      " + ipn)

my_file = open("some.txt", "w")
my_file.write(server + "      " + port1 + "      " + ip1)
my_file.write(server + "      " + port1 + "      " + ipn)
my_file.write(server + "      " + port2 + "      " + ip1)
my_file.write(server + "      " + port2 + "      " + ipn)
my_file.write(server + "      " + portn + "      " + ip1)
my_file.write(server + "      " + portn + "      " + ipn)
my_file.close()