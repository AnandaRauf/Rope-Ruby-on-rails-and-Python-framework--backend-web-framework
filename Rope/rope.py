import mysql.connector
import os

print("==========================================================================================\n")
print("Selamat datang di Rope backend web framework ^-^\n")
namaaplikasi = "Rope backend web framework\n"
versi = "Version 1.0\n"
devby = "Ananda Rauf Maududi\n"
print(namaaplikasi)
print(versi)
print("Developed by:",devby)
print("==========================================================================================\n")

def MenuRope():
      print("Pilih nomor yang ada didalam menu :")
      print
      print("1.RopePy")
      print("2.RopeRb")


    
def RopePy():
       #BuatKoneksiDatabasePython  
        dbcon = mysql.connector.connect(host="localhost",user="root",passwd="")
        createdb = dbcon.cursor()
        createdb.execute("CREATE DATABASE db_testPY")
        print("Database berhasil dibuat ^-^\n")
        
        #BuatDatabasePython
        dbcon = mysql.connector.connect(host="localhost",user="root",passwd="",database="db_testPY")
        if dbcon.is_connected():
         print("Database berhasil dihubungkan ^-^\n")
        
         #BuatTableDatabasePython
        dbcon = mysql.connector.connect(host="localhost",user="root",passwd="",database="db_testPY")
        createtable = dbcon.cursor()
        sql = "CREATE TABLE tb_datapembayaranPY(Kd_bayar INT(255) PRIMARY KEY,NIM INT(255),Jumlah_pembayaran DECIMAL)"
        createtable.execute(sql)
        print("Tabel berhasil dibuat\n")
       
        
        #RestAPIPython
        print("Tambahkan sendiri, jika ada job rest api")

    
def RopeRb():
        #BuatDatabasePakaiFrameworkRails 
        os.system("Ror.bat")
        os.system("Ror.bat > outrails.txt")
        print("Berhasil buat database menggunakan framework rails ^-^\n")
        #BuatDatabaseRuby
       
        os.system("createdb.rb")
        os.system("createdb.rb > outputruby.txt")
           
   
        #BuatKoneksiDBRuby
        
        os.system("conndb.rb")
        os.system("conndb.rb > outputruby.txt") 
        
        
        #BuatTableDBRuby
        
        os.system("createtb.rb")
        os.system("createtb.rb > outputruby.txt")
        
       
        #RestAPiRuby
        
        os.system("restapi.rb")
        os.system("restapi.rb > outputruby.txt")
        print("Berhasil excute Ruby ^-^")

MenuRope()

pilih = int(input("Masukan nomor pilihan dalam menu :"))

if pilih == 1:
        RopePy()
elif pilih==2:
       RopeRb()
else:
        exit
