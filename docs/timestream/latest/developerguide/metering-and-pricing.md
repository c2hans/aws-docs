---
source_url: https://docs.aws.amazon.com/timestream/latest/developerguide/metering-and-pricing.html
---

For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com/timestream/latest/developerguide/timestream-for-influxdb.html).

# Metering and cost optimization
<a name="metering-and-pricing"></a>

With Amazon Timestream for LiveAnalytics, you pay only for what you use. Timestream for LiveAnalytics meters separately for writes, data stored, and data scanned by queries. The price of each metering dimension is specified on the [pricing page](https://aws.amazon.com/timestream/pricing/). You can estimate your monthly bill using the [Amazon Timestream for LiveAnalytics Pricing Calculator](samples/Amazon_Timestream_Pricing_Calculator.zip).

This section describes how metering works for writes, storage and queries in Timestream for LiveAnalytics. Example scenarios and calculations are also provided. In addition, a list of best practices for cost optimization is included. You can select a topic below:

**Topics**
+ [Writes](metering-and-pricing.writes.md)
+ [Storage](metering-and-pricing.storage.md)
+ [Queries](metering-and-pricing.queries.md)
+ [Cost optimization](metering-and-pricing.cost-optimization.md)
+ [Monitoring with Amazon CloudWatch](monitoring-cloudwatch.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Timestream. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query timestream` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
