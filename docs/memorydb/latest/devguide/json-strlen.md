---
source_url: https://docs.aws.amazon.com/memorydb/latest/devguide/json-strlen.html
---

# JSON.STRLEN
<a name="json-strlen"></a>

Get lengths of the JSON string values at the path.

Syntax

```
JSON.STRLEN <key> [path]
```
+ key (required) – key of JSON document type
+ path (optional) – a JSON path. Defaults to the root if not provided

**Return**

If the path is enhanced syntax:
+ Array of integers, representing the length of string value at each path.
+ If a value is not a string, its corresponding return value is null.
+ Null if the document key does not exist.

If the path is restricted syntax:
+ Integer, the string's length.
+ If multiple string values are selected, the command returns the first string's length.
+ `WRONGTYPE` error if the value at the path is not a string.
+ `NONEXISTENT` error if the path does not exist.
+ Null if the document key does not exist.

**Examples**

 Enhanced path syntax:

```
127.0.0.1:6379> JSON.SET k1 $ '{"a":{"a":"a"}, "b":{"a":"a", "b":1}, "c":{"a":"a", "b":"bb"}, "d":{"a":1, "b":"b", "c":3}}'
OK
127.0.0.1:6379> JSON.STRLEN k1 $.a.a
1) (integer) 1
127.0.0.1:6379> JSON.STRLEN k1 $.a.*
1) (integer) 1
127.0.0.1:6379> JSON.STRLEN k1 $.c.*
1) (integer) 1
2) (integer) 2
127.0.0.1:6379> JSON.STRLEN k1 $.c.b
1) (integer) 2
127.0.0.1:6379> JSON.STRLEN k1 $.d.*
1) (nil)
2) (integer) 1
3) (nil)
```

 Restricted path syntax:

```
127.0.0.1:6379> JSON.SET k1 $ '{"a":{"a":"a"}, "b":{"a":"a", "b":1}, "c":{"a":"a", "b":"bb"}, "d":{"a":1, "b":"b", "c":3}}'
OK
127.0.0.1:6379> JSON.STRLEN k1 .a.a
(integer) 1
127.0.0.1:6379> JSON.STRLEN k1 .a.*
(integer) 1
127.0.0.1:6379> JSON.STRLEN k1 .c.*
(integer) 1
127.0.0.1:6379> JSON.STRLEN k1 .c.b
(integer) 2
127.0.0.1:6379> JSON.STRLEN k1 .d.*
(integer) 1
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon MemoryDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query memorydb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
