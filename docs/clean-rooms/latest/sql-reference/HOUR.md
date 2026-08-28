---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/HOUR.html
---

# HOUR function
<a name="HOUR"></a>

The HOUR function is a time extraction function that takes a time or timestamp as input and returns the hour component (a value between 0 and 23).

This time extraction function is useful when you need to work with specific components of a time or timestamp, such as when performing time-based calculations, filtering data, or formatting time values.

## Syntax
<a name="HOUR-syntax"></a>

```
hour(timestamp)
```

## Arguments
<a name="HOUR-arguments"></a>

*timestamp*
A TIMESTAMP expression.

## Returns
<a name="HOUR-returns"></a>

The HOUR function returns an INTEGER.

## Example
<a name="HOUR-example"></a>

The following example extracts the hour component (`12`) from the input timestamp `'2009-07-30 12:58:59'`.

```
SELECT hour('2009-07-30 12:58:59');
 12
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
