---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/json-arrpop.html
---

# JSON.ARRPOP
<a name="json-arrpop"></a>

Removes and returns element at the index from the array. Popping an empty array returns null.

Syntax

```
JSON.ARRPOP <key> [path [index]]
```
+ key (required) – A Valkey or Redis OSS key of JSON document type.
+ path (optional) – A JSON path. Defaults to the root if not provided.
+ index (optional) – The position in the array to start popping from.
  + Defaults to -1 if not provided, which means the last element.
  + Negative value means position from the last element.
  + Out of boundary indexes are rounded to their respective array boundaries.

**Return**

If the path is enhanced syntax:
+ Array of bulk strings that represent popped values at each path.
+ If a value is an empty array, its corresponding return value is null.
+ If a value is not an array, its corresponding return value is null.

If the path is restricted syntax:
+ Bulk string, which represents the popped JSON value.
+ Null if the array is empty.
+ `WRONGTYPE` error if the value at the path is not an array.

**Examples**

 Enhanced path syntax:

```
127.0.0.1:6379> JSON.SET k1 . '[[], ["a"], ["a", "b"]]'
OK
127.0.0.1:6379> JSON.ARRPOP k1 $[*]
1) (nil)
2) "\"a\""
3) "\"b\""
127.0.0.1:6379> JSON.GET k1
"[[],[],[\"a\"]]"
```

 Restricted path syntax:

```
127.0.0.1:6379> JSON.SET k1 . '[[], ["a"], ["a", "b"]]'
OK
127.0.0.1:6379> JSON.ARRPOP k1
"[\"a\",\"b\"]"
127.0.0.1:6379> JSON.GET k1
"[[],[\"a\"]]"

127.0.0.1:6379> JSON.SET k2 . '[[], ["a"], ["a", "b"]]'
OK
127.0.0.1:6379> JSON.ARRPOP k2 . 0
"[]"
127.0.0.1:6379> JSON.GET k2
"[[\"a\"],[\"a\",\"b\"]]"
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ElastiCache. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonElastiCache` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
