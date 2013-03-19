import wx
import sys
import urllib2
from MainFrame import MainFrame

class scannerApp(wx.App):
    def OnInit(self):
        str=urllib2.unquote((sys.argv[1].split('/',2))[2])
        temp=str
        fid=(temp.split('&'))[0].split('=')[1]
        name=(str.split('&'))[1].split('=')[1]
        tid=(str.split('&'))[2].split('=')[1]
        title=(str.split('&'))[3].split('=')[1]
        uid=(str.split('&'))[4].split('=')[1]
        ulink=(str.split('&'))[5].split('=')[1]
        
        self.m_frame = MainFrame(None)
        self.m_frame.SetIcon(wx.IconFromLocation(wx.IconLocation(r'scanner.ico',0)))
        self.m_frame.setParams(fid,name,tid,title,uid,ulink)
        self.m_frame.Show()
        self.SetTopWindow(self.m_frame)
        return True

app = scannerApp(0)
app.MainLoop()
