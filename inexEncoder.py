import json
import decimal
import datetime

class Encoder(json.JSONEncoder):
    """Encoder uses json.JSONEncoder and checks for instances of decimal and datetime. 
    Changes decimal.Decimal to int and datetime.datetime to unix timestamp with miliseconds."""
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return int(o)
        if isinstance(o, datetime.datetime):
            return int(o.timestamp() * 1000)
        return super().default(o)