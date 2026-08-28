---
source_url: https://docs.aws.amazon.com/timestream/latest/developerguide/best-practices.html
---

For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com/timestream/latest/developerguide/timestream-for-influxdb.html).

# Best practices
<a name="best-practices"></a>

 To fully realize the benefits of the Amazon Timestream for LiveAnalytics, follow the best practices described below.

**Note**
When running proof-of-concept applications, consider the amount of data your application will accumulate over a few months or years while evaluating the performance and scale of Timestream for LiveAnalytics. As your data grows over time, you'll notice that the performance of Timestream for LiveAnalytics remains mostly unchanged because its serverless architecture can leverage massive amounts of parallelism for processing larger data volumes and automatically scale to match needs of your application.

**Topics**
+ [Data modeling](data-modeling.md)
+ [Security](security-bp.md)
+ [Configuring Amazon Timestream for LiveAnalytics](configuration.md)
+ [Writes](data-ingest.md)
+ [Queries](queries-bp.md)
+ [Scheduled queries](scheduledqueries-bp.md)
+ [Client applications and supported integrations](client-integrations.md)
+ [General](general.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Timestream. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query timestream` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
