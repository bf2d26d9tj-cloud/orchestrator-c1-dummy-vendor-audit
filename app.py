"""Fictional Paper Lantern quote calculator. Deliberately incomplete audit fixture."""

def quote(quantity, service='standard'):
    if not isinstance(quantity, int) or quantity < 1:
        raise ValueError('Use a positive fictional quantity')
    if service != 'standard':
        raise NotImplementedError('Express service is not implemented')
    return quantity * 10 + 5


def export_csv(quantities):
    raise NotImplementedError('CSV export is not implemented')
