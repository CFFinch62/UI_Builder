# UI Layout: Login Form Example

## Container: MainWindow
- Type: Container
- Orientation: vertical
- Width: 500
- Height: 400
- Position: (0, 0)
- Padding: 20
- Background: #f5f5f5

### Container: HeaderSection
- Type: Container
- Orientation: vertical
- Width: 460
- Height: 80
- Position: (20, 20)
- Padding: 10
- Background: #2c3e50

#### Element: AppTitle
- Type: Label
- Text: "User Login"
- Width: 440
- Height: 40
- Position: (10, 20)
- Enabled: true
- Visible: true
- Properties:
  - font-size: 24
  - font-weight: bold
  - color: #ffffff
  - alignment: center

### Container: FormSection
- Type: Container
- Orientation: vertical
- Width: 460
- Height: 220
- Position: (20, 120)
- Padding: 15
- Background: #ffffff

#### Container: UsernameRow
- Type: Container
- Orientation: horizontal
- Width: 430
- Height: 50
- Position: (15, 15)
- Padding: 5
- Background: #ffffff

##### Element: UsernameLabel
- Type: Label
- Text: "Username:"
- Width: 100
- Height: 30
- Position: (5, 10)
- Enabled: true
- Visible: true
- Properties:
  - font-size: 14
  - alignment: right

##### Element: UsernameInput
- Type: TextBox
- Text: ""
- Width: 300
- Height: 30
- Position: (115, 10)
- Enabled: true
- Visible: true
- Properties:
  - placeholder: Enter your username
  - max-length: 50

#### Container: PasswordRow
- Type: Container
- Orientation: horizontal
- Width: 430
- Height: 50
- Position: (15, 75)
- Padding: 5
- Background: #ffffff

##### Element: PasswordLabel
- Type: Label
- Text: "Password:"
- Width: 100
- Height: 30
- Position: (5, 10)
- Enabled: true
- Visible: true
- Properties:
  - font-size: 14
  - alignment: right

##### Element: PasswordInput
- Type: TextBox
- Text: ""
- Width: 300
- Height: 30
- Position: (115, 10)
- Enabled: true
- Visible: true
- Properties:
  - placeholder: Enter your password
  - password: true

#### Container: RememberMeRow
- Type: Container
- Orientation: horizontal
- Width: 430
- Height: 40
- Position: (15, 135)
- Padding: 5
- Background: #ffffff

##### Element: RememberMeCheckbox
- Type: CheckBox
- Text: "Remember me"
- Width: 150
- Height: 25
- Position: (115, 7)
- Enabled: true
- Visible: true
- Properties:
  - checked: false

### Container: ButtonSection
- Type: Container
- Orientation: horizontal
- Width: 460
- Height: 60
- Position: (20, 360)
- Padding: 10
- Background: #ecf0f1

#### Element: LoginButton
- Type: Button
- Text: "Login"
- Width: 120
- Height: 40
- Position: (150, 10)
- Enabled: true
- Visible: true
- Properties:
  - style: primary
  - action: submit_login

#### Element: CancelButton
- Type: Button
- Text: "Cancel"
- Width: 120
- Height: 40
- Position: (280, 10)
- Enabled: true
- Visible: true
- Properties:
  - style: secondary
  - action: cancel_login

