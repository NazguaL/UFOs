import time
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from game_stats import GameStats
from button import Button
from game_functions import check_events
from game_functions import update_bullets
from game_functions import update_screen
from game_functions import create_fleet
from game_functions import update_aliens
from scoreboard import Scoreboard


def run_game():
    # Инициализирует игру и создает объект экрана.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption(ai_settings.window_name)
    # Создание кнопки Play.
    play_button = Button(ai_settings, screen, "Start Play")

    ship = Ship(ai_settings, screen)  # Создание корабля.
    bullets = Group()  # Создание группы для хранения пуль.
    aliens = Group()  # Создание группы пришельцев.
    create_fleet(ai_settings, screen, ship, aliens)  # Создание флота пришельцев.

    # Создание экземпляров GameStats и Scoreboard.
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # Запуск основного цикла игры.
    while True:
        time.sleep(0.0005)  # уменьшение загрузки ЦП
        # Отслеживание событий клавиатуры и мыши.
        check_events(ai_settings, screen, stats, sb, play_button, ship, bullets, aliens)
        # Обновляет позицию корабля.
        if stats.game_active:
            ship.update()
            update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            update_aliens(ai_settings, stats, sb, screen, ship, aliens, bullets)

        # Отображение прорисованного экрана при каждом проходе цикла.
        update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)

if __name__ == "__main__":
    run_game()

#
# ОБ'ЄКТНО-ОРІЄНТОВАНЕ ПРОГРАМУВАННЯ
# - - - - - - - - - - - - - -
# Викладач: Вовк Євгеній Андрійович
#
# Форма контролю: екзамен
#
# ІНДИВІДУАЛЬНЕ ЗАВДАННЯ
# - виконати віконий додаток по роботі з певною об'єктною моделлю. Тематику об'єктної моделі можна прийняти самостійно, якщо є сумніви щодо її актуальності, у цьому випадку, тематику слід погодити із викладачем.
# - немає жорстких вимог щодо технології виконання додатку, мова програмування може бути будь-яка. Головне щоб використовувалися парадигми об'єктно-орієнтованого програмування: принципи SOLID, застосовувалися інтерфейсні посилання та інше.
# - у випадку, якщо хтось вже має напрацьовані додатки, наприклад має комерційний досвід програмування, тоді варто запропонувати і погодити з викладачем даний проект, щоби його зарахувати в якості індивідуального завдання, в якому реалізуються парадигми ООП: SOLID та інш. У випадку, якщо використовувався інший підхід розробки, тоді необхідно обгрунтувати чому саме було прийнято таке рішення, в чому його переваги, грунтовно порівняти його із ООП, щоби викладач побачив що ви володієте ООП і навести приклад використання ООП.
# - для ЗВИЧАЙНОГО завдання викладач рекомендує реалізацію на WinForms, а також, можна говорити про модель де присутній зв'язок сутностей багато до багатьох через третю таблицю чи сутність в залежності від того використовуєте ви бд чи ні
# - можна також використовувати WPF, але на WPF складніше, там реалізується XAML MVVM, тому більше підходить для досвідчених користувачів
# - також бажано реалізувати розбивку на UserControl і завершену логіку поведінки в межах контролу на базі трирівневої архітектури
# - використання MVP буде плюсом
#
# ІСПИТ
# - на іспит виносяться 3 питання: 2 теоретичних і 1 практичний. Тематика питань чітко відповідає темам які розглянуті в презентаціях до курсу
# - у випадку невеликого досвіду програмування, на іспиті будуть задаватися питання по .NET : по самій програмі та рисункам, наведеним в презентації, парадигми ООП, події, делегати, поняття віконного інтерфейсу, шаблони для роботи із віконним інтерфейсом