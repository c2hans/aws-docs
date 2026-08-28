---
source_url: https://docs.aws.amazon.com/whitepapers/latest/genomics-data-transfer-analytics-and-machine-learning/appendix-i-monitoring-secondary-analysis-workflow-status-cost-and-performance.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Appendix I: Monitoring secondary analysis workflow status, cost, and performance
<a name="appendix-i-monitoring-secondary-analysis-workflow-status-cost-and-performance"></a>

 Monitoring and alerting are an important part of operational excellence. Both AWS Step Functions and AWS Batch produce a variety of operational metrics and events to monitor secondary analysis status and performance and alert you if there is an issue requiring remediation.

 First, establish a baseline of activity for your secondary analysis workflow and then set alarms that will notify personnel if secondary analysis behavior is outside of established baselines. At a minimum, monitor the Step Functions metrics—`ActivitiesStarted`, `ActivitiesTimedOut`, `ExecutionsStarted`, and `ExecutionsTimedOut`. The [AWS Solutions Implementation](https://aws.amazon.com/solutions/implementations/genomics-secondary-analysis-using-aws-step-functions-and-aws-batch) provides an Amazon CloudWatch dashboard that plots these metrics over time and provides counter widgets for each one. This dashboard can be used for monitoring your secondary analysis workflows and for establishing a workflow performance baseline. Step Functions also provides events for `ExecutionFailed`, `ExecutionTimedOut`, and `ExecutionAborted` so that you can create CloudWatch alarms that notify personnel when either of these events take place. CloudWatch alarms can be configured to send an email or publish to a Simple Notification Service (Amazon SNS) topic, notifying subscribers of the issue.

 To monitor cost over time, tag your tasks in your Step Functions state machine so that you can track them in AWS Cost Explorer. AWS Cost Explorer helps you track costs over time and compute an average cost per sample metric for a given secondary analysis workflow type, by tag. As of the date of this publication, Spot Instances costs cannot be associated with a given container instance in a compute environment. Job costs can be averaged in AWS Cost Explorer by tag.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
