---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/disable-login-banner.html
---

# Deactivate a client login banner for an existing AWS Client VPN endpoint
<a name="disable-login-banner"></a>

Use the following steps to deactivate a client login banner for an existing Client VPN endpoint.

**Deactivate client login banner on a Client VPN endpoint (console)**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Client VPN Endpoints**.

1. Select the Client VPN endpoint that you want to modify, choose **Actions**, and then choose **Modify Client VPN endpoint**.

1. Scroll down the page to the **Other parameters** section.

1. Turn off **Enable client login banner?**.

1. Choose **Modify Client VPN endpoint**.

**Deactivate client login banner on a Client VPN endpoint (AWS CLI)**
Use the [modify-client-vpn-endpoint](https://docs.aws.amazon.com/cli/latest/reference/ec2/modify-client-vpn-endpoint.html) command.
