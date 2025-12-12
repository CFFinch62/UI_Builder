"""
Canvas View for visual UI building
"""

import customtkinter as ctk
import tkinter as tk
from ui_elements import UIElement, Container


class CanvasView(ctk.CTkFrame):
    """Canvas for drawing and interacting with UI elements"""
    
    # Colors for visual representation
    CONTAINER_COLOR = "#3498db"
    CONTAINER_HORIZONTAL_COLOR = "#2ecc71"
    ELEMENT_COLOR = "#e74c3c"
    SELECTED_COLOR = "#f39c12"
    BACKGROUND_COLOR = "#2b2b2b"
    
    def __init__(self, parent, ui_layout, on_item_selected):
        super().__init__(parent)
        
        self.ui_layout = ui_layout
        self.on_item_selected = on_item_selected
        self.adding_mode = None  # What we're adding (element type or "Container")
        self.selected_item = None
        self.dragging_item = None
        self.resizing_item = None
        self.drag_start_x = 0
        self.drag_start_y = 0
        self.original_width = 0
        self.original_height = 0
        self.copied_item = None  # Store the copied item for pasting
        self.resize_handle_size = 10  # Size of the resize handle
        
        # Scrollbars (pack first so they don't get covered)
        self.v_scrollbar = ctk.CTkScrollbar(self, orientation="vertical")
        self.v_scrollbar.pack(side="right", fill="y")

        self.h_scrollbar = ctk.CTkScrollbar(self, orientation="horizontal")
        self.h_scrollbar.pack(side="bottom", fill="x")

        # Create canvas
        self.canvas = tk.Canvas(
            self,
            bg=self.BACKGROUND_COLOR,
            highlightthickness=0,
            xscrollcommand=self.h_scrollbar.set,
            yscrollcommand=self.v_scrollbar.set
        )
        self.canvas.pack(fill="both", expand=True)

        # Configure scrollbars
        self.h_scrollbar.configure(command=self.canvas.xview)
        self.v_scrollbar.configure(command=self.canvas.yview)
        self.canvas.configure(scrollregion=(0, 0, 2000, 2000))
        
        # Bind events
        self.canvas.bind("<Button-1>", self.on_canvas_click)
        self.canvas.bind("<B1-Motion>", self.on_canvas_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_canvas_release)
        self.canvas.bind("<Motion>", self.on_canvas_motion)
        
        # Draw initial layout
        self.redraw()
        
    def set_layout(self, ui_layout):
        """Set a new layout"""
        self.ui_layout = ui_layout
        self.selected_item = None
        self.redraw()
        
    def set_adding_mode(self, item_type):
        """Set the mode for adding new items"""
        self.adding_mode = item_type
        self.canvas.configure(cursor="crosshair")
        
    def clear_adding_mode(self):
        """Clear adding mode"""
        self.adding_mode = None
        self.canvas.configure(cursor="")
        
    def redraw(self):
        """Redraw the entire canvas"""
        self.canvas.delete("all")
        
        # Draw grid
        self.draw_grid()
        
        # Draw root container and all children
        self.draw_container(self.ui_layout.root_container)
        
    def draw_grid(self):
        """Draw a grid on the canvas"""
        grid_size = 20
        width = 2000
        height = 2000
        
        # Vertical lines
        for x in range(0, width, grid_size):
            self.canvas.create_line(x, 0, x, height, fill="#3a3a3a", width=1)
        
        # Horizontal lines
        for y in range(0, height, grid_size):
            self.canvas.create_line(0, y, width, y, fill="#3a3a3a", width=1)
            
    def draw_container(self, container, parent_x=0, parent_y=0):
        """Draw a container and all its children"""
        x = parent_x + container.x
        y = parent_y + container.y
        
        # Choose color based on orientation
        if container == self.selected_item:
            color = self.SELECTED_COLOR
        elif container.orientation == "horizontal":
            color = self.CONTAINER_HORIZONTAL_COLOR
        else:
            color = self.CONTAINER_COLOR
        
        # Draw container rectangle
        self.canvas.create_rectangle(
            x, y, x + container.width, y + container.height,
            outline=color,
            width=3,
            fill="",
            tags=("container", f"item_{id(container)}")
        )
        
        # Draw label
        self.canvas.create_text(
            x + 5, y + 5,
            text=f"{container.name} ({container.orientation})",
            anchor="nw",
            fill="white",
            font=("Arial", 10, "bold"),
            tags=("label", f"item_{id(container)}")
        )
        
        # Draw children
        for child in container.children:
            if isinstance(child, Container):
                self.draw_container(child, x, y)
            elif isinstance(child, UIElement):
                self.draw_element(child, x, y)
                
    def draw_element(self, element, parent_x=0, parent_y=0):
        """Draw a UI element"""
        x = parent_x + element.x
        y = parent_y + element.y
        
        # Determine element color based on selection
        is_selected = element == self.selected_item
        color = self.SELECTED_COLOR if is_selected else self.ELEMENT_COLOR
        
        # Draw element
        self.canvas.create_rectangle(
            x, y, x + element.width, y + element.height,
            outline=color,
            width=2,
            fill="#34495e",
            tags=("element", f"item_{id(element)}")
        )
        
        # Draw resize handle if selected
        if is_selected:
            self.draw_resize_handle(x, y, element, parent_x, parent_y)
        
        # Draw element type and name
        self.canvas.create_text(
            x + element.width / 2, y + element.height / 2 - 8,
            text=element.element_type,
            fill="white",
            font=("Arial", 9, "bold"),
            tags=("label", f"item_{id(element)}")
        )
        
        self.canvas.create_text(
            x + element.width / 2, y + element.height / 2 + 8,
            text=element.name,
            fill="#bdc3c7",
            font=("Arial", 8),
            tags=("label", f"item_{id(element)}")
        )
        
    def on_canvas_motion(self, event):
        """Handle mouse motion on canvas"""
        if not self.selected_item:
            return
            
        canvas_x = self.canvas.canvasx(event.x)
        canvas_y = self.canvas.canvasy(event.y)
        
        # Check if mouse is over resize handle
        if self.is_over_resize_handle(canvas_x, canvas_y, self.selected_item):
            self.canvas.config(cursor="sizing")
        else:
            self.canvas.config(cursor="")
    
    def on_canvas_click(self, event):
        """Handle canvas click"""
        canvas_x = self.canvas.canvasx(event.x)
        canvas_y = self.canvas.canvasy(event.y)
        
        if self.adding_mode:
            # Add new item
            self.add_item_at(canvas_x, canvas_y)
            self.clear_adding_mode()
        else:
            # Check if clicking on resize handle
            if (self.selected_item and 
                self.is_over_resize_handle(canvas_x, canvas_y, self.selected_item)):
                self.resizing_item = self.selected_item
                self.drag_start_x = canvas_x
                self.drag_start_y = canvas_y
                self.original_width = self.selected_item.width
                self.original_height = self.selected_item.height
            else:
                # Select item
                item = self.find_item_at(canvas_x, canvas_y)
                if item:
                    self.selected_item = item
                    self.dragging_item = item
                    self.drag_start_x = canvas_x
                    self.drag_start_y = canvas_y
                    self.on_item_selected(item)
                    self.redraw()
                
    def on_canvas_drag(self, event):
        """Handle canvas drag"""
        canvas_x = self.canvas.canvasx(event.x)
        canvas_y = self.canvas.canvasy(event.y)
        
        if self.dragging_item:
            # Handle moving the item
            dx = canvas_x - self.drag_start_x
            dy = canvas_y - self.drag_start_y
            
            self.dragging_item.x += int(dx)
            self.dragging_item.y += int(dy)
            
            self.drag_start_x = canvas_x
            self.drag_start_y = canvas_y
            
            self.redraw()
            
        elif self.resizing_item:
            # Handle resizing the item
            dx = canvas_x - self.drag_start_x
            dy = canvas_y - self.drag_start_y
            
            # Calculate new dimensions
            new_width = max(30, self.original_width + dx)
            new_height = max(30, self.original_height + dy)
            
            # Update the item's size
            self.resizing_item.width = int(new_width)
            self.resizing_item.height = int(new_height)
            
            # Update the property panel if it's open
            if hasattr(self, 'on_property_changed'):
                self.on_property_changed()
            
            self.redraw()
            
    def copy_item(self, item, parent_x=0, parent_y=0):
        """Create a deep copy of an item"""
        if item is None:
            return None
            
        if isinstance(item, Container):
            # Calculate the position relative to the parent container
            relative_x = item.x - parent_x
            relative_y = item.y - parent_y
            
            # Create a new container with the same properties
            new_container = Container(
                f"{item.name}_copy",
                relative_x + 20,  # Offset slightly from original
                relative_y + 20,
                item.width,
                item.height,
                item.orientation
            )
            new_container.padding = item.padding
            new_container.background = item.background
            
            # Store the new container's position for child positioning
            new_parent_x = parent_x + relative_x
            new_parent_y = parent_y + relative_y
            
            # Recursively copy all children with updated parent position
            for child in item.children:
                copied_child = self.copy_item(child, new_parent_x, new_parent_y)
                if copied_child:
                    new_container.add_child(copied_child)
            return new_container
            
        elif isinstance(item, UIElement):
            # Calculate the position relative to the parent container
            relative_x = item.x - parent_x
            relative_y = item.y - parent_y
            
            # Create a new element with the same properties
            new_element = UIElement(
                item.element_type,
                f"{item.name}_copy",
                relative_x + 20,  # Offset slightly from original
                relative_y + 20,
                item.width,
                item.height
            )
            # Copy all attributes
            new_element.text = item.text
            new_element.enabled = item.enabled
            new_element.visible = item.visible
            new_element.properties = item.properties.copy()
            return new_element
            
        return None
        
    def copy_selected(self):
        """Copy the currently selected item"""
        if self.selected_item:
            self.copied_item = self.copy_item(self.selected_item)
            return True
        return False
        
    def paste_item(self, x, y):
        """Paste the copied item at the specified position"""
        if not self.copied_item:
            return False
            
        # Create a new copy to allow multiple pastes
        new_item = self.copy_item(self.copied_item)
        if not new_item:
            return False
            
        # Position the new item at the specified location
        dx = x - new_item.x
        dy = y - new_item.y
        self._move_item(new_item, dx, dy)
        
        # Add to the same parent as the copied item, or to the root
        if self.selected_item and hasattr(self.selected_item, 'parent') and self.selected_item.parent:
            self.selected_item.parent.add_child(new_item)
        else:
            # Find the container at the paste position
            container = self.find_container_at(x, y)
            if container:
                container.add_child(new_item)
            else:
                self.ui_layout.root_container.add_child(new_item)
        
        # Select the new item
        self.selected_item = new_item
        self.on_item_selected(new_item)
        self.redraw()
        return True
        
    def _move_item(self, item, dx, dy):
        """Recursively move an item and its children"""
        item.x += dx
        item.y += dy
        if hasattr(item, 'children'):
            for child in item.children:
                self._move_item(child, dx, dy)

    def draw_resize_handle(self, x, y, element, parent_x=0, parent_y=0):
        """Draw a resize handle for the given element"""
        # Calculate absolute position
        abs_x = x + element.width - self.resize_handle_size
        abs_y = y + element.height - self.resize_handle_size
        
        # Draw the resize handle (a small square in the bottom-right corner)
        self.canvas.create_rectangle(
            abs_x, abs_y,
            abs_x + self.resize_handle_size,
            abs_y + self.resize_handle_size,
            fill=self.SELECTED_COLOR,
            outline="white",
            width=1,
            tags=("resize_handle", f"handle_{id(element)}")
        )
    
    def is_over_resize_handle(self, x, y, item):
        """Check if the mouse is over the resize handle of an item"""
        if not item:
            return False
            
        # Get the item's position and size
        item_x = item.x
        item_y = item.y
        item_width = item.width
        item_height = item.height
        
        # Define the resize handle area (bottom-right corner)
        handle_size = self.resize_handle_size
        handle_x1 = item_x + item_width - handle_size
        handle_y1 = item_y + item_height - handle_size
        handle_x2 = item_x + item_width
        handle_y2 = item_y + item_height
        
        # Check if the mouse is within the handle area
        return (handle_x1 <= x <= handle_x2 and 
                handle_y1 <= y <= handle_y2)
    
    def on_canvas_release(self, event):
        """Handle mouse release"""
        self.dragging_item = None
        self.resizing_item = None
        
    def add_item_at(self, x, y):
        """Add a new item at the specified position"""
        # Find which container this position is in
        target_container = self.find_container_at(x, y)
        
        if not target_container:
            target_container = self.ui_layout.root_container
            
        # Calculate relative position
        abs_x, abs_y = self.get_absolute_position(target_container)
        rel_x = int(x - abs_x)
        rel_y = int(y - abs_y)
        
        if self.adding_mode == "Container":
            # Add new container
            name = f"Container{len(self.ui_layout.get_all_containers()) + 1}"
            new_container = Container(name, rel_x, rel_y, 300, 200)
            target_container.add_child(new_container)
        else:
            # Add new element
            element_count = len(self.ui_layout.get_all_elements()) + 1
            name = f"{self.adding_mode}{element_count}"
            new_element = UIElement(self.adding_mode, name, rel_x, rel_y)
            new_element.text = name
            target_container.add_child(new_element)
            
        self.redraw()
        
    def find_item_at(self, x, y):
        """Find the item at the specified position"""
        # Check all containers and elements
        all_items = []
        
        def collect_items(container, parent_x=0, parent_y=0):
            abs_x = parent_x + container.x
            abs_y = parent_y + container.y
            
            for child in container.children:
                if isinstance(child, Container):
                    collect_items(child, abs_x, abs_y)
                    child_x = abs_x + child.x
                    child_y = abs_y + child.y
                    all_items.append((child, child_x, child_y, child.width, child.height))
                elif isinstance(child, UIElement):
                    child_x = abs_x + child.x
                    child_y = abs_y + child.y
                    all_items.append((child, child_x, child_y, child.width, child.height))
            
            # Add container itself
            all_items.append((container, abs_x, abs_y, container.width, container.height))
        
        collect_items(self.ui_layout.root_container)
        
        # Find the smallest item that contains the point (most specific)
        matching_items = []
        for item, item_x, item_y, item_w, item_h in all_items:
            if item_x <= x <= item_x + item_w and item_y <= y <= item_y + item_h:
                matching_items.append((item, item_w * item_h))
        
        if matching_items:
            # Return the item with smallest area (most specific)
            matching_items.sort(key=lambda i: i[1])
            return matching_items[0][0]
        
        return None
    
    def find_container_at(self, x, y):
        """Find the deepest container at the specified position"""
        containers = []
        
        def collect_containers(container, parent_x=0, parent_y=0):
            abs_x = parent_x + container.x
            abs_y = parent_y + container.y
            
            if abs_x <= x <= abs_x + container.width and abs_y <= y <= abs_y + container.height:
                containers.append((container, container.width * container.height))
            
            for child in container.children:
                if isinstance(child, Container):
                    collect_containers(child, abs_x, abs_y)
        
        collect_containers(self.ui_layout.root_container)
        
        if containers:
            # Return the smallest container (most specific)
            containers.sort(key=lambda c: c[1])
            return containers[0][0]
        
        return None
    
    def get_absolute_position(self, item):
        """Get the absolute position of an item"""
        x, y = item.x, item.y
        current = item.parent
        
        while current:
            x += current.x
            y += current.y
            current = current.parent
            
        return x, y

