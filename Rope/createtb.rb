@db_host = "localhost"
@db_user = "root"
@db_pass = ""
@db_name = db_testRB
sqlcon = Mysql::Client.new(:host=>@db_host, :username=>@db_user, :password=>@db_pass, :database=>@db_name)
@result = sql.query("CREATE TABLE tb_datapembayaranRB(Kd_bayar INT(255) PRIMARY KEY,NIM INT(255),Jumlah_pembayaran DECIMAL")
puts "Table database berhasil dibuat ^-^\n"
puts sqlcon
sqlcon.close
