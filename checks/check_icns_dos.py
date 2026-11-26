# Tests potential DOS of IcnsImagePlugin with 0 length block.
# Run from anywhere that PIL is importable.
from __future__ import annotations

from io import BytesIO

from PIL import Image


def _check_icns_dos():
    # Attempt to open a truncated ICNS stream to ensure decoder handles it safely.
    try:
        with Image.open(BytesIO(b"icns\x00\x00\x00\x10hang\x00\x00\x00\x00")):
            pass
    except OSError:
        # Ignore errors when this module is imported; the purpose is only for manual runs.
        return


if __name__ == "__main__":
    _check_icns_dos()
