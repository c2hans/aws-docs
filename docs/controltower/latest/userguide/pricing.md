---
source_url: https://docs.aws.amazon.com/controltower/latest/userguide/pricing.html
---

# Pricing
<a name="pricing"></a>

No additional charge exists for using AWS Control Tower. You only pay for the AWS services enabled by AWS Control Tower, and the services you use in your landing zone. For example, you pay for Service Catalog for provisioning accounts with Account Factory, and AWS CloudTrail for events tracked in your landing zone. For information about the pricing and fees associated with AWS Control Tower, see [AWS Control Tower pricing](https://aws.amazon.com/controltower/pricing).

If you are running ephemeral workloads from accounts in AWS Control Tower, you may see an increase in costs associated with AWS Config. For details, see [AWS Config pricing](https://aws.amazon.com/config/pricing). Contact your AWS account representative for more specific information about managing these costs. To learn more about how AWS Config works with AWS Control Tower, see [Monitor resource changes with AWS Config](monitoring-with-config.md).

If you implement AWS CloudTrail trails outside of AWS Control Tower, you can use them with AWS Control Tower. However, you may incur duplicate charges, if you also opt in to trails managed by AWS Control Tower. We do not recommend setting up external trails, unless you have a specific requirement. If you choose to opt in during landing zone setup or update, AWS Control Tower sets up and activates an organization-level CloudTrail trail for you in the management account. For information about managing CloudTrail costs, see [Managing CloudTrail costs](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-trail-manage-costs.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Control Tower. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query controltower` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
