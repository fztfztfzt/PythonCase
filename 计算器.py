import wx
def OnButton(event):
	global textctrl,showstr
	showstr += (event.GetEventObject()).GetLabel()
	textctrl.SetValue(showstr)
def OnDEEL(event):
	global textctrl,showstr
	showstr = showstr[:-1]
	textctrl.SetValue(showstr)
	
def OnC(event):
	global textctrl,showstr
	showstr = ''
	textctrl.SetValue(showstr)
def OnQue(event):
	global showstr,textctrl
	showstr = showstr.replace('^','**')
	showstr = showstr.replace('ln','log')
	showstr = str(eval(showstr))
	textctrl.SetValue(showstr)
	
app = wx.App(False)
window = wx.Frame(None,-1,'test',pos=(100,100),size=(400,400))
boxsize = wx.BoxSizer(wx.VERTICAL)
gridBox = wx.GridSizer(rows=6,cols=5,hgap=1,vgap=1)
panel = wx.Panel(window)
textctrl = wx.TextCtrl(panel,-1,'0')
textctrl.SetBackgroundColour((210,210,210))
textctrl.SetForegroundColour((15,15,15))
bstr = ['DEL','C','=','ln','^','7','8','9','/','(','4','5','6','*',')','1','2','3','-','+','0','.','sin','cos','tan']
showstr='0'
for i in range(len(bstr)):
	print '1'
	button = wx.Button(panel,-1,bstr[i])
	gridBox.Add(button,0,flag=wx.EXPAND)
	print bstr[i]
	if bstr[i]=='DEL':
		window.Bind(wx.EVT_BUTTON,OnDEEL,button)
	elif bstr[i]== 'C':
		window.Bind(wx.EVT_BUTTON,OnC,button)
	elif bstr[i]== '=':
		window.Bind(wx.EVT_BUTTON,OnQue,button)
	else:
		window.Bind(wx.EVT_BUTTON,OnButton,button)
boxsize.Add(textctrl,1,flag=wx.EXPAND)
boxsize.Add(gridBox,5,flag=wx.EXPAND)
panel.SetSizerAndFit(boxsize)
window.Show()
app.MainLoop()

