#!/usr/bin/env python3
"""Use an engine checkout's cartkit with the 0.2.73 FireRed base enabled.

Usage: python3 tools/cartkit_firered.py /path/to/tools/cartkit.py pack . -o OUTPUT
The engine validates base names through GameVersion.VERSIONS; old cartkit
versions hard-code the six GB/GBC games. All other validation stays intact.
"""
import importlib.util
import sys
from pathlib import Path

if len(sys.argv) < 3:
    raise SystemExit(__doc__)
source = Path(sys.argv[1]).resolve()
spec = importlib.util.spec_from_file_location('engine_cartkit', source)
kit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(kit)
if 'firered' not in kit.BASES:
    kit.BASES = (*kit.BASES, 'firered')
raise SystemExit(kit.main(sys.argv[2:]))
