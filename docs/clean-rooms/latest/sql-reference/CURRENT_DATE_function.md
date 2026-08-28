---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/CURRENT_DATE_function.html
---

# CURRENT\_DATE function
<a name="CURRENT_DATE_function"></a>

CURRENT\_DATE returns a date in the current session time zone (UTC by default) in the default format: YYYY-MM-DD.

**Note**
CURRENT\_DATE returns the start date for the current transaction, not for the start of the current statement. Consider the scenario where you start a transaction containing multiple statements on 10/01/08 23:59, and the statement containing CURRENT\_DATE runs at 10/02/08 00:00. CURRENT\_DATE returns `10/01/08`, not `10/02/08`.

## Syntax
<a name="CURRENT_DATE_function-syntax"></a>

```
CURRENT_DATE
```

## Return type
<a name="CURRENT_DATE_function-return-type"></a>

DATE

## Example
<a name="CURRENT_DATE_function-examples"></a>

The following example returns the current date (in the AWS Region where the function runs).

```
select current_date;

   date
------------
2008-10-01
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
