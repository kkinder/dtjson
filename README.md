# dtjson: json, but with datetime and timespan support

dtjson builds on regular Json, but adds support for timespan and datetime objects in Python. It does this by looking for `"__type__": "datetime"` or `"__type__": "timedelta"` in the keys, with `isoformat' and `seconds` respectively.

Example Usage::

```python
>>> import dtjson
>>> import datetime
>>> serialized = dtjson.dumps(['foo', {'bar': ('baz', None, 1.0, 2), 'spam': datetime.datetime.now()}])
>>> print(serialized)
'["foo", {"bar": ["baz", null, 1.0, 2], "spam": {"__type__": "datetime", "isoformat": "2024-05-25T14:23:36.769090"}}]'
>>> unserialized = dtjson.loads(serialized)
>>> print(unserialized)
['foo', {'bar': ['baz', None, 1.0, 2], 'spam': datetime.datetime(2024, 5, 25, 14, 23, 36, 769090)}]
```

Timespans are also similarly support. The interface for using dtjson is nearly identical to the json module, and can be generally used as a replacement.

## Installation

**NOTE**: PyPi rejected dtjson as a package name, so this is packaged as `json-dt-serializer`.

```
pip install json-dt-serializer
```

## Usage details

Usage is nearly identical to the [json](https://docs.python.org/3/library/json.html) module, with most arguments being passed directly to it.

### dtjson.dump

```python
def dump(
    obj,
    fp,
    skipkeys=False,
    ensure_ascii=True,
    check_circular=True,
    allow_nan=True,
    cls=None,
    indent=None,
    separators=None,
    default=None,
    sort_keys=False,
    **kw
)
```

Serializes obj as a JSON formatted stream to fp (a `.write()`-supporting file-like object).

Arguments:

 - obj: The Python object to serialize.
 - fp: File-like object supporting .write() where the JSON data will be written.
 - skipkeys: If True, dict keys that are not basic types will be skipped.
 - ensure_ascii: If True, non-ASCII characters are escaped in JSON strings.
 - check_circular: If False, skips circular reference check.
 - allow_nan: If False, out of range float values will raise a ValueError.
 - cls: Custom JSONEncoder subclass.
 - indent: If non-negative integer, pretty-prints with that indent level.
 - separators: Tuple (item_separator, key_separator) to specify item and key separators.
 - default: Function that returns a serializable version of obj or raises TypeError.
 - sort_keys: If True, dictionary keys are sorted.
 - **kw: Additional keyword arguments.

### dtjson.dumps

```python
def dumps(
    obj,
    skipkeys=False,
    ensure_ascii=True,
    check_circular=True,
    allow_nan=True,
    cls=None,
    indent=None,
    separators=None,
    default=None,
    sort_keys=False,
    **kw
)
```

Serializes obj to a JSON formatted string.

Arguments:

 - obj: The Python object to serialize.
 - skipkeys: If True, dict keys that are not basic types will be skipped.
 - ensure_ascii: If True, non-ASCII characters are escaped in JSON strings.
 - check_circular: If False, skips circular reference check.
 - allow_nan: If False, out of range float values will raise a ValueError.
 - cls: Custom JSONEncoder subclass.
 - indent: If non-negative integer, pretty-prints with that indent level.
 - separators: Tuple (item_separator, key_separator) to specify item and key separators.
 - default: Function that returns a serializable version of obj or raises TypeError.
 - sort_keys: If True, dictionary keys are sorted.
 - **kw: Additional keyword arguments.

### dtjson.load

```python
def load(
    fp,
    cls=None,
    object_hook=None,
    parse_float=None,
    parse_int=None,
    parse_constant=None,
    object_pairs_hook=None,
    **kw
)
```
Deserializes fp (a `.read()`-supporting file-like object containing a JSON document) to a Python object.

Arguments:

 - fp: File-like object supporting .read() containing the JSON document.
 - cls: Custom JSONDecoder subclass.
 - object_hook: Function called with the result of any object literal decode.
 - parse_float: Function to parse JSON float values.
 - parse_int: Function to parse JSON int values.
 - parse_constant: Function called with strings like -Infinity, Infinity, NaN.
 - object_pairs_hook: Function called with an ordered list of pairs for object literal decode.
 - **kw: Additional keyword arguments.

### dtjson.loads

```python
def loads(
    s,
    cls=None,
    object_hook=None,
    parse_float=None,
    parse_int=None,
    parse_constant=None,
    object_pairs_hook=None,
    **kw
)
```

Deserializes s (a `str`, `bytes` or `bytearray` instance containing a JSON document) to a Python object.

Arguments:

 - s: A string, bytes, or bytearray instance containing the JSON document.
 - cls: Custom JSONDecoder subclass.
 - object_hook: Function called with the result of any object literal decode.
 - parse_float: Function to parse JSON float values.
 - parse_int: Function to parse JSON int values.
 - parse_constant: Function called with strings like -Infinity, Infinity, NaN.
 - object_pairs_hook: Function called with an ordered list of pairs for object literal decode.
 - **kw: Additional keyword arguments.