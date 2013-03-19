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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"DCS Archiving System Scanner", pos = wx.DefaultPosition, size = wx.Size( 669,492 ), style = wx.CAPTION|wx.RESIZE_BORDER|wx.SYSTEM_MENU|wx.CLIP_CHILDREN|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer5 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_btConnect = wx.Button( self.m_panel, wx.ID_ANY, u"Connect", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_btConnect, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_btScan = wx.Button( self.m_panel, wx.ID_ANY, u"Scan", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_btScan, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_staticline2 = wx.StaticLine( self.m_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer5.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_btAdd = wx.Button( self.m_panel, wx.ID_ANY, u"New page", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_btAdd, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_btRemove = wx.Button( self.m_panel, wx.ID_ANY, u"Delete page", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_btRemove, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_btUpload = wx.Button( self.m_panel, wx.ID_ANY, u"Upload", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_btUpload, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_staticline3 = wx.StaticLine( self.m_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer5.Add( self.m_staticline3, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticText20 = wx.StaticText( self.m_panel, wx.ID_ANY, u"Page Navigation", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText20.Wrap( -1 )
		bSizer5.Add( self.m_staticText20, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_btChangePage = wx.SpinButton( self.m_panel, wx.ID_ANY, wx.DefaultPosition, wx.Size( 70,25 ), wx.SP_ARROW_KEYS|wx.SP_HORIZONTAL )
		bSizer5.Add( self.m_btChangePage, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		bSizer10 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer5.Add( bSizer10, 1, wx.EXPAND, 5 )
		
		self.m_btExit = wx.Button( self.m_panel, wx.ID_ANY, u"Exit", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		bSizer5.Add( self.m_btExit, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		bSizer3.Add( bSizer5, 0, wx.EXPAND, 5 )
		
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_scrolledWindow = wx.ScrolledWindow( self.m_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow.SetScrollRate( 5, 5 )
		bSizer6 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_bitmap = wx.StaticBitmap( self.m_scrolledWindow, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.m_bitmap, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_scrolledWindow.SetSizer( bSizer6 )
		self.m_scrolledWindow.Layout()
		bSizer6.Fit( self.m_scrolledWindow )
		bSizer4.Add( self.m_scrolledWindow, 1, wx.ALL|wx.EXPAND, 5 )
		
		fgSizer2 = wx.FlexGridSizer( 2, 4, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		fgSizer2.SetMinSize( wx.Size( 575,60 ) ) 
		self.m_staticText16 = wx.StaticText( self.m_panel, wx.ID_ANY, u"Document type:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )
		fgSizer2.Add( self.m_staticText16, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.m_lbDoctype = wx.TextCtrl( self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY|wx.NO_BORDER )
		self.m_lbDoctype.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		fgSizer2.Add( self.m_lbDoctype, 0, wx.ALIGN_CENTER, 5 )
		
		self.m_staticText17 = wx.StaticText( self.m_panel, wx.ID_ANY, u"Faculty:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )
		fgSizer2.Add( self.m_staticText17, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.m_lbFaculty = wx.TextCtrl( self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY|wx.NO_BORDER )
		self.m_lbFaculty.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		fgSizer2.Add( self.m_lbFaculty, 0, wx.ALL, 5 )
		
		self.m_staticText18 = wx.StaticText( self.m_panel, wx.ID_ANY, u"Current page:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText18.Wrap( -1 )
		fgSizer2.Add( self.m_staticText18, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.m_lbCNowpage = wx.TextCtrl( self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY|wx.NO_BORDER )
		self.m_lbCNowpage.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		fgSizer2.Add( self.m_lbCNowpage, 0, wx.ALL, 5 )
		
		self.m_staticText19 = wx.StaticText( self.m_panel, wx.ID_ANY, u"Total no. of pages:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19.Wrap( -1 )
		fgSizer2.Add( self.m_staticText19, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.m_lbAllpages = wx.TextCtrl( self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY|wx.NO_BORDER )
		self.m_lbAllpages.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		fgSizer2.Add( self.m_lbAllpages, 0, wx.ALL, 5 )
		
		bSizer4.Add( fgSizer2, 0, 0, 5 )
		
		bSizer3.Add( bSizer4, 1, wx.EXPAND, 5 )
		
		bSizer2.Add( bSizer3, 1, wx.EXPAND, 5 )
		
		self.m_panel.SetSizer( bSizer2 )
		self.m_panel.Layout()
		bSizer2.Fit( self.m_panel )
		bSizer.Add( self.m_panel, 1, wx.EXPAND |wx.ALL, 0 )
		
		self.SetSizer( bSizer )
		self.Layout()
		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_help = wx.Menu()
		self.m_about = wx.MenuItem( self.m_help, wx.ID_ANY, u"About"+ u"\t" + u"F1", u"Shows about dialog", wx.ITEM_NORMAL )
		self.m_help.AppendItem( self.m_about )
		
		self.m_menubar1.Append( self.m_help, u"Help" ) 
		
		self.SetMenuBar( self.m_menubar1 )
		
		self.m_statusBar = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.OnClose )
		self.m_btConnect.Bind( wx.EVT_BUTTON, self.m_btConnectClick )
		self.m_btConnect.Bind( wx.EVT_ENTER_WINDOW, self.m_btConnectHoverIn )
		self.m_btConnect.Bind( wx.EVT_LEAVE_WINDOW, self.m_btConnectHoverOut )
		self.m_btScan.Bind( wx.EVT_BUTTON, self.m_btScanClick )
		self.m_btScan.Bind( wx.EVT_ENTER_WINDOW, self.m_btScanHoverIn )
		self.m_btScan.Bind( wx.EVT_LEAVE_WINDOW, self.m_btScanHoverOut )
		self.m_btAdd.Bind( wx.EVT_BUTTON, self.m_btAddClick )
		self.m_btAdd.Bind( wx.EVT_ENTER_WINDOW, self.m_btAddHoverIn )
		self.m_btAdd.Bind( wx.EVT_LEAVE_WINDOW, self.m_btAddHoverOut )
		self.m_btRemove.Bind( wx.EVT_BUTTON, self.m_btRemoveClick )
		self.m_btRemove.Bind( wx.EVT_ENTER_WINDOW, self.m_btRemoveHoverIn )
		self.m_btRemove.Bind( wx.EVT_LEAVE_WINDOW, self.m_btRemoveHoverOut )
		self.m_btUpload.Bind( wx.EVT_BUTTON, self.m_btUploadClick )
		self.m_btUpload.Bind( wx.EVT_ENTER_WINDOW, self.m_btUploadHoverIn )
		self.m_btUpload.Bind( wx.EVT_LEAVE_WINDOW, self.m_btUploadHoverOut )
		self.m_btChangePage.Bind( wx.EVT_ENTER_WINDOW, self.m_btChangePageHoverIn )
		self.m_btChangePage.Bind( wx.EVT_LEAVE_WINDOW, self.m_btChangePageHoverOut )
		self.m_btChangePage.Bind( wx.EVT_SPIN_DOWN, self.m_btChangePagePrev )
		self.m_btChangePage.Bind( wx.EVT_SPIN_UP, self.m_btChangePageNext )
		self.m_btExit.Bind( wx.EVT_BUTTON, self.m_btExitClick )
		self.m_btExit.Bind( wx.EVT_ENTER_WINDOW, self.m_btExitHoverIn )
		self.m_btExit.Bind( wx.EVT_LEAVE_WINDOW, self.m_btExitHoverOut )
		self.Bind( wx.EVT_MENU, self.m_aboutClick, id = self.m_about.GetId() )
	
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
	
	def m_btAddClick( self, event ):
		event.Skip()
	
	def m_btAddHoverIn( self, event ):
		event.Skip()
	
	def m_btAddHoverOut( self, event ):
		event.Skip()
	
	def m_btRemoveClick( self, event ):
		event.Skip()
	
	def m_btRemoveHoverIn( self, event ):
		event.Skip()
	
	def m_btRemoveHoverOut( self, event ):
		event.Skip()
	
	def m_btUploadClick( self, event ):
		event.Skip()
	
	def m_btUploadHoverIn( self, event ):
		event.Skip()
	
	def m_btUploadHoverOut( self, event ):
		event.Skip()
	
	def m_btChangePageHoverIn( self, event ):
		event.Skip()
	
	def m_btChangePageHoverOut( self, event ):
		event.Skip()
	
	def m_btChangePagePrev( self, event ):
		event.Skip()
	
	def m_btChangePageNext( self, event ):
		event.Skip()
	
	def m_btExitClick( self, event ):
		event.Skip()
	
	def m_btExitHoverIn( self, event ):
		event.Skip()
	
	def m_btExitHoverOut( self, event ):
		event.Skip()
	
	def m_aboutClick( self, event ):
		event.Skip()
	

