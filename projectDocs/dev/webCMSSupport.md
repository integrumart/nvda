# Web CMS Support in NVDA

## Overview

NVDA provides comprehensive support for web-based Content Management Systems (CMS) through its virtual buffer system and web accessibility features. This document explains how NVDA handles web CMS platforms and the utilities available for developers.

## What is a Web CMS?

A Content Management System (CMS) is software that helps users create, manage, and publish digital content. Popular web-based CMS platforms include:

- **WordPress** - The most widely used CMS
- **Drupal** - Enterprise-level CMS
- **Joomla** - Community-driven CMS
- **Wix, Squarespace** - Website builders with CMS features

These platforms typically feature WYSIWYG (What You See Is What You Get) editors such as:
- CKEditor
- TinyMCE
- Gutenberg (WordPress Block Editor)
- Quill Editor

## How NVDA Supports Web CMS

### Virtual Buffer System

NVDA uses a **virtual buffer** (browse mode) to render web content, making CMS admin interfaces accessible:

- `source/virtualBuffers/gecko_ia2.py` - Firefox/Mozilla support
- `source/virtualBuffers/MSHTML.py` - Legacy IE support
- `source/virtualBuffers/webKit.py` - WebKit-based browsers
- UIA web support in `source/NVDAObjects/UIA/web.py`

### Web Accessibility APIs

CMS interfaces are accessed through browser accessibility APIs:
- **IAccessible2** (IA2) - Used by Firefox, Chrome
- **UI Automation** (UIA) - Used by Edge, Chrome

### Rich Text Editor Support

Web CMS platforms use rich text editors that NVDA handles through:
- contentEditable attribute detection
- ARIA role recognition (role="textbox", aria-multiline)
- Edit field behaviors in `source/NVDAObjects/behaviors.py`

## webCMS Module

The `source/webCMS.py` module provides utility functions for web CMS support:

### Functions

#### `isWebEditor(obj) -> bool`

Determines if an NVDA object represents a web-based rich text editor.

```python
import webCMS

if webCMS.isWebEditor(obj):
    # Handle web editor specifically
    pass
```

#### `getCMSEditorType(obj) -> Optional[str]`

Identifies the type of CMS editor being used (e.g., 'ckeditor', 'tinymce', 'gutenberg').

```python
import webCMS

editorType = webCMS.getCMSEditorType(obj)
if editorType == 'ckeditor':
    # CKEditor-specific handling
    pass
```

## Common CMS Editor Patterns

### CKEditor

- Typically uses `contentEditable` attribute
- May have class names containing "cke"
- Often has ID attributes like "ckeditor-content"

### TinyMCE

- Uses IFrame-based editing by default
- Class names often contain "mce" or "tinymce"
- ID attributes like "tinymce-editor"

### Gutenberg (WordPress)

- Block-based editor
- Uses multiple contentEditable regions
- ID attributes contain "block-editor"

## Best Practices for CMS Accessibility

### For CMS Developers

1. **Use Semantic HTML**: Proper heading structure, landmarks
2. **ARIA Labels**: Label form fields and buttons clearly
3. **Keyboard Navigation**: Ensure all functions are keyboard accessible
4. **Focus Management**: Manage focus properly in modals and dialogs

### For NVDA Developers

1. **Test with Browse Mode**: Verify navigation works in browse mode
2. **Test Focus Mode**: Ensure form editing works in focus mode
3. **Verify ARIA Support**: Check that ARIA attributes are properly exposed
4. **Test Common Workflows**: Creating posts, editing content, media upload

## Related Issues

- [#4026](https://github.com/nvaccess/nvda/issues/4026) - Difficulty navigating paragraphs in CKEditor
- [#4242](https://github.com/nvaccess/nvda/issues/4242) - W3C CSS Speech Module support

## Testing Web CMS

To test NVDA with web CMS platforms:

1. Access the CMS admin interface in a supported browser
2. Navigate to the content editor
3. Test creating and editing content with:
   - Browse mode navigation (headings, landmarks, forms)
   - Focus mode for text editing
   - Toolbar and menu access
   - Modal dialogs and popups

## Further Resources

- [Browse Mode Documentation](../../user_docs/en/userGuide.md#BrowseMode)
- [Virtual Buffers Source](../source/virtualBuffers/)
- [Web Accessibility Testing Guide](testing/contributing.md)
