---
source_url: https://docs.aws.amazon.com/r53recovery/latest/dg/quotas.region-switch.html
---

# Quotas for Region switch
<a name="quotas.region-switch"></a>

Region switch in Amazon Application Recovery Controller (ARC) is subject to the following quotas.

| Entity | Quota |
| --- | --- |
| Number of plans per account | 10<br />You can [ request a quota increase](https://console.aws.amazon.com/servicequotas/home?region=us-east-1#!/services/arc-region-switch/quotas). |
| Number of execution blocks per plan | 100 |
| Number of parallel execution blocks per step | 20 |
| Number of CloudWatch alarms per trigger condition | 10 |
| Number of Route 53 health check execution blocks per plan | 25 |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Application Recovery Controller. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query r53recovery` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
