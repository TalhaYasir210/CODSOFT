import tkinter
import tkinter.messagebox
import pickle

root=tkinter.Tk()
root.title("To-Do-List")

def add_task():
    task=entry_task.get()
    if task !="":
        listbox_tasks.insert(tkinter.END,task)
        entry_task.delete(0,tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="Warning!",message="You must enter a task.")

def delete_task():
    try:
        task_index=listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except:
        tkinter.messagebox.showwarning(title="Warning!",message="You must select a task.")

def load_task():
    try:
        tasks= pickle.load(open("tasks.dat", "rb"))
        listbox_tasks.delete(0, tkinter.END)
        for task in tasks:
            listbox_tasks.insert(tkinter.END, task)
    except:
        tkinter.messagebox.showwarning(title="Warning!",message="No data file present.")

def save_task():
    tasks=listbox_tasks.get(0, listbox_tasks.size())
    pickle.dump(tasks, open("tasks.dat" , "wb"))

#create GUI
listbox_tasks=tkinter.Listbox(root, height=15 , width=50 , bg="black" , fg="#ffffff")
listbox_tasks.pack()
entry_task=tkinter.Entry(root, width=50 , bg="grey" ,fg="black")
entry_task.pack()

button_add_task=tkinter.Button(root, text="Add Task",width=48,command=add_task , bg="red" , fg="white")
button_add_task.pack()

button_delete_task=tkinter.Button(root, text="Delete Task",width=48,command=delete_task,bg="orange" , fg="white")
button_delete_task.pack()

button_load_task=tkinter.Button(root, text="Load Task",width=48,command=load_task,bg="green" , fg="white")
button_load_task.pack()

button_save_task=tkinter.Button(root, text="Save Task",width=48,command=save_task,bg="blue" , fg="white")
button_save_task.pack()




root.mainloop()