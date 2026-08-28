---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/CARDINALITY.html
---

# CARDINALITY function
<a name="CARDINALITY"></a>

The CARDINALITY function returns the size of an ARRAY or MAP expression (*expr*).

This function is useful to find the size or length of an array.

## Syntax
<a name="CARDINALITY-syntax"></a>

```
cardinality(expr)
```

## Arguments
<a name="CARDINALITY-arguments"></a>

 *expr*
An ARRAY or MAP expression.

## Returns
<a name="CARDINALITY-returns"></a>

Returns the size of an array or a map (INTEGER).

The function returns `NULL` for null input if `sizeOfNull` is set to `false` or `enabled` is set to `true`.

Otherwise, the function returns `-1` for null input. With the default settings, the function returns `-1` for null input.

## Example
<a name="CARDINALITY-example"></a>

The following query calculates the cardinality, or the number of elements, in the given array. The array (`'b', 'd', 'c', 'a'`) has 4 elements, so the output of this query would be `4`.

```
SELECT cardinality(array('b', 'd', 'c', 'a'));
 4
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
