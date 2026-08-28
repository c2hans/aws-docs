---
source_url: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/hosted-zone-private-disassociate-vpcs.html
---

# Disassociating VPCs from a private hosted zone
<a name="hosted-zone-private-disassociate-vpcs"></a>

You can use the Amazon Route 53 console to disassociate VPCs from a private hosted zone. This causes Route 53 to stop routing traffic using records in the hosted zone for DNS queries that originate in the VPC. For example, if the example.com hosted zone is associated with a VPC and you disassociate the hosted zone from that VPC, Route 53 stops resolving DNS queries for example.com or any of the other records in the example.com hosted zone.

**Note**
You can't disassociate the last VPC from a private hosted zone. If you want to disassociate that VPC, you must first associate another VPC with the hosted zone.

**To disassociate VPCs from a private hosted zone**

1. Sign in to the AWS Management Console and open the Route 53 console at [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/).

1. In the navigation pane, choose **Hosted zones**.

1. Choose the radio button for the private hosted zone that you want to disassociate one or more VPCs from.

1. Choose **Edit**.

1. Choose **Remove VPC** next to the VPC that you want to disassociate from this hosted zone.

1. Choose **Save changes**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
