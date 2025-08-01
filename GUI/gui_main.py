### note ###
# to run this write this in install "ttkbootstrap" package


# imports
from tkinter import *
import ttkbootstrap as tb

# variables
priority_option = ["Critical", "High", "Medium", "Low"]

# set up the root, main window, title,size
root = tb.Window(themename="superhero")
root.title("TODO")
root.geometry("1600x900")

# weight of column for set size of column
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=4)



def new_task_add(root , on_add_callback):
    ## Frame
    # creating the "newTask" frame for widgets
    newtask_frame = tb.Frame(root, bootstyle="dark")
    newtask_frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=50)

    ## Title
    # label task title
    label_title = tb.Label(newtask_frame, text="Task title",
                           font=("Arial", 10),
                           bootstyle="dark,inverse")
    label_title.grid(row=0, column=0, padx=40, pady=5, sticky="w")

    # entry of task title
    title_entry = tb.Entry(newtask_frame, bootstyle="success", font=("Arial", 12), width=40)
    title_entry.grid(row=1, column=0, padx=40, pady=10)

    ##Description
    # Label Description
    label_description = tb.Label(newtask_frame, text="Description",
                                 font=("Arial", 10),
                                 bootstyle="dark,inverse")
    label_description.grid(row=2, column=0, padx=40, pady=5, sticky="w")

    # entry of task title
    description_box = tb.Text(newtask_frame, font=("Arial", 10), height=5, width=40)
    description_box.grid(row=3, column=0, padx=40, pady=5, sticky="w")

    ##Priority
    # label priority
    label_priority = tb.Label(newtask_frame, text="priority",
                              font=("Arial", 10),
                              bootstyle="dark,inverse")
    label_priority.grid(row=4, column=0, padx=40, pady=5, sticky="w")

    # dropdown priority
    priority_combo = tb.Combobox(newtask_frame, values=priority_option, font=("Arial", 10))
    priority_combo.grid(row=5, column=0, padx=40, pady=5, sticky="w")
    priority_combo.set("Medium")

    ##Date
    # label date_entry
    label_date = tb.Label(newtask_frame, text="Date",
                          font=("Arial", 10),
                          bootstyle="dark,inverse")
    label_date.grid(row=6, column=0, padx=40, pady=5, sticky="w")
    # date_entry widget
    date_entry = tb.DateEntry(newtask_frame)
    date_entry.grid(row=7, column=0, padx=40, pady=20, sticky="w")
    
    ## change by Alimate
    ## data_gathering
    def data_gather():
        data_title = title_entry.get()
        data_descript = description_box.get('1.0' , 'end-1c')
        data_priority = priority_combo.get()
        data_date = date_entry.get_date()

        # create a data dictionary to return
        final_output = {
            'Title' : data_title,
            'Description' : data_descript,
            'Priority' : data_priority,
            'Date' : data_date
        }
        return final_output
    
    # for automate the process define the handle function to run automatically
    def handle_click():
        data = data_gather()
        # send data to the out of this function (main.py)
        on_add_callback(data)
    
    ## Add button
    add_button = tb.Button(newtask_frame, text="add task", bootstyle="success" , command=handle_click)
    add_button.grid(row=9, column=0, pady=5)

    # return the data_gather func to receive the data from another file
    return data_gather



def show_all_tasks(root):
    ## Frame
    # Right frame => for showing the list of tasks
    tasklist_frame = tb.Frame(root, bootstyle="dark")
    tasklist_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=50)


