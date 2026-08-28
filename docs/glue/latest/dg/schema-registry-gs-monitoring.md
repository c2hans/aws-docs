---
source_url: https://docs.aws.amazon.com/glue/latest/dg/schema-registry-gs-monitoring.html
---

# Accessing Amazon CloudWatch metrics
<a name="schema-registry-gs-monitoring"></a>

Amazon CloudWatch metrics are available as part of CloudWatch’s free tier. You can access these metrics in the CloudWatch console. API-Level metrics include CreateSchema (Success and Latency), GetSchemaByDefinition, (Success and Latency), GetSchemaVersion (Success and Latency), RegisterSchemaVersion (Success and Latency), PutSchemaVersionMetadata (Success and Latency). Resource-level metrics include Registry.ThrottledByLimit, SchemaVersion.ThrottledByLimit, SchemaVersion.Size.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
