# UI Layout: My UI Design

## Container: MainWindow
- Type: Container
- Orientation: vertical
- Width: 800
- Height: 600
- Position: (0, 0)
- Padding: 10
- Background: #ffffff

### Container: Score_Control_Area
- Type: Container
- Orientation: vertical
- Width: 200
- Height: 500
- Position: (20, 80)
- Padding: 10
- Background: #ffffff

#### Container: Human_Score
- Type: Container
- Orientation: vertical
- Width: 180
- Height: 120
- Position: (10, 20)
- Padding: 10
- Background: #ffffff

##### Element: Human_Player
- Type: Label
- Text: "HUMAN PLAYER"
- Width: 160
- Height: 20
- Position: (10, 10)
- Enabled: true
- Visible: true

##### Element: Image8
- Type: Image
- Text: "Image8"
- Width: 100
- Height: 30
- Position: (12, 40)
- Enabled: true
- Visible: true


#### Container: AI_Score
- Type: Container
- Orientation: vertical
- Width: 180
- Height: 120
- Position: (10, 360)
- Padding: 10
- Background: #ffffff

#### Container: Controls
- Type: Container
- Orientation: vertical
- Width: 180
- Height: 200
- Position: (10, 150)
- Padding: 10
- Background: #ffffff

##### Element: Die1
- Type: Image
- Text: "Image2"
- Width: 40
- Height: 40
- Position: (40, 20)
- Enabled: true
- Visible: true

##### Element: Die2
- Type: Image
- Text: "Image3"
- Width: 40
- Height: 40
- Position: (100, 20)
- Enabled: true
- Visible: true

##### Element: Roll_Button
- Type: Button
- Text: "ROLL DICE"
- Width: 120
- Height: 20
- Position: (28, 70)
- Enabled: true
- Visible: true

##### Element: Undo_Button
- Type: Button
- Text: "UNDO MOVE"
- Width: 120
- Height: 20
- Position: (29, 100)
- Enabled: true
- Visible: true

##### Element: EndTurn_Button
- Type: Button
- Text: "END TURN"
- Width: 120
- Height: 20
- Position: (30, 130)
- Enabled: true
- Visible: true

##### Element: Double_Cube
- Type: Image
- Text: "64"
- Width: 40
- Height: 30
- Position: (66, 162)
- Enabled: true
- Visible: true



### Container: Title_Banner
- Type: Container
- Orientation: horizontal
- Width: 760
- Height: 40
- Position: (20, 20)
- Padding: 10
- Background: #ffffff

### Container: Board_Main
- Type: Container
- Orientation: vertical
- Width: 450
- Height: 450
- Position: (240, 80)
- Padding: 10
- Background: #ffffff

#### Container: Upper_Outer
- Type: Container
- Orientation: vertical
- Width: 180
- Height: 200
- Position: (20, 20)
- Padding: 10
- Background: #ffffff

#### Container: Lower_Outer
- Type: Container
- Orientation: vertical
- Width: 180
- Height: 200
- Position: (20, 230)
- Padding: 10
- Background: #ffffff

#### Container: Upper_Inner
- Type: Container
- Orientation: vertical
- Width: 180
- Height: 200
- Position: (250, 20)
- Padding: 10
- Background: #ffffff

#### Container: Lower_Inner
- Type: Container
- Orientation: vertical
- Width: 180
- Height: 200
- Position: (250, 230)
- Padding: 10
- Background: #ffffff

#### Container: Bar
- Type: Container
- Orientation: vertical
- Width: 30
- Height: 410
- Position: (210, 20)
- Padding: 10
- Background: #ffffff


### Container: BearOffArea_Black
- Type: Container
- Orientation: vertical
- Width: 80
- Height: 220
- Position: (700, 80)
- Padding: 10
- Background: #ffffff

### Container: Message_Area
- Type: Container
- Orientation: vertical
- Width: 540
- Height: 40
- Position: (240, 540)
- Padding: 10
- Background: #ffffff

### Container: BearOffArea_White
- Type: Container
- Orientation: vertical
- Width: 80
- Height: 220
- Position: (700, 310)
- Padding: 10
- Background: #ffffff
