---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/scheduled-queries-best-practices.html
---

# Best practices
<a name="scheduled-queries-best-practices"></a>

Follow these best practices to ensure reliable and efficient scheduled query operations:

**Query optimization**
+ Test queries manually before scheduling to verify performance and results
+ Use filter indexes early in your query to reduce data processing
+ Limit time ranges to avoid timeouts with high-volume log groups
+ Consider query complexity and execution time limits

**Schedule planning**
+ Avoid overlapping executions by ensuring queries complete before the next scheduled run
+ Consider log ingestion delays when setting time ranges
+ Use cron expressions for specific times
+ Spread out the schedules to ensure you do not hit query concurrency limit

**Monitoring and maintenance**
+ Monitor execution history regularly to identify failures or performance issues
+ Review and update IAM roles periodically to maintain security
+ Test destination accessibility before deploying to production

**Authorization**
+ All the APIs for scheduled query authorize on the scheduled query resource and not on the resources it takes in the input like log groups. Set up IAM policies accordingly
+ Manage authorization of log groups using the execution role passed in the APIs

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
