---
source_url: https://docs.aws.amazon.com/vpc/latest/network-access-analyzer/network-access-analyzer-limits.html
---

# Quotas and considerations for Network Access Analyzer
<a name="network-access-analyzer-limits"></a>

Your AWS account has default quotas, formerly referred to as limits, for each AWS service. You can request increases for some quotas, but not for all quotas.

To view the quotas for Network Access Analyzer, open the [Service Quotas console](https://console.aws.amazon.com/servicequotas/home). In the navigation pane, choose **AWS services**, and then select **Network Insights**. To request a quota increase, see [Requesting a quota increase](https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html) in the *Service Quotas User Guide*.

Your AWS account has the following quotas related to Network Access Analyzer.

| Name | Default | Adjustable |
| --- | --- | --- |
| Access scopes | 1,000 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/networkinsights/quotas/L-72DF2E0E) |
| Access scope analyses | 10,000 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/networkinsights/quotas/L-06B98CB1) |
| Concurrent access scope analyses | 25 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/networkinsights/quotas/L-2AC9F231) |
| Findings per scope analysis | 10,000 | No |

## Analysis runtime
<a name="run-timeout"></a>

All network interfaces in the account and Region are included in every analysis. The running analysis times out after 4 hours.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Virtual Private Cloud. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpc` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
