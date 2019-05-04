class TradeInfo:
    def __init__(self,foods):
        self.total = 0
        self.trades = []
        self.__paprse(foods)

    def __paprse(self,foods):
        self.total = len(foods)
        self.trades = [self.__map_to_trade(single) for single in foods]

    def __map_to_trade(self,single):
        if single.create_datetime:
            time = single.create_datetime.strftime('%Y-%m-%d')
        else:
            time = '未知'
        return dict(
            user_name = single.user.nickname,
            time = time,
            id = single.id
        )