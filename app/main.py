import customtkinter

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__() 
        self.InitializeComponent()
         
    def InitializeComponent(self):
        
        self.title("ventana calis")
        self.geometry('400x500')
        self.resizable(False, False)
        
        #----- BOTONES
        #-- Btn Nueva Ventana 
        self.btnVentana = customtkinter.CTkButton(self, text="my button")
        self.btnVentana.grid(row=0, column=0, padx=20, pady=20)
        
        
if __name__ == '__main__':
    app = App()
    app.mainloop()