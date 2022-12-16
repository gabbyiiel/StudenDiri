from StudenDiri import mysql

class gcash:
    @staticmethod
    def add_gcash_req(tot,specification):
        cur = mysql.connection.cursor()

        try:
            cur.execute(f''' INSERT INTO `gcash` (`orderID`, `type_of_transaction`, , `specification`) VALUES ('', '{tot}', '{specification}')''')
            mysql.connection.commit()
            return print('sakto na ang gcash?')  
        except Exception as e:
            print(e)

    @staticmethod
    def get_gcash_req():
        cur = mysql.connection.cursor()

        try: