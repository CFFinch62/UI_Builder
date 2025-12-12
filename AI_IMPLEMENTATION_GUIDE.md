# AI Implementation Guide

This guide helps AI agents understand and implement UI designs from MD UI Builder markdown files.

## Understanding the Markdown Format

### Structure Hierarchy

The markdown uses heading levels to indicate nesting:

- `#` - Layout title
- `##` - Root container (MainWindow)
- `###` - First-level children (containers or elements)
- `####` - Second-level children
- And so on...

**Rule**: Each additional `#` indicates one level deeper in the hierarchy.

### Container vs Element

**Containers** (layout components):
- Marked with `- Type: Container`
- Have `Orientation` property (horizontal or vertical)
- Can contain other containers and elements
- Map to layout widgets (frames, panels, divs)

**Elements** (UI components):
- Marked with `- Type: [Button|Label|TextBox|etc]`
- Cannot contain other items
- Map to interactive widgets

## Implementation Patterns

### PyQt/PySide Implementation

```python
# Container with vertical orientation → QVBoxLayout
# Container with horizontal orientation → QHBoxLayout

# Example:
## Container: FormSection
- Orientation: vertical

# Becomes:
form_section = QWidget()
form_layout = QVBoxLayout()
form_section.setLayout(form_layout)
```

**Element Mapping**:
- Button → QPushButton
- Label → QLabel
- TextBox → QLineEdit
- TextArea → QTextEdit
- Dropdown → QComboBox
- CheckBox → QCheckBox
- RadioButton → QRadioButton
- Slider → QSlider

**Properties**:
- `Text` → setText()
- `Width/Height` → setFixedSize() or setMinimumSize()
- `Enabled` → setEnabled()
- `Visible` → setVisible()
- Custom properties → Use as hints for styling

### CustomTkinter Implementation

```python
# Container with vertical orientation → pack() or grid() with vertical stacking
# Container with horizontal orientation → pack(side="left") or grid() with horizontal layout

# Example:
## Container: FormSection
- Orientation: vertical

# Becomes:
form_section = ctk.CTkFrame(parent)
form_section.pack(fill="both", expand=True, padx=10, pady=10)
```

**Element Mapping**:
- Button → CTkButton
- Label → CTkLabel
- TextBox → CTkEntry
- TextArea → CTkTextbox
- Dropdown → CTkComboBox
- CheckBox → CTkCheckBox
- RadioButton → CTkRadioButton
- Slider → CTkSlider

**Properties**:
- `Text` → text parameter or configure(text=...)
- `Width/Height` → width/height parameters
- `Background` → fg_color parameter
- Custom properties → Use for corner_radius, hover_color, etc.

### HTML/CSS Implementation

```html
<!-- Container with vertical orientation → div with flexbox column -->
<!-- Container with horizontal orientation → div with flexbox row -->

<!-- Example: -->
## Container: FormSection
- Orientation: vertical
- Width: 400
- Height: 300

<!-- Becomes: -->
<div class="form-section" style="
  display: flex;
  flex-direction: column;
  width: 400px;
  height: 300px;
">
</div>
```

**Element Mapping**:
- Button → `<button>`
- Label → `<label>` or `<span>`
- TextBox → `<input type="text">`
- TextArea → `<textarea>`
- Dropdown → `<select>` with `<option>`
- CheckBox → `<input type="checkbox">`
- RadioButton → `<input type="radio">`
- Slider → `<input type="range">`
- Image → `<img>`

**Properties**:
- `Text` → innerHTML or value attribute
- `Width/Height` → CSS width/height
- `Background` → CSS background-color
- Custom properties → Use for classes, IDs, data attributes

## Key Implementation Guidelines

### 1. Respect the Hierarchy

Always maintain the parent-child relationships shown in the markdown:

```markdown
## Container: Parent
### Container: Child1
#### Element: Button1
### Container: Child2
#### Element: Button2
```

This means:
- Parent contains Child1 and Child2
- Child1 contains Button1
- Child2 contains Button2

### 2. Handle Orientation

**Vertical Orientation** (default):
- Elements stack top-to-bottom
- Use vertical layouts (VBox, column flex, pack vertically)

**Horizontal Orientation**:
- Elements flow left-to-right
- Use horizontal layouts (HBox, row flex, pack horizontally)

### 3. Position and Size

**Absolute Positioning**:
- `Position: (x, y)` gives coordinates relative to parent
- Use when precise placement is needed

**Relative Sizing**:
- Percentages (e.g., `Width: 100%`) mean relative to parent
- Pixels (e.g., `Width: 300`) are absolute

**Recommendation**: Use layout managers when possible, fall back to absolute positioning only when necessary.

### 4. Custom Properties

Custom properties provide framework-specific hints:

```markdown
- Properties:
  - placeholder: Enter your name
  - max-length: 50
  - style: primary
```

**Interpret these as**:
- `placeholder` → Placeholder text for inputs
- `max-length` → Maximum character limit
- `style: primary` → Use primary/accent color scheme
- `style: secondary` → Use secondary/neutral color scheme
- `style: danger` → Use warning/error color scheme

### 5. Common Patterns

#### Form Layout Pattern

```markdown
## Container: FormSection
- Orientation: vertical

### Container: Row1
- Orientation: horizontal

#### Element: Label1
- Text: "Name:"

#### Element: Input1
- Type: TextBox
```

**Implement as**: Label-input pairs in horizontal rows, stacked vertically

#### Button Group Pattern

```markdown
## Container: ButtonGroup
- Orientation: horizontal

### Element: OkButton
### Element: CancelButton
```

**Implement as**: Buttons side-by-side

#### Dashboard Pattern

```markdown
## Container: Main
- Orientation: horizontal

### Container: LeftPanel
- Orientation: vertical

### Container: RightPanel
- Orientation: vertical
```

**Implement as**: Two-column layout with vertical content in each

## Example Implementations

### Example 1: Simple Button (PyQt)

```markdown
### Element: SubmitButton
- Type: Button
- Text: "Submit"
- Width: 120
- Height: 40
- Properties:
  - style: primary
```

```python
submit_button = QPushButton("Submit")
submit_button.setFixedSize(120, 40)
submit_button.setStyleSheet("background-color: #007bff; color: white;")
```

### Example 2: Form Row (CustomTkinter)

```markdown
### Container: NameRow
- Orientation: horizontal

#### Element: NameLabel
- Type: Label
- Text: "Name:"
- Width: 100

#### Element: NameInput
- Type: TextBox
- Width: 200
```

```python
name_row = ctk.CTkFrame(parent)
name_row.pack(fill="x", padx=10, pady=5)

name_label = ctk.CTkLabel(name_row, text="Name:", width=100)
name_label.pack(side="left", padx=5)

name_input = ctk.CTkEntry(name_row, width=200)
name_input.pack(side="left", padx=5)
```

### Example 3: Vertical Stack (HTML/CSS)

```markdown
## Container: Menu
- Orientation: vertical

### Element: Item1
- Type: Button
- Text: "Home"

### Element: Item2
- Type: Button
- Text: "About"
```

```html
<div class="menu" style="display: flex; flex-direction: column;">
  <button>Home</button>
  <button>About</button>
</div>
```

## Tips for AI Agents

1. **Start with the root**: Always begin with the MainWindow/root container
2. **Work depth-first**: Implement each container fully before moving to siblings
3. **Use layout managers**: Prefer layout managers over absolute positioning
4. **Apply styling last**: Get structure working first, then apply colors/fonts
5. **Handle missing properties**: Use sensible defaults for any unspecified properties
6. **Preserve names**: Use the element/container names for variable names or IDs
7. **Test incrementally**: Build and test each section before moving on

## Common Questions

**Q: What if Position is (0, 0)?**
A: This usually means "use default positioning" - let the layout manager handle it.

**Q: What if Width/Height is "auto"?**
A: Let the element size itself based on content.

**Q: What about spacing between elements?**
A: Use the container's `Padding` property as a guide for spacing.

**Q: How to handle nested containers?**
A: Each container becomes a widget/frame that contains its children.

**Q: What if a property is missing?**
A: Use framework defaults. The markdown shows intent, not every detail.

## Validation Checklist

When implementing a UI from markdown, verify:

- [ ] All containers are created in the correct hierarchy
- [ ] Orientation (horizontal/vertical) is respected
- [ ] All elements are created with correct types
- [ ] Text content is set where specified
- [ ] Sizes are applied (or reasonable defaults used)
- [ ] Custom properties are interpreted appropriately
- [ ] The visual result matches the described structure
- [ ] Interactive elements are functional

## Getting Help

If the markdown is unclear:
1. Check the hierarchy (heading levels)
2. Look for the Orientation property
3. Check if it's a Container or Element
4. Review the example implementations above
5. Use common UI patterns as a guide

The goal is to create a functional UI that matches the structure and intent described in the markdown, not to replicate every pixel-perfect detail.

