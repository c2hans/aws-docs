---
source_url: https://docs.aws.amazon.com/vpc/latest/tgw/view-tgw-domain-association.html
---

# View multicast domain associations in AWS Transit Gateway
<a name="view-tgw-domain-association"></a>

View your multicast domains to verify that they are available, and that they contain the appropriate subnets and attachments.

**To view a multicast domain using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. On the navigation pane, choose **Transit Gateway Multicast**.

1. Select the multicast domain.

1. Choose the **Associations** tab.

**To view a multicast domain using the AWS CLI**
Use the [describe-transit-gateway-multicast-domains](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-transit-gateway-multicast-domains.html) command.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon VPC. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpc` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
