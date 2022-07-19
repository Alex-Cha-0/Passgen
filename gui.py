def setwindow(root):
    root.title('Passgen by alex')
    root.wm_resizable(False, False)  # Менять размер окна

    w = 450
    h = 200
    ws = root.winfo_screenwidth()
    wh = root.winfo_screenheight()

    x = int(ws / 2 - w / 2)
    y = int(wh / 2 - h / 2)

    root.geometry("{0}x{1}+{2}+{3}".format(w, h, x, y))