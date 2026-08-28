---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/TO_TIMESTAMP.html
---

# TO\_TIMESTAMP function
<a name="TO_TIMESTAMP"></a>

TO\_TIMESTAMP converts a TIMESTAMP string to TIMESTAMPTZ.

## Syntax
<a name="TO_TIMESTAMP-syntax"></a>

```
to_timestamp (timestamp)
```

```
to_timestamp (timestamp, format)
```

## Arguments
<a name="TO_TIMESTAMP-arguments"></a>

*timestamp*
A timestamp string or a data type that can be cast into a timestamp string.

*format*
A string literal that matches Spark's datetime patterns. For valid datetime patterns, see [Datetime Patterns for Formatting and Parsing](https://spark.apache.org/docs/latest/sql-ref-datetime-pattern.html).

## Return type
<a name="TO_TIMESTAMP-return-type"></a>

TIMESTAMP

## Examples
<a name="TO_TIMESTAMP-examples"></a>

The following example demonstrates using the TO\_TIMESTAMP function to convert a TIMESTAMP string to a TIMESTAMP.

```
select current_timestamp() as timestamp, to_timestamp( current_timestamp(), 'YYYY-MM-DD HH24:MI:SS') as second;

timestamp                  | second
--------------------------   ----------------------
2021-04-05 19:27:53.281812 | 2021-04-05 19:27:53+00
```

It's possible to pass TO\_TIMESTAMP part of a date. The remaining date parts are set to default values. The time is included in the output:

```
SELECT TO_TIMESTAMP('2017','YYYY');

to_timestamp
--------------------------
2017-01-01 00:00:00+00
```

The following SQL statement converts the string '2011-12-18 24:38:15' to a TIMESTAMP. The result is a TIMESTAMP that falls on the next day because the number of hours is more than 24 hours:

```
select to_timestamp('2011-12-18 24:38:15', 'YYYY-MM-DD HH24:MI:SS');

to_timestamp
----------------------
2011-12-19 00:38:15+00
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
