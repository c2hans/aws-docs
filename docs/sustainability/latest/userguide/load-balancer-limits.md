---
source_url: https://docs.aws.amazon.com/sustainability/latest/userguide/load-balancer-limits.html
---

# Quotas for AWS Sustainability
<a name="load-balancer-limits"></a>

Your AWS account has default quotas, formerly referred to as limits, for each AWS service. Unless otherwise noted, each quota is Region-specific. You can request increases for some quotas, and other quotas cannot be increased.

To view the quotas for AWS Sustainability, open the [Service Quotas console](https://console.aws.amazon.com/servicequotas/home). In the navigation pane, choose **AWS services** and select **AWS Sustainability**.

To request a quota increase, see [Requesting a Quota Increase](https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html) in the *Service Quotas User Guide*. If the quota is not yet available in Service Quotas, use the [limit increase form](https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase).

Your AWS account has the following quotas related to AWS Sustainability.

| Name | Quota | Can be increased |
| --- | --- | --- |
| Rate of GetEstimatedCarbonEmissions request | 10 requests per second | No |
| Rate of GetEstimatedCarbonEmissionsDimensionValues request | 10 requests per second | No |
| Rate of GetEstimatedWaterAllocation request | 10 requests per second | No |
| Rate of GetEstimatedWaterAllocationDimensionValues request | 10 requests per second | No |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Sustainability. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sustainability` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
