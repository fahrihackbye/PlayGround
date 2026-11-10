# Layar antarmuka mandiri agar proyek dapat dijalankan tanpa aset template.

screen say(who, what):
    zorder 100
    window:
        id "window"
        xalign 0.5
        yalign 1.0
        xfill True
        background "#11131bea"
        padding (48, 28)
        vbox:
            spacing 8
            if who is not None:
                text who id "who" size 27 color "#e9c9a9"
            text what id "what" size 26 color "#f4f0eb" xmaximum 1500
    use quick_menu

screen choice(items):
    zorder 110
    vbox:
        style_prefix "choice"
        xalign 0.5
        yalign 0.62
        spacing 12
        for item in items:
            textbutton item.caption action item.action:
                xminimum 700
                background Frame(Solid("#20232bea"), 14, 14)
                hover_background Frame(Solid("#765b56ee"), 14, 14)
                padding (22, 14)
                text_color "#f4f0eb"
                text_hover_color "#ffffff"
                text_size 23

screen quick_menu():
    zorder 120
    if quick_menu:
        hbox:
            xalign 0.98
            yalign 0.98
            spacing 12
            textbutton "Simpan" action ShowMenu("save")
            textbutton "Muat" action ShowMenu("load")
            textbutton "Lewati" action Skip()
            textbutton "Riwayat" action ShowMenu("history")

screen main_menu():
    tag menu
    add Solid("#202a33")
    frame:
        xalign 0.5
        yalign 0.5
        padding (60, 48)
        background "#101319dd"
        vbox:
            xalign 0.5
            spacing 18
            text "SENJA YANG TIDAK SELESAI" size 38 color "#f4dfc7" xalign 0.5
            text "Visual novel tentang kedekatan, batas, dan pilihan" size 19 color "#d2c9c3" xalign 0.5
            null height 10
            textbutton "Mulai" action Start() xalign 0.5
            textbutton "Muat permainan" action ShowMenu("load") xalign 0.5
            textbutton "Pengaturan" action ShowMenu("preferences") xalign 0.5
            textbutton "Keluar" action Quit(confirm=True) xalign 0.5

screen navigation():
    vbox:
        spacing 10
        textbutton "Kembali" action Return()
        textbutton "Simpan" action ShowMenu("save")
        textbutton "Muat" action ShowMenu("load")
        textbutton "Pengaturan" action ShowMenu("preferences")
        textbutton "Menu utama" action MainMenu()

screen game_menu(title, scroll=None, yinitial=0.0):
    tag menu
    add Solid("#202a33")
    frame:
        xalign 0.5
        yalign 0.5
        xsize 1180
        ysize 850
        padding (35, 30)
        background "#101319ee"
        hbox:
            spacing 40
            vbox:
                xsize 800
                spacing 20
                text title size 32 color "#f4dfc7"
                transclude
            use navigation

screen save():
    tag menu
    use file_slots("Simpan Permainan", True)

screen load():
    tag menu
    use file_slots("Muat Permainan", False)

screen file_slots(title, saving):
    add Solid("#202a33")
    frame:
        xalign 0.5
        yalign 0.5
        xsize 1180
        ysize 850
        padding (35, 30)
        background "#101319ee"
        vbox:
            spacing 18
            text title size 32 color "#f4dfc7"
            grid 3 2:
                spacing 14
                for slot in range(1, 7):
                    frame:
                        xsize 340
                        ysize 175
                        padding (12, 12)
                        background "#292d36"
                        vbox:
                            spacing 8
                            text "Slot [slot]" size 17 color "#e9c9a9"
                            if FileLoadable(slot):
                                text FileTime(slot, format="%Y-%m-%d %H:%M") size 15 color "#d2c9c3"
                            else:
                                text "Kosong" size 15 color "#a9a8aa"
                            if saving:
                                textbutton "Simpan di sini" action FileSave(slot)
                            else:
                                textbutton "Muat" action FileLoad(slot)
                            if FileLoadable(slot):
                                textbutton "Hapus" action FileDelete(slot)
            textbutton "Kembali" action Return()

screen preferences():
    tag menu
    use game_menu("Pengaturan"):
        vbox:
            spacing 16
            text "Tampilan" size 22 color "#e9c9a9"
            textbutton "Jendela" action Preference("display", "window")
            textbutton "Layar penuh" action Preference("display", "fullscreen")
            text "Suara" size 22 color "#e9c9a9"
            textbutton "Alihkan suara" action Preference("all mute", "toggle")

screen history():
    tag menu
    use game_menu("Riwayat"):
        vpgrid:
            cols 1
            xsize 780
            ymaximum 650
            scrollbars "vertical"
            for h in _history_list:
                if h.who:
                    text "[h.who]: [h.what]" size 18 color "#f4f0eb"
                else:
                    text "[h.what]" size 18 color "#f4f0eb"
