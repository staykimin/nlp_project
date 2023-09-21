import mysql.connector, datetime

class DB_Core:
	def __init__(kimin):
		kimin.db = mysql.connector.connect(
			host="localhost",
			user="root",
			password="",
			database="nlp_project",
			auth_plugin='mysql_native_password'
			)
		
		kimin.cursor = kimin.db.cursor()
	
	def Get_Time(kimin, format="%Y-%m-%d"):
		now = datetime.datetime.now()
		now = now.strftime(format)
		return now
	
	def Hitung_Label(kimin, data):
		hasil = []
		for i in data:
			if not i in hasil:
				hasil.append(i)
		return len(hasil)

	def Get_Data(kimin, nama_tabel):
		kimin.cursor.execute(f"SELECT * FROM {nama_tabel}")
		data = kimin.cursor.fetchall()
		hasil = {}
		hasil['total_data'] = len(data)
		hasil['data'] = []
		for i in data:
			temp_data = {}
			for a in kimin.cursor.description:
				temp_data[a[0]] = None
			
			no = 0
			for a in temp_data:
				temp_data[a] = i[no]
				no +=1
			hasil['data'].append(temp_data)
		
		return hasil
	
	def Add_Data(kimin, nama_tabel, kolom, value):
		temp_value = []
		for i in range(len(kolom)):
			temp_value.append("%s")
		
		query = f"INSERT INTO {nama_tabel} {tuple(kolom)} VALUES {tuple(temp_value)}"
		query = query.replace("'","")
		
		kimin.cursor.execute(query, tuple(value))
		kimin.db.commit()
		return "Data Berhasil Ditambahkan"
	
	def Select_Data(kimin, nama_tabel, id_name, data):
		query = f"SELECT * FROM {nama_tabel} WHERE {id_name}= '{data}'"
		kimin.cursor.execute(query)
		data = kimin.cursor.fetchall()
		hasil = {}
		hasil['total_data'] = len(data)
		hasil['data'] = []
		for i in data:
			temp_data = {}
			for a in kimin.cursor.description:
				temp_data[a[0]] = None
			
			no = 0
			for a in temp_data:
				temp_data[a] = i[no]
				no +=1
			hasil['data'].append(temp_data)
		return hasil
	
	def Check_Data(kimin, nama_tabel, kolom, value):
		query = f"SELECT COUNT(1) FROM `{nama_tabel}` WHERE {kolom} = '{value}'"
		
		kimin.cursor.execute(query)
		if kimin.cursor.fetchone()[0]:
			return True
	
		return False
	def Delete_Data(kimin, nama_tabel, id_name, data):
		query = f"DELETE FROM {nama_tabel} WHERE {id_name}= '{data}'"
		kimin.cursor.execute(query)
		kimin.db.commit()
	
	def Update_Data(kimin, nama_tabel, kolom, value, id_name, data):
		query = f"UPDATE {nama_tabel} SET {kolom}='{value}' WHERE {id_name} = '{data}'"
		kimin.cursor.execute(query)
		kimin.db.commit()