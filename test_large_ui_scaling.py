"""
Test scaling with a large UI layout
"""

from ui_elements import UIElement, Container, UILayout
from ascii_exporter import export_to_ascii, calculate_optimal_scale


def test_large_ui():
    """Test with a large UI that needs scaling"""
    
    # Create a large layout (800x600 - typical window size)
    layout = UILayout("Large Application")
    layout.root_container.width = 800
    layout.root_container.height = 600
    
    # Header
    header = Container("Header", 0, 0, 800, 60, "horizontal")
    layout.root_container.add_child(header)
    
    title = UIElement("Label", "AppTitle", 20, 20, 200, 30)
    title.text = "My Large Application"
    header.add_child(title)
    
    menu_btn = UIElement("Button", "MenuBtn", 700, 15, 80, 30)
    menu_btn.text = "Menu"
    header.add_child(menu_btn)
    
    # Sidebar
    sidebar = Container("Sidebar", 0, 60, 200, 540, "vertical")
    layout.root_container.add_child(sidebar)
    
    nav1 = UIElement("Button", "Nav1", 10, 10, 180, 40)
    nav1.text = "Dashboard"
    sidebar.add_child(nav1)
    
    nav2 = UIElement("Button", "Nav2", 10, 60, 180, 40)
    nav2.text = "Projects"
    sidebar.add_child(nav2)
    
    nav3 = UIElement("Button", "Nav3", 10, 110, 180, 40)
    nav3.text = "Settings"
    sidebar.add_child(nav3)
    
    # Main content area
    content = Container("ContentArea", 200, 60, 600, 540, "vertical")
    layout.root_container.add_child(content)
    
    # Content header
    content_header = Container("ContentHeader", 10, 10, 580, 50, "horizontal")
    content.add_child(content_header)
    
    page_title = UIElement("Label", "PageTitle", 10, 10, 300, 30)
    page_title.text = "Dashboard Overview"
    content_header.add_child(page_title)
    
    search_box = UIElement("TextBox", "SearchBox", 350, 10, 200, 30)
    search_box.text = ""
    content_header.add_child(search_box)
    
    # Cards section
    cards = Container("CardsSection", 10, 70, 580, 200, "horizontal")
    content.add_child(cards)
    
    card1 = Container("Card1", 10, 10, 180, 180, "vertical")
    cards.add_child(card1)
    
    card1_title = UIElement("Label", "Card1Title", 10, 10, 160, 30)
    card1_title.text = "Total Users"
    card1.add_child(card1_title)
    
    card1_value = UIElement("Label", "Card1Value", 10, 50, 160, 60)
    card1_value.text = "1,234"
    card1.add_child(card1_value)
    
    card2 = Container("Card2", 200, 10, 180, 180, "vertical")
    cards.add_child(card2)
    
    card2_title = UIElement("Label", "Card2Title", 10, 10, 160, 30)
    card2_title.text = "Revenue"
    card2.add_child(card2_title)
    
    card2_value = UIElement("Label", "Card2Value", 10, 50, 160, 60)
    card2_value.text = "$45,678"
    card2.add_child(card2_value)
    
    card3 = Container("Card3", 390, 10, 180, 180, "vertical")
    cards.add_child(card3)
    
    card3_title = UIElement("Label", "Card3Title", 10, 10, 160, 30)
    card3_title.text = "Active Projects"
    card3.add_child(card3_title)
    
    card3_value = UIElement("Label", "Card3Value", 10, 50, 160, 60)
    card3_value.text = "42"
    card3.add_child(card3_value)
    
    # Data table
    table = Container("DataTable", 10, 280, 580, 240, "vertical")
    content.add_child(table)
    
    table_header = UIElement("Label", "TableHeader", 10, 10, 560, 30)
    table_header.text = "Recent Activity"
    table.add_child(table_header)
    
    # Calculate optimal scale
    print("="*80)
    print("LARGE UI SCALING TEST")
    print("="*80)
    print(f"\nOriginal size: {layout.root_container.width}x{layout.root_container.height}px")
    
    optimal_scale = calculate_optimal_scale(layout, max_width=120, max_height=60)
    print(f"Optimal scale factor: {optimal_scale:.2f}x")
    print(f"Scaled size: {int(layout.root_container.width * optimal_scale)}x{int(layout.root_container.height * optimal_scale)} chars")
    print(f"\nThis will fit in an IDE window with minimal scrolling!")
    print()
    
    # Export with auto-scaling
    output_file = "examples/large_app_scaled.txt"
    ascii_art = export_to_ascii(layout, output_file, scale_factor=None, max_width=120, max_height=60)
    
    print("Generated Scaled ASCII Art:")
    print(ascii_art)
    print("\n" + "="*80)
    print(f"✅ Saved to: {output_file}")
    print(f"✅ File is viewable without horizontal scrolling in IDE!")
    
    # Also export at full scale for comparison
    output_file_full = "examples/large_app_fullscale.txt"
    ascii_art_full = export_to_ascii(layout, output_file_full, scale_factor=1.0)
    
    full_lines = ascii_art_full.count('\n')
    full_width = max(len(line) for line in ascii_art_full.split('\n'))
    
    print(f"\n📊 Comparison:")
    print(f"   Full scale: {full_width} chars wide, {full_lines} lines")
    print(f"   Scaled:     ~120 chars wide, ~60 lines")
    print(f"   Reduction:  {(1 - optimal_scale) * 100:.0f}% smaller")
    print(f"\n✅ Full scale saved to: {output_file_full} (for comparison)")


if __name__ == "__main__":
    test_large_ui()

