import flet as ft
import time
def main(page: ft.Page):
    page.window_width = 415
    page.window_height = 825
    page.title = "Turkish Pizza Hub"

    renk = "0xFFF2F2F2"
    renk_border = "0xFFF2F2F2"
    # tıklanmaların kontrolü
    tiklama0 = ft.TextField(value="0")
    tiklama1 = ft.TextField(value="0")
    tiklama2 = ft.TextField(value="0")
    tiklama3 = ft.TextField(value="0")
    tiklama_zeytin = ft.TextField(value="0")
    tiklama_misir = ft.TextField(value="0")
    tiklama_et = ft.TextField(value="0")
    tiklama_sogan = ft.TextField(value="0")
    tiklama_peynir = ft.TextField(value="0")
    tiklama_mantar = ft.TextField(value="0")

    fiyat_tutar = ft.TextField(value="0")
    x = "Sepet tutarı {} TL".format(fiyat_tutar.value)
    fiyat = ft.Text(value=x)

    # -------------------------- KLASİK PİZZA --------------------------
    def pizza_secim_klasik(e):
        if (int(tiklama1.value) % 2 == 1 or int(tiklama2.value) % 2 == 1 or int(tiklama3.value) % 2 == 1):
            pass
        else:
            tiklama0.value = int(tiklama0.value) + 1
            if (int(tiklama0.value) % 2 == 0):

                fiyat_tutar.value = int(fiyat_tutar.value) - 109
                fiyat.value = "Sepet tutarı {} TL".format(fiyat_tutar.value)  #
                # seçili pizza için konteyner border kırmızı olsun
                konteyner_klasik.border.bottom.color = renk_border


            else:
                fiyat_tutar.value = int(fiyat_tutar.value) + 109
                fiyat.value = "Sepet tutarı {} TL".format(fiyat_tutar.value)  #
                # seçili pizza için konteyner border kırmızı olsun
                konteyner_klasik.border.bottom.color = "0xFFFF0000"
            fiyat.update()
            konteyner_klasik.update()

    # -------------------------- SADE PİZZA --------------------------
    def pizza_secim_sade(e):
        if (int(tiklama0.value) % 2 == 1 or int(tiklama2.value) % 2 == 1 or int(tiklama3.value) % 2 == 1):
            pass
        else:
            tiklama1.value = int(tiklama1.value) + 1
            if (int(tiklama1.value) % 2 == 0):
                fiyat_tutar.value = int(fiyat_tutar.value) - 95
                fiyat.value = "Sepet tutarı {} TL".format(fiyat_tutar.value)  #
                # seçili pizza için konteyner border kırmızı olsun
                konteyner_sade.border.bottom.color = renk_border

            else:
                fiyat_tutar.value = int(fiyat_tutar.value) + 95
                fiyat.value = "Sepet tutarı {} TL".format(fiyat_tutar.value)  #
                # seçili pizza için konteyner border kırmızı olsun
                konteyner_sade.border.bottom.color = "0xFFFF0000"
            fiyat.update()
            konteyner_sade.update()

    # -------------------------- MARGARİTA PİZZA --------------------------
    def pizza_secim_margarita(e):

        if (int(tiklama0.value) % 2 == 1 or int(tiklama1.value) % 2 == 1 or int(tiklama3.value) % 2 == 1):
            pass
        else:
            tiklama2.value = int(tiklama2.value) + 1
            if (int(tiklama2.value) % 2 == 0):
                fiyat_tutar.value = int(fiyat_tutar.value) - 99
                fiyat.value = "Sepet tutarı {} TL".format(fiyat_tutar.value)  #
                # seçili pizza için konteyner border kırmızı olsun
                konteyner_margarita.border.bottom.color = renk_border

            else:
                fiyat_tutar.value = int(fiyat_tutar.value) + 99
                fiyat.value = "Sepet tutarı {} TL".format(fiyat_tutar.value)  #
                # seçili pizza için konteyner border kırmızı olsun
                konteyner_margarita.border.bottom.color = "0xFFFF0000"
            fiyat.update()
            konteyner_margarita.update()

    # -------------------------- TÜRK PİZZA --------------------------
    def pizza_secim_turk(e):
        if (int(tiklama0.value) % 2 == 1 or int(tiklama1.value) % 2 == 1 or int(tiklama2.value) % 2 == 1):
            pass
        else:
            tiklama3.value = int(tiklama3.value) + 1
            if (int(tiklama3.value) % 2 == 0):
                fiyat_tutar.value = int(fiyat_tutar.value) - 115
                fiyat.value = "Sepet tutarı {} TL".format(fiyat_tutar.value)  #
                # seçili pizza için konteyner border kırmızı olsun
                konteyner_turk.border.bottom.color = renk_border

            else:
                fiyat_tutar.value = int(fiyat_tutar.value) + 115
                fiyat.value = "Sepet tutarı {} TL".format(fiyat_tutar.value)  #
                # seçili pizza için konteyner border kırmızı olsun
                konteyner_turk.border.bottom.color = "0xFFFF0000"
            fiyat.update()
            konteyner_turk.update()

    # -------------------------- MALZEMELER FONKSİYONLARI --------------------------

    # -------------------------- ZEYTİN --------------------------
    def malzeme_secim_zeytin(e):
        # herhangi bir pizza seçildiyse eğer o zaman malzeme seçimine izin verecek olan kod bloğu:
        if (int(tiklama0.value) % 2 == 1 or
                int(tiklama1.value) % 2 == 1 or
                int(tiklama2.value) % 2 == 1 or
                int(tiklama3.value) % 2 == 1):
            tiklama_zeytin.value = int(tiklama_zeytin.value) + 1
            if (int(tiklama_zeytin.value) % 2 == 0):
                # tıklanmamış:
                fiyat_tutar.value = int(fiyat_tutar.value) - 3
                fiyat.value = "Sepet tutarı {} TL".format(fiyat_tutar.value)
                konteyner_zeytin.border.bottom.color = renk_border
                konteyner_zeytin.update()
                fiyat.update()
            else:
                # tıklanmış
                fiyat_tutar.value = int(fiyat_tutar.value) + 3
                fiyat.value = "Sepet tutarı {} TL".format(fiyat_tutar.value)
                konteyner_zeytin.border.bottom.color = "0xFFFF0000"
                konteyner_zeytin.update()
                fiyat.update()
        else:
            pass

    # -------------------------- MISIR --------------------------
    def malzeme_secim_misir(e):
        # herhangi bir pizza seçildiyse eğer o zaman malzeme seçimine izin verecek olan kod bloğu:
        if (int(tiklama0.value) % 2 == 1 or
                int(tiklama1.value) % 2 == 1 or
                int(tiklama2.value) % 2 == 1 or
                int(tiklama3.value) % 2 == 1):
            tiklama_misir.value = int(tiklama_misir.value) + 1
            if (int(tiklama_misir.value) % 2 == 0):
                # tıklanmamış:
                fiyat_tutar.value = int(fiyat_tutar.value) - 3
                fiyat.value = "Sepet tutarı {} TL".format(fiyat_tutar.value)
                konteyner_misir.border.bottom.color = renk_border
                konteyner_misir.update()
                fiyat.update()
            else:
                # tıklanmış
                fiyat_tutar.value = int(fiyat_tutar.value) + 3
                fiyat.value = "Sepet tutarı {} TL".format(fiyat_tutar.value)
                konteyner_misir.border.bottom.color = "0xFFFF0000"
                konteyner_misir.update()
                fiyat.update()
        else:
            pass

    # -------------------------- ET --------------------------
    def malzeme_secim_et(e):
        # herhangi bir pizza seçildiyse eğer o zaman malzeme seçimine izin verecek olan kod bloğu:
        if (int(tiklama0.value) % 2 == 1 or
                int(tiklama1.value) % 2 == 1 or
                int(tiklama2.value) % 2 == 1 or
                int(tiklama3.value) % 2 == 1):
            tiklama_et.value = int(tiklama_et.value) + 1
            if (int(tiklama_et.value) % 2 == 0):
                # tıklanmamış:
                fiyat_tutar.value = int(fiyat_tutar.value) - 19
                fiyat.value = "Sepet tutarı {} TL".format(fiyat_tutar.value)
                konteyner_et.border.bottom.color = renk_border
                konteyner_et.update()
                fiyat.update()
            else:
                # tıklanmış
                fiyat_tutar.value = int(fiyat_tutar.value) + 19
                fiyat.value = "Sepet tutarı {} TL".format(fiyat_tutar.value)
                konteyner_et.border.bottom.color = "0xFFFF0000"
                konteyner_et.update()
                fiyat.update()
        else:
            pass

    # -------------------------- SOĞAN --------------------------
    def malzeme_secim_sogan(e):
        # herhangi bir pizza seçildiyse eğer o zaman malzeme seçimine izin verecek olan kod bloğu:
        if (int(tiklama0.value) % 2 == 1 or
                int(tiklama1.value) % 2 == 1 or
                int(tiklama2.value) % 2 == 1 or
                int(tiklama3.value) % 2 == 1):
            tiklama_sogan.value = int(tiklama_sogan.value) + 1
            if (int(tiklama_sogan.value) % 2 == 0):
                # tıklanmamış:
                fiyat_tutar.value = int(fiyat_tutar.value) - 4
                fiyat.value = "Sepet tutarı {} TL".format(fiyat_tutar.value)
                konteyner_sogan.border.bottom.color = renk_border
                konteyner_sogan.update()
                fiyat.update()
            else:
                # tıklanmış
                fiyat_tutar.value = int(fiyat_tutar.value) + 4
                fiyat.value = "Sepet tutarı {} TL".format(fiyat_tutar.value)
                konteyner_sogan.border.bottom.color = "0xFFFF0000"
                konteyner_sogan.update()
                fiyat.update()
        else:
            pass

    # -------------------------- PEYNİR --------------------------
    def malzeme_secim_peynir(e):
        # herhangi bir pizza seçildiyse eğer o zaman malzeme seçimine izin verecek olan kod bloğu:
        if (int(tiklama0.value) % 2 == 1 or
                int(tiklama1.value) % 2 == 1 or
                int(tiklama2.value) % 2 == 1 or
                int(tiklama3.value) % 2 == 1):
            tiklama_peynir.value = int(tiklama_peynir.value) + 1
            if (int(tiklama_peynir.value) % 2 == 0):
                # tıklanmamış:
                fiyat_tutar.value = int(fiyat_tutar.value) - 10
                fiyat.value = "Sepet tutarı {} TL".format(fiyat_tutar.value)
                konteyner_peynir.border.bottom.color = renk_border
                konteyner_peynir.update()
                fiyat.update()
            else:
                # tıklanmış
                fiyat_tutar.value = int(fiyat_tutar.value) + 10
                fiyat.value = "Sepet tutarı {} TL".format(fiyat_tutar.value)
                konteyner_peynir.border.bottom.color = "0xFFFF0000"
                konteyner_peynir.update()
                fiyat.update()
        else:
            pass

    # -------------------------- MANTAR --------------------------
    def malzeme_secim_mantar(e):
        # herhangi bir pizza seçildiyse eğer o zaman malzeme seçimine izin verecek olan kod bloğu:
        if (int(tiklama0.value) % 2 == 1 or
                int(tiklama1.value) % 2 == 1 or
                int(tiklama2.value) % 2 == 1 or
                int(tiklama3.value) % 2 == 1):
            tiklama_mantar.value = int(tiklama_mantar.value) + 1
            if (int(tiklama_mantar.value) % 2 == 0):
                # tıklanmamış:
                fiyat_tutar.value = int(fiyat_tutar.value) - 5
                fiyat.value = "Sepet tutarı {} TL".format(fiyat_tutar.value)
                konteyner_mantar.border.bottom.color = renk_border
                konteyner_mantar.update()
                fiyat.update()
            else:
                # tıklanmış
                fiyat_tutar.value = int(fiyat_tutar.value) + 5
                fiyat.value = "Sepet tutarı {} TL".format(fiyat_tutar.value)
                konteyner_mantar.border.bottom.color = "0xFFFF0000"
                konteyner_mantar.update()
                fiyat.update()
        else:
            pass

    # -------------------------- MALZEMELER FONKSİYONLARI --------------------------

    # -------------------------- KLASİK PİZZA --------------------------
    konteyner_klasik = ft.Container(
        content=ft.Row(
            controls=[
                ft.Image(src=r"C:\Users\90538\Desktop\pythondersleri.py\flet_ui\View\Assets\klasik.png", ),
                ft.Column(
                    controls=[
                        ft.Text(value="Klasik Pizza ",
                                weight=ft.FontWeight("bold"),
                                offset=ft.Offset(0, 0.2),
                                color=ft.colors.BLACK54, ),
                        ft.Text(value="Sucuklu, soslu, mozarellalı pizza",
                                offset=ft.Offset(0, -0.4),
                                color=ft.colors.BLACK54, ),
                    ],
                ),
            ],
        ),
        bgcolor=renk,
        width=380,
        height=70,
        padding=10,
        border_radius=10,
        on_click=pizza_secim_klasik,
        border=ft.border.all(2, renk_border),
    )

    # -------------------------- SADE PİZZA --------------------------
    konteyner_sade = ft.Container(
        content=ft.Row(
            controls=[
                ft.Image(src=r"C:\Users\90538\Desktop\pythondersleri.py\flet_ui\View\Assets\sade.png", ),
                ft.Column(
                    controls=[
                        ft.Text(value="Sade Pizza ", weight=ft.FontWeight("bold"),
                                offset=ft.Offset(0, 0.2),
                                color=ft.colors.BLACK54, ),
                        ft.Text(value="Soslu ve mozarellalı pizza", offset=ft.Offset(0, -0.4),
                                color=ft.colors.BLACK54, ),
                    ],
                ),
            ],
        ),
        bgcolor=renk,
        width=380,
        height=70,
        padding=10,
        border_radius=10,
        on_click=pizza_secim_sade,
        border=ft.border.all(2, renk_border),

    )

    # -------------------------- MARGARİTA PİZZA --------------------------
    konteyner_margarita = ft.Container(
        content=ft.Row(
            controls=[
                ft.Image(src=r"C:\Users\90538\Desktop\pythondersleri.py\flet_ui\View\Assets\margarita.png", ),
                ft.Column(
                    controls=[
                        ft.Text(value="Margarita", weight=ft.FontWeight("bold"),
                                offset=ft.Offset(0, 0.2), color=ft.colors.BLACK54, ),
                        ft.Text(value="Mozarella ve domates soslu pizza", offset=ft.Offset(0, -0.4),
                                color=ft.colors.BLACK54, ),
                    ],
                ),
            ],
        ),
        bgcolor=renk,
        width=380,
        height=70,
        padding=10,
        border_radius=10,
        on_click=pizza_secim_margarita,
        border=ft.border.all(2, renk_border),
    )

    # -------------------------- TÜRK PİZZA --------------------------
    konteyner_turk = ft.Container(
        content=ft.Row(
            controls=[
                ft.Image(src=r"C:\Users\90538\Desktop\pythondersleri.py\flet_ui\View\Assets\turk.png", ),
                ft.Column(
                    controls=[
                        ft.Text(value="Türk Pizzası", weight=ft.FontWeight("bold"),
                                offset=ft.Offset(0, 0.2), color=ft.colors.BLACK54, ),
                        ft.Text(value="Mozarella, sucuk, sosis ve pastırmalı pizza", offset=ft.Offset(0, -0.4),
                                color=ft.colors.BLACK54, ),
                    ],
                ),
            ],
        ),
        bgcolor=renk,
        width=380,
        height=70,
        padding=10,
        border_radius=10,
        margin=ft.margin.only(bottom=20),
        on_click=pizza_secim_turk,
        border=ft.border.all(2, renk_border),
    )

    # --------------------------------------------------------------------------------------

    konteyner_zeytin = ft.Container(
        content=ft.Image(src=r"C:\Users\90538\Desktop\pythondersleri.py\flet_ui\View\Assets\zeytin.png",
                         width=75),
        bgcolor=renk,
        width=100,
        height=100,
        padding=10,
        alignment=ft.alignment.center,
        border_radius=10,
        border=ft.border.all(2, renk_border),
        on_click=malzeme_secim_zeytin

    )
    konteyner_misir = ft.Container(
        content=ft.Image(src=r"C:\Users\90538\Desktop\pythondersleri.py\flet_ui\View\Assets\misir.png",
                         width=65),
        bgcolor=renk,
        width=100,
        height=100,
        padding=10,
        border_radius=10,
        alignment=ft.alignment.center,
        margin=ft.margin.only(left=30),
        border=ft.border.all(2, renk_border),
        on_click=malzeme_secim_misir
    )
    konteyner_et = ft.Container(
        content=ft.Image(src=r"C:\Users\90538\Desktop\pythondersleri.py\flet_ui\View\Assets\et.png",
                         width=60),
        bgcolor=renk,
        width=100,
        height=100,
        padding=10,
        border_radius=10,
        alignment=ft.alignment.center,
        margin=ft.margin.only(left=30),
        border=ft.border.all(2, renk_border),
        on_click=malzeme_secim_et
    )
    konteyner_sogan = ft.Container(
        content=ft.Image(src=r"C:\Users\90538\Desktop\pythondersleri.py\flet_ui\View\Assets\sogan.png",
                         width=45),
        bgcolor=renk,
        width=100,
        height=100,
        padding=10,
        border_radius=10,
        alignment=ft.alignment.center,
        border=ft.border.all(2, renk_border),
        on_click=malzeme_secim_sogan
    )
    konteyner_peynir = ft.Container(
        content=ft.Image(src=r"C:\Users\90538\Desktop\pythondersleri.py\flet_ui\View\Assets\peynir.png",
                         width=50),
        bgcolor=renk,
        width=100,
        height=100,
        padding=10,
        border_radius=10,
        alignment=ft.alignment.center,
        margin=ft.margin.only(left=30, ),
        border=ft.border.all(2, renk_border),
        on_click=malzeme_secim_peynir,
    )
    konteyner_mantar = ft.Container(
        content=ft.Image(src=r"C:\Users\90538\Desktop\pythondersleri.py\flet_ui\View\Assets\mantar.png",
                         width=45),
        bgcolor=renk,
        width=100,
        height=100,
        padding=10,
        border_radius=10,
        alignment=ft.alignment.center,
        margin=ft.margin.only(left=30, ),
        border=ft.border.all(2, renk_border),
        on_click=malzeme_secim_mantar,

    )

    ### Column widget Pizzalar
    col = ft.Column(
        controls=[
            ft.Text(value="Pizzalar", color="0xFFFF0000", weight=ft.FontWeight("bold")),
            # -------------------------- KLASİK PİZZA --------------------------
            konteyner_klasik,
            # -------------------------- SADE PİZZA --------------------------
            konteyner_sade,
            # -------------------------- MARGARİTA --------------------------
            konteyner_margarita,
            # -------------------------- TÜRK PİZZA --------------------------
            konteyner_turk,

            ft.Text(value="Malzemeler", color="0xFFFF0000", weight=ft.FontWeight("bold")),
            ### ROW widget Malzemeler
            ft.Row(
                controls=[
                    # -------------------------- ZEYTİN --------------------------
                    konteyner_zeytin,
                    # -------------------------- MISIR --------------------------
                    konteyner_misir,
                    # -------------------------- ET --------------------------
                    konteyner_et,
                ],
            ),

            ft.Row(
                controls=[
                    # -------------------------- SOĞAN --------------------------
                    konteyner_sogan,
                    # -------------------------- PEYNİR --------------------------
                    konteyner_peynir,
                    # -------------------------- MANTAR --------------------------
                    konteyner_mantar,
                ],
            ),

            ### container --- odeme ekranına git butonu
            ft.Stack(
                controls=[
                    # -------------------------- FİYAT GÖSTERGE --------------------------
                    ft.Container(
                        content=ft.Row(controls=[
                            fiyat,
                        ], ),
                        bgcolor="0xFFF2F2F2",
                        width=380,
                        height=70,
                        padding=10,
                        border_radius=10,
                        margin=ft.margin.only(top=70),
                    ),

                ],
            ),
        ],
        height=page.height,
    )

    # -------------------------- ÖDEME EKRANI BUTONU --------------------------
    buton = ft.Container(
        content=ft.Icon(color=ft.colors.WHITE, size=25, name=ft.icons.ADD_SHOPPING_CART_SHARP),
        bgcolor="0xFFFF0000",
        width=90,
        height=70,
        padding=10,
        border_radius=10,
        margin=ft.margin.only(top=0, left=290),
        on_click=lambda _: page.go("/Payment")  # payment ekranına yönlendir.
    )

    # --------- excel'e verileri kaydetme, buton border color ve snack bar işlevleri.---------
    def buton_tiklama(e):
        # tıklandığında çerçeve ve yazıyı kırmızı yap:
        kayit_butonu.border.bottom.color = "0xFFFF0000"
        buton_text.color = "0xFFFF0000"
        kayit_butonu.update()
        time.sleep(0.1)
        kayit_butonu.border.bottom.color = "0xFFF2F2F2"
        buton_text.color = ft.colors.BLACK54
        kayit_butonu.update()
        # snack bar gösterimi:
        page.snack_bar = ft.SnackBar(ft.Text(value="Ödeme işlemi başarıyla tamamlandı."))
        page.snack_bar.open = True
        page.update()
        # VeriTabanı veya Excel'e veri kaydı işlemi :
        ###

        # VeriTabanı veya Excel'e veri kaydı işlemi :

    # --------- excel'e verileri kaydetme, buton border color ve snack bar işlevleri.---------

    # ------------------------- İnputları kredi kartına yazdırma -------------------------
    def txtfield_ad_soyad(e):
        kart_isim.value = ad_soyad.value
        kart_isim.update()

    def txtfield_kart_numarasi(e):
        kart_numarasi.value = numara.value
        kart_numarasi.update()

    # ------------------------- karta yazdırmadan text'e kaydetmek için:
    def txtfield_tc(e):
        kart_tc.value = tc.value
        kart_tc.update()

    def txtfield_sifre(e):
        kart_sifre.value = sifre.value
        kart_sifre.update()

    # ------------------------- İnputları kredi kartına yazdırma -------------------------
    kart = ft.Image(
        src=r"C:\Users\90538\Desktop\pythondersleri.py\flet_ui\View\Assets\card.png",
    )
    # ------------------------- text değişken tanımlamalar -------------------------
    kart_isim = ft.Text(
        value=" ",
        offset=ft.Offset(0.3, 6),
        color=ft.colors.WHITE,
        weight=ft.FontWeight("bold"),
    )
    kart_numarasi = ft.Text(
        value=" ",
        offset=ft.Offset(0.3, 7),
        color=ft.colors.WHITE70,
        weight=ft.FontWeight("bold"),
    )
    kart_tc = ft.Text(
        value=" ",
    )
    kart_sifre = ft.Text(
        value=" ",
    )
    # ****************************************************************************************
    toplam_fiyat_tutari = ft.Text(  ### ÖNCEKİ SAYFA OLAN PİZZALARDAN GELEN FİYAT TUTARI ATAMASI.
        value="0",
    )
    # ------------------------- text değişken tanımlamalar -------------------------

    # ------------------------- İnput işlemleri -------------------------
    ad_soyad = ft.TextField(
        label="Ad soyad",
        on_change=txtfield_ad_soyad,
        offset=ft.Offset(0, 0.2),

    )
    numara = ft.TextField(
        label="Kart numarası",
        on_change=txtfield_kart_numarasi,
        offset=ft.Offset(0, 0.2),
    )
    tc = ft.TextField(
        label="Tc kimlik",
        on_change=txtfield_tc,
        offset=ft.Offset(0, 0.2),
    )
    sifre = ft.TextField(
        label="Şifre",
        password=True,  # sifrenin ekranda * halinde gizlenmesi için.
        on_change=txtfield_sifre,
        offset=ft.Offset(0, 0.2),
    )
    # ------------------------- İnput işlemleri -------------------------

    buton_text = ft.Text(value="Ödeme Yap", weight=ft.FontWeight("bold"),
                         offset=ft.Offset(1.7, 0.4),
                         color=ft.colors.BLACK54, )

    # --------- kayıt işlemlerini tamamlama, excel'e verileri kaydetme ve snackbar butonu.---------
    kayit_butonu = ft.Container(
        content=ft.Row(
            controls=[
                ft.Column(
                    controls=[
                        buton_text,
                    ],
                ),
            ],
        ),
        bgcolor="0xFFF2F2F2",
        width=380,
        height=70,
        padding=10,
        border_radius=10,
        offset=ft.Offset(0, 0.2),
        on_click=buton_tiklama,
        border=ft.border.all(2, "0xFFF2F2F2"),
    )
    # --------- kayıt işlemlerini tamamlama ve excel'e verileri kaydetme butonu.---------

    geri_donus_butonu = ft.Container(
        content=ft.Icon(color=ft.colors.BLACK54, size=20, name=ft.icons.ARROW_BACK),
        bgcolor="0xFFF2F2F2",
        width=40,
        height=40,
        padding=10,
        border_radius=10,
        on_click=lambda _: page.go("/MainView")  # payment ekranına yönlendir.
    )

    # UI - Kolon
    kolon = ft.Column(
        controls=[
            # ----------------- Kredi Kartı Bilgileri -----------------
            geri_donus_butonu,
            ft.Stack(
                controls=[

                    kart,
                    kart_isim,
                    kart_numarasi,
                ],
            ),
            ad_soyad,
            numara,
            tc,
            sifre,
            kayit_butonu,

        ],
        height=825,
    )

    konteyner_splash = ft.Container(
        height=825,
        width=415,
        content=ft.Image(
            src=r"C:\Users\90538\Desktop\pythondersleri.py\flet_ui\View\Assets\entry.png", ),
        on_hover=lambda _: page.go("/MainView"),
    )

    def ekran_degisim(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/Splash",
                [

                    ############ İLK SAYFA SPLASH SCREEN ------------------------------------------
                    konteyner_splash,

                    ############ İLK SAYFA SPLASH SCREEN ------------------------------------------

                ],
            )
        )
        if page.route == "/Payment":
            page.views.append(
                ft.View(
                    "/Payment",
                    [
                        # ---------- payment sayfasından dönüş kodları ----------
                        kolon,

                    ],
                )
            )
        if page.route == "/MainView":
            page.views.append(
                ft.View(
                    "/MainView",
                    [
                        # PİZZALAR VE MALZEMELER EKRANI
                        col,
                        buton,

                    ],
                )
            )
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = ekran_degisim
    page.on_view_pop = view_pop
    page.go(page.route)

    # page.controls.append(col)
    page.update()


ft.app(target=main)
