"""Time Utils."""
from __future__ import annotations

import platform
import time
from contextlib import suppress
from functools import partial

CLOCK_MONOTONIC_COARSE = 6


def __gen_monotonic_time_coarse() -> partial[float]:
    """Return a function that provides monotonic time in seconds.

    This is the coarse version of time_monotonic, which is faster but less accurate.

    Since many arm64 and 32-bit platforms don't support VDSO with time.monotonic
    because of errata, we can't rely on the kernel to provide a fast
    monotonic time.

    https://lore.kernel.org/lkml/20170404171826.25030-1-marc.zyngier@arm.com/
    """
    # We use a partial here since its implementation is in native code
    # which allows us to avoid the overhead of the global lookup
    # of CLOCK_MONOTONIC_COARSE.
    return partial(time.clock_gettime, CLOCK_MONOTONIC_COARSE)


monotonic_time_coarse = time.monotonic
with suppress(Exception):
    if (
        platform.system() == "Linux"
        and abs(time.monotonic() - __gen_monotonic_time_coarse()()) < 1
    ):
        monotonic_time_coarse = __gen_monotonic_time_coarse()
