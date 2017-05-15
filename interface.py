from pymongo import MongoClient
import wx
from datetime import datetime, timedelta
import shutil
import os


class FileMovePanel(wx.Panel):
    """Main panel, three buttons, two labels. Handles the main functionality for events.."""
    def __init__(self, parent, *args, **kwargs):
        """Create the MainPanel."""
        wx.Panel.__init__(self, parent, *args, **kwargs)
        self.source = "none"
        self.destination = "none"
        self.parent = parent
        self.connection = MongoClient()

        #Source buttom definitions
        SourceBtn = wx.Button(self, label="Add to Database")
        SourceBtn.Bind(wx.EVT_BUTTON, lambda evt, buttonPressed = "source": self.OnOpen(evt, buttonPressed))

        #Destination button defitions
        DestBtn = wx.Button(self, label="Query Collection")
        DestBtn.Bind(wx.EVT_BUTTON, lambda evt, buttonPressed = "destination": self.OnOpen(evt, buttonPressed ))

        #Initiate file movement button definition
        MoveBtn = wx.Button(self, label="Query Information")
        MoveBtn.Bind(wx.EVT_BUTTON, self.OnMove)

        
        
        #using a sizer for layouts. Sizers allow elements to move as the window size changes.
        Sizer = wx.BoxSizer(wx.VERTICAL)
        Sizer.Add(SourceBtn, 0, wx.ALIGN_LEFT|wx.LEFT|wx.RIGHT, 5)
        Sizer.Add(self.SourceText, 0, wx.ALIGN_RIGHT|wx.LEFT|wx.RIGHT, 5)
        Sizer.Add(DestBtn, 0, wx.ALIGN_RIGHT|wx.LEFT|wx.RIGHT, 5)
        Sizer.Add(self.DestText, 0, wx.ALIGN_RIGHT|wx.LEFT|wx.RIGHT, 5)
        Sizer.Add(MoveBtn, 0, wx.ALIGN_CENTER|wx.ALL, 5)
        Sizer.Add(self.TimeText, 0, wx.ALIGN_RIGHT|wx.LEFT|wx.RIGHT, 5)

        self.SetSizerAndFit(Sizer)
                   

class DemoFrame(wx.Frame):
    """Main Frame holding the Panel."""
    
    def __init__(self, *args, **kwargs):
        """Creates DemoFrame."""
        
        wx.Frame.__init__(self, *args, **kwargs)
        
        MenuBar = wx.MenuBar() # builds menu bar

        FileMenu = wx.Menu()

        item = FileMenu.Append(wx.ID_EXIT, text="&Quit")
        self.Bind(wx.EVT_MENU, self.OnQuit, item)

        MenuBar.Append(FileMenu, "&File")
        self.SetMenuBar(MenuBar)

        self.Panel = FileMovePanel(self) # adds widget panel

        self.Fit()

    def OnQuit(self, event=None):
        """Exit application."""
        self.Close()

def createDatabase(): # Calls database
    client = MongoClient()
    db = client['Financial Computation DataBase']
        

if __name__ == '__main__': #swap out whats commented to create the database.
    app = wx.App()
    frame = DemoFrame(None, title="Micro App")
    frame.Show()
    app.MainLoop()
