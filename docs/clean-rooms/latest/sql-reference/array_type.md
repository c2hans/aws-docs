---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/array_type.html
---

# ARRAY type
<a name="array_type"></a>

Use the ARRAY type to represent values comprising a sequence of elements with the type of `elementType`.

```
array(elementType, containsNull)
```

Use `containsNull` to indicate if elements in an ARRAY type can have `null` values.
