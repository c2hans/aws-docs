---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/json-arrindex.html
---

# JSON.ARRINDEX
<a name="json-arrindex"></a>

Searches for the first occurrence of a scalar JSON value in the arrays at the path.
+ Out of range errors are treated by rounding the index to the array's start and end.
+ If start > end, return -1 (not found).

Syntax

```
JSON.ARRINDEX <key> <path> <json-scalar> [start [end]]
```
+ key (required) – A Valkey or Redis OSS key of JSON document type.
+ path (required) – A JSON path.
+ json-scalar (required) – The scalar value to search for. JSON scalar refers to values that are not objects or arrays. That is, string, number, Boolean, and null are scalar values.
+ start (optional) – The start index, inclusive. Defaults to 0 if not provided.
+ end (optional) – The end index, exclusive. Defaults to 0 if not provided, which means that the last element is included. 0 or -1 means the last element is included.

**Return**

If the path is enhanced syntax:
+ Array of integers. Each value is the index of the matching element in the array at the path. The value is -1 if not found.
+ If a value is not an array, its corresponding return value is null.

If the path is restricted syntax:
+ Integer, the index of matching element, or -1 if not found.
+ `WRONGTYPE` error if the value at the path is not an array.

**Examples**

 Enhanced path syntax:

```
127.0.0.1:6379> JSON.SET k1 . '[[], ["a"], ["a", "b"], ["a", "b", "c"]]'
OK
127.0.0.1:6379> JSON.ARRINDEX k1 $[*] '"b"'
1) (integer) -1
2) (integer) -1
3) (integer) 1
4) (integer) 1
```

 Restricted path syntax:

```
127.0.0.1:6379> JSON.SET k1 . '{"children": ["John", "Jack", "Tom", "Bob", "Mike"]}'
OK
127.0.0.1:6379> JSON.ARRINDEX k1 .children '"Tom"'
(integer) 2
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ElastiCache. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonElastiCache` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
