---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/Datetime_types-TIMESTAMP_NTZ.html
---

# TIMESTAMP\_NTZ
<a name="Datetime_types-TIMESTAMP_NTZ"></a>

Use the TIMESTAMP\_NTZ data type to store complete timestamp values that include the date, the time of day, without the local time zone.

TIMESTAMP represents values comprising values of fields `year`, `month`, `day`, `hour`, `minute`, and `second`. All operations are performed without taking any time zone into account.

TIMESTAMP in Spark is a user-specified alias associated with one of the TIMESTAMP\_LTZ and TIMESTAMP\_NTZ variations. You can set the default timestamp type as TIMESTAMP\_LTZ (default value) or TIMESTAMP\_NTZ via the configuration `spark.sql.timestampType`.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
