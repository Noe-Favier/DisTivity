import pystray as ps
from PIL import Image
import sys as sys
import InputBox as ib
import threading as th
from multiprocessing.pool import ThreadPool
import DiscordActivity as da

class DisTivity:
    def __init__(self):
        self.activity = da.DiscordActivity('783274457665765377') #code of the APP

        self.itemCA = ps.MenuItem('Change Activity',self.onItemChangeActivity)
        self.itemEXIT = ps.MenuItem('exit',self.onItemExit)
        
        self.itemLabelTitle = ps.MenuItem(self._title,action=self.NoAction,enabled=False)
        self.itemLabelSubTitle = ps.MenuItem(self._subtitle,action=self.NoAction,enabled=False)
        
        self.menu = ps.Menu(self.itemLabelTitle,self.itemLabelSubTitle,self.itemCA,self.itemEXIT)
        
        self.icon = ps.Icon('DisTivity',Image.open("ic.png"),menu=self.menu)

        self._title = 'no title set'
        self._subtitle = 'no sub-title set'

    def _title(self,a):
        """
            we have tu use a callable as MenuItem label to make a dynamic interface
        """
        return self._title

    def _subtitle(self,a):
        """
            we have tu use a callable as MenuItem label to make a dynamic interface
        """
        return self._subtitle

    def updateTitles(self,t,st):
        self._title = t
        self._subtitle = st
        self.icon.update_menu()

    def _ask(self,question):
        input = ib.InputBox()
        return input.getText(question)

    def ask(self,txt):
        """
            open a textbox in a thread 
        """
        #--------------------------------DIALOG BOX---------------------------------------
        pool = ThreadPool(processes=1)
        async_result = pool.apply_async(self._ask, (txt,)) #
        return async_result.get()  # get the return value from your function.
        #---------------------------------------------------------------------------------

    def run(self):
        self.icon.run()

    def onItemChangeActivity(self):
        entry = ""
        titre = None
        stitre = None


        #**********************************************************
        entry = self.ask("Enter a title")

        if (entry!=None and len(entry)<2):
            self.icon.notify("Since your title is too short (<2 letters) we will ignore it") #in fact, titles have to be bigger than 2 char 

        if entry != None :
            titre = entry

        #**********************************************************
        entry = self.ask("Enter a sub-title")

        if (entry!=None and len(entry)<2):
            self.icon.notify("Since your sub-title is too short (<2 letters) we will ignore it")

        if entry != None :
            stitre = entry

        #**********************************************************
        self.updateTitles(titre,stitre)
        self.activity.updatePresence(titre,stitre)

    def onItemExit(self):
        self.icon.stop()

    def NoAction(self):
        pass
