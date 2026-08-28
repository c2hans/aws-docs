---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/dynamodb-global-tables/checklist.html
---

# Preparation checklist
<a name="checklist"></a>

Use the following checklist for decisions and tasks when you deploy global tables.
+ Determine if your use case benefits more from an MRSC or MREC consistency mode. Do you need strong consistency, even with the higher latency and other tradeoffs?
+ Determine how many and which Regions should participate in the global table. If you plan to use MRSC, decide if you want the third Region to be a replica or a witness.
+ Determine your application's [write mode](write-modes.md). (This is not the same as the consistency mode.)
+ Plan your [routing strategy](routing-strategies.md), based on your write mode.
+ Define your [evacuation plan](evacuation-processes.md#evacuate-live-region), based on your consistency mode, write mode, and routing strategy.
+ Capture metrics on the health, latency, and errors across each Region. For a list of DynamoDB metrics, see the AWS blog post [Monitoring Amazon DynamoDB for operational awareness](https://aws.amazon.com/blogs/database/monitoring-amazon-dynamodb-for-operational-awareness/). You should also use [synthetic canaries](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.html) (artificial requests designed to detect failures) as well as live observation of customer traffic. Not all issues appear in the DynamoDB metrics.
+ If you're using MREC, set alarms for any sustained increase in `ReplicationLatency`. An increase might indicate an accidental misconfiguration in which the global table has different write settings in different Regions, which leads to failed replicated requests and increased latencies. It could also indicate that there is a Regional disruption. A [good example ](https://aws.amazon.com/blogs/database/monitoring-amazon-dynamodb-for-operational-awareness/)is to generate an alert if the recent average exceeds 180,000 milliseconds. You might also watch for `ReplicationLatency` dropping to 0, which indicates stalled replication.
+ Assign sufficient maximum read and write settings for each global table.
+ Identify the conditions where you would evacuate a Region. If the decision involves human judgment, document all considerations. This work should be done carefully in advance, not under stress.
+ Maintain a runbook for every action that must take place when you evacuate a Region. Usually very little work is involved for the global tables, but moving the rest of the stack might be complex. Note: With failover procedures, it's best practice to rely only on data plane operations and not on control plane operations, because some control plane operations might be degraded during Region failures. For more information, see the AWS blog post [Build resilient applications with Amazon DynamoDB global tables: Part 4](https://aws.amazon.com/blogs/database/part-4-build-resilient-applications-with-amazon-dynamodb-global-tables/).
+ Test all aspects of the runbook periodically, including Region evacuations. An untested runbook is an unreliable runbook.
+ Consider using [AWS Resilience Hub](https://docs.aws.amazon.com/resilience-hub/latest/userguide/how-it-works.html)to evaluate the resilience of your entire application (including global tables). This service provides a comprehensive view of the resiliency status of your application portfolio through its dashboard.
+ Consider using [ARC](https://docs.aws.amazon.com/r53recovery/latest/dg/what-is-route53-recovery.html) readiness checks to evaluate the current configuration of your application and track any deviances from best practices.
+ When you write health checks for use with Route 53 or Global Accelerator, make a set of calls that cover the full database flow. If you limit your check to confirm only that the DynamoDB endpoint is up, you won't be able to cover many failure modes such as AWS Identity and Access Management (IAM) configuration errors, code deployment problems, failure in the stack outside DynamoDB, higher than average read or write latencies, and so on.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
