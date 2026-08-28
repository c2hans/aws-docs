---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/array_distinct.html
---

# ARRAY\_DISTINCT function
<a name="array_distinct"></a>

The ARRAY\_DISTINCT function can be used to remove duplicate values from an array. The ARRAY\_DISTINCT function is useful when you need to remove duplicates from an array and work with only the unique elements. This can be helpful in scenarios where you want to perform operations or analyses on a dataset without the interference of repeated values.

## Syntax
<a name="array_distinct-syntax"></a>

```
array_distinct(array)
```

## Arguments
<a name="array_distinct-arguments"></a>

 *array*
An ARRAY expression.

## Return type
<a name="array_distinct-return-type"></a>

The ARRAY\_DISTINCT function returns an ARRAY that contains only the unique elements from the input array.

## Examples
<a name="array_distinct-example"></a>

In this example, the input array `[1, 2, 3, null, 3]` contains a duplicate value of `3`. The `array_distinct` function removes this duplicate value `3` and returns a new array with the unique elements: `[1, 2, 3, null]`.

```
SELECT array_distinct(array(1, 2, 3, null, 3));
 [1,2,3,null]
```

In this example, the input array `[1, 2, 2, 3, 3, 3]` contains duplicate values of `2` and `3`. The `array_distinct` function removes these duplicates and returns a new array with the unique elements: `[1, 2, 3]`.

```
SELECT array_distinct(array(1, 2, 2, 3, 3, 3))
  [1,2,3]
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
