screen mouse_holder():
    style_prefix "choice"

    vbox:
        align (0.5, 0.5)
        spacing 30

        textbutton "Да" action [Hide("mouse_holder"), Return(True)]
        textbutton "Нет" action [Return(False)]

    on "show" action MouseMove(950, 500, 0.3)
    timer 0.3 repeat True action MouseMove(950, 500, 0.3)