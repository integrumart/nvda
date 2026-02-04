# A part of NonVisual Desktop Access (NVDA)
# This file is covered by the GNU General Public License.
# See the file COPYING for more details.
# Copyright (C) 2026 NV Access Limited

"""Unit tests for the webCMS module."""

import unittest
from unittest.mock import Mock
import controlTypes
import webCMS


class TestWebCMSDetection(unittest.TestCase):
	"""Tests for web CMS editor detection functions."""

	def test_isWebEditor_withEditableText(self):
		"""Test that isWebEditor returns True for editable text with contentEditable."""
		obj = Mock()
		obj.role = controlTypes.Role.EDITABLETEXT
		obj.IA2Attributes = {'contentEditable': 'true'}
		self.assertTrue(webCMS.isWebEditor(obj))

	def test_isWebEditor_withNonEditableText(self):
		"""Test that isWebEditor returns False for non-editable text."""
		obj = Mock()
		obj.role = controlTypes.Role.STATICTEXT
		self.assertFalse(webCMS.isWebEditor(obj))

	def test_isWebEditor_withNone(self):
		"""Test that isWebEditor handles None gracefully."""
		self.assertFalse(webCMS.isWebEditor(None))

	def test_getCMSEditorType_ckeditor(self):
		"""Test identification of CKEditor."""
		obj = Mock()
		obj.IA2Attributes = {'id': 'ckeditor-content'}
		self.assertEqual(webCMS.getCMSEditorType(obj), 'ckeditor')

	def test_getCMSEditorType_tinymce(self):
		"""Test identification of TinyMCE editor."""
		obj = Mock()
		obj.IA2Attributes = {'id': 'tinymce-editor'}
		self.assertEqual(webCMS.getCMSEditorType(obj), 'tinymce')

	def test_getCMSEditorType_gutenberg(self):
		"""Test identification of Gutenberg editor."""
		obj = Mock()
		obj.IA2Attributes = {'id': 'block-editor-main'}
		self.assertEqual(webCMS.getCMSEditorType(obj), 'gutenberg')

	def test_getCMSEditorType_unknown(self):
		"""Test that unknown editor types return None."""
		obj = Mock()
		obj.IA2Attributes = {'id': 'unknown-editor'}
		self.assertIsNone(webCMS.getCMSEditorType(obj))

	def test_getCMSEditorType_withNone(self):
		"""Test that getCMSEditorType handles None gracefully."""
		self.assertIsNone(webCMS.getCMSEditorType(None))
