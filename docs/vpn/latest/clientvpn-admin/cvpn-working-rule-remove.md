---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-rule-remove.html
---

# Remove an authorization rule from an AWS Client VPN endpoint
<a name="cvpn-working-rule-remove"></a>

You can remove authorization rules for a specific Client VPN endpoint using the console and the AWS CLI.

**To remove authorization rules (console)**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Client VPN Endpoints**.

1. Select the Client VPN endpoint for which to which the authorization rule was added, and then choose **Authorization rules**.

1. Select the authorization rule to delete, choose **Remove authorization rule**, and then choose **Remove authorization rule **again to confirm the deletion.

**To remove authorization rules (AWS CLI)**
Use the [revoke-client-vpn-ingress](https://docs.aws.amazon.com/cli/latest/reference/ec2/revoke-client-vpn-ingress.html) command.
