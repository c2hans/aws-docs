---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/YEAR.html
---

# YEAR function
<a name="YEAR"></a>

The YEAR function is a date extraction function that takes a date or timestamp as input and returns the year component (a four-digit number).

## Syntax
<a name="YEAR-syntax"></a>

```
year(date)
```

## Arguments
<a name="YEAR-arguments"></a>

*date*
A DATE or TIMESTAMP expression.

## Returns
<a name="YEAR-returns"></a>

The YEAR function returns an INTEGER.

## Example
<a name="YEAR-example"></a>

The following example extracts the year component (`2016`) from the input date `'2016-07-30'`.

```
SELECT year('2016-07-30');
 2016
```

The following example extracts the year component from the `birthday` column of the `squirrels` table and returns the results as the output of the SELECT statement. The output of this query will be a list of year values, one for each row in the `squirrels` table, representing the year of each squirrel's birthday.

```
SELECT year(birthday) FROM squirrels
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
