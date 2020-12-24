# Module  `nanoasgi`

NanoASGI is a fast and simple micro-framework for small web applications.

EXPAND SOURCE CODE

## Classes

`class  App`

EXPAND SOURCE CODE

### Methods

`async def  http_handler(self, scope, receive, send)`

EXPAND SOURCE CODE

`async def  lifespan_handler(self, scope, receive, send)`

EXPAND SOURCE CODE

`def  on(self, event)`

EXPAND SOURCE CODE

`def  route(self, method, path)`

EXPAND SOURCE CODE

`class  CaselessMultiDict(items)`

EXPAND SOURCE CODE

### Ancestors

-   [MultiDict](#nanoasgi.MultiDict "nanoasgi.MultiDict")
-   collections.abc.Mapping
-   collections.abc.Collection
-   collections.abc.Sized
-   collections.abc.Iterable
-   collections.abc.Container

`class  MultiDict(items)`

EXPAND SOURCE CODE

### Ancestors

-   collections.abc.Mapping
-   collections.abc.Collection
-   collections.abc.Sized
-   collections.abc.Iterable
-   collections.abc.Container

### Subclasses

-   [CaselessMultiDict](#nanoasgi.CaselessMultiDict "nanoasgi.CaselessMultiDict")

### Methods

`def  get_list(self, key)`

EXPAND SOURCE CODE

`class  Request(path: str, method: str, headers: [CaselessMultiDict](#nanoasgi.CaselessMultiDict "nanoasgi.CaselessMultiDict"), query: [MultiDict](#nanoasgi.MultiDict "nanoasgi.MultiDict"), body: bytes)`

Request(path, method, headers, query, body)

EXPAND SOURCE CODE

### Ancestors

-   builtins.tuple

### Instance variables

`var  body  : bytes`

Alias for field number 4

`var  headers  : [CaselessMultiDict](#nanoasgi.CaselessMultiDict "nanoasgi.CaselessMultiDict")`

Alias for field number 2

`var  json  : object`

EXPAND SOURCE CODE

`var  method  : str`

Alias for field number 1

`var  path  : str`

Alias for field number 0

`var  query  : [MultiDict](#nanoasgi.MultiDict "nanoasgi.MultiDict")`

Alias for field number 3

`var  text  : str`

EXPAND SOURCE CODE

`class  Response(data: Union[bytes, str, list, dict, NoneType] = None, status: int = 200, headers: List[Tuple[str, str]] = [])`

Response(data, status, headers)

EXPAND SOURCE CODE

### Ancestors

-   builtins.tuple

### Instance variables

`var  body  : bytes`

EXPAND SOURCE CODE

`var  data  : Union[bytes, str, list, dict, NoneType]`

Alias for field number 0

`var  headers  : List[Tuple[str, str]]`

Alias for field number 2

`var  status  : int`

Alias for field number 1
