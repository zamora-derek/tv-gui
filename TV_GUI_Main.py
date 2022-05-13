from TV_GUI import *


def main():
    window = Tk()
    window.title('Remote')
    window.geometry('250x600')
    window.resizable(False, False)

    widgets = Television(window)

    window.mainloop()


if __name__ == '__main__':
    main()


