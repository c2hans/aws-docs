---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/Examples_with_datetime_types.html
---

# Examples with datetime types
<a name="Examples_with_datetime_types"></a>

The following examples show you how to work with datetime types that are supported by AWS Clean Rooms.

## Date examples
<a name="Examples_with_datetime_types-date-examples"></a>

The following examples insert dates that have different formats and display the output.

```
select * from datetable order by 1;

start_date |  end_date
-----------------------
2008-06-01 | 2008-12-31
2008-06-01 | 2008-12-31
```

If you insert a timestamp value into a DATE column, the time portion is ignored and only the date is loaded.

## Time examples
<a name="Examples_with_datetime_types-time-examples"></a>

The following examples insert TIME and TIMETZ values that have different formats and display the output.

```
select * from timetable order by 1;
start_time |  end_time
------------------------
 19:11:19  | 20:41:19+00
 19:11:19  | 20:41:19+00
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
