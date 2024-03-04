import tkinter as tk
root=tk.Tk()
root.geometry("500x500")
root.title("BMI CALCULATOR")
fr=tk.Frame()
fr.columnconfigure(0,weight=1)
fr.columnconfigure(1,weight=1)
fr.pack()

out=tk.Label(fr,text="Please enter weight   ",font=('Georgia',15))
out.grid(row=1,column=0,sticky=tk.W+tk.E)
weight=tk.Text(fr,height=1,width=10,font=('Ariel',18))

weight.grid(row=1,column=1,sticky=tk.W+tk.E)
out=tk.Label(fr,text="Please enter height   ",font=('Georgia',15))
out.grid(row=2,column=0,sticky=tk.W+tk.E)
height=tk.Text(fr,height=1,width=10,font=('Ariel',18))
height.grid(row=2,column=1,sticky=tk.W+tk.E)
res=tk.Label(fr,text="your BMI is   ",font=('Georgia',20))

out=tk.Text(fr,height=1,width=10,font=('Ariel',18))
out.grid(row=3,column=1,sticky=tk.W+tk.E)

inss=tk.Menubutton(root,text="Click",height=3,width=2)
inss.pack
root.mainloop()
