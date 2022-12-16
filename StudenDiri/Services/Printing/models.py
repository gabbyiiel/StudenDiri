from StudenDiri import mysql

class PrintingService:
    @staticmethod
    def add_print_request(file,no_copies,specification):
        cur = mysql.connection.cursor()

        try:
            cur.execute(f''' INSERT INTO `printing` (`orderID`, `file`, `number_of_copies`, `specification`) VALUES ('', '{file}', '{no_copies}', '{specification}')''')
            mysql.connection.commit()
            return print('sakto na ang print')  
        except Exception as e:
            print(e)

    @staticmethod
    def get_print_request():
        cur = mysql.connection.cursor()