from __future__ import annotations

import sys

from PIL import Image

if sys.maxsize < 2**32:

    def create_large_test_image():
        """Return a very large test image. Creation is deferred to avoid resource usage at import time."""
        return Image.new("L", (999999, 999999), 0)
else:

    def create_large_test_image():
        """Placeholder when large image creation is not appropriate on this platform."""
        raise RuntimeError("Large test image creation not supported on this platform")
