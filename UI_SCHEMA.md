# UI Markdown Schema Documentation

## Overview
This schema provides a standardized way to represent UI layouts in markdown format that can be easily understood by AI agents and implemented in various frameworks (PyQt, CustomTkinter, HTML/CSS, etc.).

## Basic Structure

### Container Definition
Containers are rectangular areas that hold UI elements. They can be nested and oriented horizontally or vertically.

```markdown
## Container: [Name]
- Type: Container
- Orientation: [horizontal|vertical]
- Width: [pixels or percentage]
- Height: [pixels or percentage]
- Position: (x, y)
- Padding: [pixels]
- Background: [color]
```

### UI Element Definition
UI elements are interactive or display components placed within containers.

```markdown
### Element: [Name]
- Type: [Button|Label|TextBox|TextArea|Dropdown|ComboBox|CheckBox|RadioButton|Slider|Image|Spacer]
- Text: [display text]
- Width: [pixels or percentage]
- Height: [pixels or percentage]
- Position: (x, y) [relative to parent container]
- Enabled: [true|false]
- Visible: [true|false]
- Properties:
  - [key]: [value]
```

## Complete Example

```markdown
# UI Layout: User Registration Form

## Container: MainWindow
- Type: Container
- Orientation: vertical
- Width: 800
- Height: 600
- Position: (0, 0)
- Padding: 20
- Background: #f0f0f0

### Container: HeaderSection
- Type: Container
- Orientation: horizontal
- Width: 100%
- Height: 80
- Position: (0, 0)
- Padding: 10
- Background: #2c3e50

#### Element: AppTitle
- Type: Label
- Text: "User Registration"
- Width: auto
- Height: auto
- Position: (10, 25)
- Properties:
  - font-size: 24
  - font-weight: bold
  - color: #ffffff
  - alignment: left

### Container: FormSection
- Type: Container
- Orientation: vertical
- Width: 100%
- Height: 400
- Position: (0, 80)
- Padding: 20
- Background: #ffffff

#### Container: NameRow
- Type: Container
- Orientation: horizontal
- Width: 100%
- Height: 60
- Position: (0, 0)
- Padding: 5

##### Element: NameLabel
- Type: Label
- Text: "Full Name:"
- Width: 150
- Height: 30
- Position: (0, 15)
- Properties:
  - font-size: 14
  - alignment: right

##### Element: NameInput
- Type: TextBox
- Text: ""
- Width: 300
- Height: 30
- Position: (160, 15)
- Properties:
  - placeholder: "Enter your full name"
  - max-length: 100

#### Container: EmailRow
- Type: Container
- Orientation: horizontal
- Width: 100%
- Height: 60
- Position: (0, 60)
- Padding: 5

##### Element: EmailLabel
- Type: Label
- Text: "Email:"
- Width: 150
- Height: 30
- Position: (0, 15)
- Properties:
  - font-size: 14
  - alignment: right

##### Element: EmailInput
- Type: TextBox
- Text: ""
- Width: 300
- Height: 30
- Position: (160, 15)
- Properties:
  - placeholder: "email@example.com"
  - validation: email

#### Container: ButtonRow
- Type: Container
- Orientation: horizontal
- Width: 100%
- Height: 60
- Position: (0, 120)
- Padding: 5

##### Element: SubmitButton
- Type: Button
- Text: "Submit"
- Width: 120
- Height: 40
- Position: (160, 10)
- Properties:
  - style: primary
  - action: submit_form

##### Element: CancelButton
- Type: Button
- Text: "Cancel"
- Width: 120
- Height: 40
- Position: (290, 10)
- Properties:
  - style: secondary
  - action: cancel_form

### Container: FooterSection
- Type: Container
- Orientation: horizontal
- Width: 100%
- Height: 60
- Position: (0, 540)
- Padding: 10
- Background: #ecf0f1

#### Element: StatusLabel
- Type: Label
- Text: "Ready"
- Width: auto
- Height: auto
- Position: (10, 20)
- Properties:
  - font-size: 12
  - color: #7f8c8d
```

## Element Types Reference

### Button
- Properties: style (primary|secondary|danger), action, icon

### Label
- Properties: font-size, font-weight, color, alignment (left|center|right)

### TextBox
- Properties: placeholder, max-length, validation, password (true|false)

### TextArea
- Properties: placeholder, rows, cols, max-length, wrap (true|false)

### Dropdown
- Properties: options (list), default-value, editable (true|false)

### ComboBox
- Properties: options (list), default-value

### CheckBox
- Properties: checked (true|false), label

### RadioButton
- Properties: group, selected (true|false), label

### Slider
- Properties: min, max, value, step, orientation (horizontal|vertical)

### Image
- Properties: source, alt-text, scale-mode (fit|fill|stretch)

### Spacer
- Properties: flexible (true|false)

## Notes for AI Implementation

1. **Hierarchy**: Markdown heading levels (##, ###, ####) indicate nesting depth
2. **Containers**: Can be mapped to Frame, Panel, Div, or similar layout components
3. **Orientation**: 
   - `horizontal` = elements flow left-to-right (row)
   - `vertical` = elements flow top-to-bottom (column)
4. **Positioning**: Can be absolute (x, y) or relative (within parent container)
5. **Sizing**: Supports pixels (e.g., 300) or percentages (e.g., 100%)
6. **Properties**: Framework-specific attributes can be added as needed

## Framework Mapping Examples

### PyQt/PySide
- Container → QFrame, QWidget, QVBoxLayout, QHBoxLayout
- Button → QPushButton
- Label → QLabel
- TextBox → QLineEdit
- TextArea → QTextEdit
- Dropdown → QComboBox

### CustomTkinter
- Container → CTkFrame with pack/grid
- Button → CTkButton
- Label → CTkLabel
- TextBox → CTkEntry
- TextArea → CTkTextbox
- Dropdown → CTkComboBox

### HTML/CSS
- Container → div with flexbox (flex-direction: row|column)
- Button → button
- Label → label or span
- TextBox → input type="text"
- TextArea → textarea
- Dropdown → select

