import json

def filter_inventory_message(message):
    """
    Filter inventory messages based on the 'type' field.
    
    Args:
        message (str): JSON-encoded message.
        
    Returns:
        bool: True if the message type is 'inventory', otherwise False.
    """
    try:
        data = json.loads(message)
        return data.get('type') == 'inventory'
    except json.JSONDecodeError:
        return False

def filter_delivery_message(message):
    """
    Filter delivery messages based on the 'type' field.
    
    Args:
        message (str): JSON-encoded message.
        
    Returns:
        bool: True if the message type is 'delivery', otherwise False.
    """
    try:
        data = json.loads(message)
        return data.get('type') == 'delivery'
    except json.JSONDecodeError:
        return False
