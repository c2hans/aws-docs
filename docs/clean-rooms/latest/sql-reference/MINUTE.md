---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/MINUTE.html
---

# MINUTE function
<a name="MINUTE"></a>

The MINUTE function is a time extraction function that takes a time or timestamp as input and returns the minute component (a value between 0 and 60).

## Syntax
<a name="MINUTE-syntax"></a>

```
minute(timestamp)
```

## Arguments
<a name="MINUTE-arguments"></a>

*timestamp*
A TIMESTAMP expression or a STRING of a valid timestamp format.

## Returns
<a name="MINUTE-returns"></a>

The MINUTE function returns an INTEGER.

## Example
<a name="MINUTE-example"></a>

The following example extracts the minute component (`58`) from the input timestamp `'2009-07-30 12:58:59'`.

```
SELECT minute('2009-07-30 12:58:59');
 58
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
