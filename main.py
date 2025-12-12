"""
MD UI Builder - Main Application
A visual UI builder that generates markdown representations
"""

import customtkinter as ctk
from tkinter import filedialog, messagebox
import json
from ui_elements import UIElement, Container, UILayout
from canvas_view import CanvasView
from properties_panel import PropertiesPanel
from element_palette import ElementPalette
from ascii_exporter import export_to_ascii

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class MDUIBuilder(ctk.CTk):
    """Main application window"""
    
    def __init__(self):
        super().__init__()
        
        self.title("MD UI Builder")
        self.geometry("1400x900")
        
        # Initialize the UI layout
        self.ui_layout = UILayout("My UI Design")
        self.selected_item = None
        
        # Setup UI
        self.setup_ui()
        
        # Bind keyboard shortcuts
        self.bind("<Control-c>", self.on_copy)
        self.bind("<Control-v>", self.on_paste)
        
        # Status bar for copy/paste feedback
        self.status_var = ctk.StringVar()
        self.status_bar = ctk.CTkLabel(self, textvariable=self.status_var, height=20, anchor="w")
        self.status_bar.grid(row=2, column=0, columnspan=3, sticky="ew", padx=5, pady=(0, 5))
        self.status_var.set("Ready")
        
    def setup_ui(self):
        """Setup the main application UI"""
        
        # Configure grid
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        # Left panel - Element Palette
        self.left_panel = ctk.CTkFrame(self, width=200)
        self.left_panel.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        self.left_panel.grid_propagate(False)
        
        self.palette = ElementPalette(self.left_panel, self.on_element_selected)
        self.palette.pack(fill="both", expand=True)
        
        # Center panel - Canvas View
        self.center_panel = ctk.CTkFrame(self)
        self.center_panel.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)
        self.center_panel.grid_rowconfigure(1, weight=1)  # Canvas row gets all the space
        self.center_panel.grid_columnconfigure(0, weight=1)

        # Canvas toolbar - fixed height, no weight
        self.canvas_toolbar = ctk.CTkFrame(self.center_panel, height=40)
        self.canvas_toolbar.grid(row=0, column=0, sticky="ew", padx=5, pady=(5, 0))
        self.canvas_toolbar.grid_propagate(False)  # Prevent toolbar from expanding

        ctk.CTkLabel(self.canvas_toolbar, text="Canvas", font=("Arial", 14, "bold")).pack(side="left", padx=10)

        ctk.CTkButton(
            self.canvas_toolbar,
            text="Add Container",
            command=self.add_container,
            height=28
        ).pack(side="left", padx=5)

        ctk.CTkButton(
            self.canvas_toolbar,
            text="Delete Selected",
            command=self.delete_selected,
            fg_color="darkred",
            height=28
        ).pack(side="left", padx=5)

        # Canvas - takes all remaining space
        self.canvas_view = CanvasView(
            self.center_panel,
            self.ui_layout,
            self.on_item_selected
        )
        self.canvas_view.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
        
        # Right panel - Properties
        self.right_panel = ctk.CTkFrame(self, width=300)
        self.right_panel.grid(row=0, column=2, sticky="nsew", padx=5, pady=5)
        self.right_panel.grid_propagate(False)
        
        self.properties_panel = PropertiesPanel(
            self.right_panel,
            self.on_property_changed
        )
        self.properties_panel.pack(fill="both", expand=True)
        
        # Bottom panel - Actions
        self.bottom_panel = ctk.CTkFrame(self, height=60)
        self.bottom_panel.grid(row=1, column=0, columnspan=3, sticky="ew", padx=5, pady=5)
        
        ctk.CTkButton(
            self.bottom_panel,
            text="Export to ASCII Art",
            command=self.export_ascii,
            font=("Arial", 14, "bold"),
            height=40,
            fg_color="#27ae60"
        ).pack(side="left", padx=10, pady=10)

        ctk.CTkButton(
            self.bottom_panel,
            text="Export to Markdown",
            command=self.export_markdown,
            font=("Arial", 14, "bold"),
            height=40
        ).pack(side="left", padx=10, pady=10)

        ctk.CTkButton(
            self.bottom_panel,
            text="Save Project",
            command=self.save_project,
            height=40
        ).pack(side="left", padx=10, pady=10)
        
        ctk.CTkButton(
            self.bottom_panel,
            text="Load Project",
            command=self.load_project,
            height=40
        ).pack(side="left", padx=10, pady=10)
        
        ctk.CTkButton(
            self.bottom_panel,
            text="New Project",
            command=self.new_project,
            height=40
        ).pack(side="left", padx=10, pady=10)
        
    def on_element_selected(self, element_type):
        """Handle element selection from palette"""
        self.canvas_view.set_adding_mode(element_type)
        
    def on_item_selected(self, item):
        """Handle item selection from canvas"""
        self.selected_item = item
        self.properties_panel.load_item(item)
        
    def on_property_changed(self):
        """Handle property changes"""
        self.canvas_view.redraw()
        
    def on_copy(self, event=None):
        """Handle copy command"""
        if self.canvas_view.copy_selected():
            self.status_var.set("Copied item to clipboard")
        else:
            self.status_var.set("No item selected to copy")
        return "break"  # Prevent default behavior
        
    def on_paste(self, event=None):
        """Handle paste command"""
        if not hasattr(self.canvas_view, 'copied_item') or not self.canvas_view.copied_item:
            self.status_var.set("No item in clipboard to paste")
            return "break"
            
        # Get mouse position relative to canvas
        x = self.canvas_view.canvas.canvasx(self.winfo_pointerx() - self.canvas_view.winfo_rootx())
        y = self.canvas_view.canvas.canvasy(self.winfo_pointery() - self.canvas_view.winfo_rooty())
        
        if self.canvas_view.paste_item(x, y):
            self.status_var.set("Item pasted")
        else:
            self.status_var.set("Failed to paste item")
        return "break"  # Prevent default behavior
        
    def add_container(self):
        """Add a new container"""
        self.canvas_view.set_adding_mode("Container")
        
    def delete_selected(self):
        """Delete the selected item"""
        if self.selected_item and self.selected_item != self.ui_layout.root_container:
            if self.selected_item.parent:
                self.selected_item.parent.remove_child(self.selected_item)
                self.selected_item = None
                self.properties_panel.clear()
                self.canvas_view.redraw()
        else:
            messagebox.showwarning("Cannot Delete", "Cannot delete the root container or no item selected")
    
    def export_ascii(self):
        """Export the UI layout to ASCII art"""
        filename = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )

        if filename:
            try:
                # Auto-scale to fit in IDE window (120 chars wide, 60 lines tall)
                # This makes it easy to view without scrolling
                export_to_ascii(self.ui_layout, filename, scale_factor=None, max_width=120, max_height=60)
                messagebox.showinfo("Success", f"Exported ASCII art to {filename}\n\nScaled to fit IDE window (max 120x60 chars)")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to export: {str(e)}")

    def export_markdown(self):
        """Export the UI layout to markdown"""
        filename = filedialog.asksaveasfilename(
            defaultextension=".md",
            filetypes=[("Markdown files", "*.md"), ("All files", "*.*")]
        )

        if filename:
            try:
                self.ui_layout.save_to_file(filename)
                messagebox.showinfo("Success", f"UI layout exported to {filename}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to export: {str(e)}")

    def save_project(self):
        """Save the project to JSON"""
        filename = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
        )

        if filename:
            try:
                self.ui_layout.save_to_json(filename)
                messagebox.showinfo("Success", f"Project saved to {filename}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save: {str(e)}")

    def load_project(self):
        """Load a project from JSON"""
        filename = filedialog.askopenfilename(
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
        )

        if filename:
            try:
                self.ui_layout = UILayout.load_from_json(filename)
                self.selected_item = None
                self.properties_panel.clear()
                self.canvas_view.set_layout(self.ui_layout)
                self.canvas_view.redraw()
                messagebox.showinfo("Success", f"Project loaded from {filename}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load: {str(e)}")
    
    def new_project(self):
        """Create a new project"""
        if messagebox.askyesno("New Project", "Create a new project? Unsaved changes will be lost."):
            self.ui_layout = UILayout("My UI Design")
            self.selected_item = None
            self.properties_panel.clear()
            self.canvas_view.set_layout(self.ui_layout)
            self.canvas_view.redraw()


def main():
    """Main entry point"""
    app = MDUIBuilder()
    app.mainloop()


if __name__ == "__main__":
    main()

