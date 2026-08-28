---
source_url: https://docs.aws.amazon.com/directconnect/latest/UserGuide/encryption-in-transit.html
---

# Encryption in AWS Direct Connect
<a name="encryption-in-transit"></a>

AWS Direct Connect does not encrypt your traffic that is in transit by default. To encrypt the data in transit that traverses AWS Direct Connect, you must use the transit encryption options for that service. To learn about EC2 instance traffic encryption, see [Encryption in Transit](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/data-protection.html#encryption-transit) in the Amazon EC2 User Guide.

With AWS Direct Connect and AWS Site-to-Site VPN, you can combine one or more AWS Direct Connect dedicated network connections with the Amazon VPC VPN. This combination provides an IPsec-encrypted private connection that also reduces network costs, increases bandwidth throughput, and provides a more consistent network experience than internet-based VPN connections. For more information, see [Amazon VPC-to-Amazon VPC Connectivity Options](https://aws.amazon.com/answers/networking/aws-single-data-center-ha-network-connectivity/).

MAC Security (MACsec) is an IEEE standard that provides data confidentiality, data integrity, and data origin authenticity. You can use Direct Connect connections that support MACsec to encrypt your data from your corporate data center to the Direct Connect location. For more information, see [MAC Security in Direct Connect](MACsec.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Direct Connect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query directconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
