from pathlib import Path
import subprocess
import sys

import pytest

from pkg1 import p1 as pkg1_p1, p2 as pkg1_p2
from pkg2 import p1 as pkg2_p1, p2 as pkg2_p2


@pytest.mark.parametrize("value", [5, 0, -3])
def test_pkg1_mysquare_returns_label(value):
    assert pkg1_p1.mysquare(value) == f"Square: {value}"


@pytest.mark.parametrize("value", [5, 0, -3])
def test_pkg1_mysum_returns_label(value):
    assert pkg1_p2.mysum(value) == f"Sum {value}"


@pytest.mark.parametrize("value, expected", [(5, 25), (0, 0), (-3, 9)])
def test_pkg2_mysquare_returns_square(value, expected):
    assert pkg2_p1.mysquare(value) == expected


@pytest.mark.parametrize("value, expected", [(5, 10), (0, 0), (-3, -6)])
def test_pkg2_mysum_returns_double(value, expected):
    assert pkg2_p2.mysum(value) == expected


def test_main_prints_exact_output():
    root = Path(__file__).resolve().parents[1]
    result = subprocess.run(
        [sys.executable, str(root / "main.py")],
        cwd=root,
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stderr
    assert result.stdout == "Square: 5\nSum 5\n25\n10\nit's done\n"
    assert result.stderr == ""
