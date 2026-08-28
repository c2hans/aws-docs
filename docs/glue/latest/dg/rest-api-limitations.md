---
source_url: https://docs.aws.amazon.com/glue/latest/dg/rest-api-limitations.html
---

# Limitations
<a name="rest-api-limitations"></a>

The following are limitations for the REST API connector
+  REST API connector is only available through the AWS API, CLI, or SDK. You cannot configure REST connectors through the console.
+  The AWS Glue REST ConnectionType can only be configured to READ data from the REST API-based data source. The connection can only be used as a SOURCE in AWS Glue ETL jobs.
+  The connector does not support field selection.
+  The connector does not support JSON POST body filtering. Use query parameter or filter string modes instead.
+  The filter configuration model cannot express complex native query languages that require entity-dependent branching.
+  The connector does not support custom partition logic (such as primary key partitioning) through configuration.
+  The connector does not support custom proxies or custom certificates for VPC REST connections.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
