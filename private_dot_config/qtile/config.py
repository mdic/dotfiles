from libqtile.lazy import lazy
from libqtile import layout, bar, widget, hook
from libqtile.config import Click, Drag, Group, Key, KeyChord, Match, Screen
from typing import List  # noqa: F401

mod = "mod4"

keys = [

    # Switch between windows in current stack pane
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    # Move windows up and down in current stack
    Key([mod, "control"], "j", lazy.layout.shuffle_down()),
    Key([mod, "control"], "k", lazy.layout.shuffle_up()),

    # Increase and decrease window size
    Key([mod, "control"], "l", lazy.layout.grow()),
    Key([mod, "control"], "h", lazy.layout.shrink()),
    Key([mod, "control"], "n", lazy.layout.normalize()),

    # Switch window focus to other pane(s) of stack
    Key([mod], "space", lazy.layout.next()),

    # Swap panes of split stack
    # Key([mod, "shift"], "space", lazy.layout.rotate()),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split()),
    Key([mod], "f", lazy.window.toggle_floating()),
    Key([mod], "Return", lazy.spawn("kitty")),  # es = emacsclient
    Key([mod], "t", lazy.spawn("alacritty -e /usr/bin/fish")),
    Key([mod, "shift"], "t", lazy.spawn("alacritty")),
    Key(
        [mod, "shift"],
        "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen on the focused window",
    ),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout()),
    Key([mod], "w", lazy.window.kill()),

    # Volume and Backlight keys
    Key([], "XF86AudioLowerVolume",
        lazy.spawn("amixer set Master 5%- unmute")),
    Key([], "XF86AudioRaiseVolume",
        lazy.spawn("amixer set Master 5%+ unmute")),
    Key([], "XF86AudioMute", lazy.spawn("amixer set Master togglemute")),
    Key([], "XF86AudioMicMute", lazy.spawn("amixer set Capture togglemute")),
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +5%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 5%-")),


    Key([mod, "control"], "r", lazy.restart()),
    Key([mod, "control"], "q", lazy.shutdown()),
    Key([mod], "r", lazy.spawn("rofi -show drun")),
    Key([mod, "shift"], "r", lazy.spawncmd()),

    # Take screenshot
    Key([], "Print", lazy.spawn("scrot /home/mmk2410/Pictures/screenshots/")),
]

groups = [Group(i) for i in "1234567890"]

for i in groups:
    keys.extend([
        Key([mod], i.name, lazy.group[i.name].toscreen()),
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
    ])

layout_defaults = dict(
    margin=10,
    border_width=3,
    border_focus="#d65d0e",
    border_normal="#928374",
)

layouts = [
    layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    layout.RatioTile(),
    # layout.Tile(),
    layout.TreeTab(),
]

widget_defaults = dict(
    font='Hack',
    fontsize=14,
    padding=3,
    foreground="ebdbb2",
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    active="ebdbb2",
                    inactive="928374",
                    this_screen_border="458588",
                    urgent_border="cc241d",
                    urgent_text="cc241d"
                ),
                widget.Prompt(),
                widget.WindowName(),
                widget.Notify(),
                widget.TextBox(
                    text='🞀',
                    fontsize="35",
                    foreground="689d6a",
                    padding=-2,
                ),
                widget.CurrentLayout(
                    background="689d6a",
                    foreground="282828",
                ),
                widget.TextBox(
                    text='🞀',
                    fontsize="35",
                    foreground="b16268",
                    background="689d6a",
                    padding=-2,
                ),
                widget.Volume(
                    background="b16268",
                    foreground="282828",
                ),
                widget.TextBox(
                    text='🞀',
                    fontsize="35",
                    foreground="458588",
                    background="b16268",
                    padding=-2,
                ),
                widget.Battery(
                    background="458588",
                    foreground="282828",
                    format='{char} {percent:2.0%} {hour:d}:{min:02d}',
                ),
                widget.TextBox(
                    text='🞀',
                    fontsize="35",
                    foreground="d79921",
                    background="458588",
                    padding=-2,
                ),
                widget.Backlight(
                    backlight_name="intel_backlight",
                    background="d79921",
                    foreground="282828",
                ),
                widget.TextBox(
                    text='🞀',
                    fontsize="35",
                    foreground="98971a",
                    background="d79921",
                    padding=-2,
                ),
                widget.Clock(
                    format='%d/%m/%y %H:%M',
                    background="98971a",
                    foreground="282828",
                ),
                widget.TextBox(
                    text='🞀',
                    fontsize="35",
                    foreground="282828",
                    background="98971a",
                    padding=-2,
                ),
                widget.WidgetBox(widgets=[
                    widget.TextBox(text="This widget is in the box"),
                    widget.StatusNotifier(
                        background="#3B4252",
                        padding=5,
                        # decorations=[
                        #     BorderDecoration(
                        #         border_width=[0, 0, 2, 0],
                        #         colour="#5E81AC",
                        #         padding_x=None,
                        #         padding_y=None,
                        #     ),
                        # ],
                    ),
                ]
                ),
            ],
            24,
            background="#282828",
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="kdewaller"),  # GPG key password entry
    ]
)

# floating_layout = layout.Floating(float_rules=[
#     # Run the utility of `xprop` to see the wm class and name of an X client.
#     {'wmclass': 'confirm'},
#     {'wmclass': 'dialog'},
#     {'wmclass': 'download'},
#     {'wmclass': 'error'},
#     {'wmclass': 'file_progress'},
#     {'wmclass': 'notification'},
#     {'wmclass': 'splash'},
#     {'wmclass': 'toolbar'},
#     {'wmclass': 'confirmreset'},  # gitk
#     {'wmclass': 'makebranch'},  # gitk
#     {'wmclass': 'maketag'},  # gitk
#     {'wname': 'branchdialog'},  # gitk
#     {'wname': 'pinentry'},  # GPG key password entry
#     {'wmclass': 'pinentry-gtk-2'},  # GTK+2 GPG password entry
#     {'wmclass': 'ssh-askpass'},  # ssh-askpass
# ])
auto_fullscreen = True
focus_on_window_activation = "smart"

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"


@hook.subscribe.startup_once
def start_once():
    """Run after qtile is started"""
    import os
    import subprocess

    autostart_file = os.path.expanduser('/home/mdic/.config/qtile/startup.sh')
    subprocess.call([autostart_file])

#
# @hook.subscribe.client_new
# def auto_togroup(window):
#     if window.match(wmclass="keepassxc"):
#         window.togroup("0")
