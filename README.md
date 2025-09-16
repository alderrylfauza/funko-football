1. Membuat proyek Django baru dengan judul funko-football, dengan menggunakan command django-admin startproject <name> .
2. connect proyeknya ke github dan website pws
3. membuat aplikasi mainnya, dan juga membuat model product serta atribut atribut yang biasanya dimiliki oleh website penjualan barang
4. lalu, membuat views.py untuk mengisi model-modelnya dengan nama, harga, deskripsi, foto, stock, dan kategori.
5. membuat htmlnya (display seperti apa yang orang akan lihat saat membuka websitenya) masih sangat barebones.
6. migrasi database setelah selesai karena setiap perubahan models.py harus dilanjutkan dengan migrasi.
7. lalu di push ke pws dan github yang sudah di-connect.

urls.py menerima request clientnya, lalu views.py mengambil data dari model dalam models.py, dan merender template akhirnya.
lalu html mengambil code yang dikasih dan di-tampilkan kedalam website akhirnya.

peran settings.py adalah untuk menentukan hal-hal seperti
- installed_apps: daftar app yang aktif dalam proyek ini
- databases: konfig koneksi database
- allowed_hosts: host url yang boleh membuka hasil proyek djangonya.
tanpa settings.py maka django tidak akan tahu bagaimana aplikasi berjalan.

cara kerja migrasi database di Django adalah misal saat kita mengubah models.py, django itu tidak langsung mengubah seluruh databasenya.
lalu, perintah makemigrations itu membuat file migrasi, dan perintah migrate membuat file itu di migrasi ke dalam database.

menurut saya, django cukup mudah untuk dipahami, apalagi dengan adanya tutorial yang sangat membantu dalam cara kerja django
