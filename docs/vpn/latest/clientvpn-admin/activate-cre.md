---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/activate-cre.html
---

# Activate Client Route Enforcement for an AWS Client VPN endpoint
<a name="activate-cre"></a>

You can activate Client Route Enforcement on existing Client VPN endpoints using either the console or the AWS CLI.

**To activate Client Route Enforcement using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Client VPN endpoints**.

1. Choose the Client VPN endpoint that you want to modify, choose **Actions**, and then choose **Modify Client VPN endpoint**.

1. Scroll down the page to the **Other parameters** section.

1. Turn on **Client Route Enforcement**.

1. Choose **Modify Client VPN endpoint**.

**To activate Client Route Enforcement using the AWS CLI)**
+ Use the [modify-client-vpn-endpoint](https://docs.aws.amazon.com/cli/latest/reference/ec2/modify-client-vpn-endpoint.html) command.
