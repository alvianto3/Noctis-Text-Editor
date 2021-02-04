import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import font
from tkinter import colorchooser

class Menubar:
    
    def __init__(self, parent):
        font_specs = ("ubuntu", 8)

        menubar = tk.Menu(parent.master, font=font_specs)
        parent.master.config(menu=menubar)
        
        # file menu drop_down
        file_dropdown = tk.Menu(menubar,
                                font=font_specs,
                                tearoff=0)
        file_dropdown.add_command(label="New File",
                                  accelerator="Ctrl+N",
                                  command=parent.new_file)
        file_dropdown.add_command(label="New Window",
                                  accelerator="Ctrl+Shift+N",
                                  command=parent.new_window)
        file_dropdown.add_separator()
        file_dropdown.add_command(label="Open File",
                                  accelerator="Ctrl+O",
                                  command=parent.open_file)
        file_dropdown.add_command(label="Save",
                                  accelerator="Ctrl+S",
                                  command=parent.save)
        file_dropdown.add_command(label="Save As",
                                  accelerator="Ctrl+Shift+S",
                                  command=parent.save_as)
        file_dropdown.add_separator()
        file_dropdown.add_command(label="Exit",
                                  command=parent.master.destroy)

        # Edit menu drop_down
        edit_dropdown = tk.Menu(menubar,
                                font=font_specs,
                                tearoff=0)
        edit_dropdown.add_command(label="Undo",
                                  accelerator="Ctrl+Z",
                                  command=parent.textarea.edit_undo)
        edit_dropdown.add_command(label="Redo",
                                  accelerator="Ctrl+Y",
                                  command=parent.textarea.edit_redo)
        edit_dropdown.add_separator()
        edit_dropdown.add_command(label="Cut",
                                  accelerator="Ctrl+X",        
                                  command=parent.cut_text)
        edit_dropdown.add_command(label="Copy",
                                  accelerator="Ctrl+C",
                                  command=parent.copy_text)
        edit_dropdown.add_command(label="Paste",
                                  accelerator="Ctrl+V",
                                  command=parent.paste_text)
        edit_dropdown.add_command(label="Delete",
                                  accelerator="Del",
                                  command=parent.delete_text)

        # Text menu drop_down
        text_dropdown = tk.Menu(menubar,
                                font=font_specs,
                                tearoff=0)
        text_dropdown.add_command(label="Bold",
                                  command=parent.bold_text)
        text_dropdown.add_command(label="Italic",
                                  command=parent.italic_text)
        
        # Format menu drop_down
        format_dropdown = tk.Menu(menubar,
                                font=font_specs,
                                tearoff=0)
        format_dropdown.add_command(label="Text Color",
                                    command=parent.text_color)
        format_dropdown.add_command(label="Background color",
                                    command=parent.background_color)
        format_dropdown.add_command(label="All Text Color",
                                    command=parent.all_text_color)

        # About menu drop_down
        about_dropdown = tk.Menu(menubar,
                                 font=font_specs,
                                 tearoff=0)
        about_dropdown.add_command(label="Release Notes",
                                   command=self.show_release_notes)
        about_dropdown.add_separator()
        about_dropdown.add_command(label="About Noctis Text",
                                   command=self.show_about_message)

        # Menubar
        menubar.add_cascade(label="File",
                            menu=file_dropdown)
        menubar.add_cascade(label="Edit",
                            menu=edit_dropdown)
        menubar.add_cascade(label="Text",
                            menu=text_dropdown)
        menubar.add_cascade(label="Format",
                            menu=format_dropdown)
        menubar.add_cascade(label="About",
                            menu=about_dropdown)
        
    # Show release notes Noctis
    def show_release_notes(self):
        box_title = "Release Notes"
        box_message = "Version 0.1 - Alvin"
        messagebox.showinfo(box_title, box_message)
    
    # Show about Noctis App
    def show_about_message(self):
        box_title = "About Noctis"
        box_message = "A Simple Text Editor"
        messagebox.showinfo(box_title, box_message)

    # Show feature version
    def show_feature(self):
        box_title = "Show Feature"
        box_message = "Version 0.1 - Alvin. the text editor is trial. wait a update"
        messagebox.showinfo(box_title, box_message)


class Statusbar:

    def __init__(self, parent):
        
        font_specs = ("ubuntu", 8)
        
        self.status = tk.StringVar()
        self.status.set("Noctis - 0.1 Alvin")

        #statusbar
        label = tk.Label(parent.textarea, textvariable=self.status,
                         fg="black", bg="lightgrey", anchor='sw',
                         font=font_specs)
        label.pack(fill=tk.X, side=tk.BOTTOM)
    
    # Show status update
    def update_status(self, *args):
        if isinstance(args[0], bool):
            self.status.set("Your File Has Been Saved!")
        else:
            self.status.set("Noctis - 0.1 Alvin")

class NoctisText:

    def __init__(self, master):
        master.title("Untitled - Noctis")
        master.iconbitmap('icon/text-editor.ico')
        master.geometry("800x700")
        font_specs = ("Consolas", 12)
        
        self.master = master
        self.filename = None
       
        # Main view textarea & scrollbar
        self.textarea = tk.Text(master, font=font_specs)
        self.scroll = tk.Scrollbar(self.textarea, command=self.textarea.yview)
        self.hor_scroll = tk.Scrollbar(self.textarea, orient="horizontal",
                                       command=self.textarea.xview)

        # Textarea settings
        self.textarea.configure(xscrollcommand=self.hor_scroll.set,
                                yscrollcommand=self.scroll.set,
                                undo=True, wrap="none")

        # Menubar, statusbar, sortcutsbarr call
        self.menubar = Menubar(self)
        self.statusbar = Statusbar(self)
        self.bind_shortcuts()

        # Call scrollbar
        self.hor_scroll.pack(side=tk.BOTTOM, fill=tk.X)
        self.scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.textarea.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)


    # Windows title set
    def set_window_title(self, name=None):
        if name:
            self.master.title(name + " - Noctis")
        else:
            self.master.title("Untitled - Noctis")
    
    # New File
    def new_file(self, *args):
        self.textarea.delete(1.0, tk.END)
        self.filename = None
        self.set_window_title()
    
    # New Window
    def new_window(self, *args):
        master = tk.Tk()
        nt = NoctisText(master)
        master.mainloop()
    
    # Open File
    def open_file(self, *args):
        self.filename = filedialog.askopenfilename(
            defaultextension=".txt",
            filetypes=[("All Files", "*.*"),
                       ("Text Files", "*.txt"),
                       ("Python Scripts", "*.py"),
                       ("Markdown Documents", "*.md"),
                       ("JavaScript Files", "*.js"),
                       ("HTML documents", "*.html"),
                       ("CSS Documents", "*.css")])

        if self.filename:
            self.textarea.delete(1.0, tk.END)
            with open(self.filename, "r") as f:
                self.textarea.insert(1.0, f.read())
            self.set_window_title(self.filename)

    # Save File
    def save(self, *args):
        if self.filename:
            try:
                textarea_content = self.textarea.get(1.0, tk.END)
                with open(self.filename, "w") as f:
                    f.write(textarea_content)
                self.statusbar.update_status(True)
            except Exception as e:
                print(e)
        else:
            self.save_as()

    # Save As File
    def save_as(self, *args):
        try:
            new_file = filedialog.asksaveasfilename(
                initialfile="Untitled.txt",
                defaultextension=".txt",
                filetypes=[("All Files", "*.*"),
                           ("Text Files", "*.txt"),
                           ("Python Scripts", "*.py"),
                           ("Markdown Documents", "*.md"),
                           ("JavaScript Files", "*.js"),
                           ("HTML documents", "*.html"),
                           ("CSS Documents", "*.css")])
            textarea_content = self.textarea.get(1.0, tk.END)
            with open(new_file, "w") as f:
                f.write(textarea_content)
            self.filename = new_file
            self.set_window_title(self.filename)
            self.statusbar.update_status(True)
        except Exception as e:
            print(e)
    
    # Cut Text
    def cut_text(self, *args):
        #make cut text global 
        global selected
        
        if self.textarea.selection_get():
            #grab selected text from text area
            selected = self.textarea.selection_get()
            
            #delete selected text from text area
            self.textarea.delete("sel.first", "sel.last")
    
    # Copy Text
    def copy_text(self, *args):
        #make copy text global 
        global selected
        
        if self.textarea.selection_get():
            #grab selected text from text area
            selected = self.textarea.selection_get()
    
    # Paste Text
    def paste_text(self, *args):
        if selected:
            position = self.textarea.index(INSERT)
            self.textarea.insert(position, selected)

    # Delete Text
    def delete_text(self, *args):
        if self.textarea.selection_get():
            #delete selected text from text area
            self.textarea.delete("sel.first", "sel.last")
    
    # Bold Text
    def bold_text(self, *args):
        # Create our font
        bold_font = font.Font(self.textarea, self.textarea.cget("font"))
        bold_font.configure(weight="bold")

        # Configure a tag
        self.textarea.tag_configure("bold", font=bold_font)

        # Define Current current_tags
        current_tags = self.textarea.tag_names("sel.first")

        # If statements to see bold text
        if "bold" in current_tags:
            self.textarea.tag_remove("bold", "sel.first", "sel.last")
        else:
            self.textarea.tag_add("bold", "sel.first", "sel.last")

    # Italic Text
    def italic_text(self, *args):
        # Create our font
        italics_font = font.Font(self.textarea, self.textarea.cget("font"))
        italics_font.configure(slant="italic")

        # Configure a tag
        self.textarea.tag_configure("italic", font=italics_font)

        # Define Current current_tags
        current_tags = self.textarea.tag_names("sel.first")

        # If statements to see bold text
        if "italic" in current_tags:
            self.textarea.tag_remove("italic", "sel.first", "sel.last")
        else:
            self.textarea.tag_add("italic", "sel.first", "sel.last")
    
    # Change Selected Text Color
    def text_color(self, *args):
        # Pick a color
        my_color = colorchooser.askcolor()[1]
        if my_color:
            # Create our font
            color_font = font.Font(self.textarea, self.textarea.cget("font"))

            # Configure a tag
            self.textarea.tag_configure("colored", font=color_font, foreground=my_color)

            # Define Current current_tags
            current_tags = self.textarea.tag_names("sel.first")

            # If statements to see color text
            if "colored" in current_tags:
                self.textarea.tag_remove("colored", "sel.first", "sel.last")
            else: 
                self.textarea.tag_add("colored", "sel.first", "sel.last")
    
    # Change Background color
    def background_color(self, *args):
        my_color = colorchooser.askcolor()[1]
        if my_color:
            self.textarea.config(bg=my_color)
    
    # Change all color text
    def all_text_color(self, *args):
        my_color = colorchooser.askcolor()[1]
        if my_color:
            self.textarea.config(fg=my_color)

    # Shortcuts
    def bind_shortcuts(self):
        #shortcuts file menubar
        self.textarea.bind('<Control-n>', self.new_file)
        self.textarea.bind('<Control-N>', self.new_window)
        self.textarea.bind('<Control-o>', self.open_file)
        self.textarea.bind('<Control-s>', self.save)
        self.textarea.bind('<Control-S>', self.save_as)

        #shortcuts edit menubar
        self.textarea.bind('<Control-x>', self.cut_text)
        self.textarea.bind('<Control-c>', self.copy_text)
        self.textarea.bind('<Control-v>', self.paste_text)
        self.textarea.bind('<Delete>', self.delete_text)
        
        #Key statusbar
        self.textarea.bind('<Key>', self.statusbar.update_status)

    

if __name__ == "__main__":
    master = tk.Tk()
    nt = NoctisText(master)
    master.mainloop()