---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-certificates-export.html
---

# Export an AWS Client VPN client certificate revocation list
<a name="cvpn-working-certificates-export"></a>

You can export Client VPN client certificate revocation lists using the console and the AWS CLI.

**To export a client certificate revocation list (console)**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Client VPN Endpoints**.

1. Select the Client VPN endpoint for which to export the client certificate revocation list.

1. Choose **Actions**, choose **Export Client Certificate CRL**, and choose **Export Client Certificate CRL**.

**To export a client certificate revocation (AWS CLI)**
Use the [export-client-vpn-client-certificate-revocation-list](https://docs.aws.amazon.com/cli/latest/reference/ec2/export-client-vpn-client-certificate-revocation-list.html) command.
