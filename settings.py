class Settings:

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

        # Параметры корабля
        self.ship_speed_factor = 1.5

        # Параметры пули
        self.bullet_speed_factor = 1
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 5

        # Параметры пришельцев
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet_direction = 1 обозначает движение вправо; а -1 - влево.
        self.fleet_direction = 1

