---
source_url: https://docs.aws.amazon.com/glue/latest/dg/stripe-limitations.html
---

# Limitations
<a name="stripe-limitations"></a>

The following are limitations for the Stripe connector:
+  Only Field Based Partitioning supported by connector.
+  Record Based Partitioning not supported by connector, no provision to retrieve the total count of records.
+  Primary key datatype is String, so Id Based Partitioning does not support by connector.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
