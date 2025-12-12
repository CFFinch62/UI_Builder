"""
Test save and load functionality
"""

from ui_elements import UIElement, Container, UILayout
import tempfile
import os


def test_save_load():
    """Test saving and loading a project"""
    
    # Create a layout
    layout = UILayout("Test Project")
    layout.root_container.width = 600
    layout.root_container.height = 400
    
    # Add a container
    header = Container("Header", 10, 10, 580, 60, "horizontal")
    layout.root_container.add_child(header)
    
    # Add elements
    title = UIElement("Label", "Title", 20, 20, 200, 30)
    title.text = "My Application"
    header.add_child(title)
    
    button = UIElement("Button", "ActionBtn", 400, 20, 100, 30)
    button.text = "Click Me"
    button.set_property("style", "primary")
    header.add_child(button)
    
    # Add another container
    content = Container("Content", 10, 80, 580, 300, "vertical")
    layout.root_container.add_child(content)
    
    text_input = UIElement("TextBox", "Input1", 20, 20, 300, 30)
    text_input.text = ""
    text_input.set_property("placeholder", "Enter text here")
    content.add_child(text_input)
    
    # Save to temporary file
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json') as f:
        temp_file = f.name
    
    try:
        print("Saving project...")
        layout.save_to_json(temp_file)
        print(f"✓ Saved to {temp_file}")
        
        # Load it back
        print("\nLoading project...")
        loaded_layout = UILayout.load_from_json(temp_file)
        print(f"✓ Loaded from {temp_file}")
        
        # Verify the data
        print("\nVerifying data...")
        assert loaded_layout.name == "Test Project"
        print(f"✓ Layout name: {loaded_layout.name}")
        
        assert loaded_layout.root_container.width == 600
        assert loaded_layout.root_container.height == 400
        print(f"✓ Root container size: {loaded_layout.root_container.width}x{loaded_layout.root_container.height}")
        
        assert len(loaded_layout.root_container.children) == 2
        print(f"✓ Root has {len(loaded_layout.root_container.children)} children")
        
        # Check header
        loaded_header = loaded_layout.root_container.children[0]
        assert loaded_header.name == "Header"
        assert loaded_header.orientation == "horizontal"
        print(f"✓ Header container: {loaded_header.name} ({loaded_header.orientation})")
        
        assert len(loaded_header.children) == 2
        print(f"✓ Header has {len(loaded_header.children)} children")
        
        # Check title element
        loaded_title = loaded_header.children[0]
        assert loaded_title.name == "Title"
        assert loaded_title.text == "My Application"
        assert loaded_title.element_type == "Label"
        print(f"✓ Title element: {loaded_title.name} - '{loaded_title.text}'")
        
        # Check button element
        loaded_button = loaded_header.children[1]
        assert loaded_button.name == "ActionBtn"
        assert loaded_button.text == "Click Me"
        assert loaded_button.get_property("style") == "primary"
        print(f"✓ Button element: {loaded_button.name} - '{loaded_button.text}' (style: {loaded_button.get_property('style')})")
        
        # Check content container
        loaded_content = loaded_layout.root_container.children[1]
        assert loaded_content.name == "Content"
        assert loaded_content.orientation == "vertical"
        print(f"✓ Content container: {loaded_content.name} ({loaded_content.orientation})")
        
        # Check text input
        loaded_input = loaded_content.children[0]
        assert loaded_input.name == "Input1"
        assert loaded_input.element_type == "TextBox"
        assert loaded_input.get_property("placeholder") == "Enter text here"
        print(f"✓ TextBox element: {loaded_input.name} (placeholder: {loaded_input.get_property('placeholder')})")
        
        print("\n" + "="*60)
        print("✅ All tests passed! Save/Load functionality works correctly.")
        print("="*60)
        
        # Show file contents
        print("\nSaved JSON content:")
        with open(temp_file, 'r') as f:
            print(f.read())
        
    finally:
        # Clean up
        if os.path.exists(temp_file):
            os.remove(temp_file)
            print(f"\n✓ Cleaned up temporary file")


if __name__ == "__main__":
    test_save_load()

