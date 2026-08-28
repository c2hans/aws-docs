---
source_url: https://docs.aws.amazon.com/solutions/latest/media2cloud-on-aws/amazon-dynamodb.html
---

# Amazon DynamoDB
<a name="amazon-dynamodb"></a>

 The solution deploys the following Amazon DynamoDB tables which are configured to use on-demand capacity and encryption at rest using Server-Side Encryption (SSE).
+  A table to store ingestion information
+  A table to store machine learning metadata
+  A table to temporarily store state machine run tokens that are used internally to communicate back to specific state machine runs
+  A table to temporarily store service backlog requests, an internal queue management system to support large number of AI requests

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Media2Cloud on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
