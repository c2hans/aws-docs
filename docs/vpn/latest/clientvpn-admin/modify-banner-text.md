---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/modify-banner-text.html
---

# Modify existing banner text on a AWS Client VPN endpoint
<a name="modify-banner-text"></a>

Use the following steps to modify existing text on a Client VPN client login banner.

**Modify existing banner text on a Client VPN endpoint (console)**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Client VPN Endpoints**.

1. Select the Client VPN endpoint that you want to modify, choose **Actions**, and then choose **Modify Client VPN endpoint**.

1. For **Enable client login banner?**, verify that it's turned on.

1. For **Client login banner text**, replace the existing text with new text that you want displayed in a banner on AWS provided clients when a VPN session is established. Use UTF-8 encoded characters only, with a maximum of 1400 characters.

1. Choose **Modify Client VPN endpoint**.

**Modify client login banner on a Client VPN endpoint (AWS CLI)**
Use the [modify-client-vpn-endpoint](https://docs.aws.amazon.com/cli/latest/reference/ec2/modify-client-vpn-endpoint.html) command.
