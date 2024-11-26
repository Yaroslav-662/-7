from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime

# Налаштування бази даних
engine = create_engine('sqlite:///notes.db', echo=False)
Base = declarative_base()

# Модель таблиці Notes
class Note(Base):
    __tablename__ = 'notes'

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    content = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now)

# Створення таблиці
Base.metadata.create_all(engine)

# Сесія для взаємодії з базою даних
Session = sessionmaker(bind=engine)
session = Session()

# Функції CRUD
def create_note(title, content):
    new_note = Note(title=title, content=content)
    session.add(new_note)
    session.commit()
    print("Нотатку додано!")

def read_notes():
    notes = session.query(Note).all()
    for note in notes:
        print(f"ID: {note.id} | Title: {note.title} | Created At: {note.created_at}")
        print(f"Content: {note.content}\n")

def update_note(note_id, new_title, new_content):
    note = session.query(Note).filter_by(id=note_id).first()
    if note:
        note.title = new_title
        note.content = new_content
        session.commit()
        print("Нотатку оновлено!")
    else:
        print("Нотатку не знайдено!")

def delete_note(note_id):
    note = session.query(Note).filter_by(id=note_id).first()
    if note:
        session.delete(note)
        session.commit()
        print("Нотатку видалено!")
    else:
        print("Нотатку не знайдено!")

# Головне меню програми
def main():
    while True:
        print("\nМеню:")
        print("1. Додати нотатку")
        print("2. Переглянути всі нотатки")
        print("3. Оновити нотатку")
        print("4. Видалити нотатку")
        print("5. Вийти")

        choice = input("Виберіть опцію: ")
        if choice == "1":
            title = input("Введіть заголовок: ")
            content = input("Введіть зміст: ")
            create_note(title, content)
        elif choice == "2":
            read_notes()
        elif choice == "3":
            note_id = int(input("Введіть ID нотатки: "))
            new_title = input("Введіть новий заголовок: ")
            new_content = input("Введіть новий зміст: ")
            update_note(note_id, new_title, new_content)
        elif choice == "4":
            note_id = int(input("Введіть ID нотатки: "))
            delete_note(note_id)
        elif choice == "5":
            print("До побачення!")
            break
        else:
            print("Невірний вибір, спробуйте ще раз.")

if __name__ == "__main__":
    main()
