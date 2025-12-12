"""
Test properties panel clearing
"""

import customtkinter as ctk
from properties_panel import PropertiesPanel
from ui_elements import Container, UIElement


def test_properties_clearing():
    """Test that properties panel clears properly"""
    
    # Create a simple window
    root = ctk.CTk()
    root.geometry("400x600")
    root.title("Properties Panel Clear Test")
    
    # Track property changes
    change_count = [0]
    
    def on_property_changed():
        change_count[0] += 1
        print(f"Property changed (count: {change_count[0]})")
    
    # Create properties panel
    props_panel = PropertiesPanel(root, on_property_changed)
    props_panel.pack(fill="both", expand=True, padx=10, pady=10)
    
    # Create test items
    container1 = Container("Container1", 10, 10, 200, 150, "vertical")
    container1.padding = 15
    
    container2 = Container("Container2", 50, 50, 300, 200, "horizontal")
    container2.padding = 20
    
    element1 = UIElement("Button", "Button1", 10, 10, 100, 30)
    element1.text = "Click Me"
    element1.set_property("style", "primary")
    
    element2 = UIElement("Label", "Label1", 20, 20, 150, 25)
    element2.text = "Hello World"
    element2.set_property("color", "blue")
    element2.set_property("font-size", "14")
    
    # Test sequence
    test_items = [container1, container2, element1, element2, container1, element2]
    current_index = [0]
    
    def load_next_item():
        """Load the next test item"""
        if current_index[0] < len(test_items):
            item = test_items[current_index[0]]
            print(f"\n{'='*60}")
            print(f"Loading item {current_index[0] + 1}/{len(test_items)}: {item}")
            print(f"{'='*60}")
            
            # Count widgets before
            widget_count_before = len(props_panel.property_widgets)
            print(f"Widgets tracked before clear: {widget_count_before}")
            
            # Load the item (this calls clear() first)
            props_panel.load_item(item)
            
            # Count widgets after
            widget_count_after = len(props_panel.property_widgets)
            print(f"Widgets tracked after load: {widget_count_after}")
            
            # Check for widget accumulation
            if widget_count_before > 0 and widget_count_after > widget_count_before * 1.5:
                print(f"⚠️  WARNING: Possible widget accumulation!")
                print(f"   Expected ~{widget_count_after} widgets, but had {widget_count_before} before")
            else:
                print(f"✅ Widget count looks normal")
            
            current_index[0] += 1
        else:
            print(f"\n{'='*60}")
            print("✅ Test completed!")
            print(f"{'='*60}")
            print(f"Total property changes: {change_count[0]}")
    
    # Create control buttons
    button_frame = ctk.CTkFrame(root)
    button_frame.pack(fill="x", padx=10, pady=10)
    
    next_btn = ctk.CTkButton(
        button_frame,
        text="Load Next Item",
        command=load_next_item
    )
    next_btn.pack(side="left", padx=5)
    
    clear_btn = ctk.CTkButton(
        button_frame,
        text="Clear Panel",
        command=props_panel.clear
    )
    clear_btn.pack(side="left", padx=5)
    
    quit_btn = ctk.CTkButton(
        button_frame,
        text="Quit",
        command=root.quit
    )
    quit_btn.pack(side="left", padx=5)
    
    # Instructions
    instructions = ctk.CTkLabel(
        root,
        text="Click 'Load Next Item' repeatedly to test clearing.\nWatch the console for widget counts.",
        font=("Arial", 12)
    )
    instructions.pack(pady=10)
    
    print("\n" + "="*60)
    print("PROPERTIES PANEL CLEAR TEST")
    print("="*60)
    print("Instructions:")
    print("1. Click 'Load Next Item' to load different items")
    print("2. Watch the console for widget counts")
    print("3. Check if widgets accumulate or clear properly")
    print("="*60 + "\n")
    
    root.mainloop()


if __name__ == "__main__":
    test_properties_clearing()

