---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advcost04-bp01.html
---

# ADVCOST04-BP01 Consider lower cost storage for older User Profile data
<a name="advcost04-bp01"></a>

 As the 30 most recent days are most relevant, using DynamoDB can prioritize high performance for the most relevant data (typically within the last 30 days), and archiving to Amazon S3 can reduce costs for less relevant data.

 **For S3 profile data:**
+  Enable S3 Intelligent-Tiering on your bucket
+  Configure lifecycle policies to transition older data
+  Set up monitoring to track access patterns

1.  **For DynamoDB:**
   +  Implement TTL for old profile records
   +  Create export jobs to move historical data to S3
   +  Use S3 Lifecycle policies for long-term archival

 **Cost optimization best practices**
+  Regularly analyze data access patterns
+  Use AWS Cost Explorer to track storage expenses
+  Consider object size and retrieval frequency
+  Implement tagging for better cost tracking

## Key AWS services
<a name="key-aws-services-48"></a>
+  DynamoDB
+  S3
+  Intelligent Tiering

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
