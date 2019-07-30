from decimal import Decimal

from .utils import _RATIOS_MASS, M10SException

__all__ = [
    'convert',
    'convert_si',
]

def convert(value, in_unit, out_unit):
    if in_unit not in _RATIOS_MASS:
        raise M10SException(f'Not a valid mass unit: "{in_unit}"')

    if out_unit not in _RATIOS_MASS:
        raise M10SException(f'Not a valid mass unit: "{out_unit}"')

    return float(Decimal(value) * _RATIOS_MASS[in_unit] / _RATIOS_MASS[out_unit])

def convert_si(value, unit):
    return convert(value, unit, 'kg')

def from_volume(volume, density):
    return float(Decimal(volume) * Decimal(density))
