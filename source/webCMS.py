# A part of NonVisual Desktop Access (NVDA)
# Copyright (C) 2026 NV Access Limited
# This file is covered by the GNU General Public License.
# See the file COPYING for more details.

"""
Utilities and helpers for web-based Content Management Systems (CMS).

This module provides common functionality to enhance NVDA's support for 
web-based CMS platforms like WordPress, Drupal, Joomla, and others that 
use WYSIWYG editors such as CKEditor, TinyMCE, Gutenberg, etc.

Web CMS platforms are typically accessed through web browsers and rely on
NVDA's virtual buffer and web accessibility features provided by the
browser's accessibility APIs (IAccessible2, UIA).
"""

from typing import Optional
import controlTypes


def isWebEditor(obj) -> bool:
	"""
	Determine if an object represents a web-based rich text editor.
	
	Web CMS platforms commonly use WYSIWYG editors that may have
	special characteristics that indicate they are editing surfaces.
	
	@param obj: The NVDA object to check
	@return: True if the object appears to be a web editor, False otherwise
	"""
	if not obj:
		return False
	
	# Check if this is an editable region
	if obj.role != controlTypes.Role.EDITABLETEXT:
		return False
	
	# Check for common ARIA roles used in web editors
	ariaProps = getattr(obj, 'ariaProperties', {})
	if ariaProps:
		# Check for textbox role with multiline
		role = ariaProps.get('role', '')
		if 'textbox' in role.lower():
			return True
	
	# Check for contentEditable attribute (common in web editors)
	ia2Attrs = getattr(obj, 'IA2Attributes', {})
	if ia2Attrs:
		# contentEditable is a common attribute for web editors
		if 'contentEditable' in ia2Attrs or 'contenteditable' in ia2Attrs:
			return True
	
	return False


def getCMSEditorType(obj) -> Optional[str]:
	"""
	Attempt to identify the type of CMS editor being used.
	
	This can help provide editor-specific optimizations or announcements.
	
	@param obj: The NVDA object representing the editor
	@return: A string identifying the editor type (e.g., 'ckeditor', 'tinymce', 'gutenberg'),
	         or None if the editor type cannot be determined
	"""
	if not obj:
		return None
	
	# Try to identify editor by checking various attributes and properties
	# CKEditor typically has specific class names or identifiers
	if hasattr(obj, 'windowClassName'):
		className = obj.windowClassName.lower()
		if 'cke' in className:
			return 'ckeditor'
	
	# TinyMCE has its own identifiers
	ia2Attrs = getattr(obj, 'IA2Attributes', {})
	if ia2Attrs:
		htmlId = ia2Attrs.get('id', '').lower()
		if 'tinymce' in htmlId or htmlId.startswith('mce'):
			return 'tinymce'
		elif 'ckeditor' in htmlId or 'cke' in htmlId:
			return 'ckeditor'
		# WordPress Gutenberg editor
		elif 'gutenberg' in htmlId or 'block-editor' in htmlId:
			return 'gutenberg'
	
	return None
