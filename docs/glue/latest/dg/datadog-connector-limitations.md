---
source_url: https://docs.aws.amazon.com/glue/latest/dg/datadog-connector-limitations.html
---

# Limitations
<a name="datadog-connector-limitations"></a>

The following are limitations for the Datadog connector:
+ Datadog doesn’t support either field based or record based partitioning.
+ `from` is mandatory filter parameter for `Log Queries` entity.
+ `from_to_date` and `query` are mandatory filter parameters for `Metrics Timeseries` entity.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
