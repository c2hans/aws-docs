---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/display-login-banner.html
---

# View a currently configured AWS Client VPN login banner
<a name="display-login-banner"></a>

Use the following steps to view a currently configured Client VPN client login banner.

**View current login banner for a Client VPN endpoint (console)**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Client VPN Endpoints**.

1. Select the Client VPN endpoint that you want to view.

1. Verify that the **Details** tab is selected.

1. View the currently configured login banner text next to **Client login banner text**.

**View currently configured login banner for a Client VPN endpoint (AWS CLI)**
Use the [describe-client-vpn-endpoints](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-client-vpn-endpoints.html) command.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS VPN. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
