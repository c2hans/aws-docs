---
source_url: https://docs.aws.amazon.com/inspector/v1/userguide/using-cloudwatch.html
---

 End of support notice: On May 20, 2026, AWS will end support for Amazon Inspector Classic. After May 20, 2026, you will no longer be able to access the Amazon Inspector Classic console or Amazon Inspector Classic resources. Amazon Inspector Classic no longer available to new accounts and accounts that have not completed an assessment in the last 6 months. For all other accounts, access will remain valid until May 20, 2026, after which you will no longer be able to access the Amazon Inspector Classic console or Amazon Inspector Classic resources. For more information, see [Amazon Inspector Classic end of support](https://docs.aws.amazon.com/inspector/v1/userguide/inspector-migration.html).

# Monitoring Amazon Inspector Classic using Amazon CloudWatch
<a name="using-cloudwatch"></a>

You can monitor Amazon Inspector Classic using Amazon CloudWatch, which collects and processes raw data into readable, near real-time metrics. By default, Amazon Inspector Classic sends metric data to CloudWatch in 5-minute periods. You can use the AWS Management Console, the AWS CLI, or an API to view the metrics that Amazon Inspector Classic sends to CloudWatch.

For more information about Amazon CloudWatch, see the [Amazon CloudWatch User Guide](http://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html).

## Amazon Inspector Classic CloudWatch metrics
<a name="inspector_metrics"></a>

The Amazon Inspector Classic namespace includes the following metrics.

**`AssessmentTargetARN` metrics:**

| Metric | Description |
| --- | --- |
| `TotalMatchingAgents` | Number of agents that match this target |
| `TotalHealthyAgents` | Number of agents that match this target that are healthy |
| `TotalAssessmentRuns` | Number of assessment runs for this target |
| `TotalAssessmentRunFindings` | Number of findings for this target |

**`AssessmentTemplateARN` metrics:**

| Metric | Description |
| --- | --- |
| `TotalMatchingAgents` | Number of agents that match this template |
| `TotalHealthyAgents` | Number of agents that match this template that are healthy |
| `TotalAssessmentRuns` | Number of assessment runs for this template |
| `TotalAssessmentRunFindings` | Number of findings for this template |

**Aggregate metrics**

| Metric | Description |
| --- | --- |
| `TotalAssessmentRuns`  | Number of assessment runs in this AWS account |
