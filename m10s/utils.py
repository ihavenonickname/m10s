from decimal import Decimal

class M10SException(Exception):
    pass

_RATIOS_LENGTH = {
    'km': Decimal(1_000),

     'm': Decimal(1),

    'dm': Decimal(1) / Decimal(10),
    'cm': Decimal(1) / Decimal(100),
    'mm': Decimal(1) / Decimal(1_000),
    'um': Decimal(1) / Decimal(1_000_000),
    'nm': Decimal(1) / Decimal(1_000_000_000),
}

_RATIOS_MASS = {
     'Mg': Decimal(1_000),

     'kg': Decimal(1),

      'g': Decimal(1) / Decimal(1_000),
     'mg': Decimal(1) / Decimal(1_000_000),
     'ug': Decimal(1) / Decimal(1_000_000_000),
     'ng': Decimal(1) / Decimal(1_000_000_000_000),
}
