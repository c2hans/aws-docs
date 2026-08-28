---
source_url: https://docs.aws.amazon.com/timestream/latest/developerguide/comparison-operators.html
---

For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com/timestream/latest/developerguide/timestream-for-influxdb.html).

# Comparison operators
<a name="comparison-operators"></a>

Timestream for LiveAnalytics supports the following comparison operators.

| Operator | Description |
| --- | --- |
| < | Less than |
| > | Greater than |
| <= | Less than or equal to |
| >= | Greater than or equal to |
| = | Equal |
| <> | Not equal |
| \!= | Not equal |

**Note**
The `BETWEEN` operator tests if a value is within a specified range. The syntax is as follows:

  ```
  BETWEEN min AND max
  ```
The presence of `NULL` in a `BETWEEN` or `NOT BETWEEN` statement will result in the statement evaluating to `NULL`.
`IS NULL `and `IS NOT NULL` operators test whether a value is null (undefined). Using `NULL` with `IS NULL` evaluates to true.
In SQL, a `NULL` value signifies an unknown value.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Timestream. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query timestream` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
