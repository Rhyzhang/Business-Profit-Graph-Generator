import csv
import tkinter as tk

import matplotlib.pyplot as plt


def get_data():
    with open('data.txt', 'r') as csvfile:
        plots= csv.reader(csvfile, delimiter=',')
        for row in plots:
            date.append(str(row[0]))
            profit.append(int(row[1]))

def store_data():
    """Stores the data into csv file"""
    with open('data.txt', 'a+', newline='') as file:
        for data in every_new_data:
            file.write("\n")
            file.write(', '.join(data))

def add_data():
    """add_data command for adding the new data"""
    new_data = []

    #Gets inputs
    new_date = date_entry.get()
    new_profit = profit_entry.get()

    #Adds the input to new data
    new_data.append(new_date)
    new_data.append(new_profit)

    #Add the new_data to every_new_data
    every_new_data.append(new_data)

    date_entry.delete(0, 'end')
    profit_entry.delete(0, 'end')

    #Stores the data
    store_data()

def generate_graph():
    """Draws the graph"""

    #Gets data
    date.clear()
    profit.clear()
    get_data()

    #Draws the graph
    plt.plot(date,profit, marker='o')

    plt.title('Business Profit Graph')

    plt.xlabel('Date')
    plt.ylabel('Profit')

    plt.show()

"""
Variables for functions
"""
new_data = []
every_new_data = []
date=[]
profit=[]




"""
Code for GUI
"""
root = tk.Tk()
root.title("Business Profit Graph")

#Entry for Date
date_entry = tk.Entry(root, borderwidth=5)
date_entry.insert(0, "Date")
date_entry.grid(row=0, column=0)

#Entry for Profit
profit_entry = tk.Entry(root, borderwidth=5)
profit_entry.insert(0, "Profit")
profit_entry.grid(row=1, column=0)

#Add Button
add_button = tk.Button(root, text="Add", padx=30, pady=30, command=add_data)
add_button.grid(row=0, column=1, rowspan=2)

#Generate Button
generate_button = tk.Button(root, text="Generate",  padx=30, pady=30, command=generate_graph)
generate_button.grid(row=3, column=0, columnspan=2)

root.grid_rowconfigure(3, minsize=200)

root.mainloop()
