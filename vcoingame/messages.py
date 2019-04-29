class Message:
    Commands = """✌️ Привет! Со мной Вы можете поиграть в игру Орёл-Решка!

Часто задаваемые вопросы: vk.cc/9j8rNr"""
    Score = """💰 Ваш баланс: {}"""

    Deposit = """Пополнить счет можно по следующей ссылке: {}"""
    Withdraw = """Отправьте сумму, которую хотите вывести"""

    Bet = """Пожалуйста, сделайте Вашу ставку:"""
    OverMaxBet = """Ставка слишком высока, максимальная ставка составляет {} коинов. Введите Вашу ставку:"""
    MakeAChoice = """Пожалуйста, сделайте выбор! Выиграйте свои {} коинов!"""
    BetMade = """Ставка сделана, пожалуйста, сделайте свой выбор и сорвите куш в размере {} коинов!"""

    Bum = """😢 На Вашем баланс недостаточно средств.

Вы можете пополнить его нажав на кнопку "Пополнить" 

‼ Не хватает коинов для пополнения? Жмите на "Получить коины"‼"""
    BumLeft = """😢 На Вашем балансе не хватает {} монет!

Вы можете пополнить его нажав на кнопку "Пополнить" 

‼ Не хватает коинов для пополнения? Жмите на "Получить коины"‼"""

    Send = """✅ {} монет было успешно выведено!"""
    Credited = """✅ {} монет успешно зачислены на Ваш баланс!"""

    Lose = """😢 {}, вы проиграли :("""
    Win = """🙂 Поздравляю! Вы выиграли {}!"""

    NotGroupMember = """Не желаете ли подписаться на @vcoingame (нашу группу)?
    
‼Хотите получить МНОГО коинов ничего не делая? Жмите на "Получить коины"‼    """

    Statistics = """Ваша статистика:

Сыграно игр: {}
Выиграно игр: {}
Проиграно игр: {}

Шанс победы: {}%
Ушли в плюс на: {}

Места в доске лидеров:

Сыграно игр: {}
Выиграно игр: {}
Шанс победы: {}
Ушли в плюс: {}
Баланс: {}
        """

    Leaderboards = """Выберите доску почета:"""
    LeaderboardRow = "@id{} (ТОП-{}) - {}\n"
    LeaderboardSeparator = "---------------\n"
    LeaderboardMyPosition = "У вас {}. Вы на {} месте"

    WinrateError = """Винрейт считаетя после 20-и сыгранных игр"""

    VCoinBank = """💰 Получить коины можно по следующей ссылке: {}
    
📝 Перед оплатой обязательно ознакомьтесь с инструкцией: vk.cc/9giWdY"""

    DonationError = """Вы купили коинов на недостаточную сумму. Вам осталось {}$
Воспользуйтесь кнопкой "Получить коины!" для пополнения"""
    RaiseInput = """Пожалуйста, введите на сколько Вы хотите повысить максимальную ставку:"""
    Raise = """Вы успешно повысили макимальную ставку на {}"""
