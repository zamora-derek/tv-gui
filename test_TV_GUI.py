from TV_GUI import *



class Test:
    def setup_method(self):
        self.tv = Television()

    def teardown_method(self):
        del self.tv

    def test_init(self):
        assert self.tv.__str__() == 'TV Status: Is on = False, Channel = 0, Volume = 0'

    def test_power(self):
        assert self.tv.__str__() == 'TV Status: Is on = False, Channel = 0, Volume = 0'
        self.tv.power()
        self.tv.increase_volume()
        self.tv.increase_channel()
        assert self.tv.__str__() == 'TV Status: Is on = True, Channel = 1, Volume = 1'
        self.tv.power()
        assert self.tv.__str__() == 'TV Status: Is on = False, Channel = 0, Volume = 0'

    def test_channel_up(self):
        self.tv.increase_channel()
        assert self.tv.__str__() == 'TV Status: Is on = False, Channel = 0, Volume = 0'

        self.tv.power()
        self.tv.increase_channel()
        assert self.tv.__str__() == 'TV Status: Is on = True, Channel = 1, Volume = 0'

        self.tv.increase_channel()
        self.tv.increase_channel()
        self.tv.increase_channel()
        self.tv.increase_channel()
        self.tv.increase_channel() # Testing channel rollover (10 -> 0)
        self.tv.increase_channel()
        self.tv.increase_channel()
        self.tv.increase_channel()
        self.tv.increase_channel()
        assert self.tv.__str__() == 'TV Status: Is on = True, Channel = 0, Volume = 0'

    def test_channel_down(self):
        self.tv.decrease_channel()
        assert self.tv.__str__() == 'TV Status: Is on = False, Channel = 0, Volume = 0'

        self.tv.power()
        self.tv.decrease_channel()
        assert self.tv.__str__() == 'TV Status: Is on = True, Channel = 9, Volume = 0'

        self.tv.decrease_channel()
        assert self.tv.__str__() == 'TV Status: Is on = True, Channel = 8, Volume = 0'

    def test_volume_up(self):
        self.tv.increase_volume()
        assert self.tv.__str__() == 'TV Status: Is on = False, Channel = 0, Volume = 0'

        self.tv.power()
        self.tv.increase_volume()
        assert self.tv.__str__() == 'TV Status: Is on = True, Channel = 0, Volume = 1'

        self.tv.increase_volume()
        self.tv.increase_volume()
        self.tv.increase_volume()
        self.tv.increase_volume()
        self.tv.increase_volume()
        self.tv.increase_volume()
        self.tv.increase_volume()
        self.tv.increase_volume()
        self.tv.increase_volume()
        self.tv.increase_volume()
        assert self.tv.__str__() == 'TV Status: Is on = True, Channel = 0, Volume = 10'

    def test_volume_down(self):
        self.tv.decrease_volume()
        assert self.tv.__str__() == 'TV Status: Is on = False, Channel = 0, Volume = 0'

        self.tv.power()
        self.tv.increase_volume()
        self.tv.increase_volume()
        self.tv.decrease_volume()
        assert self.tv.__str__() == 'TV Status: Is on = True, Channel = 0, Volume = 1'

        self.tv.decrease_volume()
        self.tv.decrease_volume()
        assert self.tv.__str__() == 'TV Status: Is on = True, Channel = 0, Volume = 0'

    def test_mute(self):
        self.tv.power()
        self.tv.increase_volume()
        self.tv.increase_volume()
        self.tv.increase_volume()
        assert self.tv.__str__() == 'TV Status: Is on = True, Channel = 0, Volume = 3'
        self.tv.mute()
        assert self.tv.__str__() == 'TV Status: Is on = True, Channel = 0, Volume = 0'
        self.tv.mute()
        assert self.tv.__str__() == 'TV Status: Is on = True, Channel = 0, Volume = 3'
        self.tv.mute()
        self.tv.increase_volume()
        assert self.tv.__str__() == 'TV Status: Is on = True, Channel = 0, Volume = 4'










