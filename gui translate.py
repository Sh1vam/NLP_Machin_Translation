
from transformers import MBartForConditionalGeneration, MBart50TokenizerFast

model = MBartForConditionalGeneration.from_pretrained("facebook/mbart-large-50-one-to-many-mmt")

tokenizer = MBart50TokenizerFast.from_pretrained("facebook/mbart-large-50-one-to-many-mmt", src_lang="en_XX")

from tkinter import *
from tkinter import ttk

class Root(Tk):
    
    def __init__(self):
        
        super(Root, self).__init__()
        
        self.title("Text Translator")
        self.minsize(5, 5)
        
        self.labelFrame = ttk.LabelFrame(self, text = "SELECT")
        self.labelFrame.grid(column = 0, row = 2, padx = 10, pady = 10)
        
        self.labelFrame2=ttk.LabelFrame(self, text = "SUBMIT")
        self.labelFrame2.grid(column = 0, row = 1, padx = 10, pady = 10)
        self.button()

    def button(self):

        self.button = ttk.Button(self.labelFrame, text = "Select Language To Translate",command = self.Dropdown)
        self.button.grid(column = 0, row = 0)
        
        self.text_area = Text(self, height=5, width=20, font=("",15))
        self.text_area.grid()
        
        self.button2 = ttk.Button(self.labelFrame2, text = "Enter Text To Translate",command = self.Input)
        self.button2.grid(column = 3, row = 5)

        self.output_area = Text(self, height=5, width=20, font=("", 15))
        self.output_area.grid()

    def Dropdown(self):
        
        self.language_var = StringVar()
        self.language_dropdown = ttk.Combobox(self.labelFrame, textvariable=self.language_var)
        self.language_dropdown['values'] = ["hi_IN", "ta_IN"]
        self.language_dropdown.grid(column=0, row=1)
        
    def Input(self):

        global article_en
        article_en = self.text_area.get("1.0", "end-1c")
    
        #print(self.language_var.get())
        model_inputs = tokenizer(article_en, return_tensors="pt")

        generated_tokens = model.generate(
            **model_inputs,
            forced_bos_token_id=tokenizer.lang_code_to_id[self.language_var.get()]
        )
        translation = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
        
        self.output_area.delete("1.0", "end-1c")
        self.output_area.insert(END, translation[0])
       
root = Root()
root.mainloop()
