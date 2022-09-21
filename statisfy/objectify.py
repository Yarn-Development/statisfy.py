import json
try:
    from types import SimpleNamespace as Namespace
except ImportError:
    # Python 2.x fallback
    from argparse import Namespace

def objectify(data):
    """
    It takes a JSON string and returns a Python object. 
    
    .. note:: 
        This function will need to be used if you want to access the data in the JSON object.
    
    :param data: The JSON string to be converted to a Python object
    :type data: str

    :return: A list of objects.
    :rtype: object

    :example:
    >>> yt = YouTube("API_KEY")
    >>> json_string = yt.getVideobyQuery("Hello World")
    >>> object = objectify(json_string)
    >>> print(object.items[0].id)
    1234567890


    """
    obj = json.loads(data, object_hook=lambda d: Namespace(**d))
    return obj