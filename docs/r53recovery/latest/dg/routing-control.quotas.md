---
source_url: https://docs.aws.amazon.com/r53recovery/latest/dg/routing-control.quotas.html
---

# Quotas for routing control
<a name="routing-control.quotas"></a>

Routing control in Amazon Application Recovery Controller (ARC) is subject to the following quotas (formerly referred to as limits).

| Entity | Quota |
| --- | --- |
| Number of clusters per account | 2 |
| Number of control panels per cluster | 50 |
| Number of routing controls per control panel | 100 |
| Total number of routing controls (in all control panels) per cluster | 300 |
| Number of safety rules per control panel | 20 |
| Number of routing controls per [UpdateRoutingControlStates](https://docs.aws.amazon.com/routing-control/latest/APIReference/API_UpdateRoutingControlStates.html) operation call | 10 |
| Number of mutating API calls to a cluster endpoint, per second | 3 |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Application Recovery Controller. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query r53recovery` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
