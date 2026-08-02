---
source_url: https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-lower.html
---

# LOWER
<a name="sql-reference-lower"></a>

```
LOWER ( <character-expression> )
```

Converts a string to all lower-case characters. Returns null if input argument is null, and the empty string if the input argument is an empty string.

## Examples
<a name="sql-reference-lower-examples"></a>

| Function | Result |
| --- | --- |
| LOWER('abcDEFghi123') | abcdefghi123 |
