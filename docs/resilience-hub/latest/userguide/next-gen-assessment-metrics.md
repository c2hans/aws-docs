---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/userguide/next-gen-assessment-metrics.html
---

# Assessment metrics
<a name="next-gen-assessment-metrics"></a>

The following metrics are emitted after each successful failure mode assessment. One data point is published per policy component that has assessment results.

| Metric | Dimensions | Description | Values |
| --- | --- | --- | --- |
| PolicyAchievable | Service, PolicyComponent=AvailabilitySlo | Whether your availability SLO target is achievable. | 1.0 or 0.0 |
| PolicyAchievable | Service, PolicyComponent=MultiAzRtoRpo | Whether your multi-AZ RTO and RPO targets are achievable. | 1.0 or 0.0 |
| PolicyAchievable | Service, PolicyComponent=MultiRegionRtoRpo | Whether your multi-Region RTO and RPO targets are achievable. | 1.0 or 0.0 |

The following table describes the metric dimensions.

| Dimension | Description |
| --- | --- |
| Service | The name of the service being assessed. |
| PolicyComponent | The resilience policy component being evaluated. Possible values: AvailabilitySlo, MultiAzRtoRpo, MultiRegionRtoRpo. |

**Note**
Only policy components for which the assessment produces an achievability result are emitted.

Use the `Minimum` statistic when creating alarms on this metric. A `Minimum` of 0.0 indicates that at least one assessment found the policy not achievable during the evaluation period.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
