#!/usr/bin/env python3
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GLib, Gdk
import time

class FloatingClock(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Clock")
        self.set_decorated(False)
        self.set_keep_above(False)  # always on top
        self.set_default_size(250, 50)  # height kam kiya
        self.set_resizable(True)
        self.set_app_paintable(True)
        self.set_type_hint(Gdk.WindowTypeHint.NORMAL)  # normal window instead of DESKTOP
        self.set_skip_taskbar_hint(True)
        self.set_skip_pager_hint(True)
        self.stick()

        # Top-left position with margin
        self.move(40, 40)

        screen = self.get_screen()
        visual = screen.get_rgba_visual()
        if visual:
            self.set_visual(visual)

        # Overlay container for label on top of drawing
        overlay = Gtk.Overlay()
        self.add(overlay)

        # Drawing area for glassy rectangle
        darea = Gtk.DrawingArea()
        darea.connect("draw", self.on_draw)
        overlay.add(darea)

        # Label for time
        self.label = Gtk.Label()
        self.label.set_markup("<span font='30' foreground='#000'>00:00:00</span>")  # font black for white bg
        self.label.set_halign(Gtk.Align.CENTER)
        self.label.set_valign(Gtk.Align.CENTER)
        overlay.add_overlay(self.label)

        # Update clock every second
        GLib.timeout_add(1000, self.update_time)
        self.update_time()

        self.show_all()

    def on_draw(self, widget, cr):
        # Draw semi-transparent black rounded rectangle
        alloc = self.get_allocation()
        width, height = alloc.width, alloc.height
        cr.set_source_rgba(0, 0, 0, 0.8)  # black + alpha
        radius = 15
        cr.move_to(radius, 0)
        cr.line_to(width-radius, 0)
        cr.arc(width-radius, radius, radius, -90*3.14/180, 0)
        cr.line_to(width, height-radius)
        cr.arc(width-radius, height-radius, radius, 0, 90*3.14/180)
        cr.line_to(radius, height)
        cr.arc(radius, height-radius, radius, 90*3.14/180, 180*3.14/180)
        cr.line_to(0, radius)
        cr.arc(radius, radius, radius, 180*3.14/180, 270*3.14/180)
        cr.close_path()
        cr.fill()
        return False

    def update_time(self):
        # 24-hour format
        self.label.set_markup(f"<span font='30' foreground='white'>{time.strftime('%I:%M:%S %p')}</span>")
        return True


if __name__ == "__main__":
    win = FloatingClock()
    win.connect("destroy", Gtk.main_quit)
    Gtk.main()
