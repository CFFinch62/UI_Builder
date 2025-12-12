"""
Properties Panel - Edit properties of selected items
"""

import customtkinter as ctk
from ui_elements import UIElement, Container


class PropertiesPanel(ctk.CTkScrollableFrame):
    """Panel for editing properties of selected items"""

    def __init__(self, parent, on_property_changed):
        super().__init__(parent)

        self.on_property_changed = on_property_changed
        self.current_item = None

        # Create a container frame for all property widgets
        # This makes it easy to clear everything at once
        self.properties_container = None

        # Title (permanent widget)
        self.title_label = ctk.CTkLabel(
            self,
            text="Properties",
            font=("Arial", 16, "bold")
        )
        self.title_label.pack(pady=10)

        # No selection label (permanent widget)
        self.no_selection_label = ctk.CTkLabel(
            self,
            text="No item selected",
            font=("Arial", 12),
            text_color="gray"
        )
        self.no_selection_label.pack(pady=20)

    def clear(self):
        """Clear all property widgets"""
        # Hide the no selection label if it exists
        if hasattr(self, 'no_selection_label') and self.no_selection_label.winfo_ismapped():
            self.no_selection_label.pack_forget()

        # Destroy the entire properties container if it exists
        if hasattr(self, 'properties_container') and self.properties_container is not None:
            try:
                # First, destroy all children of the properties container
                for widget in self.properties_container.winfo_children():
                    widget.destroy()
                # Then destroy the container itself
                self.properties_container.destroy()
            except Exception as e:
                print(f"Error clearing properties container: {e}")
            self.properties_container = None

        self.current_item = None

        # Show the no selection label if it exists
        if hasattr(self, 'no_selection_label'):
            self.no_selection_label.pack(pady=20)
        
    def load_item(self, item):
        """Load an item's properties for editing"""
        # Clear existing widgets first
        self.clear()
        
        # Hide the no selection label if it exists
        if hasattr(self, 'no_selection_label'):
            self.no_selection_label.pack_forget()

        # Create a new container frame for all property widgets
        if self.properties_container is not None:
            self.properties_container.destroy()
            
        self.properties_container = ctk.CTkFrame(self, fg_color="transparent")
        self.properties_container.pack(fill="both", expand=True, padx=5, pady=5)

        self.current_item = item

        if item is not None:
            if isinstance(item, Container):
                self.load_container_properties(item)
            elif isinstance(item, UIElement):
                self.load_element_properties(item)
        else:
            # Show no selection label if item is None
            if hasattr(self, 'no_selection_label'):
                self.no_selection_label.pack(pady=20)
            
    def load_container_properties(self, container):
        """Load container properties"""
        # Name
        self.add_property_field("Name", container.name, self.update_name)
        
        # Position
        self.add_property_field("X Position", str(container.x), lambda v: self.update_position(v, "x"))
        self.add_property_field("Y Position", str(container.y), lambda v: self.update_position(v, "y"))
        
        # Size
        self.add_property_field("Width", str(container.width), lambda v: self.update_size(v, "width"))
        self.add_property_field("Height", str(container.height), lambda v: self.update_size(v, "height"))
        
        # Orientation
        self.add_dropdown_field(
            "Orientation",
            container.orientation,
            ["horizontal", "vertical"],
            self.update_orientation
        )
        
        # Padding
        self.add_property_field("Padding", str(container.padding), self.update_padding)
        
        # Background
        self.add_property_field("Background", container.background, self.update_background)
        
    def load_element_properties(self, element):
        """Load element properties"""
        # Name
        self.add_property_field("Name", element.name, self.update_name)
        
        # Type (read-only)
        type_label = ctk.CTkLabel(self.properties_container, text="Type:", anchor="w")
        type_label.pack(fill="x", padx=10, pady=(10, 0))
        type_value = ctk.CTkLabel(
            self.properties_container,
            text=element.element_type,
            anchor="w",
            text_color="gray"
        )
        type_value.pack(fill="x", padx=10, pady=(0, 5))
        
        # Position
        self.add_property_field("X Position", str(element.x), lambda v: self.update_position(v, "x"))
        self.add_property_field("Y Position", str(element.y), lambda v: self.update_position(v, "y"))
        
        # Size
        self.add_property_field("Width", str(element.width), lambda v: self.update_size(v, "width"))
        self.add_property_field("Height", str(element.height), lambda v: self.update_size(v, "height"))
        
        # Text
        self.add_property_field("Text", element.text, self.update_text)
        
        # Enabled
        self.add_checkbox_field("Enabled", element.enabled, self.update_enabled)
        
        # Visible
        self.add_checkbox_field("Visible", element.visible, self.update_visible)
        
        # Custom properties section
        self.add_separator()
        custom_label = ctk.CTkLabel(
            self.properties_container,
            text="Custom Properties",
            font=("Arial", 12, "bold")
        )
        custom_label.pack(fill="x", padx=10, pady=10)

        # Add custom property button
        add_prop_btn = ctk.CTkButton(
            self.properties_container,
            text="+ Add Property",
            command=self.add_custom_property
        )
        add_prop_btn.pack(fill="x", padx=10, pady=5)

        # Show existing custom properties
        for key, value in element.properties.items():
            self.add_custom_property_field(key, str(value))
            
    def add_separator(self):
        """Add a visual separator"""
        separator = ctk.CTkFrame(self.properties_container, height=2, fg_color="gray")
        separator.pack(fill="x", padx=10, pady=10)

    def add_property_field(self, label, value, callback):
        """Add a text property field"""
        label_widget = ctk.CTkLabel(self.properties_container, text=f"{label}:", anchor="w")
        label_widget.pack(fill="x", padx=10, pady=(10, 0))

        entry = ctk.CTkEntry(self.properties_container)
        entry.insert(0, value)
        entry.pack(fill="x", padx=10, pady=(0, 5))

        # Bind change event
        entry.bind("<KeyRelease>", lambda e: callback(entry.get()))

    def add_dropdown_field(self, label, value, options, callback):
        """Add a dropdown property field"""
        label_widget = ctk.CTkLabel(self.properties_container, text=f"{label}:", anchor="w")
        label_widget.pack(fill="x", padx=10, pady=(10, 0))

        dropdown = ctk.CTkComboBox(
            self.properties_container,
            values=options,
            command=callback
        )
        dropdown.set(value)
        dropdown.pack(fill="x", padx=10, pady=(0, 5))

    def add_checkbox_field(self, label, value, callback):
        """Add a checkbox property field"""
        checkbox = ctk.CTkCheckBox(
            self.properties_container,
            text=label,
            command=lambda: callback(checkbox.get())
        )
        if value:
            checkbox.select()
        checkbox.pack(fill="x", padx=10, pady=5)
        
    def add_custom_property_field(self, key, value):
        """Add a custom property field"""
        frame = ctk.CTkFrame(self.properties_container)
        frame.pack(fill="x", padx=10, pady=2)

        key_entry = ctk.CTkEntry(frame, width=100, placeholder_text="Key")
        key_entry.insert(0, key)
        key_entry.pack(side="left", padx=2)

        value_entry = ctk.CTkEntry(frame, placeholder_text="Value")
        value_entry.insert(0, value)
        value_entry.pack(side="left", fill="x", expand=True, padx=2)

        # Bind change events
        key_entry.bind("<KeyRelease>", lambda e: self.update_custom_property(key, key_entry.get(), value_entry.get()))
        value_entry.bind("<KeyRelease>", lambda e: self.update_custom_property(key, key_entry.get(), value_entry.get()))

        delete_btn = ctk.CTkButton(
            frame,
            text="X",
            width=30,
            command=lambda: self.delete_custom_property(key, frame)
        )
        delete_btn.pack(side="left", padx=2)
        
    def add_custom_property(self):
        """Add a new custom property"""
        if isinstance(self.current_item, UIElement):
            self.add_custom_property_field("", "")
            
    def update_name(self, value):
        """Update item name"""
        if self.current_item:
            self.current_item.name = value
            self.on_property_changed()
            
    def update_position(self, value, axis):
        """Update item position"""
        if self.current_item:
            try:
                if axis == "x":
                    self.current_item.x = int(value)
                else:
                    self.current_item.y = int(value)
                self.on_property_changed()
            except ValueError:
                pass
                
    def update_size(self, value, dimension):
        """Update item size"""
        if self.current_item:
            try:
                if dimension == "width":
                    self.current_item.width = int(value)
                else:
                    self.current_item.height = int(value)
                self.on_property_changed()
            except ValueError:
                pass
                
    def update_orientation(self, value):
        """Update container orientation"""
        if isinstance(self.current_item, Container):
            self.current_item.orientation = value
            self.on_property_changed()
            
    def update_padding(self, value):
        """Update container padding"""
        if isinstance(self.current_item, Container):
            try:
                self.current_item.padding = int(value)
                self.on_property_changed()
            except ValueError:
                pass
                
    def update_background(self, value):
        """Update container background"""
        if isinstance(self.current_item, Container):
            self.current_item.background = value
            self.on_property_changed()
            
    def update_text(self, value):
        """Update element text"""
        if isinstance(self.current_item, UIElement):
            self.current_item.text = value
            self.on_property_changed()
            
    def update_enabled(self, value):
        """Update element enabled state"""
        if isinstance(self.current_item, UIElement):
            self.current_item.enabled = bool(value)
            self.on_property_changed()
            
    def update_visible(self, value):
        """Update element visible state"""
        if isinstance(self.current_item, UIElement):
            self.current_item.visible = bool(value)
            self.on_property_changed()
            
    def update_custom_property(self, old_key, new_key, value):
        """Update a custom property"""
        if isinstance(self.current_item, UIElement):
            if old_key in self.current_item.properties:
                del self.current_item.properties[old_key]
            if new_key:
                self.current_item.properties[new_key] = value
            self.on_property_changed()
            
    def delete_custom_property(self, key, frame):
        """Delete a custom property"""
        if isinstance(self.current_item, UIElement):
            if key in self.current_item.properties:
                del self.current_item.properties[key]
            frame.destroy()
            self.on_property_changed()

