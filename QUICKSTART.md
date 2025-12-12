# Quick Start Guide

## Installation

1. Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

```bash
python main.py
```

## Building Your First UI

### Step 1: Understanding the Interface

The application has three main panels:

- **Left Panel (Element Palette)**: Contains all available UI elements you can add
- **Center Panel (Canvas)**: Visual workspace where you build your UI
- **Right Panel (Properties)**: Edit properties of selected items

### Step 2: Add Containers

1. Click the **"Add Container"** button in the canvas toolbar
2. Click anywhere on the canvas to place the container
3. The container appears as a blue rectangle (vertical) or green rectangle (horizontal)

**Container Tips:**
- Blue containers = Vertical orientation (elements stack top-to-bottom)
- Green containers = Horizontal orientation (elements flow left-to-right)
- Containers can be nested inside other containers
- Click and drag containers to reposition them

### Step 3: Add UI Elements

1. Click any element from the **Element Palette** (e.g., "Button", "Label", "TextBox")
2. Click inside a container on the canvas to place the element
3. Elements appear as red rectangles with their type and name

**Available Elements:**
- **Input**: TextBox, TextArea, Dropdown, ComboBox
- **Selection**: CheckBox, RadioButton, Slider
- **Display**: Label, Image
- **Action**: Button
- **Layout**: Spacer

### Step 4: Edit Properties

1. Click any container or element on the canvas to select it
2. The **Properties Panel** on the right shows all editable properties
3. Modify properties like:
   - Name
   - Position (X, Y)
   - Size (Width, Height)
   - Text content
   - Custom properties

**For Containers:**
- Change orientation (horizontal/vertical)
- Adjust padding
- Set background color

**For Elements:**
- Set display text
- Toggle enabled/visible states
- Add custom properties for framework-specific features

### Step 5: Build Your Layout

**Example: Simple Login Form**

1. Start with the default MainWindow container
2. Add a vertical container for the form (click "Add Container", then click in MainWindow)
3. Select the new container and set:
   - Width: 400
   - Height: 300
   - Orientation: vertical
4. Add elements inside the form container:
   - Click "Label" in palette, click in container → "Username Label"
   - Click "TextBox" in palette, click in container → "Username Input"
   - Click "Label" in palette, click in container → "Password Label"
   - Click "TextBox" in palette, click in container → "Password Input"
   - Click "Button" in palette, click in container → "Login Button"
5. Adjust positions and sizes using the Properties panel

### Step 6: Export to Markdown

1. Click **"Export to Markdown"** button at the bottom
2. Choose a filename and location
3. The markdown file is generated with your complete UI structure

### Step 7: Use with AI Agents

Share the generated markdown file with AI agents using prompts like:

**For PyQt:**
```
Please implement this UI design in PyQt6. Here's the UI specification:
[paste markdown content]
```

**For CustomTkinter:**
```
Create this interface using CustomTkinter. Here's the layout:
[paste markdown content]
```

**For HTML/CSS:**
```
Build this UI in HTML/CSS with flexbox. Here's the structure:
[paste markdown content]
```

## Tips and Tricks

### Organizing Your Layout

1. **Use nested containers** for complex layouts
2. **Horizontal containers** for rows of elements (like button groups)
3. **Vertical containers** for columns of elements (like forms)
4. **Mix orientations** to create grid-like layouts

### Naming Convention

- Use descriptive names: "LoginButton" instead of "Button1"
- Group related elements: "HeaderSection", "FormSection", "FooterSection"
- This makes the markdown more readable for AI agents

### Custom Properties

Add framework-specific properties using the custom properties feature:

- **PyQt**: `stylesheet`, `icon`, `tooltip`
- **CustomTkinter**: `corner_radius`, `fg_color`, `hover_color`
- **HTML**: `class`, `id`, `data-*` attributes

### Positioning

- Elements are positioned relative to their parent container
- Use the grid (visible on canvas) to align elements
- Drag elements to reposition them visually
- Fine-tune positions in the Properties panel

### Saving Your Work

- Use **"Save Project"** to save your work (coming soon)
- Use **"Export to Markdown"** to generate the output file
- Keep both the project file and markdown file for future edits

## Keyboard Shortcuts

- **Click + Drag**: Move selected item
- **Delete Selected**: Remove the selected item (cannot delete root container)

## Common Workflows

### Creating a Form Layout

1. Add vertical container for the form
2. For each field:
   - Add horizontal container (for label + input pair)
   - Add Label element
   - Add TextBox/Dropdown/etc element
3. Add horizontal container for buttons
4. Add Button elements

### Creating a Dashboard Layout

1. Add horizontal container for header
2. Add horizontal container for main content area
3. Inside main content, add multiple vertical containers for columns
4. Add elements to each column
5. Add horizontal container for footer

### Creating a Dialog Box

1. Add vertical container for dialog
2. Add Label for title/message
3. Add horizontal container for buttons
4. Add Button elements (OK, Cancel, etc.)

## Troubleshooting

**Can't see my element:**
- Make sure you clicked inside a container
- Check if the element is too small (adjust width/height)
- Verify the element isn't positioned outside the container bounds

**Container not showing:**
- Containers need to be placed inside other containers (or the root)
- Check the container size (width/height)

**Can't delete an item:**
- You cannot delete the root MainWindow container
- Make sure an item is selected (click it first)

**Properties not updating:**
- Make sure you've selected the item you want to edit
- Some properties require valid values (e.g., numbers for width/height)

## Next Steps

1. Experiment with different layouts
2. Try exporting and implementing with different frameworks
3. Build a library of common UI patterns
4. Share your markdown files with AI agents to see how they interpret them

Happy building! 🎨

