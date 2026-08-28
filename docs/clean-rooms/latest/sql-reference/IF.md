---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/IF.html
---

# IF expression
<a name="IF"></a>

The IF conditional function returns one of two values based on a condition.

This function is a common control flow statement used in SQL to make decisions and return different values based on the evaluation of a condition. It's useful for implementing simple if-else logic within a query.

## Syntax
<a name="IF-syntax"></a>

```
if(expr1, expr2, expr3)
```

## Arguments
<a name="IF-arguments"></a>

*expr1*
The condition or expression that is evaluated. If it is `true`, the function will return the value of *expr2*. If *expr1* is `false`, the function will return the value of *expr3*.

*expr2*
The expression that is evaluated and returned if *expr1* is `true`.

*expr3*
The expression that is evaluated and returned if *expr1* is `false`.

## Returns
<a name="IF-returns"></a>

If `expr1` evaluates to `true`, then returns `expr2`; otherwise returns `expr3`.

## Example
<a name="IF-example"></a>

The following example uses the `if()` function to return one of two values based on a condition. The condition being evaluated is `1 < 2`, which is `true`, so the first value `'a'` is returned.

```
SELECT if(1 < 2, 'a', 'b');
 a]
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
