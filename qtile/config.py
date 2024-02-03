import os
import subprocess
from libqtile import bar, layout, widget, hook, qtile
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from qtile_extras import widget
from qtile_extras.widget.decorations import BorderDecoration
from qtile_extras.widget.decorations import RectDecoration


mod = "mod4"
terminal = "alacritty" 
home = os.path.expanduser('~')

keys = [

        # ESSENTIALS #

        # Important keys
        Key([mod, "shift"], "m", lazy.spawn("dmenu_run -i"), desc="Dmenu app"),
        Key([mod, "shift"], "d", lazy.spawn("rofi -show drun"), desc="App launcher"),
        Key([mod, "shift"], "r", lazy.reload_config(), desc="Reload the config"),
        Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
        Key([mod], "Space", lazy.next_layout(), desc="Toggle between layouts"),
        Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
        Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen on the focused window",),
        Key([mod], "r", lazy.spawncmd(), desc="Spawn prompt widget"),

        # Multimedia keys 
        # Lenovo Legion
        # Key([], "XF86MonBrightnessUp", lazy.spawn(home + "/.config/qtile/scripts/brightness_control.sh increase"), desc="Increase brightness"),
        # Key([], "XF86MonBrightnessDown", lazy.spawn(home + "/.config/qtile/scripts/brightness_control.sh decrease"), desc="Decrease birghtness"),
        Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +5%"), desc="Raise brightness level by 5%"),
        Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 5%-"), desc="Lower brightness level by 5%"),
        Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer sset Master 5%+"), desc="Raise volume level by 5%"),
        Key([], "XF86AudioLowerVolume", lazy.spawn("amixer sset Master 5%-"), desc="Lower volume level by 5%"),
        Key([], "XF86AudioMute", lazy.spawn("amixer sset Master 1+ toggle"), desc="Mute or unmute volume level"),

        # Applications
        Key([mod, "shift"], "Return", lazy.spawn("thunar"), desc="File manager"),
        Key([mod], "Return", lazy.spawn(terminal), desc="Terminal"),
        Key([mod], "b", lazy.spawn("chromium"), desc="Web browser"),
        Key([mod], "d", lazy.spawn("discord"), desc="Discord app"),
        Key([mod], "s", lazy.spawn("slack"), desc="Slack app"),
        Key([mod], "p", lazy.spawn("flameshot"), desc="Screenshot tool"),



        # WINDOW FOCUSING #

        # Change Window Focus
        Key([mod], "Up", lazy.layout.up()),
        Key([mod], "Down", lazy.layout.down()),
        Key([mod], "Left", lazy.layout.left()),
        Key([mod], "Right", lazy.layout.right()),

        # Resize Windows
        Key([mod, "control"], "Right",
            lazy.layout.grow_right(),
            lazy.layout.grow(),
            lazy.layout.increase_ratio(),
            lazy.layout.delete(),
            ),
        Key([mod, "control"], "Left",
            lazy.layout.grow_left(),
            lazy.layout.shrink(),
            lazy.layout.decrease_ratio(),
            lazy.layout.add(),
            ),
    Key([mod, "control"], "Up",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        ),
    Key([mod, "control"], "Down",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        ),

    # Shift focused window
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "Left", lazy.layout.swap_left()),
    Key([mod, "shift"], "Right", lazy.layout.swap_right()),

]

groups = [Group(i) for i in "1234567890"]

for i in groups:
    keys.extend(
            [
                # Change workspaces
                Key([mod], i.name, lazy.group[i.name].toscreen()),
                Key([mod], "Tab", lazy.screen.next_group()),
                Key([mod, "shift" ], "Tab", lazy.screen.prev_group()),

                # Move focused window to workspace 1-10 / follow
                Key([mod, "shift"],i.name,lazy.window.togroup(i.name, switch_group=True), desc="Switch to & move focused window to group {}".format(i.name),),

                # Moved focused window to workspace 1-10 / stay
                Key([mod, "control"], i.name, lazy.window.togroup(i.name), desc="move focused window to group {}".format(i.name)),
                ])

def init_layout_theme():
    return {"margin":8,
            "border_width":2,
            "border_focus": "#ff0000",
            "border_normal": "#2e3440"
            }

layout_theme = init_layout_theme()

layouts = [
        layout.MonadTall(**layout_theme, new_client_position='top'),
        layout.MonadWide(**layout_theme, new_client_position='top'),
        layout.Max(),
        ]


widget_defaults = dict(
        font="RobotoMono Nerd Font",
        fontsize=12,
        padding=3,
        )
extension_defaults = widget_defaults.copy()

screens = [
        Screen(
            top=bar.Bar(
                [
                    widget.Sep(
                        linewidth = 1,
                        padding = 5,
                        foreground = "#ff0000",
                        background = "#2e3440"
                        ),
                    widget.CurrentLayoutIcon(
                        padding = 4,
                        scale = 0.7,
                        foreground = "#d8dee9",
                        background = "#2e3440"
                        ),
                    widget.Sep(
                        linewidth = 1,
                        padding = 5,
                        foreground = "#ff0000",
                        background = "#2e3440"
                        ),
                    widget.GroupBox(
                        font = "RobotoMono Nerd Font Bold",
                        fontsize = 12,
                        margin_y = 2,
                        margin_x = 3,
                        padding_y = 2,
                        padding_x = 3,
                        borderwidth = 0,
                        disable_drag = True,
                        active = "#4c566a",
                        inactive = "#2e3440",
                        rounded = False,
                        highlight_method = "text",
                        this_current_screen_border = "#d8dee9",
                        foreground = "#4c566a",
                        background = "#2e3440"
                        ),
                    widget.Prompt(
                        font = "RobotoMono Nerd Font",
                        fontsize = 12,
                        background = "#2e3440",
                        foreground = "#d8dee9"
                        ),
                    widget.Sep(
                        linewidth = 1,
                        padding = 5,
                        foreground = "#ff0000",
                        background = "#2e3440"
                        ),
                    widget.WindowTabs(
                        font = "RobotoMono Nerd Font",
                        fontsize = 12,
                        foreground = "#d8dee9",
                        background = "#2e3440"
                        ),
                widget.Sep(
                        linewidth = 1,
                        padding = 5,
                        foreground = "#ff0000",
                        background = "#2e3440"
                        ),
                widget.Clock(
                        background = "#2e3440",
                        foreground = "#d8dee9",
                        font = "RobotoMono Nerd Font Bold",
                        fontsize = 12,
                        format = "%a %d %b %H:%M",
                        ),
                widget.Sep(
                        linewidth = 1,
                        padding = 5,
                        foreground = "#ff0000",
                        background = "#2e3440"
                        ),
                widget.Wlan(
                        font = "RobotoMono Nerd Font Bold",
                        fontsize = 12,
                        background = "#2e3440",
                        foreground = "#d8dee9",
                        format = "{essid} {percent:2.0%}"
                        ),
                widget.Sep(
                        linewidth = 1,
                        padding = 5,
                        foreground = "#ff0000",
                        background = "#2e3440"
                        ),
                widget.Volume(
                        font = "RobotoMono Nerd Font Bold",
                        fontsize = 12,
                        background = "#2e3440",
                        foreground = "#d8dee9",
                        fmt = "Vol: {}"
                        ),
                widget.Sep(
                        linewidth = 1,
                        padding = 5,
                        foreground = "#ff0000",
                        background = "#2e3440"
                        ),
                widget.Battery(
                        format = "Battery: {percent:2.0%}",
                        show_short_text = "False",
                        font = "RobotoMono Nerd Font Bold",
                        fontsize = 12,
                        background = "#2e3440",
                        foreground = "#d8dee9",
                        ),
                widget.Sep(
                        linewidth = 1,
                        padding = 5,
                        background = "#2e3440",
                        foreground = "#ff0000"
                        ),
                widget.Image(
                        filename = "~/Downloads/pngwing.com.png",
                        background = "#2e3440",
                        mouse_callbacks = {"Button1": lambda: qtile.cmd_spawn("shutdown now")}
                        ),
            ],
            # Sets bar height
           24,
        ),
        # Set wallpaper
        wallpaper="~/Downloads/code_wallpaper.png",
        wallpaper_mode='fill',
    ),
]

# Drag floating layouts.
mouse = [
        Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
        Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
        Click([mod], "Button2", lazy.window.bring_to_front()),
        ]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list

main = None

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/scripts/autostart.sh'])

follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(border_width=2, border_focus="#5e81ac", border_normal="#2e3440",
                                  float_rules=[
                                      # Run the utility of `xprop` to see the wm class and name of an X client.
                                      *layout.Floating.default_float_rules,
                                      Match(wm_class="confirmreset"),  # gitk
                                      Match(wm_class="makebranch"),  # gitk
                                      Match(wm_class="maketag"),  # gitk
                                      Match(wm_class="ssh-askpass"),  # ssh-askpass
                                      Match(title="branchdialog"),  # gitk
                                      Match(title="pinentry"),  # GPG key password entry
                                      ]
                                  )
auto_fullscreen = True
focus_on_window_activation = "focus"
reconfigure_screens = False 

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# Something about java being dumb?
wmname = "LG3D"
