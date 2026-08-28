---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/DAYOFMONTH.html
---

# DAYOFMONTH function
<a name="DAYOFMONTH"></a>

The DAYOFMONTH function returns the day of month of the date/timestamp (a value between 1 and 31, depending on the month and year).

The DAYOFMONTH function is similar to the DAY function, but they have slightly different names and slightly different behavior. The DAY function is more commonly used, but the DAYOFMONTH function can be used as an alternative. This type of query can be useful when you need to perform date-based analysis or filtering on a table that contains date or timestamp data, such as extracting specific components of a date for further processing or reporting.

## Syntax
<a name="DAYOFMONTH-syntax"></a>

```
dayofmonth(date)
```

## Arguments
<a name="DAYOFMONTH-arguments"></a>

*date*
A DATE or TIMESTAMP expression.

## Returns
<a name="DAYOFMONTH-returns"></a>

The DAYOFMONTH function returns an INTEGER.

## Example
<a name="DAYOFMONTH-example"></a>

The following example extracts the day of the month (`30`) from the input date `'2009-07-30'`.

```
SELECT dayofmonth('2009-07-30');
 30
```

The following example applies the DAYOFMONTH function to the `birthday` column of the `squirrels` table. For each row in the `squirrels` table, the day of the month from the `birthday` column will be extracted and returned as the output of the SELECT statement. The output of this query will be a list of day values, one for each row in the `squirrels` table, representing the day of the month for each squirrel's birthday.

```
SELECT dayofmonth(birthday) FROM squirrels
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
