import psycopg2
import time
import pyodbc
import telepot




bot = telepot.Bot('---------')
chat_id = -......



  def ms_212():
        constr = ''
        mscon = pyodbc.connect(constr)
        mscur = mscon.cursor()
        qry = ""
        exe = mscur.execute(qry)
        fe = exe.fetchall()
        mscon.commit()
        for l in fe:
            print('Server-212', l, end='\n')
            bot.sendMessage(chat_id, f"'Server-212', {l}")




  def ms_46():
        constr = ''
        mscon = pyodbc.connect(constr)
        mscur = mscon.cursor()
        qry = ""
        exe = mscur.execute(qry)
        fe = exe.fetchall()
        mscon.commit()
        for ll in fe:
          print('Server-46', ll, end='\n')
          bot.sendMessage(chat_id, f"'Server-46', {ll}")
        bot.sendMessage(chat_id, '--------------------------')



  def airflow():
        connection = psycopg2.connect(user="",
                                      password="",
                                      database='',
                                      host="",
                                      port="")
        cursor = connection.cursor()
        select = """  """
        cursor.execute(select)
        c = cursor.fetchall()
        if c == []:
            print('Airflow - Ошибок нет')
            bot.sendMessage(chat_id,'Airflow:  Ошибок нет')
            print('----------')
            bot.sendMessage(chat_id, '--------------------------')
        else:
         print('Airflow')
         bot.sendMessage(chat_id, 'Airflow')
         print(c)
         bot.sendMessage(chat_id, f'{c}')
         print('----------')
         bot.sendMessage(chat_id, '--------------------------')
         