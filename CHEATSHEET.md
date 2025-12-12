# MD UI Builder - Quick Reference Cheat Sheet

## Running the App

```bash
./run.sh
# or
source venv/bin/activate && python main.py
```

## Basic Workflow

1. **Add Container** → Click "Add Container" → Click on canvas
2. **Add Element** → Click element in palette → Click in container
3. **Select Item** → Click on canvas item
4. **Edit Properties** → Use right panel
5. **Move Item** → Click and drag
6. **Delete Item** → Select → Click "Delete Selected"
7. **Export** → Click "Export to Markdown"

## Container Colors

- 🟦 **Blue** = Vertical container (elements stack top-to-bottom)
- 🟩 **Green** = Horizontal container (elements flow left-to-right)
- 🟧 **Orange** = Selected item

## Available Elements

### Input Elements
- **TextBox** - Single-line text input
- **TextArea** - Multi-line text input
- **Dropdown** - Select from list (closed)
- **ComboBox** - Select or type

### Selection Elements
- **CheckBox** - Toggle option
- **RadioButton** - Choose one from group
- **Slider** - Select value from range

### Display Elements
- **Label** - Static text
- **Image** - Picture/icon

### Action Elements
- **Button** - Clickable action

### Layout Elements
- **Spacer** - Flexible spacing

## Common Properties

### All Items
- **Name** - Identifier
- **X Position** - Horizontal position
- **Y Position** - Vertical position
- **Width** - Width in pixels
- **Height** - Height in pixels

### Containers Only
- **Orientation** - horizontal | vertical
- **Padding** - Internal spacing
- **Background** - Color code

### Elements Only
- **Text** - Display text
- **Enabled** - true | false
- **Visible** - true | false
- **Custom Properties** - Framework-specific

## Markdown Structure

```markdown
# UI Layout: [Name]

## Container: MainWindow
- Type: Container
- Orientation: vertical
- Width: 800
- Height: 600

### Container: Section1
- Orientation: horizontal

#### Element: Button1
- Type: Button
- Text: "Click Me"
```

## Heading Levels = Nesting

- `#` = Layout title
- `##` = Root container
- `###` = First-level child
- `####` = Second-level child
- `#####` = Third-level child
- etc.

## Common Layouts

### Form Layout
```
Container (vertical)
├── Container (horizontal) - Row 1
│   ├── Label
│   └── TextBox
├── Container (horizontal) - Row 2
│   ├── Label
│   └── TextBox
└── Container (horizontal) - Buttons
    ├── Button (Submit)
    └── Button (Cancel)
```

### Dashboard Layout
```
Container (vertical)
├── Container (horizontal) - Header
├── Container (horizontal) - Main
│   ├── Container (vertical) - Left Panel
│   └── Container (vertical) - Right Panel
└── Container (horizontal) - Footer
```

### Dialog Layout
```
Container (vertical)
├── Label - Title
├── Label - Message
└── Container (horizontal) - Buttons
    ├── Button (OK)
    └── Button (Cancel)
```

## AI Prompts

### PyQt
```
Implement this UI in PyQt6:
[paste markdown]
```

### CustomTkinter
```
Create this interface using CustomTkinter:
[paste markdown]
```

### HTML/CSS
```
Build this layout in HTML/CSS with flexbox:
[paste markdown]
```

### Tkinter
```
Implement this UI using standard Tkinter:
[paste markdown]
```

## Tips & Tricks

### Layout Tips
- Start with main sections (header, content, footer)
- Use nested containers for complex layouts
- Vertical containers for forms
- Horizontal containers for button groups

### Naming Tips
- Use descriptive names: "LoginButton" not "Button1"
- Group by section: "HeaderTitle", "FormUsername"
- Makes markdown more readable

### Property Tips
- Use custom properties for framework-specific features
- Add placeholders for text inputs
- Set style hints (primary, secondary, danger)

### Positioning Tips
- Let layout managers handle positioning when possible
- Use absolute positioning only when necessary
- Align to grid for cleaner layouts

## Keyboard Shortcuts

- **Click** - Select item
- **Click + Drag** - Move item
- **Delete Selected Button** - Remove item

## File Locations

- **Exports** - Save markdown files anywhere
- **Examples** - `examples/` folder
- **Documentation** - Root folder (*.md files)

## Testing

```bash
source venv/bin/activate
python -m unittest test_ui_elements.py -v
```

## Common Issues

### Can't see element
- Check if inside a container
- Verify width/height > 0
- Check position is within container bounds

### Can't delete item
- Can't delete root MainWindow
- Must select item first

### Properties not updating
- Make sure item is selected
- Enter valid values (numbers for size/position)

## Custom Properties Examples

### PyQt-specific
```
- Properties:
  - stylesheet: QPushButton { background: blue; }
  - icon: path/to/icon.png
  - tooltip: Click to submit
```

### CustomTkinter-specific
```
- Properties:
  - corner_radius: 10
  - fg_color: #007bff
  - hover_color: #0056b3
```

### HTML-specific
```
- Properties:
  - class: btn btn-primary
  - id: submit-button
  - data-action: submit
```

## Quick Reference: Element → Framework

| Element | PyQt | CustomTkinter | HTML |
|---------|------|---------------|------|
| Button | QPushButton | CTkButton | button |
| Label | QLabel | CTkLabel | label/span |
| TextBox | QLineEdit | CTkEntry | input[text] |
| TextArea | QTextEdit | CTkTextbox | textarea |
| Dropdown | QComboBox | CTkComboBox | select |
| CheckBox | QCheckBox | CTkCheckBox | input[checkbox] |
| RadioButton | QRadioButton | CTkRadioButton | input[radio] |
| Slider | QSlider | CTkSlider | input[range] |

## Version Info

- **Version**: 1.0.0
- **Python**: 3.12+
- **CustomTkinter**: 5.2+
- **License**: MIT

## Getting Help

1. Read `QUICKSTART.md` for detailed guide
2. Check `UI_SCHEMA.md` for markdown format
3. See `AI_IMPLEMENTATION_GUIDE.md` for AI usage
4. Review `examples/` for sample outputs
5. Run tests to verify installation

## Next Steps

1. ✅ Design your UI visually
2. ✅ Export to markdown
3. ✅ Share with AI agent
4. ⏳ Get implementation
5. ⏳ Test and iterate

---

**Happy Building!** 🎨

