---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/limits.html
---

# AWS Client VPN quotas
<a name="limits"></a>

Your AWS account has the following quotas, formerly referred to as limits, related to Client VPN endpoints. Unless otherwise noted, each quota is Region-specific. You can request increases for some quotas, and other quotas cannot be increased.

To request a quota increase for an adjustable quota, choose **Yes** in the **Adjustable** column. For more information, see [Requesting a quota increase](https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html) in the *Service Quotas User Guide*.

## Client VPN quotas
<a name="quotas-endpoints"></a>

| Name | Default | Adjustable |
| --- | --- | --- |
| Authorization rules per Client VPN endpoint | 200 For dual-stack endpoints, this limit is shared between IPv4 and IPv6 routes. | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-9A1BC94B) |
| Client VPN endpoints per Region | 5 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-8EA77D34) |
| Concurrent client connections per Client VPN endpoint | This value depends on the number of subnet associations per endpoint.+  1 – 7,000 <br />+  2 – 36,500 <br />+  3 – 66,500 <br />+  4 – 96,500 <br />+  5 – 126,000 <br />For dual-stack endpoints, this limit is shared between IPv4 and IPv6 connections. | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-C4B238BF) |
| Concurrent operations per Client VPN endpoint † | 10 | No |
| Entries in a client certificate revocation list for Client VPN endpoints | 20,000 | No |
| Routes per Client VPN target network association | 100 For dual-stack endpoints, this limit is shared between IPv4 and IPv6 routes. | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-401D78F7) |

† Operations include:
+ Associate or disassociate subnets
+ Create or delete security groups

## Users and groups quotas
<a name="quotas-users-groups"></a>

When you configure users and groups for Active Directory or a SAML-based IdP, the following quotas apply:
+ Users can belong to a maximum of 200 groups. We ignore any groups after the 200th group.
+ The maximum length for the group ID is 255 characters.
+ The maximum length for the name ID is 255 characters. We truncate characters after the 255th character.

## General considerations
<a name="quotas-general"></a>

Take the following into consideration when you use Client VPN endpoints:
+ If you use Active Directory to authenticate the user, the Client VPN endpoint must belong to the same account as the AWS Directory Service resource used for Active Directory authentication.
+ If you use SAML-based federated authentication to authenticate a user, the Client VPN endpoint must belong to the same account as the IAM SAML identity provider that you create to define the IdP to AWS trust relationship. The IAM SAML identity provider can be shared across multiple Client VPN endpoints in the same AWS account.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS VPN. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
