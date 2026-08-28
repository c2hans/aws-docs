---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/Datetime_types-timestamp_LTZ.html
---

# TIMESTAMP\_LTZ
<a name="Datetime_types-timestamp_LTZ"></a>

Use the TIMESTAMP\_LTZ data type to store complete timestamp values that include the date, the time of day, and the local time zone.

TIMESTAMP represents values comprising values of fields `year`, `month`, `day`, `hour`, `minute`, and `second`, with the session local timezone. The `timestamp` value represents an absolute point in time.

TIMESTAMP in Spark is a user-specified alias associated with one of the TIMESTAMP\_LTZ and TIMESTAMP\_NTZ variations. You can set the default timestamp type as TIMESTAMP\_LTZ (default value) or TIMESTAMP\_NTZ via the configuration `spark.sql.timestampType`.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
