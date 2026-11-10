# Senja yang Tidak Selesai
# Visual novel dewasa 18+ | Seluruh tokoh utama berusia 21 tahun ke atas.
# Tidak memerlukan aset eksternal; latar berwarna dibuat dengan Solid agar langsung bisa dijalankan.

# --- Identitas visual ---
image bg apartment = Solid("#302b35")
image bg kitchen = Solid("#39313a")
image bg campus = Solid("#293840")
image bg cafe = Solid("#493a36")
image bg office = Solid("#303743")
image bg rooftop = Solid("#38424b")
image bg rain = Solid("#202d38")
image bg dawn = Solid("#514343")

# --- Tokoh ---
default niko = 0
default nara = 0
default satria = 0
default mira = 0
default trust = 0
default selfcare = 0
default chapter = 0
default quick_menu = True

define p = Character("Aku", color="#e7c7a6")
define n = Character("Nara", color="#e9b9c9")
define s = Character("Satria", color="#a9cee0")
define m = Character("Mira", color="#e7c98e")
define d = Character("Dimas", color="#b4d2b7")
define narrator = Character(None)

# Panel ringkas untuk konteks adegan. Simpan/load tetap memakai sistem standar Ren'Py.
screen chapter_stamp(title, subtitle):
    zorder 20
    frame:
        xalign 0.03
        yalign 0.06
        padding (18, 12)
        background "#101319bb"
        vbox:
            spacing 3
            text title size 22 color "#f4dfc7"
            text subtitle size 13 color "#c2c1c5"

screen relationship_hud():
    zorder 15
    frame:
        xalign 0.98
        yalign 0.04
        padding (12, 8)
        background "#101319aa"
        vbox:
            text "Kedekatan" size 15 color "#f4dfc7"
            text "Nara [nara]  ·  Satria [satria]  ·  Mira [mira]" size 12 color "#dedde0"

label start:
    $ niko = 0
    $ nara = 0
    $ satria = 0
    $ mira = 0
    $ trust = 0
    $ selfcare = 0
    $ chapter = 0
    scene bg apartment with fade
    show screen chapter_stamp("SENJA YANG TIDAK SELESAI", "Bandung · cerita dewasa tentang batas, kehilangan, dan pilihan")
    narrator "Semua tokoh dalam cerita ini berusia 21 tahun ke atas. Kedekatan dibangun lewat pilihan yang saling menghormati; adegan intim ditulis secara sensual, tanpa gambaran grafis."
    narrator "Bandung, akhir musim hujan. Aku berusia dua puluh tujuh tahun, baru pindah ke apartemen kecil dekat kampus untuk menyelesaikan tesis yang tertunda dan bekerja lepas sebagai penyunting."
    narrator "Sudah enam bulan sejak hubungan panjangku berakhir. Aku menyebut diriku baik-baik saja karena kalimat itu lebih mudah daripada menjelaskan kenapa suara notifikasi masih membuat dadaku mengencang."
    narrator "Di luar, hujan merapikan kota menjadi pantulan lampu. Di dalam, tiga nama mulai muncul di hari-hariku—dengan cara yang tidak pernah terasa sederhana."
    hide screen chapter_stamp
    call character_notes
    jump act_one

label character_notes:
    scene bg apartment with dissolve
    narrator "CATATAN TOKOH · Semua orang dewasa, dengan hidup dan batas masing-masing."
    narrator "Aku / Niko, 27. Rambut hitam selalu sedikit berantakan, kemeja lengan digulung, kebiasaan menunda makan saat tenggelam dalam pekerjaan. Anak pertama keluarga perantau; ingin menyelesaikan tesis tanpa menjadikan pencapaian sebagai satu-satunya alasan untuk merasa berharga."
    narrator "Nara, 25. Mahasiswi pascasarjana arsitektur, rambut sebahu, membawa pensil di sanggulnya dan menghafal rute bus. Terbiasa merawat semua orang setelah tumbuh di keluarga yang komunikasinya penuh diam. Ingin merancang ruang komunitas, tetapi belajar bahwa perhatian bukan kewajiban untuk menyelamatkan siapa pun."
    narrator "Satria, 29. Fotografer dokumenter lepas, tubuh tinggi, jaket denim pudar, selalu memotret sebelum menyentuh kopi. Pernah kehilangan pekerjaan tetap dan masih takut bergantung pada orang lain. Ingin membuat proyek tentang kota yang berubah tanpa menjadikan kesedihan orang sebagai komoditas."
    narrator "Mira, 32. Editor di penerbit kecil tempatku mengambil kontrak, rambut pendek rapi, jam tangan tua, dan kebiasaan menandai naskah dengan pensil merah. Perceraian mengajarinya menyamakan kendali dengan keamanan. Ingin menerbitkan buku yang jujur, sambil berlatih menjadi dekat tanpa memakai jabatan atau pengalaman sebagai alat tekan."
    narrator "Dimas, 28. Teman sekamar lama Niko yang kini bekerja sebagai konselor sebaya kampus. Tawa mudah, botol minum penuh stiker; percaya meminta bantuan adalah keterampilan, bukan kegagalan."
    return

label act_one:
    $ chapter = 1
    scene bg campus with dissolve
    show screen chapter_stamp("BAB 1 · RUANG YANG KITA HUNI", "Kampus · Selasa, 16.20")
    show screen relationship_hud
    narrator "Aku datang ke kampus untuk mengembalikan buku, lalu mendapati hujan memerangkap semua orang di selasar perpustakaan. Di meja dekat jendela, Nara menggambar denah kecil di balik struk makan."
    n "Kalau kamu mau lewat, tunggu dua menit. Ini bukan denah gedung. Ini denah tempat yang bikin orang betah duduk tanpa merasa diawasi."
    p "Kamu menggambar tempat yang belum ada?"
    n "Aku menggambar sesuatu yang seharusnya ada. Ada bedanya."
    narrator "Ia mengatakan itu tanpa menatapku. Bukan dingin; hanya sedang menjaga garis tipis antara berbagi ide dan membiarkan orang lain memilikinya."
    n "Kamu kelihatan seperti orang yang datang untuk meminjam buku dan pulang membawa masalah baru."
    p "Kebiasaan buruk. Aku sedang memperbaiki tesis."
    n "Aku juga sedang memperbaiki sesuatu. Mungkin tesis, mungkin cara bilang tidak."
    narrator "Di sisi lain halaman, Satria memotret genangan air yang memantulkan papan pengumuman. Kami pernah berbagi lift; percakapan kami biasanya berhenti di lantai masing-masing."
    s "Boleh aku tanya? Kamu lebih suka foto yang menunjukkan tempatnya, atau foto yang menunjukkan orang pernah ada di sana?"
    p "Pertanyaan yang aneh untuk orang yang sedang memotret lantai."
    s "Aku fotografer. Pertanyaanku memang sering terdengar seperti pembelaan diri."
    narrator "Ponselku bergetar. Pesan dari Mira: 'Naskahmu bagus. Besok kita bahas revisi dan kontrak. Jangan lembur demi membuktikan sesuatu.'"
    narrator "Perhatian kecil seharusnya terasa sederhana. Entah kenapa, belakangan ini aku selalu mencari harga yang harus dibayar sesudahnya."
    menu:
        "Tetap bersama Nara dan bertanya tentang proyek ruang komunitas.":
            $ nara += 2
            $ trust += 1
            n "Tempat yang orang boleh diam tanpa harus menjelaskan kenapa, itu terlalu mewah?"
            p "Tidak. Tapi mungkin sulit dibangun kalau semua orang mengira diam berarti tidak butuh siapa-siapa."
            n "Kamu terdengar seperti pernah salah paham soal itu."
            p "Aku masih belajar membedakannya."
        "Minta Satria menunjukkan hasil fotonya, lalu dengarkan ceritanya.":
            $ satria += 2
            $ trust += 1
            s "Yang ini bekas toko buku. Pemiliknya pindah, tapi orang-orang masih duduk di tangga seolah tokonya akan buka lagi."
            p "Kamu memotret mereka?"
            s "Tidak tanpa izin. Kehilangan bukan berarti orang kehilangan hak atas wajahnya."
            narrator "Ia menunjukkan satu foto kosong. Entah bagaimana, ruang kosong itu terasa ramai."
        "Balas Mira: aku akan datang, tapi tak perlu membahasnya setelah jam kerja.":
            $ mira += 2
            $ trust += 1
            p "Aku datang besok. Kita bahas di jam kerja saja. Dan terima kasih sudah mengingatkan soal lembur."
            narrator "Tanda mengetik muncul, hilang, muncul lagi."
            m "Diterima. Batas yang jelas membuat percakapan lebih mudah, bukan lebih dingin. Sampai besok, Niko."
        "Pulang sendiri dan beri diriku malam tanpa harus menyenangkan siapa pun.":
            $ selfcare += 2
            $ niko += 1
            narrator "Aku menutup buku, mematikan notifikasi, lalu berjalan pulang di bawah hujan. Kesendirian kali ini tidak terasa seperti hukuman."
            p "Aku boleh lelah tanpa menjadikannya teka-teki untuk orang lain."
    hide screen relationship_hud
    hide screen chapter_stamp
    jump act_two

label act_two:
    $ chapter = 2
    scene bg kitchen with dissolve
    show screen chapter_stamp("BAB 2 · HAL-HAL YANG TIDAK DIUCAPKAN", "Apartemen · Jumat malam")
    show screen relationship_hud
    narrator "Tiga hari kemudian, listrik di apartemenku padam selama dua jam. Dimas datang membawa mi instan, senter, dan ekspresi orang yang tahu ia sedang melakukan intervensi kecil."
    d "Kamu bilang baik-baik saja dengan nada yang biasanya dipakai orang untuk mengakhiri percakapan."
    p "Kamu konselor sebaya, bukan pembaca pikiran."
    d "Betul. Jadi aku bertanya, bukan menyimpulkan. Kamu ingin ditemani, diberi ruang, atau dibantu mencari orang profesional?"
    narrator "Pertanyaan itu terasa lebih sulit daripada seharusnya. Aku memilih menjawabnya dengan jujur."
    menu:
        "Minta Dimas tinggal sebentar. Aku tidak ingin sendirian malam ini.":
            $ trust += 2
            $ niko += 1
            d "Oke. Kita tidak harus membahas apa pun. Aku cuma perlu tahu kamu aman."
            p "Aku aman. Tapi pikiranku ramai."
            d "Kalau berubah, bilang. Dan kita bisa cari konselor kampus besok, tanpa membuatnya jadi keputusan besar malam ini."
        "Minta ruang, tapi sepakati untuk bicara besok.":
            $ selfcare += 1
            $ trust += 1
            p "Aku butuh sendiri dulu. Boleh telepon besok?"
            d "Tentu. Terima kasih sudah bilang jelas. Aku kirim nomor layanan konseling kampus kalau kamu mau."
            narrator "Ia meninggalkan mi di meja dan tidak meminta penjelasan tambahan."
        "Alihkan pembicaraan dengan bercanda; aku belum siap membuka diri.":
            $ niko += 1
            p "Aku hanya ingin memastikan mi ini tidak lebih matang daripada tesis."
            d "Boleh menghindar sebentar. Tapi kalau nanti kamu siap, aku tetap ada."
    scene bg cafe with dissolve
    narrator "Sabtu siang, hujan mereda. Aku bertemu Nara di kedai dekat kampus. Ia menggulung lengan kemeja, menatap orang-orang yang datang dan pergi, bukan layar ponselnya."
    n "Aku sempat berpikir membatalkan. Bukan karena kamu. Aku cuma sedang tidak punya tenaga untuk berpura-pura mudah diajak bicara."
    p "Kita bisa duduk tanpa membuatnya mudah."
    n "Aku suka jawaban itu. Aku juga mau tanya sesuatu. Kamu ingin mengenalku, atau ingin merasa dibutuhkan?"
    narrator "Pertanyaannya tidak menuduh. Itu justru membuatku tak bisa bersembunyi di balik jawaban yang bagus."
    menu:
        "Aku ingin mengenalmu. Aku tidak berharap kamu mengurus perasaanku.":
            $ nara += 2
            $ trust += 2
            p "Aku tertarik padamu. Tapi aku bertanggung jawab atas diriku sendiri, termasuk saat aku sedang berantakan."
            n "Bagus. Aku juga tidak selalu tahu apa yang kubutuhkan. Kita bisa bertanya, bukan menebak."
        "Aku belum yakin, dan tidak mau memberimu janji yang belum kupahami.":
            $ nara += 1
            $ trust += 1
            p "Aku ingin tahu, tapi belum tahu bentuknya. Aku tidak mau menjadikan ketidakpastian sebagai janji."
            n "Kejujuran bukan jawaban yang paling nyaman, tapi biasanya awal yang lebih baik."
        "Aku ingin merasa dibutuhkan. Aku baru menyadarinya sekarang.":
            $ nara -= 1
            $ trust += 1
            $ selfcare += 1
            p "Mungkin sebagian diriku memang mencari itu. Aku tidak mau menaruh beban itu padamu."
            n "Terima kasih sudah melihatnya. Kita bisa tetap bicara, pelan-pelan."
    scene bg rooftop with dissolve
    narrator "Malamnya, Satria mengajakku melihat foto-foto untuk pameran kecil. Atap gedung apartemen dibuka hanya untuk penghuni; kota menyebar di bawah kami seperti sesuatu yang belum selesai ditulis."
    s "Aku ingin menunjukkan foto ini, tapi aku tidak mau menjelaskan terlalu banyak. Rasanya seperti menjual kesedihan orang."
    p "Apa yang kamu butuhkan dariku?"
    s "Temani aku melihatnya. Jangan langsung bilang semua akan baik-baik saja."
    narrator "Ia berdiri cukup dekat hingga bahu kami bersentuhan. Ketika ia tidak menjauh, aku juga tidak buru-buru mengubahnya menjadi sesuatu yang harus diberi nama."
    menu:
        "Tanyakan apakah ia nyaman jika kamu menggenggam tangannya.":
            $ satria += 2
            $ trust += 1
            p "Aku ingin menggenggam tanganmu. Kamu nyaman?"
            s "Ya. Terima kasih sudah bertanya."
            narrator "Tangannya hangat, jemarinya sedikit dingin. Kami berdiri melihat lampu kota, tanpa membuat sentuhan itu menjadi janji."
        "Tetap di sampingnya tanpa menyentuh; biarkan ia menentukan jarak.":
            $ satria += 1
            $ trust += 1
            p "Aku di sini. Tidak perlu bicara kalau belum ingin."
            s "Itu lebih membantu dari yang kamu kira."
        "Tanyakan bagaimana ia akan menjaga privasi orang-orang dalam foto.":
            $ satria += 1
            $ niko += 1
            s "Aku akan minta izin. Kalau mereka menolak, fotonya tidak dipakai. Cerita yang kuat bukan alasan untuk mengambil sesuatu."
            p "Aku senang kamu memikirkan itu."
    scene bg office with dissolve
    narrator "Senin, rapat naskah dengan Mira berlangsung lebih lama daripada jadwal. Ruangan kantor sudah hampir kosong. Ia melepas jam tangannya dan menggosok bekas talinya di pergelangan."
    m "Aku minta maaf kalau pesanku malam itu terasa seperti perintah. Aku atasan kontrakmu, dan itu membuat batas kita penting. Kamu tidak berutang kedekatan karena aku membayar pekerjaanmu."
    p "Aku menghargai kamu mengatakannya. Aku juga ingin tahu: kalau kontrak ini selesai, kamu tetap ingin bertemu?"
    m "Aku ingin. Tapi hanya kalau kamu juga ingin, dan kita bisa menunggu sampai relasi kerja kita selesai."
    narrator "Ada ketertarikan di antara kami, tetapi juga kenyataan tentang kuasa yang tak bisa diselesaikan hanya dengan senyum."
    menu:
        "Sepakati untuk menunggu sampai kontrak selesai; bicarakan lagi dengan jujur.":
            $ mira += 2
            $ trust += 2
            p "Aku tertarik. Aku setuju kita tunggu sampai kontrak selesai dan meninjau ulang tanpa tekanan."
            m "Itu terdengar dewasa. Dan, jujur saja, agak melegakan."
        "Bilang bahwa saat ini kamu ingin menjaga hubungan profesional saja.":
            $ mira += 1
            $ selfcare += 1
            p "Aku menghargai kamu, tapi saat ini aku ingin menjaga batas profesional."
            m "Baik. Terima kasih sudah jelas. Pekerjaan kita tetap dihargai sama."
        "Minta waktu memikirkannya sebelum menjawab.":
            $ trust += 1
            p "Aku belum bisa menjawab malam ini. Aku perlu waktu untuk memikirkannya."
            m "Tentu. Kamu tidak harus memutuskan apa pun sekarang."
    hide screen relationship_hud
    hide screen chapter_stamp
    jump act_three

label act_three:
    $ chapter = 3
    scene bg rain with dissolve
    show screen chapter_stamp("BAB 3 · MEMILIH DENGAN SADAR", "Tiga minggu kemudian · halte kota")
    show screen relationship_hud
    narrator "Tiga minggu berjalan dalam ritme yang tidak dramatis: revisi, makan malam seadanya, pesan yang kadang dibalas terlambat, dan beberapa malam ketika aku akhirnya tidur sebelum tengah malam."
    narrator "Lalu kota memberi kami satu malam yang sama-sama terlalu berat. Pameran Satria ditunda setelah ruangnya terkena banjir. Presentasi proyek Nara ditolak karena pendanaan dipangkas. Penerbit Mira kehilangan naskah andalan."
    narrator "Kami bertemu di kedai yang hampir tutup. Tidak ada yang tampak ingin menjadi orang paling kuat di ruangan itu."
    n "Aku marah, tapi juga malu karena marah. Proyek itu berarti banyak."
    s "Aku ingin menghapus semua foto dan pura-pura tidak pernah memulai."
    m "Aku menghabiskan bertahun-tahun menganggap rencana cadangan sebagai kegagalan. Mungkin malam ini aku lelah berpura-pura."
    narrator "Aku mengenali cara lama diriku: memilih satu orang untuk diselamatkan agar tak perlu menghadapi hidupku sendiri. Kali ini, aku ingin bertanya sebelum bergerak."
    menu:
        "Tawarkan dukungan, lalu tanyakan apa yang mereka butuhkan; jangan mengambil alih.":
            $ trust += 2
            $ niko += 1
            n "Aku butuh didengarkan, bukan strategi dulu."
            s "Aku butuh besok pagi. Malam ini, aku butuh makan sesuatu yang hangat."
            m "Aku perlu tidur. Besok aku bisa lihat opsi penerbitan dengan kepala lebih jernih."
            p "Baik. Kita lakukan satu hal pada satu waktu."
        "Ajak semua orang membuat rencana praktis untuk besok.":
            $ selfcare += 1
            $ trust += 1
            p "Kalau kalian mau, kita tulis pilihan besok. Tidak untuk menyelesaikan semuanya malam ini."
            n "Asal kita boleh berhenti kalau mulai terasa seperti rapat."
            s "Setuju. Dan pesan makanan dulu."
            m "Sebuah rencana yang mengizinkan istirahat. Aku suka itu."
        "Mengaku bahwa kamu tidak mampu menanggung masalah semua orang.":
            $ selfcare += 2
            $ trust += 1
            p "Aku peduli, tapi aku tidak bisa menanggung semua ini untuk kalian. Aku bisa menemani, bukan memperbaiki semuanya."
            n "Itu batas yang sehat. Aku juga tidak mau menjadikanmu tempat pembuangan semua takutku."
            s "Kita semua boleh jadi manusia biasa malam ini."
    scene bg apartment with dissolve
    narrator "Beberapa hari kemudian, aku berdiri di balkon apartemen saat senja. Satu pesan baru masuk dari orang yang paling dekat denganku selama cerita ini. Tidak ada angka yang bisa menggantikan percakapan; keputusan tetap milikku."
    narrator "Aku menimbang rasa tertarik, rasa aman, dan hal yang paling sering kulupakan: apakah aku bisa hadir sebagai diriku sendiri?"
    menu:
        "Aku ingin mengenal Nara lebih jauh, perlahan dan tanpa saling menyelamatkan.":
            $ nara += 1
            $ choice = "nara"
        "Aku ingin mencoba hubungan dengan Satria, dengan ruang untuk jujur dan berubah pikiran.":
            $ satria += 1
            $ choice = "satria"
        "Aku ingin menunggu kontrak selesai, lalu bertemu Mira setara sebagai dua orang dewasa.":
            $ mira += 1
            $ choice = "mira"
        "Untuk saat ini, aku memilih diriku sendiri dan hubungan yang tidak romantis.":
            $ selfcare += 2
            $ choice = "alone"
    hide screen relationship_hud
    hide screen chapter_stamp
    jump ending_check

label ending_check:
    if choice == "nara" and nara >= 3 and trust >= 3:
        jump ending_nara
    elif choice == "satria" and satria >= 3 and trust >= 2:
        jump ending_satria
    elif choice == "mira" and mira >= 3 and trust >= 3:
        jump ending_mira
    elif choice == "nara":
        jump ending_nara_slow
    elif choice == "satria":
        jump ending_satria_slow
    elif choice == "mira":
        jump ending_mira_slow
    else:
        jump ending_self

label ending_nara:
    scene bg dawn with dissolve
    show screen chapter_stamp("ENDING · RUANG UNTUK DUA ORANG", "Nara · akhir musim hujan")
    narrator "Nara mengirim pesan dua hari kemudian: 'Aku ingin berjalan ke lokasi proyek lamaku. Bukan untuk membicarakan solusi. Mau ikut?'"
    narrator "Kami berjalan menyusuri gang yang akan berubah menjadi ruang komunitas kecil. Ia bercerita tentang ibunya, tentang kebiasaan meminta maaf sebelum meminta bantuan, tentang ketakutannya mengulang pola keluarga. Aku bercerita tentang cara diamku sendiri pernah berubah menjadi hukuman."
    n "Aku ingin mencoba ini. Bukan karena kamu bisa membuatku lebih mudah. Karena di dekatmu, aku tidak harus menjadi orang yang selalu tahu arah."
    p "Aku juga ingin mencoba. Pelan-pelan, dan kita tetap boleh berkata tidak."
    n "Terutama kalau kita lupa bertanya."
    narrator "Ia menyentuh punggung tanganku, berhenti sejenak, lalu menatapku. Aku mengangguk. Ciuman kami singkat, lembut, dan terasa seperti pertanyaan yang dijawab bersama."
    narrator "Malam itu berakhir dengan teh di dapurku dan bahu yang bersandar tanpa tuntutan. Ada kehangatan, ada keinginan, ada pintu yang sengaja kami biarkan tetap terbuka untuk kata 'cukup'."
    narrator "Keesokan paginya, hidup tetap meminta banyak hal. Tetapi kini, kami mulai belajar bahwa kedekatan bukan berarti kehilangan ruang."
    jump credits

label ending_satria:
    scene bg rooftop with dissolve
    show screen chapter_stamp("ENDING · CAHAYA YANG TIDAK DIMILIKI", "Satria · malam pembukaan pameran")
    narrator "Pameran Satria akhirnya berlangsung di sebuah ruang kecil. Foto-foto yang dipilihnya tidak menjadikan kehilangan sebagai tontonan. Di bawah setiap gambar, ada nama dan persetujuan orang yang bersedia bercerita."
    s "Aku dulu kira kalau seseorang melihat bagian paling rapuhku, dia akan tahu cara memperbaikinya. Sekarang aku lebih suka kalau dia bertanya apakah aku ingin ditemani."
    p "Aku bisa melakukan itu. Dan kalau aku lupa, bilang padaku."
    s "Bisa. Tapi jangan jadikan aku satu-satunya tempat kamu pulang. Aku ingin menjadi bagian hidupmu, bukan seluruh hidupmu."
    narrator "Di atap selepas pameran, ia bertanya sebelum mendekat. Aku menjawab dengan menautkan jemari kami. Ciuman itu membawa sisa gugup, kopi dingin, dan sesuatu yang tidak perlu diburu."
    narrator "Kami menghabiskan malam dengan bicara sampai kota mulai sepi. Sentuhan yang lebih intim berhenti ketika salah satu dari kami mengatakannya; tidak ada yang berubah menjadi marah atau menjauh."
    narrator "Pagi datang tanpa janji bahwa semuanya mudah. Hanya dua orang yang bersedia tetap jujur, bahkan saat cerita mereka belum selesai."
    jump credits

label ending_mira:
    scene bg cafe with dissolve
    show screen chapter_stamp("ENDING · SETARA", "Mira · setelah kontrak berakhir")
    narrator "Kontrakku selesai pada akhir bulan. Kami menunggu satu minggu lagi, membiarkan angka di rekening dan tanda tangan terakhir menjadi benar-benar masa lalu. Lalu Mira mengirim pesan: 'Kopi? Kali ini tanpa naskah.'"
    m "Aku sudah terbiasa memegang kendali. Kadang aku masih mengira itu sama dengan menjaga semua orang tetap aman. Aku tidak ingin melakukan itu padamu."
    p "Aku juga tidak ingin menyamarkan ketertarikan sebagai kewajiban atau rasa terima kasih."
    m "Bagus. Kalau nanti ada yang terasa tidak seimbang, kita bicarakan. Kalau kamu berubah pikiran, kamu boleh mengatakannya."
    narrator "Di luar kedai, ia bertanya apakah boleh menggenggam tanganku. Aku menjawab ya. Senyumnya kali ini tak seperti editor yang menemukan kalimat tepat; lebih seperti seseorang yang tidak perlu menguasai akhir cerita."
    narrator "Malam kami berakhir dengan ciuman pelan di depan pintu apartemen dan janji untuk bertemu lagi, bukan janji bahwa kami akan selalu tahu caranya."
    narrator "Beberapa awal yang dewasa tidak terasa seperti terjun bebas. Kadang ia terasa seperti dua orang yang memeriksa pijakan sebelum melangkah."
    jump credits

label ending_nara_slow:
    scene bg campus with dissolve
    show screen chapter_stamp("ENDING · JALAN YANG TETAP TERBUKA", "Nara · beberapa minggu kemudian")
    n "Aku senang kamu jujur ingin mencoba. Tapi aku belum merasa cukup aman untuk menyebut ini hubungan. Aku ingin kita tetap berteman dan tidak memaksa kedekatan."
    p "Aku mengerti. Aku juga perlu belajar hadir tanpa menganggap perhatian sebagai janji."
    narrator "Kami berjalan pulang bersama, lalu berpisah di persimpangan. Ada kecewa, tetapi tidak ada yang berutang akhir bahagia kepada siapa pun."
    narrator "Belakangan, Nara mengirim foto ruang komunitas yang sedang ia rancang. Aku membalas dengan selamat, bukan dengan tuntutan untuk masuk ke dalam hidupnya."
    jump credits

label ending_satria_slow:
    scene bg rooftop with dissolve
    show screen chapter_stamp("ENDING · TANPA MEMAKSA FOKUS", "Satria · selepas hujan")
    s "Aku suka kamu. Tapi aku belum punya kapasitas untuk hubungan sekarang. Aku perlu tahu kita bisa berhenti di sini tanpa saling menghukum."
    p "Bisa. Aku memang ingin mencoba, tapi keinginan bukan alasan untuk mendesakmu."
    narrator "Kami menatap lampu kota dalam diam. Rasanya bukan seperti kehilangan sesuatu yang sudah menjadi milikku. Rasanya seperti menerima jawaban dari seseorang yang berhak memilih."
    narrator "Satria mengirim satu foto kosong beberapa minggu setelahnya. Aku menyimpannya bukan sebagai kode, hanya sebagai foto bagus."
    jump credits

label ending_mira_slow:
    scene bg office with dissolve
    show screen chapter_stamp("ENDING · BATAS YANG MENJAGA", "Mira · setelah kontrak")
    m "Aku senang kita menunggu. Tapi setelah punya waktu berpikir, aku ingin menjaga hubungan profesional dan pertemanan saja. Aku tidak mau rasa bersalah atau kebiasaan lama menentukan jawabanku."
    p "Terima kasih sudah bilang. Aku menghargai kejelasan itu."
    narrator "Ada sedikit canggung saat kami bertemu lagi, lalu berkurang. Mira tetap merekomendasikan tulisanku dengan alasan yang sama seperti dulu: karena tulisannya layak."
    narrator "Kadang bentuk paling dewasa dari kedekatan adalah tidak mengubah sebuah batas menjadi tawar-menawar."
    jump credits

label ending_self:
    scene bg dawn with dissolve
    show screen chapter_stamp("ENDING · KEMBALI KE DIRI SENDIRI", "Bandung · pagi yang biasa")
    narrator "Aku memilih tidak memulai hubungan romantis. Bukan karena takut selamanya, bukan karena tak ada orang yang menarik. Hanya karena untuk sekarang, aku ingin membangun hari-hari yang tidak ditopang oleh validasi seseorang."
    narrator "Aku membuat janji dengan konselor kampus. Aku menyelesaikan satu bab tesis, gagal menyelesaikan bab berikutnya, lalu makan siang pada jam yang wajar. Kemajuan tidak terlihat seperti montase."
    narrator "Aku tetap berteman dengan Nara, Satria, dan Mira. Masing-masing punya batas dan kehidupannya sendiri. Tidak satu pun harus menjadi hadiah atas pilihan yang tepat."
    narrator "Di balkon, matahari terbit di balik gedung-gedung yang belum selesai. Untuk pertama kalinya setelah lama, aku tidak buru-buru memberi makna pada semuanya."
    jump credits

label credits:
    hide screen chapter_stamp
    scene bg apartment with fade
    narrator "SENJA YANG TIDAK SELESAI · Tamat untuk saat ini."
    narrator "Hubungan tumbuh melalui waktu, komunikasi, dan pilihan. Affection points membuka kemungkinan, bukan menggantikan persetujuan. Kamu dapat memulai ulang untuk menemukan akhir yang lain."
    call screen ending_menu
    return

screen ending_menu():
    modal True
    frame:
        xalign 0.5
        yalign 0.68
        padding (24, 20)
        background "#101319dd"
        vbox:
            spacing 12
            text "Terima kasih telah bermain" size 24 color "#f4dfc7" xalign 0.5
            textbutton "Mulai lagi" action Start() xalign 0.5
            textbutton "Kembali ke menu utama" action MainMenu(confirm=False) xalign 0.5
