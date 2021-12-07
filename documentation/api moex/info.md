# Заметки по API Московской биржи


## получение основных данных
1. engines - идентификатор в ИСС
2. markets - рынок на котором торгуется бумага
3. boards - режим торгов

### Получить данные
1. [Получить список идентификаторов (engines)](http://iss.moex.com/iss/engines.xml)
2. [Получить список рынков (markets)](http://iss.moex.com/iss/engines/[engines]/markets.xml)
3. [Получить список режимы тогов (boards)](http://iss.moex.com/iss/engines/[engines]/markets/[markets]/boards.xml)

### Пример для фьючер золота
1. engines = futures   
2. markets = forts
3. boards = RFUD 
4. securities = GDZ1
5. boardgroup =45

### Получаемые данные 
[Данные по запросу](https://iss.moex.com/iss/engines/futures/markets/forts/boards/RFUD/securities/GDZ1.xml)
* SECID - наименование (GDZ1)
* BOARDID - режим торгов
* SHORTNAME - короткое имя (GOLD-12.21)
* SECNAME - (Фьючерсный контракт GOLD-12.21)
* PREVSETTLEPRICE - ПРЕДВАРИТЕЛЬНАЯ ЦЕНА
* STATUS
* DECIMALS
* MINSTEP
* LASTTRADEDATE - ДАТА ПОСЛЕДНЕЙ ТОРГОВЛИ
* LASTDELDATE - ПОСЛЕДНЯЯ ДАТА
* SECTYPE - РАЗДЕЛ (GD)
* LATNAME - (GOLD-12.21)
* ASSETCODE - АКТИВНЫЙ КОД
* PREVOPENPOSITION - ПРЕДВАРИТЕЛЬНОЕ ПОЛОЖЕНИЕ
* LOTVOLUME - минимальный объем
* INITIALMARGIN - НАЧАЛЬНАЯ МАРЖА
* HIGHLIMIT - ВЫСОКИЙ ПРЕДЕЛ
* LOWLIMIT - НИЗКИЙ ПРЕДЕЛ
* STEPPRICE - ШАГОВАЯ ЦЕНА
* LASTSETTLEPRICE - ПОСЛЕДНЯЯ РАСЧЕТНАЯ ЦЕНА
* PREVPRICE - ПРЕДВАРИТЕЛЬНАЯ ЦЕНА
* FIRSTTRADEDATE - ПЕРВАЯ ПРОДАЖА


## Получение исторических данных
https://iss.moex.com/iss/history/engines/futures/markets/forts/boards/FIQS/securities/GDH2
http://iss.moex.com/iss/history/engines/stock/markets/index/securities.json?date=2010-08-20

https://iss.moex.com/iss/engines/futures/markets/forts/boards/FIQS/securities/GDH2/orderbook
https://iss.moex.com/iss/engines/futures/markets/forts/boardgroups//orderbook

https://iss.moex.com/iss/engines/futures/markets/forts/boards/RFUD/securities/GDZ1.json

    engines = 'futures'
    markets = 'forts'
    boards = 'RFUD'
    securities = 'GDZ1'

https://iss.moex.com/iss/engines/futures/markets/forts/securities/GDZ1

https://iss.moex.com/cs/engines/futures/markets/forts/boardgroups/45/securities/GDZ1.hs?s1.type=candles&interval=1&candles=500&indicators=&_=1638856206896
https://iss.moex.com/cs/engines/futures/markets/forts/boardgroups/45/securities/GDZ1.hs?s1.type=candles&interval=1&candles=500&indicators=&_=1638856206896
https://iss.moex.com/cs/engines/futures/markets/forts/boardgroups/45/securities/GDZ1.xml?interval=1&candles=500&s1.type=candles

https://iss.moex.com/cs/engines/futures/markets/forts/boardgroups/45/securities/GDZ1.xml?interval=1&candles=500&s1.type=candles


## ссылки
* [справочник запросов](https://iss.moex.com/iss/reference/)
* [Авторизация](https://passport.moex.com/authenticate)
* [библиотека для API](https://github.com/WLM1ke/aiomoex)
