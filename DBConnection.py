import mysql.connector
class ABC:

    def DBConnect(self, msg):

        conn = mysql.connector.connect(user='root',
                               password='cuixiang0711',
                               host='localhost',
                               database='stockDB')

        #print(SelectQuery())
        print("Connected")
        print("msg is " + msg)
        cursor = conn.cursor()

        #Select_query = "SELECT * FROM tb_Historical"
        #Select_query = SelectQuery()
        #print(SelectQuery())
        cursor.execute(msg)
        conn.commit()
        print("Inserted")

        for(stock_date,
            stock_ticker,
            open_price,
            high,
            low,
            close_price,
            adj_close,
            volume,
            dividend
            ) in cursor:
            print("stock_date is {}, open price is {}, high is {}, low is {}, close price is {}, adj close is {}, volume is {}, dividend is {}".format(stock_date, stock_ticker,open_price,high,low,close_price,adj_close,volume,dividend))
        cursor.close()

        conn.close()

    #def InsertData():
        #return "INSERT INTO tb_Historical (stock_date,
        #                                          stock_ticker,
        #                                          open_price,
        #                                          high,
        #                                          low,
        #                                          close_price,
        #                                          adj_close,
        #                                          volume,
        #                                          dividend) VALUES
        #                                          ('2018-3-20',
        #                                           'BABA',
        #                                            1150,
        #                                            1230,
        #                                            1111,
        #                                            4431231234,
        #                                            534243242);
