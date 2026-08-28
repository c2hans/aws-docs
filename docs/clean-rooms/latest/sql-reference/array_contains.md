---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/array_contains.html
---

# ARRAY\_CONTAINS function
<a name="array_contains"></a>

The ARRAY\_CONTAINS function can be used to perform basic membership checks on array data structures. The ARRAY\_CONTAINS function is useful when you need to check if a specific value is present within an array.

## Syntax
<a name="array_contains-syntax"></a>

```
array_contains(array, value)
```

## Arguments
<a name="array_contains-arguments"></a>

 *array*
An ARRAY to be searched.

 *value*
An expression with a type sharing a least common type with the array elements.

## Return type
<a name="array_contains-return-type"></a>

The ARRAY\_CONTAINS function returns a BOOLEAN.

If value is NULL, the result is NULL.

If any element in array is NULL, the result is NULL if value is not matched to any other element.

## Examples
<a name="array_contains-example"></a>

The following example checks if the array `[1, 2, 3]` contains the value `4`. Since the array `[1, 2, 3`] doesn't contain the value `4`, the array\_contains function returns `false`.

```
SELECT array_contains(array(1, 2, 3), 4)
false
```

The following example checks if the array `[1, 2, 3]` contains the value `2`. Since the array `[1, 2, 3]` does contain the value `2`, the array\_contains function returns `true`.

```
SELECT array_contains(array(1, 2, 3), 2);
 true
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
