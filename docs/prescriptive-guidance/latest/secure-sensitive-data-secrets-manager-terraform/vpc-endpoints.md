---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/secure-sensitive-data-secrets-manager-terraform/vpc-endpoints.html
---

# Using VPC endpoints to keep sensitive data in known networks
<a name="vpc-endpoints"></a>

Secrets should never be accessible over the internet. AWS offers options for maintaining privacy when routing traffic through known and private network routes.

When you're configuring traffic between AWS Secrets Manager and on-premises clients and applications, you can use either of the following approaches:
+ An [AWS Site-to-Site VPN VPN](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html) connection
+ An [AWS Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html) connection

If you want to secure traffic between Secrets Manager and API clients with the same AWS Region, use [AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/what-is-privatelink.html) to create interface VPC endpoints. By using this option, you keep all traffic for the secret within your private network. For more information, see [Using an AWS Secrets Manager VPC endpoint](https://docs.aws.amazon.com/secretsmanager/latest/userguide/vpc-endpoint-overview.html).

![Using Amazon VPC service endpoints to connect to AWS Secrets Manager.](http://docs.aws.amazon.com/prescriptive-guidance/latest/secure-sensitive-data-secrets-manager-terraform/images/guide-img/e6185df2-3707-4018-a94c-6edc793f0353/images/17a0b502-f720-4d25-a0a2-795b565c6524.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
