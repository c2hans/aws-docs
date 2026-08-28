---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/MONTH.html
---

# MONTH function
<a name="MONTH"></a>

The MONTH function is a time extraction function that takes a time or timestamp as input and returns the month component (a value between 0 and 12).

## Syntax
<a name="MONTH-syntax"></a>

```
month(date)
```

## Arguments
<a name="MONTH-arguments"></a>

*date*
A TIMESTAMP expression or a STRING of a valid timestamp format.

## Returns
<a name="MONTH-returns"></a>

The MONTH function returns an INTEGER.

## Example
<a name="MONTH-example"></a>

The following example extracts the month component (`7`) from the input timestamp `'2016-07-30'`.

```
SELECT month('2016-07-30');
 7
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
