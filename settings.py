class Settings():

    def __new__(cls):
        # Singleton
        if not hasattr(cls, 'instance'):
            cls.instance = super(Settings, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        # Параметры экрана
        self.window_name = "UFOs"
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
