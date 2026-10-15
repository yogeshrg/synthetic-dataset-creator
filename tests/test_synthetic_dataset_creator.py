"""Tests for synthetic-dataset-creator."""

import pytest
from app.core.config import settings


class TestConfig:
    """Test configuration loading."""

    def test_settings_defaults(self):
        """Test default settings values."""
        assert settings.app_name == "synthetic-dataset-creator"
        assert settings.app_version == "0.1.0"
