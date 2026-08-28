---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/DAYOFYEAR.html
---

# DAYOFYEAR function
<a name="DAYOFYEAR"></a>

The DAYOFYEAR function is a date extraction function that takes a date or timestamp as input and returns the day of the year (a value between 1 and 366, depending on the year and whether it's a leap year).

This function is useful when you need to work with specific components of a date or timestamp, such as when performing date-based calculations, filtering data, or formatting date values.

## Syntax
<a name="DAYOFYEAR-syntax"></a>

```
dayofyear(date)
```

## Arguments
<a name="DAYOFYEAR-arguments"></a>

*date*
A DATE or TIMESTAMP expression.

## Returns
<a name="DAYOFYEAR-returns"></a>

The DAYOFYEAR function returns an INTEGER (between 1 and 366, depending on the year and whether it's a leap year).

## Examples
<a name="DAYOFYEAR-example"></a>

The following example extracts the day of the year (`100`) from the input date `'2016-04-09'`.

```
SELECT dayofyear('2016-04-09');
 100
```

The following example extracts the day of the year from the `birthday` column of the `squirrels` table and returns the results as the output of the SELECT statement.

```
SELECT dayofyear(birthday) FROM squirrels
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
