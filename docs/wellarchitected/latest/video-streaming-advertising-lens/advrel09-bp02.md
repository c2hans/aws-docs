---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advrel09-bp02.html
---

# ADVREL09-BP02 Establish robust data collection and validation pipelines for measurement accuracy
<a name="advrel09-bp02"></a>

 Build reliable data collection and validation pipelines, emphasizing real-time monitoring, automated reconciliation, and recovery procedures to maintain measurement accuracy in advertising systems.

## Implementation guidance
<a name="implementation-guidance-advrel09-bp02"></a>
+  Implement data validation at collection points
+  Set up real-time data quality monitoring
+  Create automated data reconciliation processes
+  Configure dead letter queues for failed events
+  Implement idempotent processing for measurement events
+  Establish clear data freshness SLAs
+  Deploy automated data recovery procedures

## Key AWS services
<a name="aws-key-services-4"></a>
+  Amazon Kinesis
+  Amazon SQS
+  Amazon S3
+  AWS Glue
+  Amazon EMR

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
