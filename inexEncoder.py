import json
import decimal
import datetime

class Encoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return int(o)
        if isinstance(o, datetime.datetime):
            return int(o.timestamp() * 1000)
        return super().default(o)