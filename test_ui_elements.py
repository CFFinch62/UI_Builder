"""
Unit tests for UI elements
"""

import unittest
from ui_elements import UIElement, Container, UILayout


class TestUIElement(unittest.TestCase):
    """Test UIElement class"""
    
    def test_create_element(self):
        """Test creating a UI element"""
        element = UIElement("Button", "MyButton", 10, 20, 100, 30)
        self.assertEqual(element.element_type, "Button")
        self.assertEqual(element.name, "MyButton")
        self.assertEqual(element.x, 10)
        self.assertEqual(element.y, 20)
        self.assertEqual(element.width, 100)
        self.assertEqual(element.height, 30)
        
    def test_element_properties(self):
        """Test element properties"""
        element = UIElement("TextBox", "Input1")
        element.set_property("placeholder", "Enter text")
        element.set_property("max-length", 50)
        
        self.assertEqual(element.get_property("placeholder"), "Enter text")
        self.assertEqual(element.get_property("max-length"), 50)
        self.assertIsNone(element.get_property("nonexistent"))
        
    def test_element_to_markdown(self):
        """Test element markdown conversion"""
        element = UIElement("Button", "SubmitBtn", 50, 100, 120, 40)
        element.text = "Submit"
        element.set_property("style", "primary")
        
        markdown = element.to_markdown()
        
        self.assertIn("Element: SubmitBtn", markdown)
        self.assertIn("Type: Button", markdown)
        self.assertIn('Text: "Submit"', markdown)
        self.assertIn("Width: 120", markdown)
        self.assertIn("Height: 40", markdown)
        self.assertIn("Position: (50, 100)", markdown)
        self.assertIn("style: primary", markdown)


class TestContainer(unittest.TestCase):
    """Test Container class"""
    
    def test_create_container(self):
        """Test creating a container"""
        container = Container("MyContainer", 0, 0, 400, 300, "vertical")
        self.assertEqual(container.name, "MyContainer")
        self.assertEqual(container.orientation, "vertical")
        self.assertEqual(container.width, 400)
        self.assertEqual(container.height, 300)
        
    def test_add_remove_children(self):
        """Test adding and removing children"""
        container = Container("Parent", 0, 0, 400, 300)
        element = UIElement("Button", "Btn1")
        
        container.add_child(element)
        self.assertEqual(len(container.children), 1)
        self.assertEqual(element.parent, container)
        
        container.remove_child(element)
        self.assertEqual(len(container.children), 0)
        self.assertIsNone(element.parent)
        
    def test_nested_containers(self):
        """Test nested containers"""
        parent = Container("Parent", 0, 0, 400, 300)
        child = Container("Child", 10, 10, 200, 150)
        
        parent.add_child(child)
        self.assertEqual(child.parent, parent)
        
        all_children = parent.get_all_children()
        self.assertEqual(len(all_children), 1)
        self.assertIn(child, all_children)
        
    def test_container_to_markdown(self):
        """Test container markdown conversion"""
        container = Container("FormSection", 20, 20, 400, 300, "vertical")
        container.padding = 15
        container.background = "#ffffff"
        
        element = UIElement("Label", "Title")
        element.text = "Form Title"
        container.add_child(element)
        
        markdown = container.to_markdown()
        
        self.assertIn("Container: FormSection", markdown)
        self.assertIn("Orientation: vertical", markdown)
        self.assertIn("Width: 400", markdown)
        self.assertIn("Padding: 15", markdown)
        self.assertIn("Background: #ffffff", markdown)
        self.assertIn("Element: Title", markdown)


class TestUILayout(unittest.TestCase):
    """Test UILayout class"""
    
    def test_create_layout(self):
        """Test creating a layout"""
        layout = UILayout("My App")
        self.assertEqual(layout.name, "My App")
        self.assertIsNotNone(layout.root_container)
        self.assertEqual(layout.root_container.name, "MainWindow")
        
    def test_get_all_containers(self):
        """Test getting all containers"""
        layout = UILayout("Test")
        
        container1 = Container("Section1", 0, 0, 200, 200)
        container2 = Container("Section2", 0, 200, 200, 200)
        
        layout.root_container.add_child(container1)
        layout.root_container.add_child(container2)
        
        all_containers = layout.get_all_containers()
        self.assertEqual(len(all_containers), 3)  # root + 2 children
        self.assertIn(layout.root_container, all_containers)
        self.assertIn(container1, all_containers)
        self.assertIn(container2, all_containers)
        
    def test_get_all_elements(self):
        """Test getting all elements"""
        layout = UILayout("Test")
        
        element1 = UIElement("Button", "Btn1")
        element2 = UIElement("Label", "Lbl1")
        
        layout.root_container.add_child(element1)
        layout.root_container.add_child(element2)
        
        all_elements = layout.get_all_elements()
        self.assertEqual(len(all_elements), 2)
        self.assertIn(element1, all_elements)
        self.assertIn(element2, all_elements)
        
    def test_find_by_name(self):
        """Test finding items by name"""
        layout = UILayout("Test")
        
        container = Container("MySection", 0, 0, 200, 200)
        element = UIElement("Button", "MyButton")
        
        layout.root_container.add_child(container)
        container.add_child(element)
        
        found_container = layout.find_by_name("MySection")
        self.assertEqual(found_container, container)
        
        found_element = layout.find_by_name("MyButton")
        self.assertEqual(found_element, element)
        
        not_found = layout.find_by_name("NonExistent")
        self.assertIsNone(not_found)
        
    def test_layout_to_markdown(self):
        """Test layout markdown conversion"""
        layout = UILayout("Login Form")
        
        form_section = Container("FormSection", 20, 20, 400, 300)
        layout.root_container.add_child(form_section)
        
        username_label = UIElement("Label", "UsernameLabel")
        username_label.text = "Username:"
        form_section.add_child(username_label)
        
        markdown = layout.to_markdown()
        
        self.assertIn("# UI Layout: Login Form", markdown)
        self.assertIn("Container: MainWindow", markdown)
        self.assertIn("Container: FormSection", markdown)
        self.assertIn("Element: UsernameLabel", markdown)
        
    def test_save_to_file(self):
        """Test saving layout to file"""
        import tempfile
        import os
        
        layout = UILayout("Test Layout")
        element = UIElement("Button", "TestButton")
        element.text = "Click Me"
        layout.root_container.add_child(element)
        
        # Create temporary file
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.md') as f:
            temp_file = f.name
        
        try:
            layout.save_to_file(temp_file)
            
            # Read and verify
            with open(temp_file, 'r') as f:
                content = f.read()
            
            self.assertIn("# UI Layout: Test Layout", content)
            self.assertIn("Element: TestButton", content)
            self.assertIn('Text: "Click Me"', content)
        finally:
            # Clean up
            if os.path.exists(temp_file):
                os.remove(temp_file)


class TestComplexLayout(unittest.TestCase):
    """Test complex nested layouts"""
    
    def test_complex_nested_structure(self):
        """Test a complex nested structure"""
        layout = UILayout("Dashboard")
        
        # Header
        header = Container("Header", 0, 0, 800, 80, "horizontal")
        layout.root_container.add_child(header)
        
        title = UIElement("Label", "AppTitle")
        title.text = "My Dashboard"
        header.add_child(title)
        
        # Main content with two columns
        main = Container("MainContent", 0, 80, 800, 520, "horizontal")
        layout.root_container.add_child(main)
        
        left_column = Container("LeftColumn", 0, 0, 400, 520, "vertical")
        right_column = Container("RightColumn", 400, 0, 400, 520, "vertical")
        
        main.add_child(left_column)
        main.add_child(right_column)
        
        # Add elements to columns
        left_button = UIElement("Button", "LeftBtn")
        left_button.text = "Left Action"
        left_column.add_child(left_button)
        
        right_label = UIElement("Label", "RightLabel")
        right_label.text = "Right Panel"
        right_column.add_child(right_label)
        
        # Verify structure
        all_containers = layout.get_all_containers()
        self.assertEqual(len(all_containers), 5)  # root + header + main + 2 columns
        
        all_elements = layout.get_all_elements()
        self.assertEqual(len(all_elements), 3)  # title + left_button + right_label
        
        # Verify markdown generation
        markdown = layout.to_markdown()
        self.assertIn("Container: Header", markdown)
        self.assertIn("Container: MainContent", markdown)
        self.assertIn("Container: LeftColumn", markdown)
        self.assertIn("Container: RightColumn", markdown)


if __name__ == '__main__':
    unittest.main()

