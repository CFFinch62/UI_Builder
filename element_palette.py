"""
Element Palette - UI element selection panel
"""

import customtkinter as ctk
from ui_elements import UIElement


class ElementPalette(ctk.CTkFrame):
    """Palette of UI elements that can be added to the canvas"""
    
    def __init__(self, parent, on_element_selected):
        super().__init__(parent)
        
        self.on_element_selected = on_element_selected
        
        # Title
        title = ctk.CTkLabel(
            self,
            text="Element Palette",
            font=("Arial", 16, "bold")
        )
        title.pack(pady=10)
        
        # Scrollable frame for elements
        self.scrollable_frame = ctk.CTkScrollableFrame(self)
        self.scrollable_frame.pack(fill="both", expand=True, padx=5, pady=5)
        
        # Add element buttons
        self.create_element_buttons()
        
    def create_element_buttons(self):
        """Create buttons for each element type"""
        
        # Group elements by category
        categories = {
            "Input Elements": ["TextBox", "TextArea", "Dropdown", "ComboBox"],
            "Selection Elements": ["CheckBox", "RadioButton", "Slider"],
            "Display Elements": ["Label", "Image"],
            "Action Elements": ["Button"],
            "Layout Elements": ["Spacer"]
        }
        
        for category, elements in categories.items():
            # Category label
            category_label = ctk.CTkLabel(
                self.scrollable_frame,
                text=category,
                font=("Arial", 12, "bold"),
                anchor="w"
            )
            category_label.pack(fill="x", padx=5, pady=(10, 5))
            
            # Element buttons
            for element_type in elements:
                btn = ctk.CTkButton(
                    self.scrollable_frame,
                    text=element_type,
                    command=lambda et=element_type: self.select_element(et),
                    anchor="w",
                    height=35
                )
                btn.pack(fill="x", padx=5, pady=2)
        
        # Instructions
        instructions = ctk.CTkLabel(
            self.scrollable_frame,
            text="\nClick an element, then\nclick on the canvas to\nplace it.",
            font=("Arial", 10),
            text_color="gray",
            justify="center"
        )
        instructions.pack(pady=20)
        
    def select_element(self, element_type):
        """Handle element selection"""
        self.on_element_selected(element_type)

