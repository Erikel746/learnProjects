const gi = require("node-gtk");
const Gtk = gi.require("Gtk", "3.0");
const Gdk = gi.require("Gdk", "3.0");

gi.startLoop();
Gtk.init(null);
const window = new Gtk.Window();
window.setDefaultSize(400, 400);
window.on("destroy", () => Gtk.mainQuit());
window.showAll();

Gtk.main();
