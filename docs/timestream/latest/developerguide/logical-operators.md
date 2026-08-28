---
source_url: https://docs.aws.amazon.com/timestream/latest/developerguide/logical-operators.html
---

For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com/timestream/latest/developerguide/timestream-for-influxdb.html).

# Logical operators
<a name="logical-operators"></a>

Timestream for LiveAnalytics supports the following logical operators.

| Operator | Description | Example |
| --- | --- | --- |
| AND | True if both values are true | a AND b |
| OR | True if either value is true | a OR b |
| NOT | True if the value is false | NOT a |
+ The result of an `AND` comparison may be `NULL` if one or both sides of the expression are `NULL`.
+ If at least one side of an `AND` operator is `FALSE` the expression evaluates to `FALSE`.
+ The result of an `OR` comparison may be `NULL` if one or both sides of the expression are `NULL`.
+ If at least one side of an `OR` operator is `TRUE` the expression evaluates to `TRUE`.
+ The logical complement of `NULL` is `NULL`.

The following truth table demonstrates the handling of `NULL` in `AND` and `OR`:

| A | B | A and b | A or b |
| --- | --- | --- | --- |
| null | null | null | null |
| false  | null | false | null |
| null | false | false | null |
| true | null | null | true |
| null | true | null | true |
| false | false | false | false |
| true | false | false | true |
| false | true | false | true |
| true | true | true | true |

The following truth table demonstrates the handling of NULL in NOT:

| A | Not a |
| --- | --- |
| null | null |
| true | false |
| false | true |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Timestream. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query timestream` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
