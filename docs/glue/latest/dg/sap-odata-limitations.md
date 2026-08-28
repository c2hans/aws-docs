---
source_url: https://docs.aws.amazon.com/glue/latest/dg/sap-odata-limitations.html
---

# Limitations / Callouts
<a name="sap-odata-limitations"></a>
+ ODP entities are not compatible with Record Based Partitioning since pagination is handled using skip token/delta token. Consequently, for Record Based Partitioning, the default value for maxConcurrency is set to "null" irrespective of the user input.
+ When both limit and partition is applied, the limit takes precedence over partitioning.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
