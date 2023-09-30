from typing import Any


class SpekulatioException(Exception):
    """Spekulatio base exeption."""

    pass


class SpekulatioError(SpekulatioException):
    """Base exeption for Spekulatio errors."""

    pass


class SpekulatioInputError(SpekulatioError):
    """Invalid user provided data."""

    pass


class SpekulatioInternalError(SpekulatioError):
    """Exeption for internal, unexpected errors."""

    pass

