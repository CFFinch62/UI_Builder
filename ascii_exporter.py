"""
ASCII Art Exporter - Creates visual text representations of UI layouts
"""

from ui_elements import UIElement, Container, UILayout


class ASCIIExporter:
    """Export UI layouts as ASCII art / text-based visual representations"""

    def __init__(self, ui_layout, scale_factor=1.0):
        self.ui_layout = ui_layout
        self.scale_factor = scale_factor
        self.grid = []
        self.width = 0
        self.height = 0

    def export(self):
        """Export the layout as ASCII art"""
        # Calculate dimensions based on root container with scaling
        root = self.ui_layout.root_container
        scaled_width = int(root.width * self.scale_factor)
        scaled_height = int(root.height * self.scale_factor)

        self.width = max(scaled_width, 60)
        self.height = max(scaled_height, 40)

        # Initialize grid with spaces
        self.grid = [[' ' for _ in range(self.width)] for _ in range(self.height)]

        # Draw the layout
        self._draw_container(root, 0, 0)

        # Convert grid to string
        return self._grid_to_string()
    
    def _draw_container(self, container, offset_x, offset_y):
        """Draw a container and its children"""
        # Apply scaling to positions and dimensions
        x = int((offset_x + container.x) * self.scale_factor)
        y = int((offset_y + container.y) * self.scale_factor)
        w = int(container.width * self.scale_factor)
        h = int(container.height * self.scale_factor)

        # Ensure dimensions are within bounds
        if x >= self.width or y >= self.height:
            return

        # Adjust dimensions if they exceed grid
        w = min(w, self.width - x)
        h = min(h, self.height - y)

        if w < 2 or h < 2:
            return

        # Draw container border
        self._draw_box(x, y, w, h, container.name)

        # Draw children (pass original offset for recursive scaling)
        for child in container.children:
            if isinstance(child, Container):
                self._draw_container(child, offset_x + container.x, offset_y + container.y)
            elif isinstance(child, UIElement):
                self._draw_element(child, offset_x + container.x, offset_y + container.y)
    
    def _draw_element(self, element, offset_x, offset_y):
        """Draw a UI element"""
        # Apply scaling to positions and dimensions
        x = int((offset_x + element.x) * self.scale_factor)
        y = int((offset_y + element.y) * self.scale_factor)
        w = int(element.width * self.scale_factor)
        h = int(element.height * self.scale_factor)

        # Ensure dimensions are within bounds
        if x >= self.width or y >= self.height:
            return

        # Adjust dimensions if they exceed grid
        w = min(w, self.width - x)
        h = min(h, self.height - y)

        if w < 2 or h < 2:
            return

        # Create label for element
        label = element.name
        if element.text:
            label = f"{element.text}"

        # Draw element box with label
        self._draw_box(x, y, w, h, label, element.element_type)
    
    def _draw_box(self, x, y, w, h, label="", element_type=None):
        """Draw a box with optional label"""
        # Ensure we're within bounds
        if x >= self.width or y >= self.height or w < 2 or h < 2:
            return
        
        # Adjust if box extends beyond grid
        max_x = min(x + w, self.width)
        max_y = min(y + h, self.height)
        
        # Draw top border
        if y < self.height:
            self._set_char(x, y, '+')
            for i in range(x + 1, max_x - 1):
                self._set_char(i, y, '-')
            if max_x - 1 > x:
                self._set_char(max_x - 1, y, '+')
        
        # Draw bottom border
        if max_y - 1 < self.height and max_y - 1 > y:
            self._set_char(x, max_y - 1, '+')
            for i in range(x + 1, max_x - 1):
                self._set_char(i, max_y - 1, '-')
            if max_x - 1 > x:
                self._set_char(max_x - 1, max_y - 1, '+')
        
        # Draw side borders
        for j in range(y + 1, max_y - 1):
            if j < self.height:
                self._set_char(x, j, '|')
                if max_x - 1 > x:
                    self._set_char(max_x - 1, j, '|')
        
        # Add label in the middle or top
        if label:
            # Truncate label if too long
            max_label_len = w - 4
            if len(label) > max_label_len:
                label = label[:max_label_len - 2] + ".."
            
            # Position label
            label_y = y + 1 if h > 2 else y
            label_x = x + 2
            
            # Add element type prefix if it's an element
            if element_type:
                type_prefix = self._get_type_prefix(element_type)
                label = f"{type_prefix} {label}"
            
            # Write label
            if label_y < self.height:
                for i, char in enumerate(label):
                    if label_x + i < max_x - 1:
                        self._set_char(label_x + i, label_y, char)
    
    def _get_type_prefix(self, element_type):
        """Get a short prefix for element type"""
        prefixes = {
            'Button': '[BTN]',
            'Label': 'LBL:',
            'TextBox': '[___]',
            'TextArea': '[TXT]',
            'Dropdown': '[v]',
            'ComboBox': '[^v]',
            'CheckBox': '[ ]',
            'RadioButton': '( )',
            'Slider': '[---]',
            'Image': '[IMG]',
            'Spacer': '~~~'
        }
        return prefixes.get(element_type, '')
    
    def _set_char(self, x, y, char):
        """Set a character in the grid"""
        if 0 <= y < self.height and 0 <= x < self.width:
            self.grid[y][x] = char
    
    def _grid_to_string(self):
        """Convert grid to string"""
        lines = []
        for row in self.grid:
            lines.append(''.join(row))
        return '\n'.join(lines)


def calculate_optimal_scale(ui_layout, max_width=120, max_height=60):
    """Calculate optimal scale factor to fit within max dimensions"""
    root = ui_layout.root_container

    # Calculate scale factors for width and height
    width_scale = max_width / root.width if root.width > max_width else 1.0
    height_scale = max_height / root.height if root.height > max_height else 1.0

    # Use the smaller scale to ensure both dimensions fit
    optimal_scale = min(width_scale, height_scale)

    # Don't scale up, only down
    return min(optimal_scale, 1.0)


def export_to_ascii(ui_layout, filename, scale_factor=None, max_width=120, max_height=60):
    """
    Export a UI layout to ASCII art file

    Args:
        ui_layout: The UILayout to export
        filename: Output filename
        scale_factor: Manual scale factor (0.0-1.0). If None, auto-calculates optimal scale
        max_width: Maximum width in characters (default 120, fits most IDE windows)
        max_height: Maximum height in lines (default 60, minimal scrolling)

    Returns:
        The ASCII art string
    """
    # Auto-calculate scale if not provided
    if scale_factor is None:
        scale_factor = calculate_optimal_scale(ui_layout, max_width, max_height)

    exporter = ASCIIExporter(ui_layout, scale_factor)
    ascii_art = exporter.export()

    # Add header with scale info
    header = f"# UI Layout: {ui_layout.name}\n"
    header += f"# Scale: {scale_factor:.2f}x ({int(ui_layout.root_container.width * scale_factor)}x{int(ui_layout.root_container.height * scale_factor)} chars)\n"
    header += f"# Original size: {ui_layout.root_container.width}x{ui_layout.root_container.height}px\n\n"

    full_output = header + ascii_art

    with open(filename, 'w') as f:
        f.write(full_output)

    return full_output

