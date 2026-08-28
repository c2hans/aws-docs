---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/array.html
---

# ARRAY function
<a name="array"></a>

Creates an array with the given elements.

## Syntax
<a name="array-synopsis"></a>

```
ARRAY( [ expr1 ] [ , expr2 [ , ... ] ] )
```

## Argument
<a name="array-argument"></a>

 *expr1, expr2*
Expressions of any data type except date and time types. The arguments don't need to be of the same data type.

## Return type
<a name="array-return-type"></a>

The array function returns an ARRAY with the elements in the expression.

## Example
<a name="array-example"></a>

The following example shows an array of numeric values and an array of different data types.

```
--an array of numeric values
select array(1,50,null,100);
      array
------------------
 [1,50,null,100]
(1 row)

--an array of different data types
select array(1,'abc',true,3.14);
        array
-----------------------
 [1,"abc",true,3.14]
(1 row)
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
