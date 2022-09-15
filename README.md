
Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html. 

-> https://drive.google.com/file/d/1zg8kLgU8Ro_dN_HwNyfRsCeB5OQcQyHE/view?usp=sharing
-> 
views.py
Bagian ini menambahkan variabel baru seperti nama, NPM, dan item yang akan dimunculkan datanya pada katalog.html.. 

urls.py
Bagian ini dilakukannya routing sehingga yang terdapat pada katalog.html dapat dilihat pada tampilan browser.

katalog.HTML
Bagian ini menggunakan for loop untuk pengambilan data yang sebelumnya sudah dituliskan pada urls.py.

deploy
Bagian ini menghubungkan antara aplikasi heroku dengan github dengan menuliskan action secret HEROKU_APP_NAME dan HEROKU_API_KEY.

Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.

-> Yang pertama melakukan loaddata json ke dalam database django. Lalu, melakukan load data ke dalam models. Models diproses melalui views untuk dikirim ke template (berkas html). Nantinya, user akan membuka web sesuai route yang telah di atur oleh urls.py.

Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

-> Aplikasi web berbasis Django tanpa menggunakan virtual environment bisa saja dilakukan, namun kegunaan-kegunaan dari venv itu sendiri seperti supaya konsisten jika ada perpindahan device, dependencies tidak tercampur, dan package lebih terorganisir.



