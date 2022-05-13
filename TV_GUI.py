from tkinter import *
from PIL import ImageTk, Image
# Original Code - https://youtu.be/rDjTo8Sd7GA
# Added GUI, mute, channel buttons, TV screen


class Television:
    """
    A class representing details for a television object
    """
    MIN_CHANNEL = 0
    MAX_CHANNEL = 9
    MIN_VOLUME = 0
    MAX_VOLUME = 10

    def __init__(self, window, channel=MIN_CHANNEL, volume=MIN_VOLUME, status=False, mute_status=False, vol_temp=0):

        """

        :param channel: Television's channel
        :param volume:  Television's volume
        :param status:  Television's status (on/off)
        :param mute_status: Television's mute status (on/off)
        :param vol_temp: Television's temporary volume (Used for keeping track of volume when muted)
        """

        self.channel = channel
        self.volume = volume
        self.status = status
        self.mute_status = mute_status
        self.vol_temp = vol_temp

        self.window = window

        # Frame for power and mute buttons
        self.frame_top = Frame(self.window)

        self.power_button = Button(self.frame_top, text='POWER', command=self.power)
        self.mute_button = Button(self.frame_top, text='MUTE', command=lambda: self.mute())

        self.mute_button.pack(side=RIGHT)
        self.power_button.pack(side=BOTTOM, padx=(0, 15))
        self.frame_top.pack()

        # Frame for buttons 1, 2, 3
        self.frame_123 = Frame(self.window)
        self.one_button = Button(self.frame_123, text='1',
                                 command=lambda: [self.change_channel(1), self.change_image(1)])
        self.two_button = Button(self.frame_123, text='2',
                                 command=lambda: [self.change_channel(2), self.change_image(2)])
        self.three_button = Button(self.frame_123, text='3',
                                   command=lambda: [self.change_channel(3), self.change_image(3)])
        self.one_button.pack(side=LEFT)
        self.two_button.pack(side=LEFT)
        self.three_button.pack(side=LEFT)
        self.frame_123.pack(pady=(50, 0))

        # Frame for buttons 4, 5, 6
        self.frame_456 = Frame(self.window)
        self.four_button = Button(self.frame_456, text='4',
                                  command=lambda: [self.change_channel(4), self.change_image(4)])
        self.five_button = Button(self.frame_456, text='5',
                                  command=lambda: [self.change_channel(5), self.change_image(5)])
        self.six_button = Button(self.frame_456, text='6',
                                 command=lambda: [self.change_channel(6), self.change_image(6)])
        self.four_button.pack(side=LEFT)
        self.five_button.pack(side=LEFT)
        self.six_button.pack(side=LEFT)
        self.frame_456.pack()

        # Frame for buttons 7, 8, 9
        self.frame_789 = Frame(self.window)
        self.seven_button = Button(self.frame_789, text='7',
                                   command=lambda: [self.change_channel(7), self.change_image(7)])
        self.eight_button = Button(self.frame_789, text='8',
                                   command=lambda: [self.change_channel(8), self.change_image(8)])
        self.nine_button = Button(self.frame_789, text='9',
                                  command=lambda: [self.change_channel(9), self.change_image(9)])
        self.seven_button.pack(side=LEFT)
        self.eight_button.pack(side=LEFT)
        self.nine_button.pack(side=LEFT)
        self.frame_789.pack()

        # Frame for 0 button
        self.frame_zero = Frame(self.window)
        self.zero_button = Button(self.frame_zero, text='0',
                                  command=lambda: [self.change_channel(0), self.change_image(0)])
        self.zero_button.pack()
        self.frame_zero.pack()

        # Frame for volume and channel increase buttons
        self.frame_inc = Frame(self.window)
        self.vol_inc_button = Button(self.frame_inc, text='∧', width=1, command=lambda: self.increase_volume())
        self.ch_inc_button = Button(self.frame_inc, text='∧', width=1, command=lambda: self.increase_channel())
        self.vol_inc_button.pack(side=LEFT)
        self.ch_inc_button.pack(side=RIGHT, padx=(50, 0))
        self.frame_inc.pack(pady=(15, 0))

        # Frame for volume and channel buttons
        self.frame_vol_ch = Frame(self.window)
        self.vol_button = Button(self.frame_vol_ch, text='VOL', width=1)
        self.ch_button = Button(self.frame_vol_ch, text='CH', width=1)
        self.vol_button.pack(side=LEFT)
        self.ch_button.pack(side=RIGHT, padx=(50, 0))
        self.frame_vol_ch.pack()

        # Frame for volume and channel decrease buttons
        self.frame_dec = Frame(self.window)
        self.vol_dec_button = Button(self.frame_dec, text='∨', width=1, command=lambda: self.decrease_volume())
        self.ch_dec_button = Button(self.frame_dec, text='∨', width=1, command=lambda: self.decrease_channel())
        self.vol_dec_button.pack(side=LEFT)
        self.ch_dec_button.pack(side=RIGHT, padx=(50, 0))
        self.frame_dec.pack()

        # Frame for tv info, power, channel, volume
        self.frame_stat = Frame(self.window)
        self.pow_lab = Label(self.frame_stat, text='Power : Off')
        self.vol_lab = Label(self.frame_stat, text='Volume : 0')
        self.ch_lab = Label(self.frame_stat, text='Channel : 0')
        self.pow_lab.pack(side=LEFT)
        self.ch_lab.pack(side=RIGHT)
        self.vol_lab.pack(side=RIGHT, padx=10)
        self.frame_stat.pack()

        # Frame for TV screen
        self.frame_screen = Frame(self.window)
        self.img = ImageTk.PhotoImage(Image.open("choff.jpeg"))
        self.chan = Label(self.window, image=self.img)
        self.chan.image = self.img
        self.chan.pack(pady=(30, 0))
        self.frame_screen.pack()

    def change_image(self, ch) -> None:
        """
        Method used to change the display of the TV
        """
        img = 'ch{}.jpeg'.format(ch)
        i = ImageTk.PhotoImage(Image.open(img))
        self.chan.image = i
        self.chan.configure(image=i)

    def power(self) -> None:
        """
        Method used to turn the TV on/off.
        When turned off, screen turns black, everything set to 0
        """
        if self.status:
            self.status = False
            print("Power : ", self.status)
            self.pow_lab.config(text='Power : Off')
            self.ch_lab.config(text='Channel : 0')
            self.vol_lab.config(text='Volume : 0')
            self.change_image('off')

        elif not self.status:
            self.status = True
            print("Power : ", self.status)
            self.pow_lab.config(text='Power : On')
            v = 'Volume : ' + str(self.volume)
            self.vol_lab.config(text=v)
            c = 'Channel : ' + str(self.channel)
            self.ch_lab.config(text=c)
            self.change_image(self.channel)

    def increase_volume(self) -> None:
        """
        Method used to adjust the TV volume by incrementing its value
        Will only increase until it reaches MAX_VOLUME
        Only works when the television status is on
        """
        if self.mute_status:
            self.mute_status = False
            self.volume = self.vol_temp
        if self.status:
            if self.mute_status:
                self.volume = self.vol_temp + 1
                print("Volume : ", self.volume)
                v = 'Volume : ' + str(self.volume)
                self.vol_lab.config(text=v)

            else:
                if self.volume != self.MAX_VOLUME:
                    self.volume += 1
                print("Volume : ", self.volume)
                v = 'Volume : ' + str(self.volume)
                self.vol_lab.config(text=v)

    def decrease_volume(self) -> None:
        """
        Method used to adjust the TV volume by decrementing its value
        Will only decrease until it reaches MIN_VOLUME
        Only works when the television status is on
        """
        if self.mute_status:
            self.mute_status = False
            self.volume = self.vol_temp
        if self.status:
            if self.mute_status:
                self.volume = self.vol_temp - 1
                print("Volume : ", self.volume)
                v = 'Volume : ' + str(self.volume)
                self.vol_lab.config(text=v)
            else:
                if self.volume != self.MIN_VOLUME:
                    self.volume -= 1
                print("Volume : ", self.volume)
                v = 'Volume : ' + str(self.volume)
                self.vol_lab.config(text=v)

    def mute(self) -> None:
        """
        Method used to mute/unmute.
        Changes value to 0, or to the value before it was muted
        """
        if self.status:
            if not self.mute_status:
                self.vol_temp = self.volume
                self.volume = 0
                self.mute_status = True
                print("Volume : ", self.volume)
                v = 'Volume : ' + str(self.volume)
                self.vol_lab.config(text=v)
            elif self.mute_status:
                self.volume = self.vol_temp
                self.mute_status = False
                print("Volume : ", self.volume)
                v = 'Volume : ' + str(self.volume)
                self.vol_lab.config(text=v)

    def change_channel(self, ch) -> None:
        """
        Method used to change channel with numeric buttons
        """
        if self.status:
            self.channel = ch
            print("Channel : ", ch)
            c = 'Channel : ' + str(self.channel)
            self.ch_lab.config(text=c)

    def increase_channel(self) -> None:
        """
        Method used to adjust the TV channel by incrementing its value
        If the channel is increased at its maximum, it will roll over to the lowest channel
        Only works when the television status is on
        """
        if self.status:
            if self.MIN_CHANNEL <= self.channel < self.MAX_CHANNEL:
                self.channel += 1
                print("Channel: ", self.channel)
                c = 'Channel : ' + str(self.channel)
                self.ch_lab.config(text=c)
                self.change_image(self.channel)
            elif self.channel == self.MAX_CHANNEL:
                self.channel = self.MIN_CHANNEL
                print("Channel: ", self.channel)
                c = 'Channel : ' + str(self.channel)
                self.ch_lab.config(text=c)
                self.change_image(self.channel)

    def decrease_channel(self) -> None:
        """
        Method used to adjust the TV channel by decrementing its value
        If the channel is decreased at 0, it will roll over to the highest channel
        Only works when the television status is on
        """
        if self.status:
            if self.MIN_CHANNEL < self.channel <= self.MAX_CHANNEL:
                self.channel -= 1
                print("Channel: ", self.channel)
                c = 'Channel : ' + str(self.channel)
                self.ch_lab.config(text=c)
                self.change_image(self.channel)
            elif self.channel == self.MIN_CHANNEL:
                self.channel = self.MAX_CHANNEL
                print("Channel: ", self.channel)
                c = 'Channel : ' + str(self.channel)
                self.ch_lab.config(text=c)
                self.change_image(self.channel)

    def __str__(self) -> str:
        """
        Method used to return the television's status
        """
        return f'TV Status: Is on = {self.status}, Channel = {self.channel}, Volume = {self.volume}'
