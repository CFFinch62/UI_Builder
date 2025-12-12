"""
Test ASCII export functionality
"""

from ui_elements import UIElement, Container, UILayout
from ascii_exporter import ASCIIExporter, export_to_ascii, calculate_optimal_scale
import tempfile
import os


def test_simple_layout():
    """Test a simple layout similar to the example"""
    layout = UILayout("Backgammon UI")
    
    # Adjust root container size
    layout.root_container.width = 80
    layout.root_container.height = 30
    
    # Create header
    header = Container("TitleBanner", 0, 0, 80, 3, "horizontal")
    layout.root_container.add_child(header)
    
    title = UIElement("Label", "Title", 10, 1, 60, 1)
    title.text = "TITLE BANNER"
    header.add_child(title)
    
    # Create main content area (horizontal layout)
    main = Container("MainContent", 0, 3, 80, 22, "horizontal")
    layout.root_container.add_child(main)
    
    # Left panel (vertical)
    left_panel = Container("LeftPanel", 0, 0, 15, 22, "vertical")
    main.add_child(left_panel)
    
    # Human section
    human_section = Container("HumanSection", 1, 0, 13, 8, "vertical")
    left_panel.add_child(human_section)
    
    human_label = UIElement("Label", "HumanLabel", 1, 0, 11, 1)
    human_label.text = "HUMAN"
    human_section.add_child(human_label)
    
    pip_count = UIElement("Label", "PipCount", 1, 1, 11, 1)
    pip_count.text = "pip count"
    human_section.add_child(pip_count)
    
    score = UIElement("Label", "Score", 1, 2, 11, 1)
    score.text = "score"
    human_section.add_child(score)
    
    # Dice section
    dice_section = Container("DiceSection", 1, 8, 13, 7, "vertical")
    left_panel.add_child(dice_section)
    
    die1 = UIElement("Label", "Die1", 1, 0, 11, 1)
    die1.text = "die 1"
    dice_section.add_child(die1)
    
    die2 = UIElement("Label", "Die2", 1, 1, 11, 1)
    die2.text = "die 2"
    dice_section.add_child(die2)
    
    roll_btn = UIElement("Button", "RollBtn", 1, 3, 11, 1)
    roll_btn.text = "roll btn"
    dice_section.add_child(roll_btn)
    
    # Board area (center)
    board_area = Container("BoardArea", 15, 0, 50, 22, "vertical")
    main.add_child(board_area)
    
    board_label = UIElement("Label", "BoardLabel", 5, 10, 40, 1)
    board_label.text = "BOARD AREA"
    board_area.add_child(board_label)
    
    # Right panel
    right_panel = Container("RightPanel", 65, 0, 15, 22, "vertical")
    main.add_child(right_panel)
    
    bear_off_label = UIElement("Label", "BearOff", 1, 1, 12, 1)
    bear_off_label.text = "BEAR OFF"
    right_panel.add_child(bear_off_label)
    
    # Message area at bottom
    message_area = Container("MessageArea", 0, 25, 80, 5, "horizontal")
    layout.root_container.add_child(message_area)
    
    msg_label = UIElement("Label", "Message", 5, 1, 70, 1)
    msg_label.text = "MESSAGE AREA"
    message_area.add_child(msg_label)
    
    # Calculate optimal scale
    optimal_scale = calculate_optimal_scale(layout, max_width=120, max_height=60)
    print(f"Optimal scale factor: {optimal_scale:.2f}x")
    print(f"Original size: {layout.root_container.width}x{layout.root_container.height}")
    print(f"Scaled size: {int(layout.root_container.width * optimal_scale)}x{int(layout.root_container.height * optimal_scale)}")
    print()

    # Export to ASCII with auto-scaling
    output_file = "examples/backgammon_ui_ascii_scaled.txt"
    os.makedirs("examples", exist_ok=True)
    ascii_art = export_to_ascii(layout, output_file, scale_factor=None, max_width=120, max_height=60)

    print("Generated Scaled ASCII Art:")
    print(ascii_art)
    print("\n" + "="*80 + "\n")
    print(f"Saved to: {output_file}")
    
    print(f"Also saved to: {output_file}")
    
    return ascii_art


def test_login_form():
    """Test a simple login form"""
    layout = UILayout("Login Form")
    
    layout.root_container.width = 60
    layout.root_container.height = 25
    
    # Header
    header = Container("Header", 5, 2, 50, 4, "vertical")
    layout.root_container.add_child(header)
    
    title = UIElement("Label", "Title", 5, 1, 40, 1)
    title.text = "User Login"
    header.add_child(title)
    
    # Form section
    form = Container("FormSection", 5, 7, 50, 12, "vertical")
    layout.root_container.add_child(form)
    
    # Username row
    username_row = Container("UsernameRow", 2, 2, 46, 3, "horizontal")
    form.add_child(username_row)
    
    username_label = UIElement("Label", "UsernameLabel", 1, 1, 12, 1)
    username_label.text = "Username:"
    username_row.add_child(username_label)
    
    username_input = UIElement("TextBox", "UsernameInput", 14, 1, 30, 1)
    username_input.text = ""
    username_row.add_child(username_input)
    
    # Password row
    password_row = Container("PasswordRow", 2, 6, 46, 3, "horizontal")
    form.add_child(password_row)
    
    password_label = UIElement("Label", "PasswordLabel", 1, 1, 12, 1)
    password_label.text = "Password:"
    password_row.add_child(password_label)
    
    password_input = UIElement("TextBox", "PasswordInput", 14, 1, 30, 1)
    password_input.text = ""
    password_row.add_child(password_input)
    
    # Button section
    button_section = Container("ButtonSection", 5, 20, 50, 3, "horizontal")
    layout.root_container.add_child(button_section)
    
    login_btn = UIElement("Button", "LoginBtn", 10, 1, 12, 1)
    login_btn.text = "Login"
    button_section.add_child(login_btn)
    
    cancel_btn = UIElement("Button", "CancelBtn", 25, 1, 12, 1)
    cancel_btn.text = "Cancel"
    button_section.add_child(cancel_btn)
    
    # Calculate optimal scale
    optimal_scale = calculate_optimal_scale(layout, max_width=120, max_height=60)
    print(f"Optimal scale factor: {optimal_scale:.2f}x")
    print(f"Original size: {layout.root_container.width}x{layout.root_container.height}")
    print(f"Scaled size: {int(layout.root_container.width * optimal_scale)}x{int(layout.root_container.height * optimal_scale)}")
    print()

    # Export to ASCII with auto-scaling
    output_file = "examples/login_form_ascii_scaled.txt"
    os.makedirs("examples", exist_ok=True)
    ascii_art = export_to_ascii(layout, output_file, scale_factor=None, max_width=120, max_height=60)

    print("Login Form ASCII Art (Scaled):")
    print(ascii_art)
    print("\n" + "="*80 + "\n")
    print(f"Saved to: {output_file}")

    return ascii_art


if __name__ == "__main__":
    print("Testing ASCII Export\n")
    print("="*80)
    print("\nTest 1: Backgammon-style Layout")
    print("="*80 + "\n")
    test_simple_layout()
    
    print("\nTest 2: Login Form")
    print("="*80 + "\n")
    test_login_form()
    
    print("\n✅ All tests completed!")

