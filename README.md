TUGAS 2

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

TUGAS 3

menurut saya, data delivery sangat penting dalam implementasi platform karena:
- komunikasi antara backend, database, api, dan frontend sangat penting dan perlu dilakukan
- platform sering menggunakanan layanan eksternal seperti API pihak ketiga, cloud, dan yang lain
- memiliki scalability yang sangat bagus dengan data delivery yang baik
- update secara real time sudah menjadi norma, sehingga perlu mekanisme untuk mengirim data real time
dan yang menurut saya paling penting,
- platform compatibility, agar no matter desktop, mobile, or other platforms, data delivery memungkinkan platform web bekerja

menurut saya, json lebih baik karena syntax yang lebih sederhana untuk dibaca, ukuran file yang pada umumnya lebih kecil, dan lebih mudah untuk di parse dengan bahasa-bahasa pemograman, apalagi javascript
json lebih populer karena itu merupakan bagian dari native javascript support dan ecosystem, dan developer lebih suka format yang simple dan tidak all over the place

is_valid() berarti di-validasi apakah data yang diinput sesuai aturan yang ditetapkan dalam formnya, selain itu juga digunakan untuk mencegah input berbahaya yang dapat crash website or worse

CSRF token dibutuhkan sebagai mekanisme keamanan untuk mencegah serangan user melakukan aksi yang tidak diinginkan dengan generate unique token untuk setiap sesi, dan saat form di submit django verify dulu apakah token yang digunakan valid or not. jika tidak, maka request ditolak.
jika tidak menggunakan CSRF token, false inputs lebih gampang untuk dilakukan, dan dapat merugikan pengguna lain dalam platform. penyerang dapat melakukan hidden forms, or automatic submission yang dapat menghasilkan sensitive information dari korban

pertama dimulai dengan menambahkan 4 fungsi baru di views.py untuk melihat format XML,JSON, XML by ID, and JSON by ID
lalu dibuat routing untuk setiap views didalam url.py
setelah itu, membuat base.html untuk meliputi file html yang akan dibuat, yaitu create_product.html dan product_detail.html
setelah itu, ubah main.html untuk menambahkan tombol add yang akan meroute web ke dalam create_product, dimana create product adalah page yang digunakan untuk menambahkan product baru.
ubah settings.py untuk menambahkan web pws dalam CSRF
tambah base_dir and templates dalam 'DIRS' agar bisa membuka page selain main.html
bikin function show dan create product dalam views yang gunanya untuk merender new products being made and get more detail juga
finishing touches seperti merapihkan html, memastikan routing new products and product sudah dibuat
lalu commit ke pws dan ke github dan tugas 3 sudah dianggap selesai

tugas 3 merupakan tugas yang sangat seru, mudah dipahami juga karena tutorial sangat terstruktur dan lengkap, penjelasan tentang Django didalamnya juga komprehensif, dan step-by-step implementation tugas jelas

