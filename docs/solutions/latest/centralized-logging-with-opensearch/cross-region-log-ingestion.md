---
source_url: https://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/cross-region-log-ingestion.html
---

# Cross-Region log ingestion
<a name="cross-region-log-ingestion"></a>

When you deploy Centralized Logging with OpenSearch in one Region, the solution allows you to ingest service logs from another Region.

**Note**
For Amazon RDS/Aurora and AWS Lambda service logs, this feature is not supported.

The Region where the service resides is referred to as "Source Region", while the Region where the Centralized Logging with OpenSearch console is deployed as "Logging Region".

For AWS CloudTrail, you can create a new trail that sends logs into a S3 bucket in the Logging Region, and you can find the CloudTrail in the list. To learn how to create a new trail, refer to [Creating a trail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-a-trail-using-the-console-first-time.html).

For other services with logs located in S3 buckets, you can manually transfer logs (for example, using the S3 Cross-Region Replication feature) to the Logging Region S3 bucket.

You can complete the following steps to implement cross-Region log ingestion:

1. Set the service log location in another Region to be the Logging Region (such as AWS WAF), or automatically copy logs from the Source Region to the Logging Region using [Cross-Region Replication (CRR)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication-how-setup.html).

1. In the solution console, choose **AWS Service Log** in the left navigation pane, and choose **Create a pipeline**.

1. In the **Select an AWS Service** area, choose a service in the list, and choose **Next**.

1. In **Creation Method**, choose **Manual**, then enter the resource name and Amazon S3 log location parameter, and choose **Next**.

1. Change log analytics engines and log lifecycle settings, and choose **Next**.

1. Add tags if you need, and choose **Next** to create the pipeline.

Then you can use the OpenSearch dashboard or Grafana to discover logs and view dashboards.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Centralized Logging with OpenSearch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
