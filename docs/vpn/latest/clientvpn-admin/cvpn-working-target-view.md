---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-target-view.html
---

# View AWS Client VPN target networks
<a name="cvpn-working-target-view"></a>

You can view the targets associated with a Client VPN endpoint using the console or the AWS CLI.

**To view target networks (console)**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Client VPN Endpoints**.

1. Select the appropriate Client VPN endpoint and choose **Target network associations**.

**To view target networks using the AWS CLI**
Use the [describe-client-vpn-target-networks](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-client-vpn-target-networks.html) command.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS VPN. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
