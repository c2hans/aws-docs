---
source_url: https://docs.aws.amazon.com/keyspaces/latest/devguide/monitor-prewarming-cloudwatch.html
---

# Monitor the performance of a pre-warmed table using Amazon CloudWatch
<a name="monitor-prewarming-cloudwatch"></a>

Amazon Keyspaces pre-warming doesn't introduce new CloudWatch metrics, but you can monitor the performance of pre-warmed tables using existing Amazon Keyspaces metrics:

SuccessfulRequestLatency
Monitor this metric to verify that the pre-warmed table is handling requests with expected latency.

WriteThrottleEvents and ReadThrottleEvents
These metrics should remain low for a properly pre-warmed table. If you see insufficient capacity errors despite pre-warming, you might need to adjust your warm-throughput values.

ConsumedReadCapacityUnits and ConsumedWriteCapacityUnits
These metrics show the actual consumption of capacity, which can help validate if your pre-warming configuration is appropriate.

ProvisionedReadCapacityUnits and ProvisionedWriteCapacityUnits
For provisioned tables, these metrics show the currently allocated capacity.

These metrics can be viewed in the CloudWatch console or queried using the CloudWatch API. For more information, see [Monitoring Amazon Keyspaces with Amazon CloudWatch](monitoring-cloudwatch.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Keyspaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query keyspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
