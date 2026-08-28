---
source_url: https://docs.aws.amazon.com/vpc/latest/tgw/sharing-identify.html
---

# Identify a shared multicast domain in AWS Transit Gateway
<a name="sharing-identify"></a>

Owners and consumers can identify shared multicast domains using the Amazon Virtual Private Cloud and AWS CLI

**To identify a shared multicast domain using the \*Amazon Virtual Private Cloud Console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Multicast Domains**.

1. Select your multicast domain.

1. On the **Transit Multicast Domain Details **page, view the **Owner ID** to identify the AWS account ID of the multicast domain.

**To identify a shared multicast domain using the AWS CLI**
Use the [describe-transit-gateway-multicast-domains](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-transit-gateway-multicast-domains.html) command. The command returns the multicast domains that you own and multicast domains that are shared with you. `OwnerId` shows the AWS account ID of the multicast domain owner.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon VPC. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpc` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
