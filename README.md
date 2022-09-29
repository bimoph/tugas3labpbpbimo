-  Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?
Middleware CSRF dan tag template memberikan perlindungan yang mudah digunakan terhadap Pemalsuan Permintaan Lintas Situs. Jenis serangan ini terjadi ketika situs web berbahaya berisi tautan, tombol formulir, atau beberapa JavaScript yang dimaksudkan untuk melakukan beberapa tindakan di situs web Anda, menggunakan kredensial pengguna yang masuk yang mengunjungi situs jahat di browser mereka. Jenis serangan terkait, 'login CSRF', di mana situs penyerang menipu browser pengguna untuk masuk ke situs dengan kredensial orang lain, juga tercakup.


-  Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.
Bisa, gambarannya menggunakan html, form dari html tersebut di assign/dimasukkan ke model.


-  Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
Data di input oleh user dari form. lalu data tersebut diproses oleh fungsi di views untuk di masukkan ke dalam model. lalu data dari user dalam bentuk model masuk ke database. untuk menampilkan, views meminta data dari database dalam bentuk model lalu memberinya ke templat html.


-  Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
membuat app, membuat model sesuai ketentuan, mengimplementasikan login management menggunakan package/library yang sudah digunakan oleh django. membuat halaman menggunakan html dan membuat forms untuk model Task menggunakan generator django. halaman-halaman tersebut diberi url dan fungsi views.