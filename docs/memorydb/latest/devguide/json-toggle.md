---
source_url: https://docs.aws.amazon.com/memorydb/latest/devguide/json-toggle.html
---

# JSON.TOGGLE
<a name="json-toggle"></a>

Toggle boolean values between true and false at the path.

Syntax

```
JSON.TOGGLE <key> [path]
```
+ key (required) – key of JSON document type
+ path (optional) – a JSON path. Defaults to the root if not provided

**Return**

If the path is enhanced syntax:
+ Array of integers (0 - false, 1 - true) representing the resulting boolean value at each path.
+ If a value is a not boolean, its corresponding return value is null.
+ `NONEXISTENT` if the document key does not exist.

If the path is restricted syntax:
+ String ("true"/"false") representing the resulting boolean value.
+ `NONEXISTENT` if the document key does not exist.
+ `WRONGTYPE` error if the value at the path is not a boolean.

**Examples**

 Enhanced path syntax:

```
127.0.0.1:6379> JSON.SET k1 . '{"a":true, "b":false, "c":1, "d":null, "e":"foo", "f":[], "g":{}}'
OK
127.0.0.1:6379> JSON.TOGGLE k1 $.*
1) (integer) 0
2) (integer) 1
3) (nil)
4) (nil)
5) (nil)
6) (nil)
7) (nil)
127.0.0.1:6379> JSON.TOGGLE k1 $.*
1) (integer) 1
2) (integer) 0
3) (nil)
4) (nil)
5) (nil)
6) (nil)
7) (nil)
```

 Restricted path syntax:

```
127.0.0.1:6379> JSON.SET k1 . true
OK
127.0.0.1:6379> JSON.TOGGLE k1
"false"
127.0.0.1:6379> JSON.TOGGLE k1
"true"

127.0.0.1:6379> JSON.SET k2 . '{"isAvailable": false}'
OK
127.0.0.1:6379> JSON.TOGGLE k2 .isAvailable
"true"
127.0.0.1:6379> JSON.TOGGLE k2 .isAvailable
"false"
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon MemoryDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query memorydb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
