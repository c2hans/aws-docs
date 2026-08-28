---
source_url: https://docs.aws.amazon.com/interconnect/latest/userguide/quotas_for_aws_interconnect.html
---

# Quotas for AWS Interconnect
<a name="quotas_for_aws_interconnect"></a>

## Quotas for AWS Interconnect
<a name="load-balancer-limits"></a>

Your AWS account has default quotas, formerly referred to as limits, for each AWS service. Unless otherwise noted, each quota is Region-specific. You can request increases for some quotas, and other quotas cannot be increased.

To view the quotas for AWS Interconnect, open the [Service Quotas console](https://console.aws.amazon.com/servicequotas/home). In the navigation pane, choose **AWS services** and select **AWS Interconnect**.

To request a quota increase, see [Requesting a Quota Increase](https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html) in the *Service Quotas User Guide*. If the quota is not yet available in Service Quotas, use the [limit increase form](https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase).

Your AWS account has the following quotas related to AWS Interconnect.

| Component | Quota | Description |
| --- | --- | --- |
| Interconnect Maximum Created Connections | 10 | The maximum number of AWS Interconnect Connections allowed per account. |
| Interconnect Outstanding Requested Connections | 4 | The maximum number of AWS Interconnect Connections in the `requested` state allowed per account. |
| Multicloud Connections Per Provider | 2 | The maximum number of AWS Interconnect multicloud Connections allowed per provider per account. |
| Last Mile Connections Per Provider | 2 | The maximum number of AWS Interconnect last mile Connections allowed per provider per account. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Interconnect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query interconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
