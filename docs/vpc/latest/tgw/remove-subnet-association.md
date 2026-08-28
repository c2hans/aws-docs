---
source_url: https://docs.aws.amazon.com/vpc/latest/tgw/remove-subnet-association.html
---

# Disassociate a subnet from a multicast domain in AWS Transit Gateway
<a name="remove-subnet-association"></a>

Use the following procedure to disassociate subnets from a multicast domain.

**To disassociate subnets using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. On the navigation pane, choose **Transit Gateway Multicast**.

1. Select the multicast domain.

1. Choose the **Associations** tab.

1. Select the subnet, and then choose **Actions**, **Delete association**.

**To disassociate subnets using the AWS CLI**
Use the [disassociate-transit-gateway-multicast-domain](https://docs.aws.amazon.com/cli/latest/reference/ec2/disassociate-transit-gateway-multicast-domain.html) command.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon VPC. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpc` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
