from decimal import Decimal

from .utils import _RATIOS_LENGTH, M10SException

__all__ = [
    'convert',
    'convert_si',
]

def convert(value, in_unit, out_unit):
    if in_unit not in _RATIOS_LENGTH:
        raise M10SException(f'Not a valid length unit: "{in_unit}"')

    if out_unit not in _RATIOS_LENGTH:
        raise M10SException(f'Not a valid length unit: "{out_unit}"')

    return float(Decimal(value) * _RATIOS_LENGTH[in_unit] / _RATIOS_LENGTH[out_unit])

def convert_si(value, unit):
    return convert(value, unit, 'm')
