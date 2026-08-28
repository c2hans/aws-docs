---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/TIMESTAMP.html
---

# TIMESTAMP function
<a name="TIMESTAMP"></a>

The TIMESTAMP function takes a value (typically a number) and converts it to a timestamp data type.

This function is useful when you need to convert a numeric value representing a time or date to a timestamp data type. This can be helpful when you are working with data that is stored in a numeric format, such as Unix timestamps or epoch time.

## Syntax
<a name="TIMESTAMP-syntax"></a>

```
timestamp(expr)
```

## Arguments
<a name="TIMESTAMP-arguments"></a>

*expr*
Any expression that can be cast to TIMESTAMP.

## Returns
<a name="TIMESTAMP-returns"></a>

The TIMESTAMP function returns a TIMESTAMP.

## Example
<a name="TIMESTAMP-example"></a>

The following example converts a numeric Unix timestamp (`1632416400`) to its corresponding timestamp data type: September 22, 2021 at 12:00:00 PM UTC.

```
SELECT timestamp(1632416400);
 2021-09-22 12:00:00 UTC
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
