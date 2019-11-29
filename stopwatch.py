from tkinter import*
import time

class StopWatch(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self._start = 0.0
        self.waktuSekarang = 0.0
        self.sedangBerjalan = False
        self.waktuString = StringVar()
        self.textStart= StringVar()
        self.textStart.set('Start')
        parent.configure(background='light blue')
        parent.title('stopwatch')
        self.buatTeks()
        self.buatKolom()
        self.buatTombol()
        self.posisi=1

    def buatTeks(self):
        self.teks = Label(self, textvariable=self.waktuString,font="Verdana 19 bold", bg='light blue', fg='blue')
        self.aturWaktu(self.waktuSekarang)
        self.teks.grid(row=0, column=0)

    def perbarui(self):
        self.waktuSekarang = time.time() - self._start
        self.aturWaktu(self.waktuSekarang)
        self._timer = self.after(50, self.perbarui)

    def aturWaktu(self, waktu):
        menit = int(waktu / 60)
        detik = int(waktu - menit * 60.0)
        jam = int((waktu - menit * 60.0 - detik) * 100)
        self.waktuString.set('%02d:%02d:%02d' % (menit, detik, jam))

    def Start(self):
        if not self.sedangBerjalan and self.textStart.get() == 'Start' :
            self.textStart.set('Cetak')
            self._start = time.time() - self.waktuSekarang
            self.perbarui()
            self.sedangBerjalan = True
        elif self.sedangBerjalan and self.textStart.get() == 'Cetak' :
            self.setKolom(str(self.posisi)+ ". " + self.waktuString.get()+"\n")
            self.posisi+=1

    def pause(self):
        if self.sedangBerjalan:
            self.textStart.set('Start')
            self.after_cancel(self._timer)
            self.waktuSekarang = time.time() - self._start
            self.aturWaktu(self.waktuSekarang)
            self.sedangBerjalan = False

    def Reset(self):
        self._start = time.time()
        self.waktuSekarang = 0.0
        self.aturWaktu(self.waktuSekarang)
        self.kolom.config(state=NORMAL)
        self.kolom.delete('1.0',END)
        self.kolom.configure(state=DISABLED)

    def buatKolom(self):
        self.kolom = Text(height=12, width=30, bg='blue', fg='white')
        self.scrollBar()
        self.kolom.grid(row=1,column=0,columnspan=4,pady=4)
        self.kolom.configure(state=DISABLED)

    def setKolom(self, nilai):
        self.kolom.config(state=NORMAL)
        self.kolom.insert(END,nilai)
        self.kolom.configure(state=DISABLED)

    def scrollBar(self):
        scroll = Scrollbar()
        scroll.grid(row=1, column=5, rowspan=1, sticky=N+S+W)
        scroll.config(command=self.kolom.yview)
        self.kolom.config(yscrollcommand=scroll.set)

    def buatTombol(self):
        Button(textvariable=self.textStart, command=self.Start).grid(row=2, column=0)
        Button(text='Pause', command=self.pause).grid(row=2, column=1)
        Button(text='Reset', command=self.Reset).grid(row=2, column=2)
        Button(text='Quit', command=self.quit).grid(row=2, column=3)

def main():
    root = Tk()
    sw = StopWatch(root)
    sw.grid(row=0,column=0, columnspan=4)
    root.mainloop()

if __name__ == '__main__':
    main()



    
