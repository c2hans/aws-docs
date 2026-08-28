---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/IS_NOT_NULL.html
---

# IS\_NOT\_NULL expression
<a name="IS_NOT_NULL"></a>

The IS\_NOT\_NULL conditional expression is used to check if a value is not null.

This expression is a synonym for IS NOT NULL.

## Syntax
<a name="IS_NOT_NULL-syntax"></a>

```
is_not_null(expr)
```

## Arguments
<a name="IS_NOT_NULL-arguments"></a>

*expr*
An expression of any type.

## Returns
<a name="IS_NOT_NULL-returns"></a>

The IS\_NOT\_NULL conditional expression returns a Boolean. If `expr1` is not NULL, returns `true`, otherwise returns `false`.

## Examples
<a name="IS_NOT_NULL-example"></a>

The following example checks if the value `1` is not null, and returns the boolean result `true` because 1 is a valid, non-null value.

```
SELECT is not null(1);
 true
```

The following example selects the `id` column from the `squirrels` table, but only for the rows where the age column is not `null`.

```
SELECT id FROM squirrels WHERE is_not_null(age)
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
