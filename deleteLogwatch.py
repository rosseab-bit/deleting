import os
import sys
import json
import time
import math

def deleteLog():
    directory_root = "/path/de/archivos" # directorio donde se encuentran los archivos o directorios a borrar.
    dir_log = "/path/dellDir.tmp" # archivo donde se guardar la salida de archivos a borrar.
    cmd = "ls -lhtr %s | awk '{print $9}' > %s" % (directory_root, dir_log)
    os.system(cmd)
    tmp = open(dir_log, 'r')
    list_dir = []
    for directorio in tmp:
        if len(directorio)>1:
            directorio = directorio.rstrip('\n')
            list_dir.append(directorio)
    print (list_dir)
    print (len(list_dir))
    i = 0
    # borra la mitad de los archivos mas viejos.
    # modificando podemos tomar porcentajes a borrar con fracciones.
    x = len(list_dir)/2
    x_dec, x_int = math.modf(x)
    print (x_entero)
    while (i<x_int):
        path = "%s/%s" % (directory_root, list_dir[i])
        #print (path)
        if os.path.isdir(path):
            print (list_dir[i]+" : "+"Es una carpeta")
            time.sleep(2)
            print ("----------------------------------------")
            print ("Borrando carpeta: rm -rf "+list_dir[i])
            cmd = "rm -rf %s" % path
            os.system(cmd)
            print (cmd)
            print ("----------------------------------------")
            time.sleep(2)
        else:
            print (list_dir[i]+" : "+"Es un archivo")
            print ("----------------------------------------")
            time.sleep(2)
            print ("Borrando archivo: rm -f "+list_dir[i])
            cmd = "rm -f %s" % path
            os.system(cmd)
            print (cmd)
            print ("----------------------------------------")
            time.sleep(2)
        i+=1

deleteLog()
