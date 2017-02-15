import xmlrpclib

def make_file(data):
    file_name = "data.txt"
    file = open(file_name,'w+') # creates the file
    i = 0
    for item in data:
        if (i != 0):
            file.write("\n" + str(item))
        else:
            file.write(str(item))
        i += 1
    file.close()
    return file_name

proxy = xmlrpclib.ServerProxy('http://localhost:8000/')
a = [1,2,3,4]
file_name = make_file(a) # lo pone en un archivo de texto
print ("file_name (from client) : ", file_name)

answer = proxy.get_file_name(file_name)
# envia el archivo de texto
with open("client" + file_name, "wb") as handle:
    handle.write(proxy.receive_data(file_name).data)
