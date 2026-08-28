---
source_url: https://docs.aws.amazon.com/managed-flink/latest/java/how-table-timeattributes.html
---

# Table API time attributes
<a name="how-table-timeattributes"></a>

Each record in a data stream has several timestamps that define when events related to the record occurred:
+ **Event Time**: A user-defined timestamp that defines when the event that created the record occurred.
+ **Ingestion Time**: The time when your application retrieved the record from the data stream.
+ **Processing Time**: The time when your application processed the record.

When the Apache Flink Table API creates windows based on record times, you define which of these timestamps it uses by using the `setStreamTimeCharacteristic` method.

For more information about using timestamps with the Table API, see [ Time Attributes](https://nightlies.apache.org/flink/flink-docs-release-1.19/docs/dev/table/concepts/time_attributes/) and [ Timely Stream Processing](https://nightlies.apache.org/flink/flink-docs-release-1.19/docs/concepts/time/) in the Apache Flink Documentation.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Managed Service for Apache Flink. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managed-flink` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
