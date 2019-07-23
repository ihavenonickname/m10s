import re
from decimal import Decimal

import sv_converter
from .utils import _RATIOS_LENGTH, _RATIOS_MASS, SVConverterException

__all__ = [
    'convert',
    'convert_si',
]

def convert(value, in_unit, out_unit):
    def get_flat_units(x):
        m = re.match(r'([a-z]+)/([a-z]+[3³])', x, re.IGNORECASE)
        return (m.group(1), m.group(2)) if m else (None, None)

    in_mass, in_volume = get_flat_units(in_unit)
    out_mass, out_volume = get_flat_units(out_unit)

    x = sv_converter.mass.convert(value, in_mass, out_mass)
    y = sv_converter.volume.convert(1, in_volume, out_volume)

    return float(Decimal(str(x)) / Decimal(str(y)))

def convert_si(value, unit):
    return convert(value, unit, 'kg/m³')
