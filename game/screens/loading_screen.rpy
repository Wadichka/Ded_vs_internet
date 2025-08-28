screen loading_screen(progress=0.0):
    tag menu  # чтобы заменял меню
    frame:
        align (0.5, 0.5)
        xsize 1200
        ysize 500
        vbox:
            xalign 0.5
            yalign 0.5

            spacing 50

            text "Идет докачка файлов. Пожалуйста, не выходите из игры." xalign 0.5

            bar value progress range 1.0 xmaximum 400:
                xalign 0.5
                yalign 0.5

            text "Скачано [str_progress] Мб из 200 Мб" xalign 0.5

