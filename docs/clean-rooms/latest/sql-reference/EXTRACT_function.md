---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/EXTRACT_function.html
---

# EXTRACT function
<a name="EXTRACT_function"></a>

The EXTRACT function returns a date or time part from a TIMESTAMP, TIMESTAMPTZ, TIME, or TIMETZ value. Examples include a day, month, year, hour, minute, second, millisecond, or microsecond from a timestamp.

## Syntax
<a name="EXTRACT_function-synopsis"></a>

```
EXTRACT(datepart FROM source)
```

## Arguments
<a name="EXTRACT_function-arguments"></a>

 *datepart*
The subfield of a date or time to extract, such as a day, month, year, hour, minute, second, millisecond, or microsecond. For possible values, see [Date parts for date or timestamp functions](Dateparts_for_datetime_functions.md).

 *source*
A column or expression that evaluates to a data type of TIMESTAMP, TIMESTAMPTZ, TIME, or TIMETZ.

## Return type
<a name="EXTRACT_function-return-type"></a>

INTEGER if the *source* value evaluates to data type TIMESTAMP, TIME, or TIMETZ.

DOUBLE PRECISION if the *source* value evaluates to data type TIMESTAMPTZ.

## Examples with TIME
<a name="EXTRACT_function-examples-time"></a>

The following example table TIME\_TEST has a column TIME\_VAL (type TIME) with three values inserted.

```
select time_val from time_test;

time_val
---------------------
20:00:00
00:00:00.5550
00:58:00
```

The following example extracts the minutes from each time\_val.

```
select extract(minute from time_val) as minutes from time_test;

minutes
-----------
         0
         0
         58
```

The following example extracts the hours from each time\_val.

```
select extract(hour from time_val) as hours from time_test;

hours
-----------
         20
         0
         0
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
