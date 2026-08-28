---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-rule-view.html
---

# View AWS Client VPN authorization rules
<a name="cvpn-working-rule-view"></a>

You can view authorization rules for a specific Client VPN endpoint using the console and the AWS CLI.

**To view authorization rules (console)**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Client VPN Endpoints**.

1. Select the Client VPN endpoint for which to view authorization rules and choose **Authorization rules**.

**To view authorization rules (AWS CLI)**
Use the [describe-client-vpn-authorization-rules](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-client-vpn-authorization-rules.html) command.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS VPN. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
