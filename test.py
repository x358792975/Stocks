from DBConnection import ABC
insertQ = "INSERT INTO tb_Historical(stock_date,stock_ticker,open_price,high,low,close_price,adj_close,volume,dividend)VALUES('2018-6-27','GOOGL',152,122,1151,1231,1112,44331234,243242)"
selectQ = "SELECT * FROM tb_Historical"
deleteQ = "DELETE FROM tb_Historical where open_price = 120"
mytest = ABC();
mytest.DBConnect(deleteQ)
#mytest.DBConnect(selectQ)
