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

TUGAS 4

authenticationform adalah form bawaan django untuk melakukan proses login, memiliki field username dan password, ada authenticate() untuk mengecek kredensial; ada juga form.get_user() untuk mengambil user, dan pada umumnya digunakan dengan form bawaan lain seperti login, dan logout.
kelebihan dari menggunakan authenticationform adalah karena ini bawaan django, maka mekanismenya secure, selain itu, lebih mudah digunakan dibandingkan memulai dari nol
kekurangan dari menggunakan authenticationform adalah tidak bisa menggunakan email untuk login, dan susah jika ada login khusus (ex: sso) tanpa di-modifikasi

authenticate() (memeriksa kredensial via authentication backends) dan login() (menetapkan user ke session).
otorisasi lebih untuk mengecek apakah perlu login jika ingin melakukan sesuatu (@login_required)


session (server-side) — contoh: DB, cache (Redis), cached_db
Kelebihan
Data sensitif disimpan di server (lebih aman).
Mudah invalidasi (server-side logout atau hapus session).
Ukuran data tidak dibatasi ketat seperti cookie.
Kekurangan
Butuh penyimpanan server (skalabilitas: butuh shared store seperti Redis ketika ada banyak instance).

Cookies (client-side storage)
Kelebihan
Stateless server (skala horizontal lebih mudah).
Cepat, tidak perlu lookup server untuk data kecil.
Kekurangan
Rentan terhadap XSS (jika cookie dapat diakses oleh JS) dan manipulasi.
Sulit untuk melakukan revocation (mencabut akses) kecuali ada mekanisme server-side tambahan


Risiko utama:
XSS (Cross-Site Scripting): attacker dapat baca cookie kalau cookie tidak HttpOnly.
CSRF (Cross-Site Request Forgery): attacker bisa mengirim request dari domain lain yang menyertakan cookie login.
Man-in-the-Middle: jika tidak memakai HTTPS, cookie bisa dicuri.
Cookie tampering: jika tidak signed/encrypted, user bisa memodifikasi isi cookie.
Django menyediakan / merekomendasikan mitigasi:
Session server-side (django.contrib.sessions) — aplikasi tidak menyimpan data sensitif di cookie; cookie hanya menyimpan session id.
CSRF protection via CsrfViewMiddleware + {% csrf_token %} di form; Django mensyaratkan token untuk POST/unsafe methods.

pertama dimulai dengan menambahkan register, login user, logout user kedalam urls, lalu masukkan path untuk register, login dan logout
lalu menambahkan model baru dalam product class dengan nama user, digunakan sebagai untuk mendapatkan nama user yang sedang dalam web
lalu, tambahkan otorisasi dalam showmain, showproduct dimana perlu login sebelumnya
buat register, login dan logout methods dalam views.py
buat 2 file html baru, satu untuk login dan satu untuk register
ubah main html agar bisa mengecek artikel siapakah yang kita sedang baca, juga last login dan login logout
dalam product detail, tambahkan author name, dan apabila tidak ada dibuat anonymous
commit ke github dan pws
semua implementasi sudah selesai, lanjut dengan membuat dua user dan 3 dummy info dalam websitenya

TUGAS 5

pertama, ada yang namanya !important. ini seperti sebuah perintah mutlak yang tidak bisa diganggu gugat. kalau ada aturan yang ditandai dengan ini, misalnya p { color: blue !important; }, maka aturan ini akan mengalahkan semua aturan lain yang mungkin ada, tidak peduli seberapa spesifik aturan lainnya.
kedua, ada inline css. ini adalah instruksi yang kita tulis langsung di dalam tag html itu sendiri, lewat atribut style. 
ketiga, ada id selector. setiap elemen idealnya hanya punya satu id unik, seperti nomor ktp. jadi, kalau kita menargetkan sebuah id, browser menganggap ini perintah yang sangat spesifik karena hanya menunjuk ke satu elemen saja.
keempat, ada sekelompok selector yang punya kekuatan setara. ini adalah class (.highlight), dan juga pseudo-class karena satu class bisa dipakai oleh banyak elemen, kekuatannya ada di bawah id.
terakhir, yang paling lemah adalah selektor elemen. ini adalah ketika kita menargetkan semua elemen dengan tag html tertentu, misalnya semua p atau semua h1. karena ini sangat umum dan tidak spesifik, kekuatannya paling rendah.
kalau ada dua aturan yang tingkat spesifisitasnya sama persis, maka yang akan menang adalah aturan yang ditulis paling bawah atau paling akhir di dalam file css.

cara kita mengakses internet sudah berubah total. dulu, hampir semua orang membuka website dari komputer. sekarang, mayoritas traffic internet datang dari ponsel. bayangkan membuka sebuah website di ponsel tapi tulisannya kecil sekali sampai harus dicubit-cubit untuk zoom, lalu harus geser-geser layar ke kanan dan kiri hanya untuk membaca satu kalimat. pengalaman seperti itu akan membuat pengunjung langsung menutup website kita dan tidak akan pernah kembali lagi.
desain yang responsif itu soal user experience. ini tentang memberikan kemudahan. di layar kecil, menu navigasi yang tadinya melebar bisa disembunyikan di dalam sebuah ikon "hamburger" (tiga garis) untuk menghemat tempat. layout yang tadinya tiga kolom di desktop bisa diubah menjadi satu kolom vertikal yang enak untuk di-scroll. ini membuat pengguna merasa nyaman dan dihargai.

padding itu adalah ruang kosong antara lukisan (konten) dan bingkainya (border). ini seperti karton putih yang sering ada di sekeliling foto di dalam bingkai. fungsinya untuk memberikan "ruang bernapas" bagi konten di dalamnya. kalau kita punya tombol dengan teks, padding akan membuat teks itu tidak mepet ke pinggiran tombol.
border adalah bingkainya itu sendiri. ini adalah garis yang terlihat yang mengelilingi konten dan padding. kita bisa atur ketebalannya, warnanya, dan gayanya.
margin adalah jarak dari bingkai lukisan kita ke bingkai lukisan lain yang ada di dinding. ini adalah ruang kosong di luar elemen. fungsinya untuk memberikan jarak antar elemen, supaya mereka tidak saling menempel dan terlihat berantakan.

flexbox itu paling jago untuk mengatur hal-hal dalam satu dimensi. kita ingin semua link menu (home, add product, login) berjejer rapi secara horizontal. flexbox adalah alat yang cocok untuk itu, alat itu bisa dengan mudah mengatur jarak di antara mereka, atau membuatnya rata kanan, kiri, atau tengah.
grid memungkinkan kita untuk mengontrol baris dan kolom secara bersamaan. ini sangat bagus untuk merancang layout halaman secara keseluruhan. 

pertama, aku ambil halaman register.html dan login.html yang masih sederhana, lalu aku memikirkan tentang visi desain. kita sepakat untuk tema gelap yang modern, dan akhirnya rombak total kedua halaman itu menggunakan tailwind css. pastikan setiap input field, tombol, dan pesan error terlihat serasi dengan tema premium yang diinginkan, sesuatu yang tutorial lakukan di tahap akhir, tapi aku prioritaskan di awal untuk menetapkan nuansa aplikasi.
aku mengimplementasikan fungsi edit_product dan delete_product di views.py dan urls.py. tapi, aku terjebak pada error reverse for 'show_product' not found. melalui serangkaian percakapan, aku belajar bersama tentang pentingnya app_name, perbedaan antara id dan pk, dan bagaimana semua bagian (template, url, dan view) harus sinkron. ini adalah pengalaman belajar yang jauh lebih mendalam daripada sekadar mengikuti instruksi.
memutuskan untuk membuat rebranding total dari "toko funko pop" menjadi "marketplace lifestyle pemain bola" dengan tema gelap yang keren. pemilihan font "inter" dari google fonts, penggunaan warna aksen biru, hingga desain card yang minimalis

TUGAS 6


perbedaan antara synchronous dan asynchronous request
perbedaan utamanya adalah cara browser menangani waktu tunggu.

synchronous request (permintaan sinkron)
ini adalah cara kerja web tradisional. saat anda mengklik link, browser mengirim permintaan, lalu berhenti total dan menunggu sampai server mengirim kembali seluruh halaman html yang baru. selama menunggu, halaman akan membeku. setelah respons diterima, seluruh halaman akan dimuat ulang.

asynchronous request (permintaan asinkron)
ini adalah cara kerja ajax. saat sebuah aksi terjadi, javascript mengirim permintaan ke server di latar belakang. pengguna bisa terus berinteraksi dengan halaman tanpa gangguan. saat server mengirimkan kembali data kecil (biasanya json), javascript akan memperbarui hanya bagian kecil dari halaman yang relevan tanpa perlu memuat ulang seluruhnya.


bagaimana ajax bekerja di django (alur request–response)
alur kerja ajax di django melibatkan komunikasi antara javascript di front-end dan sebuah view khusus di back-end.

trigger (front-end): pengguna melakukan aksi (misalnya, klik tombol) yang memicu sebuah fungsi javascript.

request (front-end): fungsi javascript (menggunakan fetch() api) mengirimkan request ke sebuah url spesifik di django, seringkali membawa data dari form.

url routing (django): urls.py django menerima url tersebut dan mengarahkannya ke sebuah view function.

view processing (django): view function di views.py menerima request, memproses data, dan berinteraksi dengan database.

response (django): view tidak me-render seluruh template html. sebaliknya, view mengembalikan data dalam format ringan, paling umum menggunakan jsonresponse.

dom manipulation (front-end): javascript menggunakan data dari json tersebut untuk memperbarui halaman html (dom) secara langsung, misalnya mengubah angka jumlah suka tanpa me-reload halaman.

keuntungan menggunakan ajax dibandingkan render biasa
pengalaman pengguna (ux) yang lebih baik: interaksi terasa lebih mulus dan cepat, mirip aplikasi desktop, karena tidak ada kedipan layar putih saat halaman dimuat ulang.

mengurangi beban server & bandwidth: ajax hanya mengirim dan menerima data yang diperlukan, bukan seluruh file html. ini membuat transfer data lebih efisien.

peningkatan performa: karena data yang ditransfer lebih kecil dan halaman tidak dimuat ulang sepenuhnya, website terasa jauh lebih cepat.

perbedaan antara synchronous dan asynchronous request
perbedaan utamanya adalah cara browser menangani waktu tunggu.

synchronous request (permintaan sinkron)
ini adalah cara kerja web tradisional. saat anda mengklik link, browser mengirim permintaan, lalu berhenti total dan menunggu sampai server mengirim kembali seluruh halaman html yang baru. selama menunggu, halaman akan membeku. setelah respons diterima, seluruh halaman akan dimuat ulang.

asynchronous request (permintaan asinkron)
ini adalah cara kerja ajax. saat sebuah aksi terjadi, javascript mengirim permintaan ke server di latar belakang. pengguna bisa terus berinteraksi dengan halaman tanpa gangguan. saat server mengirimkan kembali data kecil (biasanya json), javascript akan memperbarui hanya bagian kecil dari halaman yang relevan tanpa perlu memuat ulang seluruhnya.


bagaimana ajax bekerja di django (alur request–response)
alur kerja ajax di django melibatkan komunikasi antara javascript di front-end dan sebuah view khusus di back-end.

trigger (front-end): pengguna melakukan aksi (misalnya, klik tombol) yang memicu sebuah fungsi javascript.

request (front-end): fungsi javascript (menggunakan fetch() api) mengirimkan request ke sebuah url spesifik di django, seringkali membawa data dari form.

url routing (django): urls.py django menerima url tersebut dan mengarahkannya ke sebuah view function.

view processing (django): view function di views.py menerima request, memproses data, dan berinteraksi dengan database.

response (django): view tidak me-render seluruh template html. sebaliknya, view mengembalikan data dalam format ringan, paling umum menggunakan jsonresponse.

dom manipulation (front-end): javascript menggunakan data dari json tersebut untuk memperbarui halaman html (dom) secara langsung, misalnya mengubah angka jumlah suka tanpa me-reload halaman.


keuntungan menggunakan ajax dibandingkan render biasa
pengalaman pengguna (ux) yang lebih baik: interaksi terasa lebih mulus dan cepat, mirip aplikasi desktop, karena tidak ada kedipan layar putih saat halaman dimuat ulang.

mengurangi beban server & bandwidth: ajax hanya mengirim dan menerima data yang diperlukan, bukan seluruh file html. ini membuat transfer data lebih efisien.

peningkatan performa: karena data yang ditransfer lebih kecil dan halaman tidak dimuat ulang sepenuhnya, website terasa jauh lebih cepat.

interaksi yang kompleks: memungkinkan pembuatan fitur dinamis seperti infinite scroll, live search, atau validasi form secara real-time.


keamanan ajax untuk fitur login dan register
menggunakan ajax tidak mengurangi keamanan. semua fitur keamanan standar django tetap harus diterapkan.

csrf protection: semua request post melalui ajax harus menyertakan csrf token. javascript harus membaca token ini dari halaman dan mengirimkannya dalam request header.

gunakan decorators django: lindungi view ajax anda sama seperti view biasa. gunakan @login_required untuk memastikan hanya pengguna yang sudah login yang bisa mengaksesnya.

validasi di sisi server: jangan pernah percaya data yang dikirim dari front-end. selalu validasi semua input menggunakan django forms untuk melindungi dari serangan seperti sql injection.

pengaruh ajax pada pengalaman pengguna (user experience)
pengguna mendapatkan respons langsung atas tindakan mereka. contoh: pesan "username sudah terpakai" bisa muncul seketika tanpa harus mengirim form dan menunggu halaman dimuat ulang.
