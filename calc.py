from Tkinter import *
import tkMessageBox
import ScrolledText
import matplotlib.pyplot as plt
import numpy as np
from tkFileDialog import askopenfilename,asksaveasfilename
import FileDialog
import warnings,webbrowser

class Koushik(object):


    def __init__(self,master):
        self.master=master
        master.title("RLC")
        master.iconbitmap(default="SLR.ico")
        menu=Menu(master)


        master.config(menu=menu)


        subMenu=Menu(menu,tearoff=0)
        menu.add_cascade(label="File",menu=subMenu)
        subMenu.add_command(label="Open",command=self.open_f)
        subMenu.add_command(label="Save",command=self.save)
        subMenu.add_separator()
        subMenu.add_command(label="Exit",command=master.quit)


        subMenu2=Menu(menu,tearoff=0)
        menu.add_cascade(label="Plot",menu=subMenu2)
        subMenu2.add_command(label="Regression Plot",command=self.plot)
        subMenu2.add_command(label="Cubic Spline PLot",command=self.cubic_spline_plot)
        subMenu2.add_separator()
        subMenu2.add_command(label="Useful data",command=self.useful_data)


        subMenu1=Menu(menu,tearoff=0)
        menu.add_cascade(label="Help",menu=subMenu1)
        subMenu1.add_command(label="Help",command=self.help)
        subMenu1.add_command(label="About",command=self.about)
        subMenu1.add_command(label="Contact author",command=lambda : webbrowser.open("https://www.facebook.com/koushik.naskar3"))




        self.label2=Label(master,text="Regression line claculator",font = "Helvetica 13 bold italic")
        self.label2.grid(row=0,column=0,columnspan=20)


        self.label=Label(master,text="Enter the data here:")
        self.label.grid(row=1,columnspan=20)


        self.textfield = ScrolledText.ScrolledText(master,wrap=WORD,width=15,height=10)
        self.textfield.grid(row=2,column=0,columnspan=20,pady=15)

        self.label3=Label(master,text="Enter the order of polynomial\n you want to fit:",justify=LEFT)
        self.label3.grid(row=3,ipady=3,sticky=W)


        self.E=Entry(master)
        self.E.grid(row=3,column=1,columnspan=20,ipady=10,sticky=E)
        self.E.bind("<Return>",self.enter)
        self.E.insert(INSERT,1)


        self.p=Button(master,text="Calculate",command=self.clicked,bg="grey")
        self.p.grid(row=6,column=0,pady=10,columnspan=20)


        self.label3=Label(master,text="The Regression line is:")
        self.label3.grid(row=7,sticky=W)
        self.label3.grid_remove()

        self.text=Text(master,background=master.cget("background"),width=3,height=3, borderwidth=0,font="Helvetica 9 italic")
        self.text.grid(row=8,columnspan=10)

        self.b1=Button(master,text="Useful data",command=self.useful_data,bg="grey")
        self.b2=Button(master,text="Plot",command=self.plot,bg="grey")
        self.b1.grid(row=9,sticky=W,columnspan=20)
        self.b2.grid(row=9,sticky=E,columnspan=20)

        self.lll=Label(master,text="Get values of x-y:")
        self.lll.grid(row=10,sticky=W,columnspan=20)

        self.ll1=Label(master,text="\t    x=")
        self.ll1.grid(row=11,sticky=W,columnspan=20)
        self.E1=Entry(master)
        self.E1.bind("<KeyRelease>",self.test1)
        self.E1.grid(row=11,columnspan=20,sticky=E)

        self.ll2=Label(master,text="\t    y=")
        self.ll2.grid(row=12,columnspan=20,sticky=W)
        self.E2=Entry(master)
        # self.E2.bind("<KeyRelease>",self.test2)      
        self.E2.grid(row=12,columnspan=20,sticky=E)
        self.forget()

        self.label9=Label(master,text="$$$___Coded by Koushik Naskar___$$$",font="Verdana 9 italic",bg="grey",pady=7)
        self.label9.grid(row=15,columnspan=20,sticky=W+E+N+S)


        for i in range(15):
            master.grid_rowconfigure(i, weight=1)
        for i in range(20):
            master.grid_columnconfigure(i, weight=1)



    def forget(self):
        self.b1.grid_remove()
        self.b2.grid_remove()
        self.lll.grid_remove()
        self.ll1.grid_remove()
        self.ll2.grid_remove()
        self.E1.grid_remove()
        self.E2.grid_remove()

    def recall(self):
        self.b1.grid()
        self.b2.grid()
        self.lll.grid()
        self.ll1.grid()
        self.ll2.grid()
        self.E1.grid()
        self.E2.grid()


#E1==x  E2==y
    def test1(self,event):
        p=self.E1.get()
        if p=="":p=0
        p=np.polynomial.polynomial.polyval(float(p),self.k)
        self.E2.delete(0, END)
        self.E2.insert(0,"{:^6}".format(p))



# this functions gets the y for a given x , not working
    def test2(self,event):
        p=self.E2.get()
        if p=="":p=0
        rrr=np.roots(self.k-float(p))
        self.E1.delete(0, END)
        self.E1.insert(0,rrr)




    def help(self):
        tt=Toplevel(self.master)
        text="""\
        Enter x and y with a space in sepate lines
        like:
        x1 y1
        x2 y2
        etc.
        Also you can copy paste excel/spreadsheet data.
        Or you can import in txt/csv file.

        Remember:  You should enter the order of the polynomial
        less than the number of data you entered.

        Once you have calculated the regression line some other 
        function will be available to use. You can plot the data
        (regression + spline plot), get some useful data or get 
        value of y for a given x.

        You can save your data in txt and csv file.


        Contact the author for any query or bug fix.
        """
        tt.title("Help")
        st=ScrolledText.ScrolledText(tt,width=70)
        st.pack()
        st.insert(INSERT, text)
        st.configure(state=DISABLED)


    def about(self):
        text="""
        Regression Line Calculator\n\
        \tVersion : 1.5\n\n\
        This is a application created by Koushik Naskar, to claculate \n\
        and plot the N-th order polynomial fit for a given 2D data\n\
        using Least Square Method.\n\n """+\
        "      Copyright: " +u"\u00a9"+ "  Koushik Naskar, March 2016.\n\n"
        tkMessageBox.showinfo("About",text)


    def open_f(self):
        f=askopenfilename(filetypes=[('csv','*.csv'),('Text file','*.txt')],defaultextension='.csv')
        if f =="": # asksaveasfile return `None` if dialog closed with "cancel".
            return
        ext=f.split(".")[-1]
        with open(f,"r") as g:
            data=g.read()
        self.textfield.delete("1.0",END)
        if ext=="csv":
            data=data.replace(","," ")
        self.textfield.insert(INSERT,data)
        self.text.delete("1.0",END)
        self.forget()


    def save(self):
        f = asksaveasfilename(initialfile="data",title="Save your data",defaultextension='.csv',
                            filetypes=[('csv','*.csv'),('Text file','*.txt')])
        if f == "": # asksaveasfile return `None` if dialog closed with "cancel".
            return
        data=self.get_data()
        ext=f.split(".")[-1]
        if ext=="csv":
            text2save="\n".join(",".join(str(j) for j in i) for i in data)
        elif ext=="txt":            
            text2save="\n".join(" ".join(str(j) for j in i) for i in data)
        with open(f,"w") as g:
            g.write(text2save)





    def enter(self,event):
        self.clicked()



    def plot(self):
        try:
            self.make_plot()
        except:
            tkMessageBox.showerror("Error!!!","Something Wrong.\nCheck your input\n\nNote: First claculate the regression line")



    def get_data(self):
        p=self.textfield.get("1.0", END)
        try:
            p = p.split("\n")
            p = filter(None,p)
            try:
                p=[map(float,filter(None,i.split(" "))) for i in p]
            except:
                p=[map(float,filter(None,i.split("\t"))) for i in p]
            return p
        except:
            return None


    def clicked(self):
        self.AA=0                           #flush the previous data
        self.A=0
        self.k=0
        self.text.delete('1.0', "end-1c")
        p=self.get_data()
        self.forget()
        if p:
            try:
                self.order = int(self.E.get())
                self.x,self.y=zip(*p)  
            except:
                   tkMessageBox.showerror("Error!!!","Something wrong with the data")
                   return       
            self.get_line()
        else:
            tkMessageBox.showerror("Error!!!","No data given")
            return
        self.recall()




    def get_line(self): 
        x=self.x 
        y=self.y 

        n=self.order+1                                                  #number of coefficients is one larger than order


        self.AA=[sum(xx**i for xx in x) for i in xrange(2*n-1)]                        
        self.A=[self.AA[i:i+n]for i in xrange(n)]
        self.B=[sum(a*(b**i) for a,b in zip(y,x)) for i in xrange(n)]


        self.k=k=np.linalg.solve(self.A,self.B)                          #numpy.inalg library introduced to speed up code






        def f(x):
            p=round(x,4)
            if p>=0: return " +"+str(p)
            else : return " "+ str(p)
            # return "{:^+.4f}".format(x)          #this line does the same but keeps the triling zeros

        self.label3.grid()

                                            

        self.text.tag_configure("s", offset=5)       #write the regression function on result


        self.text.insert("insert","y = "+str(round(k[0],4)) +f(k[1])+"x")        
        for i in xrange(2,n):            
            self.text.insert("insert",f(k[i])+"x","",str(i),"s")




        self.text.configure(width=10+n*8)                   #change text width, taken by trial

        




    def make_plot(self):
        x=self.x 
        y=self.y
        k=self.k
        n=len(k)
        f=lambda x: sum(k[i]*(x**i) for i in xrange(n))


        #this is to write the regression line on plot


        q=["{:^5.4f}".format(k[0])]
        for i in xrange(1,n):
            w="{:^+5.4f}x^{{{}}}".format(k[i],i)     #puts the sign
            q.append(w)

        txt1="y = "+"  ".join(e for e in q)
        txt="$"+txt1+"$"



        x_min=min(x)-2
        x_max=max(x)+2
        y_min=min(y)-2
        y_max=max(y)+2

        oz=1.5*(y_max-y_min )/10.0

        xx=np.arange(x_min-.5,x_max+.5,.01)
        m = f(xx)
        plt.axis([x_min,x_max,y_min,y_max])
        plt.title("Regression Line Plot",style='italic')
        plt.xlabel('Value of x')
        plt.ylabel('Value of y')
        plt.plot(x,y,"rs",label="data points")
        plt.plot(xx,m,"b-",label="regression line")
        plt.text(x_min+.5,y_max-oz,"$Regression\ line:$\n"+txt,fontsize=15)
        plt.legend()
        plt.show()



    def useful_data(self):
        self.clicked()
        a=self.AA
        b=self.B
        m=len(a)
        n=len(b)
        p=max( len(str(a[-1])), len(str(b[-1])))+4
        test="$N={}${:^40}$\sum_{{i=1}}^{{N}}y_i={}$\n".format(a[0],"",b[0])
        test+="$\sum_{{i=1}}^{{N}} x_i={}${:^8}$\sum_{{i=1}}^{{N}} x_i^{{{}}}={}${:^8}$\sum_{{i=1}}^{{N}} x_iy_i={}$\n"\
        .format(a[1],"",2,a[2]," ",b[1])

        for i in xrange(2,n):
            test+="$\sum_{{i=1}}^{{N}} x_i^{{{}}}={}$ {:^8} $\sum_{{i=1}}^{{N}} x_i^{{{}}}={}$ {:^8} $\sum_{{i=1}}^{{N}} x_i^{{{}}}y_i={}$\n"\
            .format((2*i-1),a[(2*i-1)]," ",2*i,a[2*i]," ",i,b[i])

        
        plt.figure(num=None, figsize=(10, 10), dpi=80, facecolor='w', edgecolor='k')
        plt.plot([1,m],[1,3*m],"w-",alpha=0)    #make a blanck
        plt.axis([1,m,1,m])
        plt.axis('off')
        plt.text(1,1,test,fontsize=15)
        plt.show()



    def cubic_spline_plot(self):
        p=self.textfield.get("1.0", END)
        try:
            p = p.split("\n")
            p = filter(None,p)
            try:
                p=[map(float,filter(None,i.split(" "))) for i in p]
            except:
                p=[map(float,filter(None,i.split("\t"))) for i in p]
            x,y=zip(*p)
            self.x=x 
            self.y=y
        except:
            tkMessageBox.showerror("Error!!!","Something wrong with your input")
            return

        n=len(x)
        h=[x[i+1]-x[i] for i in xrange(n-1)]
        b=[(y[i+1]-y[i])/h[i] for i in xrange(n-1)]



        u,v=[0.0]*(n-1),[0.0]*(n-1)

        u[1]=2*(h[0]+h[1])
        v[1]=6*(b[1]-b[0])




        for i in xrange(2,n-1):
            u[i]=2*(h[i]+h[i-1]) -(h[i-1])**2/u[i-1]
            v[i]=6*(b[i]-b[i-1])- (h[i-1]*v[i-1])/u[i-1]


        z=[0.0]*n


        for i in xrange(n-2,0,-1):
            z[i]=(v[i]-h[i]*z[i+1])/u[i]




        def g(p):
            for i in xrange(n-1):
                if x[i+1]>=p>=x[i]:
                    s=(z[i+1]*(p - x[i])**3  + z[i]*(x[i+1]-p)**3 )/(6*h[i])  + \
                    (y[i+1]/h[i] - h[i]*z[i+1]/6)*(p-x[i])  +  \
                    (y[i]/h[i] - h[i]*z[i]/6)*(x[i+1]-p)
                    return s

        x_min=min(x)-2
        x_max=max(x)+2
        y_min=min(y)-2
        y_max=max(y)+2

        xx=np.arange(x_min-.5,x_max+.5,.01)
        m = [g(q) for q in xx]
        plt.axis([x_min,x_max,y_min,y_max])
        plt.title("Cubic Spline Plot",style='italic')
        plt.xlabel('Value of x')
        plt.ylabel('Value of y')
        plt.plot(x,y,"rs",label="data points")
        plt.plot(xx,m,"g-",label="Spline line")
        plt.legend()
        plt.show()




if __name__=="__main__":
    root=Tk()
    app=Koushik(root)

    root.mainloop()
