# QR code generation and parsing utilities

import json


def generate_qr(info: dict) -> str:
    """Return a JSON string encoding component info for QR code generation.

    The returned string can be passed directly to a QR code library
    (e.g. ``qrcode``) to produce a scannable image.
    """
    return json.dumps(info, separators=(",", ":"))


def parse_qr(qr_data: str) -> dict:
    """Parse a QR code string back into a component info dict."""
    try:
        return json.loads(qr_data)
    except (json.JSONDecodeError, TypeError) as exc:
        raise ValueError(f"Invalid QR code format: unable to parse JSON data") from exc
