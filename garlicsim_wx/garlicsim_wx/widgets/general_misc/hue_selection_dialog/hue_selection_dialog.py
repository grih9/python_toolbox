import wx

from garlicsim_wx.widgets.general_misc import CuteDialog

from .wheel import Wheel
from .comparer import Comparer
from .textual import Textual


class HueSelectionDialog(CuteDialog):
    
    def __init__(self, parent, setter, old_hls, lightness=1, saturation=1,
                 id=-1, title='Select hue', pos=wx.DefaultPosition,
                 size=wx.DefaultSize, style=wx.DEFAULT_DIALOG_STYLE,
                 name=wx.DialogNameStr):

        
        CuteDialog.__init__(self, parent, id, title, pos, size, style, name)
        
        self.lightness = lightness

        self.saturation = saturation
        
        self.old_hls = old_hls # tododoc: fix to match give l and s
        
        self.setter = setter
        
        
        self.main_v_sizer = wx.BoxSizer(wx.VERTICAL)
        
        self.h_sizer = wx.BoxSizer(wx.HORIZONTAL)
        
        self.main_v_sizer.Add(self.h_sizer, 0)
        
        self.wheel = Wheel(self)
        
        self.h_sizer.Add(self.wheel, 0, wx.ALL, border=10)
        
        self.v_sizer = wx.BoxSizer(wx.VERTICAL)
        
        self.h_sizer.Add(self.v_sizer, 0)
        
        self.comparer = Comparer(self)
        
        self.v_sizer.Add(self.comparer, 0, wx.ALL, border=10)
        
        self.textual = Textual(self)
        
        self.v_sizer.Add(self.textual, 0, wx.ALL, border=10)
                
        self.dialog_button_sizer = wx.StdDialogButtonSizer()
        
        self.main_v_sizer.Add(self.dialog_button_sizer, 0,
                              wx.ALIGN_CENTER | wx.ALL, border=10)
        
        self.ok_button = wx.Button(self, wx.ID_OK, 'Ok', size=(70, 30))
        self.dialog_button_sizer.AddButton(self.ok_button)
        self.ok_button.SetDefault()
        self.dialog_button_sizer.SetAffirmativeButton(self.ok_button)
        self.Bind(wx.EVT_BUTTON, self.on_ok, source=self.ok_button)
        
        self.cancel_button = wx.Button(self, wx.ID_CANCEL, 'Cancel',
                                       size=(70, 30))
        self.dialog_button_sizer.AddButton(self.cancel_button)
        self.Bind(wx.EVT_BUTTON, self.on_cancel, source=self.cancel_button)
        self.dialog_button_sizer.Realize()

        
        self.SetSizer(self.main_v_sizer)
        self.main_v_sizer.Fit(self)
        
        
    def on_ok(self, event):
        self.EndModal(wx.ID_OK)
        
    
    def on_cancel(self, event):
        self.EndModal(wx.ID_CANCEL)