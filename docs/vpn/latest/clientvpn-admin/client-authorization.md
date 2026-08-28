---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/client-authorization.html
---

# Client authorization in AWS Client VPN
<a name="client-authorization"></a>

Client VPN supports two types of client authorization: security groups and network-based authorization (using authorization rules).

## Security groups
<a name="security-groups"></a>

When you create a Client VPN endpoint, you can specify the security groups from a specific VPC to apply to the Client VPN endpoint. When you associate a subnet with a Client VPN endpoint, we automatically apply the VPC's default security group. You can change the security groups after you create the Client VPN endpoint. For more information, see [Apply a security group to a target network in AWS Client VPN](cvpn-working-target-apply.md). The security groups are associated with the Client VPN network interfaces.

You can enable Client VPN users to access your applications in a VPC by adding a rule to your applications' security groups to allow traffic from the security group that was applied to the association.

Conversely, you can restrict access for Client VPN users by not specifying the security group that was applied to the association, or by removing the rule that references the Client VPN endpoint security group. The security group rules that you require might also depend on the kind of VPN access that you want to configure. For more information, see [Scenarios and examples for Client VPN](how-it-works.md#scenario).

For more information about security groups, see [Security groups for your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html) in the *Amazon VPC User Guide*.

## Network-based authorization
<a name="auth-rules"></a>

Network-based authorization is implemented using authorization rules. For each network that you want to enable access, you must configure authorization rules that limit the users who have access. For a specified network, you configure the Active Directory group or the SAML-based IdP group that is allowed access. Only users who belong to the specified group can access the specified network. If you are not using Active Directory or SAML-based federated authentication, or you want to open access to all users, you can specify a rule that grants access to all clients. For more information, see [AWS Client VPN authorization rules](cvpn-working-rules.md).

**Topics**
+ [Security groups](#security-groups)
+ [Network-based authorization](#auth-rules)
+ [Create an endpoint security group rule](client-auth-rule-create.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS VPN. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
