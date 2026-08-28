---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/display-max-duration.html
---

# View AWS Client VPN current maximum VPN session duration
<a name="display-max-duration"></a>

Use the following steps to view the current Client VPN maximum VPN session duration.

**View current maximum VPN session duration for a Client VPN endpoint (console)**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Client VPN Endpoints**.

1. Select the Client VPN endpoint that you want to view.

1. Verify that the **Details** tab is selected.

1. View the current maximum VPN session duration next to **Session timeout hours** and if **Disconnect on timeout** is enabled or disabled.

**View current maximum VPN session duration for a Client VPN endpoint (AWS CLI)**
Use the [describe-client-vpn-endpoints](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-client-vpn-endpoints.html) command.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS VPN. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
