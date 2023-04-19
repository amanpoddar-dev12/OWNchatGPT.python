
import tkinter as tk
import openai


openai.api_key = "Enter Your api key..."   
# to get  your api key go to the website open ai and then click on api reference and you create your api key to use.

def generate_response(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message


def display_response():
    input_text = input_field.get()
    response = generate_response(input_text)
    output_field.config(state='normal')
    output_field.delete(1.0, tk.END)
    output_field.insert(tk.END, response)
    output_field.config(state='disabled')
def clear():
   input_field.delete(0,tk.END)
    

    
   output_field.delete(1.0,tk.END)

import customtkinter
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


root=customtkinter.CTk()

root.title("OpenAI Chatbot")
root.geometry("600x700")


input_field =customtkinter.CTkEntry(root,width=350,placeholder_text='Enter Your Question...', font=("Arial", 14))
input_field.pack(pady=10)
submit_button = customtkinter.CTkButton(root, text="Submit", font=("Arial", 14), command=display_response)
submit_button.pack(pady=10)

clear_button = customtkinter.CTkButton(root, text="Clear", font=("Arial", 14), command=clear)
clear_button.pack(pady=10)
output_field = tk.Text(root, font=("Arial", 14), state='disabled',bg='black',foreground='white')
output_field.pack(pady=10,padx=20)


root.mainloop()