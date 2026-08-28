---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/flatten.html
---

# FLATTEN function
<a name="flatten"></a>

The FLATTEN function is used to "flatten" a nested array structure into a single flat array.

## Syntax
<a name="flatten-syntax"></a>

```
flatten(arrayOfArrays)
```

## Arguments
<a name="flatten-arguments"></a>

 *arrayOfArrays*
An array of arrays.

## Return type
<a name="flatten-return-type"></a>

The FLATTEN function returns an array.

## Example
<a name="flatten-example"></a>

In this example, the input is a nested array with two inner arrays, and the output is a single flat array containing all the elements from the inner arrays. The FLATTEN function takes the nested array `[[1, 2], [3, 4]]` and combines all the elements into a single array `[1, 2, 3, 4]`.

```
SELECT flatten(array(array(1, 2), array(3, 4)));
 [1,2,3,4]
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
