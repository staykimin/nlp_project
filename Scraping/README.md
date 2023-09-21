
## Scraping_Script
<p align="center"><img width="50%" src="../Untitled.jpeg"></p>

Script Yang Digunakan Untuk Mengumpulkan Dataset Yang Berupa Artikel Yang Terdapat Di Internet


## Cara_Penggunaan
- Import SQL Terlebih Dahulu Pada Phpmyadmin
- Install Terlebih Dahulu Library Yang Dibutuhkan
  ```bash
  pip install flask mysql-connector Scrapy mysql-connector beautifulsoup4
  ```
- Edit file core_db_web.py Pada Yang Ada Pada Folder kimin Untuk Konfigurasi Koneksi Database
  ```python
  kimin.db = mysql.connector.connect(
  			host="localhost", #hostname dari database
  			user="root", #username dari database
  			password="",  #password dari database
  			database="nlp_project", #nama dari database
  			auth_plugin='mysql_native_password'
  			)
  ```
- Run Program Python app.py kemudian akses localhost:5000
  ```
  python app.py
  ```
