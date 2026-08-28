---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/security-best-practices.html
---

# Security best practices for AWS Client VPN
<a name="security-best-practices"></a>

AWS Client VPN provides a number of security features to consider as you develop and implement your own security policies. The following best practices are general guidelines and don’t represent a complete security solution. Because these best practices might not be appropriate or sufficient for your environment, treat them as helpful considerations rather than prescriptions.

**Authorization rules**
Use authorization rules to restrict which users can access your network. For more information, see [Authorization rules](cvpn-working-rules.md).

**Security groups**
Use security groups to control which resources users can access in your VPC. For more information, see [Security groups](client-authorization.md#security-groups).

**Client certificate revocation lists**
Use client certificate revocation lists to revoke access to a Client VPN endpoint for specific client certificates. For example, when a user leaves your organization. For more information, see [Client certificate revocation lists](cvpn-working-certificates.md).

**Disconnect on session timeout**
Disconnect a session when the maximum Client VPN session time is reached, enforcing a maximum VPN session duration. For more information, see [Maximum VPN session duration](cvpn-working-max-duration.md).

**Monitoring tools**
Use monitoring tools to keep track of availability and performance of your Client VPN endpoints. For more information, see [Monitoring Client VPN](monitoring-overview.md).

**Identity and access management**
Manage access to Client VPN resources and APIs by using IAM policies for your IAM users and IAM roles. For more information, see [Identity and access management for AWS Client VPN](security-iam.md).

**Use the AWS provided VPN client**
Use the AWS provided client for AWS Client VPN, available from the [AWS Client VPN download page](https://aws.amazon.com/vpn/client-vpn-download/).

**Use the exported client configuration**
Use the client configuration file exported from your AWS Client VPN endpoint. For more information, see [Export the client configuration file](export-client-config-file.md). Do not modify the cipher or TLS settings in the configuration file. AWS Client VPN endpoints only support the following algorithms:
+ TLS 1.3: `TLS_AES_256_GCM_SHA384` and `TLS_AES_128_GCM_SHA256`
+ TLS 1.2: `TLS-ECDHE-RSA-WITH-AES-256-GCM-SHA384`, `TLS-ECDHE-RSA-WITH-AES-128-GCM-SHA256`, `TLS-ECDHE-ECDSA-WITH-AES-256-GCM-SHA384`, and `TLS-ECDHE-ECDSA-WITH-AES-128-GCM-SHA256`
+ Data channel: `AES-256-GCM`

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS VPN. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
