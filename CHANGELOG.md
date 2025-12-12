# Changelog

## Version 1.2.0 - ASCII Art Auto-Scaling

### ✨ New Feature: Auto-Scaling ASCII Export

**Problem**: ASCII art exports were too large (600+ lines, 800+ chars wide) to view in IDE windows.

**Solution**: Automatic scaling to fit IDE windows!

- **Auto-calculates optimal scale** to fit within 120x60 characters
- **Maintains aspect ratio** - proportional scaling
- **Adds header with scale info** to output files
- **90% size reduction** for large UIs (800x600 → 80x60)
- **No configuration needed** - works automatically

**Example**:
- Before: 800 chars wide, 600 lines ❌
- After: 80 chars wide, 60 lines ✅

**Files Modified**:
- `ascii_exporter.py` - Added scale_factor parameter and auto-scaling logic
- `main.py` - Updated to use auto-scaling by default
- `test_ascii_export.py` - Updated tests to use scaling

**Files Added**:
- `test_large_ui_scaling.py` - Demonstrates scaling with large UI
- `ASCII_SCALING_GUIDE.md` - Complete guide to scaling feature

See `ASCII_SCALING_GUIDE.md` for full details!

---

## Version 1.1.0 - Bug Fixes and New Features

### 🐛 Bug Fixes

#### 1. Properties Panel Not Clearing (FIXED)
**Problem**: When selecting different containers/elements, the properties panel would accumulate old property widgets instead of clearing them. This caused the panel to fill up with useless data requiring excessive scrolling.

**Solution**: 
- Changed `property_widgets` from a dictionary to a list to track ALL widgets (labels, entries, dropdowns, buttons, separators)
- Updated `clear()` method to properly destroy all tracked widgets
- Updated all widget creation methods to add widgets to the tracking list

**Files Modified**:
- `properties_panel.py` - Lines 12-212

#### 2. Canvas Toolbar Taking Too Much Space (FIXED)
**Problem**: The canvas toolbar was wasting vertical space and the canvas view was not tall enough to see the entire UI being built.

**Solution**:
- Fixed grid row configuration to give canvas row (row 1) all the weight
- Set toolbar to fixed height (40px) with `grid_propagate(False)`
- Reduced button heights to 28px for more compact toolbar
- Adjusted padding to minimize wasted space

**Files Modified**:
- `main.py` - Lines 49-83

#### 3. Scrollbar Layout Issue (FIXED)
**Problem**: An empty box with scrollbar was appearing below the canvas, taking up vertical space.

**Solution**:
- Fixed the packing order of scrollbars and canvas
- Scrollbars now pack first (right and bottom) so they don't get covered
- Canvas packs last with `fill="both", expand=True`

**Files Modified**:
- `canvas_view.py` - Lines 31-51

#### 4. Save Project Not Actually Saving (FIXED)
**Problem**: The "Save Project" button showed a success dialog but didn't actually save any file. It was marked as "coming soon".

**Solution**:
- Implemented full JSON serialization for UIElement, Container, and UILayout classes
- Added `to_dict()` and `from_dict()` methods to all classes
- Added `save_to_json()` and `load_from_json()` methods to UILayout
- Updated main.py to actually save and load projects
- Created comprehensive tests to verify functionality

**Files Modified**:
- `ui_elements.py` - Added serialization methods (lines 55-89, 150-192, 259-290)
- `main.py` - Implemented save/load (lines 195-224)
- `test_save_load.py` - New test file

### ✨ New Features

#### 1. ASCII Art Export
**Feature**: Export UI layouts as ASCII art / text-based visual representations (like your example file).

**Details**:
- New `ascii_exporter.py` module with `ASCIIExporter` class
- Draws containers and elements as boxes using ASCII characters
- Shows element types with prefixes: `[BTN]`, `LBL:`, `[___]`, etc.
- Exports to `.txt` files
- New green "Export to ASCII Art" button in the main window

**Files Added**:
- `ascii_exporter.py` - Complete ASCII art export functionality
- `test_ascii_export.py` - Test file with examples

**Files Modified**:
- `main.py` - Added ASCII export button and handler (lines 101-113, 167-180)

#### 2. Project Save/Load (JSON Format)
**Feature**: Save and load complete projects in JSON format for later editing.

**Details**:
- Saves entire UI hierarchy including all properties
- Preserves custom properties
- Human-readable JSON format
- Full round-trip support (save → load → edit → save)
- Tested and verified working

**Usage**:
- Click "Save Project" → Choose filename → Project saved as .json
- Click "Load Project" → Select .json file → Project loaded and displayed

## Testing

All new features and bug fixes have been tested:

### Unit Tests
- ✅ `test_ui_elements.py` - 14 tests passing
- ✅ `test_save_load.py` - Save/load functionality verified
- ✅ `test_ascii_export.py` - ASCII export examples generated

### Manual Testing Checklist
- ✅ Properties panel clears properly when selecting different items
- ✅ Canvas toolbar is compact and doesn't waste space
- ✅ Canvas view is tall enough to see entire UI
- ✅ No extra empty boxes with scrollbars
- ✅ Save Project actually saves files
- ✅ Load Project restores complete UI state
- ✅ ASCII Art export generates visual text representation

## Files Changed Summary

### Modified Files
1. `main.py` - UI layout fixes, ASCII export, save/load implementation
2. `canvas_view.py` - Scrollbar layout fix
3. `properties_panel.py` - Widget tracking and clearing fix
4. `ui_elements.py` - Added serialization methods

### New Files
1. `ascii_exporter.py` - ASCII art export functionality
2. `test_ascii_export.py` - ASCII export tests
3. `test_save_load.py` - Save/load tests
4. `CHANGELOG.md` - This file

## Upgrade Instructions

If you have the app running:
1. Close the application
2. The code has been updated automatically
3. Restart with `./run.sh` or `python main.py`

All your existing work can now be saved and loaded!

## Known Limitations

### Still To Do (Future Enhancements)
1. **Import from Markdown** - Load markdown files back into the builder
2. **Preview Mode** - Live preview of what the UI will look like
3. **Undo/Redo** - Undo and redo actions
4. **Copy/Paste** - Copy and paste elements/containers
5. **Alignment Tools** - Snap to grid, align multiple items
6. **Templates** - Pre-built UI patterns

## Version History

- **v1.1.0** (Current) - Bug fixes + ASCII export + Save/Load
- **v1.0.0** - Initial release with visual builder and markdown export

---

**Note**: The application is now fully functional with all core features working correctly!

