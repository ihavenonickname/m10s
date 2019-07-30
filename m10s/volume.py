import re
from decimal import Decimal

from .utils import M10SException, _RATIOS_LENGTH

__all__ = [
    'convert',
    'convert_si',
]

def convert(value, in_unit, out_unit):
    def get_flat_unit(x):
        m = re.match(r'([a-z]+)[3³]', x, re.IGNORECASE)
        return m.group(1) if m else None

    flat_in_unit = get_flat_unit(in_unit)

    if flat_in_unit not in _RATIOS_LENGTH:
        raise M10SException(f'Not a valid volume unit: "{in_unit}"')

    flat_out_unit = get_flat_unit(out_unit)

    if flat_out_unit not in _RATIOS_LENGTH:
        raise M10SException(f'Not a valid volume unit: "{out_unit}"')

    factor = _RATIOS_LENGTH[flat_out_unit] / _RATIOS_LENGTH[flat_in_unit]

    return float(Decimal(value) / pow(factor, 3))

def convert_si(value, unit):
    return convert(value, unit, 'm³')

def from_mass(mass, density):
    return float(Decimal(mass) / Decimal(density))
