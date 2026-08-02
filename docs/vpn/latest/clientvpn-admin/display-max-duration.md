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
