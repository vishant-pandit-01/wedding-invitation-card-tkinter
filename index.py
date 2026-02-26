from tkinter import *
root=Tk()
root.geometry("450x550")
root.title("invitation")
root.config(bg="pink")

frame=Frame(root,bg="pink",highlightbackground="red",highlightthickness=3)
frame.place(relx=0.5,rely=0.5,anchor="center",height=530,width=430)

design_label=Label(frame, text="🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸",bg="pink", fg="red",font=("times new roman",15))
design_label.pack(pady=(0,1))

date_label=Label(frame,text="Save the date\nTwo souls,One heart,One beautiful beginning",background="pink",foreground="red",font=("Helvetica",12,"italic"))
date_label.pack(pady=(15,5))

name_label=Label(frame,text="ANJALI\n&\nGAURAV",font=("times now roman",30,"bold"),background="pink",foreground="red")
name_label.pack(pady=(12,1))


married_label=Label(frame,text="ARE GETTING MARRIED",font=("Helvetica",10,"italic"),background="pink",foreground="red")
married_label.pack(pady=(0,15))


data_label=Label(frame,text="TUESDAY, SEPTEMBER 25TH\nAT 7 O'CLOCK IN THE EVENING\n\nTHE ROYAL PALACE\nSECTOR 12 BLOOM STREET",bg="pink",foreground="red",font=("times new roman",15,"italic"))
data_label.pack(pady=(0,0))

bless_label=Label(frame, text="Your Presence Will be Our Greatest Blessing",bg="pink", fg="red",font=("Helvetica",9,"italic"))
bless_label.pack(pady=(5,5))


recep_label=Label(frame, text="RECEPTION TO FOLLOW", font=("Helvetica", 9 , "italic"),background="pink", foreground="red")
recep_label.pack(pady=(32,0))

design_label=Label(frame,text="🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸",bg="pink",foreground="red",font=("times now roman",15))
design_label.pack(pady=(4,0))
root.mainloop()

