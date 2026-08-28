---
source_url: https://docs.aws.amazon.com/whitepapers/latest/microservices-on-aws/other-options-for-analysis.html
---

# Other options for analysis
<a name="other-options-for-analysis"></a>

 For further log analysis, Amazon Redshift, a fully-managed data warehouse service, and [Quick](https://aws.amazon.com/quicksight/), a scalable business intelligence service, offer effective solutions. QuickSight provides easy connectivity to various AWS data services such as Redshift, RDS, Aurora, EMR, DynamoDB, Amazon S3, and Kinesis, simplifying data access.

 CloudWatch Logs can stream log entries to Amazon Data Firehose, a service for delivering real-time streaming data. QuickSight then uses the data stored in Redshift for comprehensive analysis, reporting, and visualization.

![Diagram showing log analysis with Amazon Redshift and Quick](http://docs.aws.amazon.com/whitepapers/latest/microservices-on-aws/images/log-analysis-redshift-quicksight.png)

 Moreover, when logs are stored in S3 buckets, an object storage service, the data can be loaded into services like Redshift or EMR, a cloud-based big data platform, allowing for thorough analysis of the stored log data.

![Diagram showing streamlining log analysis: From AWS services to QuickSight](http://docs.aws.amazon.com/whitepapers/latest/microservices-on-aws/images/streamlining-log-analysis.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
