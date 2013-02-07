# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Sep  8 2010)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx

###########################################################################
## Class MainFrameBase
###########################################################################

class MainFrameBase ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Scanner", pos = wx.DefaultPosition, size = wx.Size( 669,492 ), style = wx.CAPTION|wx.RESIZE_BORDER|wx.SYSTEM_MENU|wx.CLIP_CHILDREN|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_scrolledWindow = wx.ScrolledWindow( self.m_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow.SetScrollRate( 5, 5 )
		bSizer6 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_bitmap = wx.StaticBitmap( self.m_scrolledWindow, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.m_bitmap, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_scrolledWindow.SetSizer( bSizer6 )
		self.m_scrolledWindow.Layout()
		bSizer6.Fit( self.m_scrolledWindow )
		bSizer4.Add( self.m_scrolledWindow, 1, wx.EXPAND |wx.ALL, 5 )
		
		bSizer3.Add( bSizer4, 1, wx.EXPAND, 5 )
		
		bSizer5 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_btConnect = wx.Button( self.m_panel, wx.ID_ANY, u"Connect", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_btConnect, 0, wx.ALL, 5 )
		
		self.m_btScan = wx.Button( self.m_panel, wx.ID_ANY, u"Scan", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_btScan, 0, wx.ALL, 5 )
		
		self.m_btUpload = wx.Button( self.m_panel, wx.ID_ANY, u"Upload", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_btUpload, 0, wx.ALL, 5 )
		
		self.m_btExit = wx.Button( self.m_panel, wx.ID_ANY, u"Exit", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_btExit, 0, wx.ALL, 5 )
		
		bSizer3.Add( bSizer5, 0, wx.EXPAND, 5 )
		
		bSizer2.Add( bSizer3, 1, wx.EXPAND, 5 )
		
		self.m_panel.SetSizer( bSizer2 )
		self.m_panel.Layout()
		bSizer2.Fit( self.m_panel )
		bSizer.Add( self.m_panel, 1, wx.EXPAND |wx.ALL, 0 )
		
		self.SetSizer( bSizer )
		self.Layout()
		self.m_statusBar = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.OnClose )
		self.m_btConnect.Bind( wx.EVT_BUTTON, self.m_btConnectClick )
		self.m_btConnect.Bind( wx.EVT_ENTER_WINDOW, self.m_btConnectHoverIn )
		self.m_btConnect.Bind( wx.EVT_LEAVE_WINDOW, self.m_btConnectHoverOut )
		self.m_btScan.Bind( wx.EVT_BUTTON, self.m_btScanClick )
		self.m_btScan.Bind( wx.EVT_ENTER_WINDOW, self.m_btScanHoverIn )
		self.m_btScan.Bind( wx.EVT_LEAVE_WINDOW, self.m_btScanHoverOut )
		self.m_btUpload.Bind( wx.EVT_BUTTON, self.m_btUploadClick )
		self.m_btUpload.Bind( wx.EVT_ENTER_WINDOW, self.m_btUploadHoverIn )
		self.m_btUpload.Bind( wx.EVT_LEAVE_WINDOW, self.m_btUploadHoverOut )
		self.m_btExit.Bind( wx.EVT_BUTTON, self.m_btExitClick )
		self.m_btExit.Bind( wx.EVT_ENTER_WINDOW, self.m_btExitHoverIn )
		self.m_btExit.Bind( wx.EVT_LEAVE_WINDOW, self.m_btExitHoverOut )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnClose( self, event ):
		event.Skip()
	
	def m_btConnectClick( self, event ):
		event.Skip()
	
	def m_btConnectHoverIn( self, event ):
		event.Skip()
	
	def m_btConnectHoverOut( self, event ):
		event.Skip()
	
	def m_btScanClick( self, event ):
		event.Skip()
	
	def m_btScanHoverIn( self, event ):
		event.Skip()
	
	def m_btScanHoverOut( self, event ):
		event.Skip()
	
	def m_btUploadClick( self, event ):
		event.Skip()
	
	def m_btUploadHoverIn( self, event ):
		event.Skip()
	
	def m_btUploadHoverOut( self, event ):
		event.Skip()
	
	def m_btExitClick( self, event ):
		event.Skip()
	
	def m_btExitHoverIn( self, event ):
		event.Skip()
	
	def m_btExitHoverOut( self, event ):
		event.Skip()
	

