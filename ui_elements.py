"""
UI Element and Container classes for the MD UI Builder
"""

class UIElement:
    """Base class for all UI elements"""
    
    ELEMENT_TYPES = [
        "Button", "Label", "TextBox", "TextArea", "Dropdown", 
        "ComboBox", "CheckBox", "RadioButton", "Slider", "Image", "Spacer"
    ]
    
    def __init__(self, element_type, name, x=0, y=0, width=100, height=30):
        self.element_type = element_type
        self.name = name
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = ""
        self.enabled = True
        self.visible = True
        self.properties = {}
        self.parent = None
        
    def set_property(self, key, value):
        """Set a custom property"""
        self.properties[key] = value
        
    def get_property(self, key, default=None):
        """Get a custom property"""
        return self.properties.get(key, default)
    
    def to_markdown(self, level=3):
        """Convert element to markdown representation"""
        indent = "#" * level
        lines = []
        lines.append(f"{indent} Element: {self.name}")
        lines.append(f"- Type: {self.element_type}")
        if self.text:
            lines.append(f"- Text: \"{self.text}\"")
        lines.append(f"- Width: {self.width}")
        lines.append(f"- Height: {self.height}")
        lines.append(f"- Position: ({self.x}, {self.y})")
        lines.append(f"- Enabled: {str(self.enabled).lower()}")
        lines.append(f"- Visible: {str(self.visible).lower()}")
        
        if self.properties:
            lines.append("- Properties:")
            for key, value in self.properties.items():
                lines.append(f"  - {key}: {value}")
        
        return "\n".join(lines)
    
    def to_dict(self):
        """Convert element to dictionary for JSON serialization"""
        return {
            "type": "element",
            "element_type": self.element_type,
            "name": self.name,
            "x": self.x,
            "y": self.y,
            "width": self.width,
            "height": self.height,
            "text": self.text,
            "enabled": self.enabled,
            "visible": self.visible,
            "properties": self.properties.copy()
        }

    @staticmethod
    def from_dict(data):
        """Create element from dictionary"""
        element = UIElement(
            data["element_type"],
            data["name"],
            data["x"],
            data["y"],
            data["width"],
            data["height"]
        )
        element.text = data.get("text", "")
        element.enabled = data.get("enabled", True)
        element.visible = data.get("visible", True)
        element.properties = data.get("properties", {}).copy()
        return element

    def __repr__(self):
        return f"{self.element_type}({self.name})"


class Container:
    """Container class for holding UI elements and other containers"""
    
    ORIENTATIONS = ["horizontal", "vertical"]
    
    def __init__(self, name, x=0, y=0, width=400, height=300, orientation="vertical"):
        self.name = name
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.orientation = orientation if orientation in self.ORIENTATIONS else "vertical"
        self.padding = 10
        self.background = "#ffffff"
        self.children = []  # Can contain both UIElements and Containers
        self.parent = None
        
    def add_child(self, child):
        """Add a child element or container"""
        if child not in self.children:
            self.children.append(child)
            child.parent = self
            
    def remove_child(self, child):
        """Remove a child element or container"""
        if child in self.children:
            self.children.remove(child)
            child.parent = None
            
    def get_all_children(self):
        """Get all children recursively"""
        all_children = []
        for child in self.children:
            all_children.append(child)
            if isinstance(child, Container):
                all_children.extend(child.get_all_children())
        return all_children
    
    def to_markdown(self, level=2):
        """Convert container and all children to markdown representation"""
        indent = "#" * level
        lines = []
        lines.append(f"{indent} Container: {self.name}")
        lines.append(f"- Type: Container")
        lines.append(f"- Orientation: {self.orientation}")
        lines.append(f"- Width: {self.width}")
        lines.append(f"- Height: {self.height}")
        lines.append(f"- Position: ({self.x}, {self.y})")
        lines.append(f"- Padding: {self.padding}")
        lines.append(f"- Background: {self.background}")
        
        # Add children
        if self.children:
            lines.append("")
            for child in self.children:
                lines.append(child.to_markdown(level + 1))
                lines.append("")
        
        return "\n".join(lines)

    def to_dict(self):
        """Convert container to dictionary for JSON serialization"""
        return {
            "type": "container",
            "name": self.name,
            "x": self.x,
            "y": self.y,
            "width": self.width,
            "height": self.height,
            "orientation": self.orientation,
            "padding": self.padding,
            "background": self.background,
            "children": [child.to_dict() for child in self.children]
        }

    @staticmethod
    def from_dict(data):
        """Create container from dictionary"""
        container = Container(
            data["name"],
            data["x"],
            data["y"],
            data["width"],
            data["height"],
            data["orientation"]
        )
        container.padding = data.get("padding", 10)
        container.background = data.get("background", "#ffffff")

        # Recursively create children
        for child_data in data.get("children", []):
            if child_data["type"] == "container":
                child = Container.from_dict(child_data)
            else:  # element
                child = UIElement.from_dict(child_data)
            container.add_child(child)

        return container

    def __repr__(self):
        return f"Container({self.name}, {len(self.children)} children)"


class UILayout:
    """Main layout class that holds the root container"""
    
    def __init__(self, name="UI Layout"):
        self.name = name
        self.root_container = Container("MainWindow", 0, 0, 800, 600)
        
    def to_markdown(self):
        """Convert entire layout to markdown"""
        lines = []
        lines.append(f"# UI Layout: {self.name}")
        lines.append("")
        lines.append(self.root_container.to_markdown(level=2))
        return "\n".join(lines)
    
    def save_to_file(self, filename):
        """Save layout to markdown file"""
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(self.to_markdown())
    
    def get_all_containers(self):
        """Get all containers in the layout"""
        containers = [self.root_container]
        
        def collect_containers(container):
            for child in container.children:
                if isinstance(child, Container):
                    containers.append(child)
                    collect_containers(child)
        
        collect_containers(self.root_container)
        return containers
    
    def get_all_elements(self):
        """Get all UI elements in the layout"""
        elements = []
        
        def collect_elements(container):
            for child in container.children:
                if isinstance(child, UIElement):
                    elements.append(child)
                elif isinstance(child, Container):
                    collect_elements(child)
        
        collect_elements(self.root_container)
        return elements
    
    def find_by_name(self, name):
        """Find a container or element by name"""
        # Check root container
        if self.root_container.name == name:
            return self.root_container
        
        # Search recursively
        def search(container):
            for child in container.children:
                if child.name == name:
                    return child
                if isinstance(child, Container):
                    result = search(child)
                    if result:
                        return result
            return None
        
        return search(self.root_container)

    def to_dict(self):
        """Convert layout to dictionary for JSON serialization"""
        return {
            "name": self.name,
            "root_container": self.root_container.to_dict()
        }

    @staticmethod
    def from_dict(data):
        """Create layout from dictionary"""
        layout = UILayout(data["name"])
        layout.root_container = Container.from_dict(data["root_container"])
        return layout

    def save_to_json(self, filename):
        """Save layout to JSON file"""
        import json
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.to_dict(), f, indent=2)

    @staticmethod
    def load_from_json(filename):
        """Load layout from JSON file"""
        import json
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return UILayout.from_dict(data)

    def __repr__(self):
        return f"UILayout({self.name})"

