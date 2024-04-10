import datetime
import uuid
from src.errors.errors import BadRequest

def is_valid_uuid(val):
    try:
        uuid.UUID(str(val))
        return True
    except Exception:
        raise BadRequest
    
def datetime_valid(dt_str):
    try:
        format_string = '%Y-%m-%dT%H:%M:%S.%f%z'
        result = datetime.datetime.strptime(dt_str, format_string)
        if (result.timestamp() < datetime.datetime.now().timestamp()):
            return None
        else:
            return result
    except:
        return None
