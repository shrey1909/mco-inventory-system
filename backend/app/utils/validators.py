# Validation helper functions


def validate_quantity(quantity: int) -> bool:
    return isinstance(quantity, int) and quantity >= 0


def validate_username(username: str) -> bool:
    return isinstance(username, str) and len(username.strip()) >= 3


def validate_data(data: dict) -> bool:
    """Generic validation: ensure data is a dict and all values are non-None."""
    if not isinstance(data, dict):
        return False
    return all(v is not None for v in data.values())
