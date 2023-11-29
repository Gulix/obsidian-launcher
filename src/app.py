import wx

# local imports
import obsidian


def get_top_left_display_rect():
    client_areas = sorted(
        [wx.Display(i).GetClientArea() for i in range(wx.Display.GetCount())],
        key=lambda x: x.topLeft.Get(),
    )
    return client_areas[0]  # main display


class Frame(wx.Frame):

    def __init__(self):
        app_width = 400
        app_height = 300

        # Center the dialog on the top-left most display
        d = get_top_left_display_rect()
        baseX = d.GetX() + (d.GetWidth() / 2) - (app_width / 2)
        baseY = d.GetY() + (d.GetHeight() / 2) - (app_height / 2)
        app_top_left_point = wx.Point(int(baseX), int(baseY))

        wx.Frame.__init__(
            self,
            None,
            title="Obsidian Launcher",
            pos=app_top_left_point,
            size=wx.Size(app_width, app_height),
            style=wx.DEFAULT_FRAME_STYLE,
        )

        # Create an enlarged font for the buttons from the native font.
        font = self.GetFont()
        font.SetPointSize(18)

        self.vaults = obsidian.get_vault_names()
        # self.vaults = []  # for testing

        panel = wx.Panel(self)

        label1 = wx.StaticText(panel, label="Click on a vault to open.")

        sz_buttons = wx.BoxSizer(wx.VERTICAL)

        for x in self.vaults:
            button = wx.Button(panel, label=x, size=(300, 100))
            button.SetFont(font)
            button.Bind(wx.EVT_BUTTON, self.on_click)
            sz_buttons.Add(button, 0, wx.ALL, 10)

        if not self.vaults:
            sz_buttons.Add(wx.StaticText(panel, label="No vaults found."), 0,
                           wx.ALL, 100)

        ######################################################################
        ##                              Layout                              ##
        ######################################################################

        sz_main = wx.BoxSizer(wx.VERTICAL)
        sz_main.Add(label1, 0, wx.ALIGN_CENTER | wx.LEFT | wx.RIGHT | wx.TOP,
                    10)
        sz_main.Add(sz_buttons, 0, wx.ALIGN_CENTER | wx.ALL, 10)
        panel.SetSizer(sz_main)

        panel.Fit()  # first fit the panel to its children
        self.Fit()  # then fit the parent frame to its child panel

    def on_click(self, event):
        obj = event.GetEventObject()
        name = obj.GetLabel()
        obsidian.open_vault_by_name(name)
        self.Close(True)


class App(wx.App):

    def __init__(self):
        wx.App.__init__(self, redirect=False)
        frame = Frame()
        frame.SetIcon(wx.Icon("resources\\obsidian-icon-windows.ico"))
        frame.Show()


if __name__ == "__main__":
    app = App()
    app.MainLoop()
