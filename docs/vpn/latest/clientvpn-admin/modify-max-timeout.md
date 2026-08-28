---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/modify-max-timeout.html
---

# Modify the maximum AWS Client VPN session duration and timeout behavior
<a name="modify-max-timeout"></a>

Use the following steps to modify an existing Client VPN maximum VPN session duration and change the disconnect on session timeout behavior.

**Modify an existing maximum VPN session duration for a Client VPN endpoint (console)**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Client VPN endpoints**.

1. Select the Client VPN endpoint that you want to modify, choose **Actions**, and then choose **Modify Client VPN Endpoint**.

1. For **Session timeout hours**, choose the desired maximum VPN session duration time in hours.

1. For **Disconnect on session timeout**, choose if you want to disconnect a session when the maximum session timeout is reached. By default, this is turned off the first time you modify an endpoint.

1. Choose **Modify Client VPN endpoint**.

**Modify an existing maximum VPN session duration for a Client VPN endpoint (AWS CLI)**
Use the [modify-client-vpn-endpoint](https://docs.aws.amazon.com/cli/latest/reference/ec2/modify-client-vpn-endpoint.html) command.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS VPN. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
