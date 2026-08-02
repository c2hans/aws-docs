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
