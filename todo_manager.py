#📁 Projekt 2 – Menedżer zadań (TODO)

#To będzie pierwszy program, który zapamiętuje dane nawet po zamknięciu.
#menu zawierające:
#add task
#show task
#complete task
#delete task
#exit

print("===== TODO =====")
print("1. Add task")
print("2. Show task")
print("3. Complete task")
print("4. Delete task")
print("5. Exit")
#zmienna listy odnosząca się do zadań
tasks= []

#wczytanie pliku txt
with open("tasks.txt", "r") as file:
    for line in file:
        line =line.strip()
        parts = line.split(" | ")
        status = parts[1] == "True"
        tasks.append([parts[0], status])
#funkcja pokazuje liste zadań
def show_tasks(tasks):
    #jeśli nie ma zadań komunikat o braku zadań.
    if not tasks:
        print("Not tasks yet.")
    #jeśli są wyświetla lista zadań ukończonych i nieskończonych.
    else:
        for i, task in enumerate(tasks, start= 1):
            if task[1]:
                print(f"{i}. [x] {task[0]}")
            else:
                print(f"{i}. [ ] {task[0]}")
#pętla while która powtarza zapytanie w chhwili
while True:
    #zmienna wyboru
    choice=int(input("choice option: "))
    #jeśli użytkownik wybierze numer 1 bedzie mógł dodac nowe zadanie
    if choice == 1:
        #zmienna dodawania tasku
        task_name= input("Add task: ")
        tasks.append([task_name, False])
        print("Succesful added task.")
    #Jeśli 2 pokaże liste zadań skończonych i nieskończonych
    elif choice == 2:
        #warunek if sprawdzający czy są dostępne zadania
    #sekcja complete task
        show_tasks(tasks)
    #opcja 3 pokazuje liste zadań i możliwość zaaktualizowania zadania czyzostało ono skończone
    elif choice == 3:
        show_tasks(tasks)
        #zmienna która pyta się uzytkownika jakie zadanie ukończyłeś.
        #zmienna complete pytająca które zadanie ukończyłeś.
        complete= int(input("Which task did you complete?: "))
        #sprawdzanie czy numer jest poprawny
        if 1 <= complete <= len(tasks):
            tasks[complete - 1][1] = True
            print("Suucessfull update task.")
        else:
            print("Don't have this task.")
    #opcja 4 odpowiada za usunięcie zadania z listy
    elif choice == 4:
        show_tasks(tasks)
        #zmienna delete
        delete=int(input("What do you have delete task: "))
        if 1 <= delete <= len(tasks):
            tasks.pop(delete - 1)
            print(f"Succesfuly deleted task number: {delete}")
        else:
            print("Don't have this task.")
    #opcja 5 zapisuje lub tworzy plik z rozrzerzeniem .txt jeżeli nie istnieje i  zamyka aplikacje
    elif choice == 5:
        #Zapis do pliku
        with open("tasks.txt", "w") as file:
            for task in tasks:
                file.write(f"{task[0]} | {task[1]}\n")
        break
    else:
        print("Invalid option")


        

