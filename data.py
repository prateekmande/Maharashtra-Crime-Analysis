import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import pandas as pd
import matplotlib
from statsmodels.tsa.arima_model import ARIMA
from sklearn.metrics import mean_squared_error 
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FingureCanvas
from matplotlib.figure import Figure
import numpy as np
import random
from scipy.constants.constants import alpha

data=pd.read_csv("2012_18.csv",index_col='DISTRICT')
option=['AHMEDNAGAR', 'AKOLA', 'AMRAVATI', 'AURANGABAD', 'BEED', 'BHANDARA',
       'BULDHANA', 'CHANDRAPUR', 'DHULE', 'GADCHIROLI', 'GONDIA', 'HINGOLI',
       'JALGAON', 'JALNA', 'KOLHAPUR', 'LATUR', 'MUMBAI', 'NAGPUR ', 'NANDED',
       'NANDURBAR', 'NASIK ', 'NAVI MUMBAI', 'OSMANABAD', 'PARBHANI', 'PUNE ',
       'RAIGAD', 'RATNAGIRI', 'SANGLI', 'SATARA', 'SINDHUDURG', 'SOLAPUR ',
       'THANE ', 'WARDHA', 'WASHIM', 'YAVATMAL']


x_label=['MURDER', 'ATTEMPT TO MURDER',
          'RAPE', 'KIDNAPPING', 'DACOITY', 'ROBBERY', 'BURGLARY', 'THEFT', 'RIOTS', 
          'CHEATING', 'COUNTERFIETING', 'ARSON', 'HURT/GREVIOUS HURT', 'DOWRY DEATHS', 
          'ASSAULT ON WOMEN', 'CAUSING DEATH BY NEGLIGENCE', 'OTHER IPC CRIMES']

rows=['MURDER', 'MURDER ATTMP.',
          'RAPE', 'KIDNAPPING', 'DACOITY', 'ROBBERY', 'BURGLARY', 'THEFT', 'RIOTS', 
          'CHEATING', 'COUNTERFIETING', 'ARSON', 'HURT', 'DOWRY DEATHS', 
          'ASSAULT ON WOMEN', 'DEATH BY NEGLIGENCE', 'OTHER IPC CRIMES']


class Window(QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 700, 500)
        self.setWindowTitle("DATA ANALYSIS")
        
        self.label=QLabel(self)
        self.label.setText("SELECT DISTRICT:")
        self.label.setFont(QFont('Times',14,QFont.Bold))
        self.label.setGeometry(QRect(600,400,300,100))
        self.label.setStyleSheet("QLabel{color:white;}")
        #self.label.move(30, 375)
        #self.label.setWordWrap(True) 
        
        self.facts=QLabel(self)
        self.fact=QLabel(self)
        self.fact.setText("   \tFACTS")
        self.fact.setGeometry(QRect(10,390,400,100))
        self.fact.setStyleSheet("QLabel{background-color:grey;color:white}")
        self.fact.setFont(QFont('Times',18,QFont.Bold))
        self.facts.setText(" -Least amount of Rape cases was recorded in DHULE in 2013.\n\n -Highest IPC crimes recorded where in SINDHUDURG in 2016.\n\n -Highest crimes in Maharashtra were recorded for HURT/GREVIOUS HURT in 2016.\n\n -Mumbai was recorded with the highest RAPE cases in 2017.\n\n -Pune was recorded with the highest MURDER cases in 2013.\n\n -Sindhudurg had the least Murder cases in 2013 ")
        self.facts.setGeometry(QRect(10,390,400,500))
        self.facts.setStyleSheet("QLabel{background-color:grey;color:white}")
        self.facts.setFont(QFont('Arial Black',10,QFont.Bold))
        self.facts.setWordWrap(True)
        
        
        self.setWindowIcon(QIcon('cuff1.png'))
        image=QImage("gun.jpg")#for background image
        images=image.scaled(QSize(1920,1080))
        palette=QPalette()
        palette.setBrush(10, QBrush(images))
        self.setPalette(palette)
        self.home()
        
        
        
    def reload(self):
        self.hide()
        self.wdp=Window()
        self.wdp.showMaximized()
        
    def home(self):
        self.comboBox = QComboBox(self)#drop-down menu
        for i in option:
            self.comboBox.addItem(i)
        self.comboBox.move(860, 430)
        self.comboBox.setFont(QFont('Times',12,QFont.Bold))
        self.comboBox.setStyleSheet('''QComboBox { min-width:190px; min-height: 40px;}''')
        
        self.btn=QPushButton('Search',self)
        self.btn.clicked.connect(self.value)
        self.btn.setFont(QFont('Times',11,QFont.Bold))
        self.btn.setGeometry(890,480,120,30)
        #self.btn.move(890,420)
        self.btn.setStyleSheet('QPushButton:pressed{background-color:blue}')
        
        self.btnW=QPushButton('HOME',self)
        self.btnW.clicked.connect(self.reload)
        self.btnW.move(10,300)
        self.btnW.setFont(QFont('Times',10,QFont.Bold))
        
        pie = PIE(self)
        pie.move(1190,390)
        self.showMaximized()#display windows
    def  value(self):
        global selected_input#making it global for the variable to be accessible in other class 
        selected_input=self.comboBox.currentText()
        self.hide()
        self.secondp=secondPage()
        self.secondp.showMaximized()
        
class PIE(FingureCanvas):#for graph in GUI
    def __init__(self, parent = None, width =7, height = 5.2, dpi =100):
        
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        fig.set_facecolor("gray")#setting background color for canvas
        FingureCanvas.__init__(self, fig)
        self.setParent(parent)
        
        self.plotp()
        
    def plotp(self):
        ax = self.figure.add_subplot(111)
        x=random.choice(option)
        y=random.choice(x_label)
        labels=['2011','2012','2013','2014','2015','2016','2017']
        rates=data.loc[x,y]
        explode=[0,0.1,0,0,0,0,0]
        ax.pie(rates,explode=explode,labels=labels,autopct='%1.1f%%',shadow=True,startangle=90)
        ax.axis('equal')
        title=x+'\n'+y
        ax.set_title(title,fontsize=16)
        
        

class secondPage(QDialog):
    def __init__(self):
        super(secondPage,self).__init__()
        self.setGeometry(50, 50, 700, 500)
        self.setWindowTitle("DATA ANALYSIS")
        self.label=QLabel(self)
        self.label.setText("  CRIMES:")
        self.label.setFont(QFont('Times',14,QFont.Bold))
        self.label.setStyleSheet("QLabel{color:white}")
        self.label.move(0,150)
        self.setWindowIcon(QIcon('cuff1.png'))
        
        image1=QImage("guns.jpg")#for background image
        images1=image1.scaled(QSize(1920,1080))
        palette1=QPalette()
        palette1.setBrush(10, QBrush(images1))
        self.setPalette(palette1)
        #RadioButton
        global radios
        radios=[]
        adj=0
      
        self.r0=QRadioButton(x_label[0],self)
        self.r0.move(10,190+adj)
        self.font=self.r0.font()
        self.font.setPointSize(9)
        self.r0.setFont(self.font)
        self.r0.setStyleSheet("QRadioButton{color:white;}")
        radios.append(self.r0)
        adj=adj+40
        self.r1=QRadioButton(x_label[1],self)
        self.r1.move(10,190+adj)
        self.font=self.r1.font()
        self.font.setPointSize(9)
        self.r1.setFont(self.font)
        self.r1.setStyleSheet("QRadioButton{color:white;}")
        radios.append(self.r1)
        adj=adj+40
        self.r2=QRadioButton(x_label[2],self)
        self.r2.move(10,190+adj)
        self.font=self.r2.font()
        self.font.setPointSize(9)
        self.r2.setFont(self.font)
        self.r2.setStyleSheet("QRadioButton{color:white;}")
        radios.append(self.r2)
        adj=adj+40
        self.r3=QRadioButton(x_label[3],self)
        self.r3.move(10,190+adj)
        self.font=self.r3.font()
        self.font.setPointSize(9)
        self.r3.setStyleSheet("QRadioButton{color:white;}")
        self.r3.setFont(self.font)
        radios.append(self.r3)
        adj=adj+40
        self.r4=QRadioButton(x_label[4],self)
        self.r4.move(10,190+adj)
        self.font=self.r4.font()
        self.font.setPointSize(9)
        self.r4.setStyleSheet("QRadioButton{color:white;}")
        self.r4.setFont(self.font)
        radios.append(self.r4)
        adj=adj+40
        self.r5=QRadioButton(x_label[5],self)
        self.r5.move(10,190+adj)
        self.font=self.r5.font()
        self.font.setPointSize(9)
        self.r5.setStyleSheet("QRadioButton{color:white;}")
        self.r5.setFont(self.font)
        radios.append(self.r5)
        adj=adj+40
        self.r6=QRadioButton(x_label[6],self)
        self.r6.move(10,190+adj)
        self.font=self.r6.font()
        self.font.setPointSize(9)
        self.r6.setStyleSheet("QRadioButton{color:white;}")
        self.r6.setFont(self.font)
        radios.append(self.r6)
        adj=adj+40
        self.r7=QRadioButton(x_label[7],self)
        self.r7.move(10,190+adj)
        self.font=self.r7.font()
        self.font.setPointSize(9)
        self.r7.setStyleSheet("QRadioButton{color:white;}")
        self.r7.setFont(self.font)
        radios.append(self.r7)
        adj=adj+40
        self.r8=QRadioButton(x_label[8],self)
        self.r8.move(10,190+adj)
        self.font=self.r8.font()
        self.font.setPointSize(9)
        self.r8.setStyleSheet("QRadioButton{color:white;}")
        self.r8.setFont(self.font)
        radios.append(self.r8)
        adj=adj+40
        self.r9=QRadioButton(x_label[9],self)
        self.r9.move(10,190+adj)
        self.font=self.r9.font()
        self.font.setPointSize(9)
        self.r9.setStyleSheet("QRadioButton{color:white;}")
        self.r9.setFont(self.font)
        radios.append(self.r9)
        adj=adj+40
        self.r10=QRadioButton(x_label[10],self)
        self.r10.move(10,190+adj)
        self.font=self.r10.font()
        self.font.setPointSize(9)
        self.r10.setStyleSheet("QRadioButton{color:white;}")
        self.r10.setFont(self.font)
        radios.append(self.r10)
        adj=adj+40
        self.r11=QRadioButton(x_label[11],self)
        self.r11.move(10,190+adj)
        self.font=self.r11.font()
        self.font.setPointSize(9)
        self.r11.setStyleSheet("QRadioButton{color:white;}")
        self.r11.setFont(self.font)
        radios.append(self.r11)
        adj=adj+40
        self.r12=QRadioButton(x_label[12],self)
        self.r12.move(10,190+adj)
        self.font=self.r12.font()
        self.font.setPointSize(9)
        self.r12.setStyleSheet("QRadioButton{color:white;}")
        self.r12.setFont(self.font)
        radios.append(self.r12)
        adj=adj+40
        self.r13=QRadioButton(x_label[13],self)
        self.r13.move(10,190+adj)
        self.font=self.r13.font()
        self.font.setPointSize(9)
        self.r13.setStyleSheet("QRadioButton{color:white;}")
        self.r13.setFont(self.font)
        radios.append(self.r13)
        adj=adj+40
        self.r14=QRadioButton(x_label[14],self)
        self.r14.move(10,190+adj)
        self.font=self.r14.font()
        self.font.setPointSize(9)
        self.r14.setStyleSheet("QRadioButton{color:white;}")
        self.r14.setFont(self.font)
        radios.append(self.r14)
        adj=adj+40
        self.r15=QRadioButton(x_label[15],self)
        self.r15.move(10,190+adj)
        self.font=self.r15.font()
        self.font.setPointSize(9)
        self.r15.setStyleSheet("QRadioButton{color:white;}")
        self.r15.setFont(self.font)
        radios.append(self.r15)
        adj=adj+40
        self.r16=QRadioButton(x_label[16],self)
        self.r16.move(10,190+adj)
        self.font=self.r16.font()
        self.font.setPointSize(9)
        self.r16.setStyleSheet("QRadioButton{color:white;}")
        self.r16.setFont(self.font)
        radios.append(self.r16)
        adj=adj+40
        #submitbutton
        self.submitB=QPushButton("Submit",self)
        self.submitB.clicked.connect(self.click)
        self.submitB.move(10,adj+190)
        self.submitB.setFont(QFont('Times',8,QFont.Bold))
        #dropdownMenu
        self.btn1=QPushButton('HOME',self)
        self.btn1.clicked.connect(self.home)
        self.btn1.move(1815,120)
        self.btn1.setFont(QFont('Times',10,QFont.Bold))
    
        canvas = Canvas(self)
        canvas.move(295,150)
    def click(self):
        global s
        for i in x_label:
            for j in radios:
                if j.isChecked():
                    if j.text()==i:
                        s=j.text()
        self.hide()
        self.Tp=TPage()
        self.Tp.showMaximized()                
    def home(self):
        self.hide()
        self.wdp=Window()
        #self.wdp.showMaximized()

class Canvas(FingureCanvas):#for graph in GUI
    def __init__(self, parent = None, width =16.2, height = 8.2, dpi =100):
        #print(s)
        fig = Figure(figsize=(width, height), dpi=dpi)
        fig.set_facecolor("gray")
        FingureCanvas.__init__(self, fig)
        self.setParent(parent)
        self.axes = fig.add_subplot(111)
        self.plot()


    
    def plot(self):
        #x = np.array([50, 30, 25])
        '''
        index=slct.crime(selected_input)#calling selection module to get index of district
        s=pf.iloc[index,0:18]
        p=list(s)
        freq=p[1:]
        x1=np.arange(len(freq))
        '''
        colors=iter(matplotlib.cm.gist_ncar(np.linspace(0,0.9,len(x_label))))
        
        ax = self.figure.add_subplot(211)
        ax1 = self.figure.add_subplot(211)
        ax.set_title(selected_input + ' CRIME CHART',fontsize=20)
        y=['2011','2012','2013','2014','2015','2016','2017']
        #l=[]
        
        cellText=[]
        c=[]
        indx=0
        for i in x_label:
            a=data.loc[selected_input,i]
            x=list(a)
            
            cellText.append(x)
            
            a=next(colors)
            c.append(a)
            
            ax.scatter(y,x ,color=a)
            indx=indx+1
            ax1.plot(y,x,color=a)
        tb=ax.table(cellText=cellText,rowLabels=rows,rowColours=c,colLabels=y,loc='bottom') 
        tb.set_fontsize(9)
        ax.xaxis.set_visible(False)   
        #ax.legend(loc='center right',bbox_to_anchor=(1.1,0.5),fancybox=True,shadow=True) 
        ax.set_ylabel("RATE",fontsize=16)
        ax.set_xlabel("YEAR",fontsize=16)
        
    
    
        
        
class TPage(QDialog):
    def __init__(self):
        super(TPage,self).__init__()
        self.setGeometry(50, 50, 700, 500)
        self.setWindowTitle("DATA ANALYSIS")
        self.setWindowIcon(QIcon('cuff1.png'))
        
        image2=QImage("guns.jpg")#for background image
        images2=image2.scaled(QSize(1920,1080))
        palette2=QPalette()
        palette2.setBrush(10, QBrush(images2))
        self.setPalette(palette2)
        
        self.btnT=QPushButton('HOME',self)
        self.btnT.clicked.connect(self.homeT)
        self.btnT.move(1830,120)
        self.btnT.setFont(QFont('Times',10,QFont.Bold))
        
        self.btnT1=QPushButton('BACK',self)
        self.btnT1.clicked.connect(self.backS)
        self.btnT1.move(0,120)
        self.btnT1.setFont(QFont('Times',10,QFont.Bold))
        
        self.p=QPushButton('Prediction',self)
        self.p.clicked.connect(self.predict)
        self.p.setGeometry(900,960,140,40)
        self.p.setFont(QFont('Times',14,QFont.Bold))
        
        graph=GRAPH(self)
        graph.move(0,150)
        
    def homeT(self):
        self.hide()
        self.wdp=Window()
        #self.wdp.showMaximized()
    def backS(self):
        self.hide()
        self.secondp=secondPage()
        self.secondp.showMaximized()
    def predict(self):
        self.hide()
        self.fp=FPage()
        self.fp.showMaximized()
        
        
           
        
class GRAPH(FingureCanvas):#for graph in GUI
    def __init__(self, parent = None, width =19.2, height = 8, dpi =100):
        #print(s)
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        FingureCanvas.__init__(self, fig)
        self.setParent(parent)
        fig.set_facecolor("gray")#setting background color for canvas
        
        self.plot1()
         
    def plot1(self,):
        #selected info
        a=data.loc[selected_input,s]
        x=list(a)
        ax = self.figure.add_subplot(111)
        ax.set_title(selected_input +"\n"+s ,fontsize=20)
        y=['2011','2012','2013','2014','2015','2016','2017']
        
        ax.bar(y,x,color='midnightblue')
        ax.plot(y,x,color='red')
        ax.set_ylabel("RATE",fontsize=16) 
        ax.set_xlabel("YEAR",fontsize=16)  

class FPage(QDialog):
    def __init__(self):
        super(FPage,self).__init__()
        self.setGeometry(50, 50, 700, 500)
        self.setWindowTitle("DATA ANALYSIS")
        self.setWindowIcon(QIcon('cuff1.png'))
        
        image2=QImage("guns.jpg")#for background image
        images2=image2.scaled(QSize(1920,1080))
        palette2=QPalette()
        palette2.setBrush(10, QBrush(images2))
        self.setPalette(palette2)
        
        self.btnT=QPushButton('HOME',self)
        self.btnT.clicked.connect(self.homef)
        self.btnT.move(1830,120)
        self.btnT.setFont(QFont('Times',10,QFont.Bold))
        
        self.btnT1=QPushButton('BACK',self)
        self.btnT1.clicked.connect(self.backf)
        self.btnT1.move(0,120)
        self.btnT1.setFont(QFont('Times',10,QFont.Bold))
        
        pd=Prediction(self)
        pd.move(0,150)
        
    def homef(self):
        self.hide()
        self.wdp=Window()
        #self.wdp.showMaximized()
    def backf(self):
        self.hide()
        self.Tp=TPage()
        self.Tp.showMaximized()
        
        
           
        
class Prediction(FingureCanvas):#for graph in GUI
    def __init__(self, parent = None, width =19.2, height = 8.2, dpi =100):
        #print(s)
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        FingureCanvas.__init__(self, fig)
        self.setParent(parent)
        fig.set_facecolor("gray")#setting background color for canvas
        
        self.plotp()
         
    def plotp(self,):
        #selected info
        a=data.loc[selected_input,s]
        X=list(a)
        size = int(len(X) * 0.429999999) 
        train, test = X[0:size], X[size:len(X)]
        history = [x for x in train]
        predictions = []
        for t in range(len(test)):
            model = ARIMA(history, order=(1,0,0))
            model_fit = model.fit(disp=0)
            output = model_fit.forecast()
            yhat = output[0]
            predictions.append(yhat)
            obs = test[t]
            history.append(obs)
            print('predicted=%f, expected=%f' % (yhat, obs))
        error = mean_squared_error(test, predictions)
        print('Test MSE: %.3f' % error)

        
        ax = self.figure.add_subplot(111)
        ax.set_title(selected_input +"\n"+s+ '\nFUTURE PREDICTION' ,fontsize=20)
        y=['2018','2019','2020','2021']
        
        ax.plot(y,test,color='c',label='Expected')
        ax.scatter(y,test,color='c')
        ax.plot(predictions,color='red',label='Prediction')
        ax.scatter(y,predictions,color='r')
        ax.set_ylabel("RATE",fontsize=16) 
        ax.set_xlabel("YEAR",fontsize=16)  
        ax.legend()             
        
              
app = QApplication(sys.argv)
GUI = Window()
sys.exit(app.exec_())
