---
source_url: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/hosted-zone-private-associate-vpcs.html
---

# Associating more VPCs with a private hosted zone
<a name="hosted-zone-private-associate-vpcs"></a>

You can use the Amazon Route 53 console to associate more VPCs with a private hosted zone if you created the hosted zone and the VPCs by using the same AWS account.

**Important**
If you want to associate VPCs that you created by using one account with a private hosted zone that you created by using a different account, you first must authorize the association. In addition, you can't use the AWS console either to authorize the association or associate the VPCs with the hosted zone. For more information, see [Associating an Amazon VPC and a private hosted zone that you created with different AWS accounts](hosted-zone-private-associate-vpcs-different-accounts.md).

For information about how to associate more VPCs with a private hosted zone using the Route 53 API, see [AssociateVPCWithHostedZone](https://docs.aws.amazon.com/Route53/latest/APIReference/API_AssociateVPCWithHostedZone.html) in the *Amazon Route 53 API Reference*.

**To associate additional VPCs with a private hosted zone using the Route 53 console**

1. Sign in to the AWS Management Console and open the Route 53 console at [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/).

1. In the navigation pane, choose **Hosted zones**.

1. Choose the radio button for the private hosted zone that you want to associate more VPCs with.

1. Choose **Edit**.

1. Choose **Add VPC**.

1. Choose the Region and the ID of the VPC that you want to associate with this hosted zone.

1. To associate more VPCs with this hosted zone, repeat steps 5 and 6.

1. Choose **Save changes**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
