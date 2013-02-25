import wx
import sys
from MainFrame import MainFrame

class scannerApp(wx.App):
    def OnInit(self):
        print 'scanner'
        #Test Inputs
##        name="LesterNacu"
##        pages="2"
##        title="Daily Time Record"
##        sessid="-1"
        
        str=(sys.argv[1].split('/'))[2]
        temp=str
        fid=(temp.split('&'))[0].split('=')[1]
        name=(str.split('&'))[1].split('=')[1]
        title=(str.split('&'))[2].split('=')[1]
        sessid=(str.split('&'))[3].split('=')[1]
        print fid,name,title,sessid
        self.m_frame = MainFrame(None)
        self.m_frame.setParams(fid,name,title,sessid)
        self.m_frame.Show()
        self.SetTopWindow(self.m_frame)
        return True

app = scannerApp(0)
app.MainLoop()
