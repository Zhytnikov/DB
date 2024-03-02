from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from my_select import *

# Підключення до бази даних
engine = create_engine('postgresql://sasha:1234@localhost:5432/db')
Session = sessionmaker(bind=engine)
session = Session()

try:
    # Виклик функцій з файлу my_select.py
    result_1 = select_1(session)
    print("Result of select_1:", result_1)

    result_2 = select_2(session, "Math")
    print("Result of select_2:", result_2)

    result_3 = select_3(session, "Math")
    print("Result of select_3:", result_3)

    result_4 = select_4(session)
    print("Result of select_4:", result_4)

    result_5 = select_5(session, "John Doe")
    print("Result of select_5:", result_5)

    result_6 = select_6(session, "Group A")
    print("Result of select_6:", result_6)

    result_7 = select_7(session, "Group A", "Math")
    print("Result of select_7:", result_7)

    result_8 = select_8(session, "John Doe")
    print("Result of select_8:", result_8)

    result_9 = select_9(session, "John Doe")
    print("Result of select_9:", result_9)

    result_10 = select_10(session, "John Doe", "Bon Smith")
    print("Result of select_10:", result_10)

except Exception as e:
    print("Error occurred:", e)

finally:
    # Закриття сесії
    session.close()
