---
source_url: https://docs.aws.amazon.com/vpn/latest/s2svpn/rotate-vpn-certificate.html
---

# Rotate AWS Site-to-Site VPN tunnel endpoint certificates
<a name="rotate-vpn-certificate"></a>

You can rotate the certificates on the tunnel endpoints on the AWS side by using the Amazon VPC console. When a tunnel endpoint’s certificate is close to expiration, AWS automatically rotates the certificate using the service-linked role. For more information, see [Service-linked roles for Site-to-Site VPN](security_iam_service-with-iam.md#security_iam_service-with-iam-roles-service-linked).

**To rotate the Site-to-Site VPN tunnel endpoint certificate using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Site-to-Site VPN connections**.

1. Select the Site-to-Site VPN connection, and then choose **Actions**, **Modify VPN tunnel certificate**.

1. Select the tunnel endpoint.

1. Choose **Save**.

**To rotate the Site-to-Site VPN tunnel endpoint certificate using the AWS CLI**
Use the [modify-vpn-tunnel-certificate](https://docs.aws.amazon.com/cli/latest/reference/ec2/modify-vpn-tunnel-certificate.html) command.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS VPN. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
