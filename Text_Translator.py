from tkinter import * #module based on UI
import googletrans #based on google translate 
import textblob #module use to process textual data
from tkinter import ttk, messagebox 
import pyttsx3  #module used to convert text to speech 


   
#Main Window Atributes
root=Tk()
root.title("Text Translator") #tite of the Application
root.geometry("880x300") #shape of the application


#function used to translate the input text                      
def translate_it():
    #deletes any previous translated texts
    translated_text.delete(1.0,END)
    try:
        #get lang from dict keys
        #get the from language key
        for key, value in languages.items():
            if(value==original_combo.get()):
                from_language_key=key

        #get the to language key
        for key, value in languages.items():
            if(value==translated_combo.get()):
                to_language_key=key

        #turn original text to textblob
        words=textblob.TextBlob(original_text.get(1.0,END))

        #translate Text
        words=words.translate(from_lang=from_language_key,to=to_language_key)

        #output translated text to screen 
        translated_text.insert(1.0,words)

        #initialize the spech engine
        engine= pyttsx3.init()
        rate = engine.getProperty('rate')
        #print (rate)
        engine.setProperty('rate', 150) # Increase the Speed Rate x1.25
        voices = engine.getProperty('voices')       #getting details of current voice
        #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
        #changing index, changes voices. 1 for female
        engine.setProperty('voice', voices[1].id)
        engine.say(words)
        #changing index, changes voices. 1 for female
        engine.runAndWait()

    except Exception as e:  
        messagebox.showerror("Translator",e) #messagebox is dispalyed if there is some error 
        #but program doesnt terminates



#clears the text on both sides
def clear():
    original_text.delete(1.0,END)
    translated_text.delete(1.0,END)


#laguages from google trans lib
languages =googletrans.LANGUAGES

  
#converted languges to list 
language_list=list(languages.values())




#text boxes
original_text=Text(root,height=12,width=40)
original_text.grid(row=0,column=0,pady=20,padx=10)

translate_button=Button(root,text="Translate!",font=("Helvetica",24),command=translate_it )
translate_button.grid(row=0,column=1,padx=10)

translated_text=Text(root,height=12,width=40)
translated_text.grid(row=0,column=2,pady=20,padx=10)


#comboboxes
original_combo=ttk.Combobox(root,width=50,value=language_list)
original_combo.current(21)
original_combo.grid(row=1,column=0)

translated_combo=ttk.Combobox(root,width=50,value=language_list)
translated_combo.current(26)
translated_combo.grid(row=1,column=2)


#clear button
clear_button=Button(root,text="Clear",font=("Helvetica",10),command=clear,width=15,height=2)
clear_button.grid(row=1,column=1)


#main execution 
root.mainloop()
