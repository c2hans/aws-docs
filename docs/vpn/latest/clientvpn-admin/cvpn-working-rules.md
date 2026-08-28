---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-rules.html
---

# AWS Client VPN authorization rules
<a name="cvpn-working-rules"></a>

Authorization rules act as ﬁrewall rules that grant access to networks. By adding authorization rules, you grant specific clients access to the specified network. You should have an authorization rule for each network you want to grant access to. You can add authorization rules to a Client VPN endpoint using the console and the AWS CLI.

**Note**
Client VPN uses longest prefix matching when evaluating authorization rules. See the troubleshooting topic [Troubleshooting AWS Client VPN: Authorization rules for Active Directory groups not working as expected](ad-group-auth-rules.md) and [Route priority](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html#route-tables-priority) in the *Amazon VPC User Guide* for more details.

## Key points for understanding authorization rules
<a name="key-points-summary"></a>

The following points explain some of the behavior of authorization rules:
+ To allow access to a destination network, an authorization rule must be explicitly added. The default behavior is to deny access.
+ You cannot add an authorization rule to *restrict* access to a destination network.
+ The `0.0.0.0/0` CIDR is handled as a special case. It is processed last, regardless of the order in which the authorization rules were created.
+ The `0.0.0.0/0` CIDR can be thought of as "any destination," or "any destination not defined by other authorization rules."
+ The longest prefix match is the rule that takes precedence.

**Topics**
+ [Key points](#key-points-summary)
+ [Example scenarios](#auth-rule-example-scenarios)
+ [Add an authorization rule](cvpn-working-rule-authorize-add.md)
+ [Remove an authorization rule](cvpn-working-rule-remove.md)
+ [View authorization rules](cvpn-working-rule-view.md)

## Example scenarios for Client VPN authorization rules
<a name="auth-rule-example-scenarios"></a>

This section describes how authorization rules work for AWS Client VPN. It includes key points for understanding authorization rules, an example architecture, and discussion of example scenarios that map to the example architecture.

**Scenarios**
+ [Example architecture for authorization rule scenarios](#example-arch-auth-rules)
+ [Access to a single destination](#auth-rules1)
+ [Use any destination (0.0.0.0/0) CIDR](#auth-rules2)
+ [Longer IP prefix match](#auth-rules3)
+ [Overlapping CIDR (same group)](#auth-rules4)
+ [Additional 0.0.0.0/0 rule](#auth-rules5)
+ [Add a rule for 192.168.0.0/24](#auth-rules6)
+ [SAML federated authentication](#auth-rules7)
+ [Access for all user groups](#auth-rules8)

### Example architecture for authorization rule scenarios
<a name="example-arch-auth-rules"></a>

The following diagram shows the example architecture that is used for the example scenarios found in this section.

![Example Client VPN architecture](http://docs.aws.amazon.com/vpn/latest/clientvpn-admin/images/cvpn-auth-rules.png)

### Access to a single destination
<a name="auth-rules1"></a>

| Rule description | Group ID | Allow access to all users | Destination CIDR |
| --- | --- | --- | --- |
| Provide engineering group access to on-premises network | S-xxxxx14 | False | 172.16.0.0/24 |
| Provide development group access to development VPC | S-xxxxx15 | False | 10.0.0.0/16 |
| Provide manager group access to Client VPN VPC | S-xxxxx16 | False | 192.168.0.0/24 |

**Resulting behavior**
+ The engineering group can access only `172.16.0.0/24`.
+ The development group can access only `10.0.0.0/16`.
+ The manager group can access only `192.168.0.0/24`.
+ All other traffic is dropped by the Client VPN endpoint.

**Note**
In this scenario, no user group has access to the public internet.

### Use any destination (0.0.0.0/0) CIDR
<a name="auth-rules2"></a>

| Rule description | Group ID | Allow access to all users | Destination CIDR |
| --- | --- | --- | --- |
| Provide engineering group access to on-premises network | S-xxxxx14 | False | 172.16.0.0/24 |
| Provide development group access to development VPC | S-xxxxx15 | False | 10.0.0.0/16 |
| Provide manager group access to any destination | S-xxxxx16 | False | 0.0.0.0/0 |

**Resulting behavior**
+ The engineering group can access only `172.16.0.0/24`.
+ The development group can access only `10.0.0.0/16`.
+ The manager group can access the public internet *and* `192.168.0.0/24`, but cannot access `172.16.0.0/24` or `10.0.0/16`.

**Note**
In this scenario, because no rules are referencing `192.168.0.0/24`, access to that network is also provided by the `0.0.0.0/0` rule.
A rule containing `0.0.0.0/0` is always evaluated last regardless of the order in which the rules were created. Because of this, keep in mind that the rules evaluated before `0.0.0.0/0` play a role in determining which networks `0.0.0.0/0` grants access to.

### Longer IP prefix match
<a name="auth-rules3"></a>

| Rule description | Group ID | Allow access to all users | Destination CIDR |
| --- | --- | --- | --- |
| Provide engineering group access to on-premises network | S-xxxxx14 | False | 172.16.0.0/24 |
| Provide development group access to development VPC | S-xxxxx15 | False | 10.0.0.0/16 |
| Provide manager group access to any destination | S-xxxxx16 | False | 0.0.0.0/0 |
| Provide manager group access to a single host in development VPC | S-xxxxx16 | False | 10.0.2.119/32 |

**Resulting behavior**
+ The engineering group can access only `172.16.0.0/24`.
+ The development group can access `10.0.0.0/16`, *except* for the single host `10.0.2.119/32`.
+ The manager group can access the public internet, `192.168.0.0/24`, and a single host (`10.0.2.119/32`) within the development VPC, but does not have access to `172.16.0.0/24` or any of the remaining hosts in the development VPC.

**Note**
Here you see how a rule with a longer IP prefix takes precedence over a rule with a shorter IP prefix. If you want the development group to have access to `10.0.2.119/32`, an additional rule granting the development team access to `10.0.2.119/32` needs to be added.

### Overlapping CIDR (same group)
<a name="auth-rules4"></a>

| Rule description | Group ID | Allow access to all users | Destination CIDR |
| --- | --- | --- | --- |
| Provide engineering group access to on-premises network | S-xxxxx14 | False | 172.16.0.0/24 |
| Provide development group access to development VPC | S-xxxxx15 | False | 10.0.0.0/16 |
| Provide manager group access to any destination | S-xxxxx16 | False | 0.0.0.0/0 |
| Provide manager group access to single host in development VPC | S-xxxxx16 | False | 10.0.2.119/32 |
| Provide engineering group access to a smaller subnet within on-premises network | S-xxxxx14 | False | 172.16.0.128/25 |

**Resulting behavior**
+ The development group can access `10.0.0.0/16`, *except* for the single host `10.0.2.119/32`.
+ The manager group can access the public internet, `192.168.0.0/24`, and a single host (`10.0.2.119/32`) within the `10.0.0.0/16` network, but does not have access to `172.16.0.0/24` or any of the remaining hosts in the `10.0.0.0/16` network.
+ The engineering group has access to `172.16.0.0/24`, including the more specific subnet `172.16.0.128/25`.

### Additional 0.0.0.0/0 rule
<a name="auth-rules5"></a>

| Rule description | Group ID | Allow access to all users | Destination CIDR |
| --- | --- | --- | --- |
| Provide engineering group access to on-premises network | S-xxxxx14 | False | 172.16.0.0/24 |
| Provide development group access to development VPC | S-xxxxx15 | False | 10.0.0.0/16 |
| Provide manager group access to any destination | S-xxxxx16 | False | 0.0.0.0/0 |
| Provide manager group access to single host in development VPC | S-xxxxx16 | False | 10.0.2.119/32 |
| Provide engineering group access to a smaller subnet within on-premises network | S-xxxxx14 | False | 172.16.0.128/25 |
| Provide engineering group access to any destination | S-xxxxx14 | False | 0.0.0.0/0 |

**Resulting behavior**
+ The development group can access `10.0.0.0/16`, *except* for the single host `10.0.2.119/32`.
+ The manager group can access the public internet, `192.168.0.0/24`, and a single host (`10.0.2.119/32`) within the `10.0.0.0/16` network, but does not have access to `172.16.0.0/24` or any of the remaining hosts in the `10.0.0.0/16` network.
+ The engineering group can access the public internet, `192.168.0.0/24`, and `172.16.0.0/24`, including the more specific subnet `172.16.0.128/25`.

**Note**
Notice that both the engineering and manager groups can now access `192.168.0.0/24`. This is because both groups have access to `0.0.0.0/0` (any destination) *and* no other rules are referencing `192.168.0.0/24`.

### Add a rule for 192.168.0.0/24
<a name="auth-rules6"></a>

| Rule description | Group ID | Allow access to all users | Destination CIDR |
| --- | --- | --- | --- |
| Provide engineering group access to on-premises network | S-xxxxx14 | False | 172.16.0.0/24 |
| Provide development group access to development VPC | S-xxxxx15 | False | 10.0.0.0/16 |
| Provide manager group access to any destination | S-xxxxx16 | False | 0.0.0.0/0 |
| Provide manager group access to single host in development VPC | S-xxxxx16 | False | 10.0.2.119/32 |
| Provide engineering group access to a subnet in the on-premises network | S-xxxxx14 | False | 172.16.0.128/25 |
| Provide engineering group access to any destination | S-xxxxx14 | False | 0.0.0.0/0 |
| Provide manager group access to Client VPN VPC | S-xxxxx16 | False | 192.168.0.0/24 |

**Resulting behavior**
+ The development group can access `10.0.0.0/16`, *except* for the single host `10.0.2.119/32`.
+ The manager group can access the public internet, `192.168.0.0/24`, and a single host (`10.0.2.119/32`) within the `10.0.0.0/16` network, but does not have access to `172.16.0.0/24` or any of the remaining hosts in the `10.0.0.0/16` network.
+ The engineering group can access the public internet, `172.16.0.0/24`, and `172.16.0.128/25`.

**Note**
Notice how adding the rule for the manager group to access `192.168.0.0/24` results in the development group no longer having access to that destination network.

### SAML federated authentication
<a name="auth-rules7"></a>

| Rule description | Group ID | Allow access to all users | Destination CIDR |
| --- | --- | --- | --- |
| Provide engineering group access to on-premises network | Engineering | False | 172.16.0.0/24 |
| Provide development group access to development VPC | Developers | False | 10.0.0.0/16 |
| Provide manager group access to Client VPN VPC | Managers | False | 192.168.0.0/24 |

**Resulting behavior**
+ Users authenticated via SAML with the "Engineering" group attribute can access only `172.16.0.0/24`.
+ Users authenticated via SAML with the "Developers" group attribute can access only `10.0.0.0/16`.
+ Users authenticated via SAML with the "Managers" group attribute can access only `192.168.0.0/24`.
+ All other traffic is dropped by the Client VPN endpoint.

**Note**
When using SAML federated authentication, the Group ID field corresponds to the SAML attribute value that identifies the user's group membership. This attribute is configured in your SAML identity provider and passed to Client VPN during authentication.

### Access for all user groups
<a name="auth-rules8"></a>

| Rule description | Group ID | Allow access to all users | Destination CIDR |
| --- | --- | --- | --- |
| Provide engineering group access to on-premises network | S-xxxxx14 | False | 172.16.0.0/24 |
| Provide development group access to development VPC | S-xxxxx15 | False | 10.0.0.0/16 |
| Provide manager group access to any destination | S-xxxxx16 | False | 0.0.0.0/0 |
| Provide manager group access to single host in development VPC | S-xxxxx16 | False | 10.0.2.119/32 |
| Provide engineering group access to a subnet in the on-premises network | S-xxxxx14 | False | 172.16.0.128/25 |
| Provide engineering group access to all networks | S-xxxxx14 | False | 0.0.0.0/0 |
| Provide manager group access to Client VPN VPC | S-xxxxx16 | False | 192.168.0.0/24 |
| Provide access to all groups | N/A | True | 0.0.0.0/0 |

**Resulting behavior**
+ The development group can access `10.0.0.0/16`, *except* for the single host `10.0.2.119/32`.
+ The manager group can access the public internet, `192.168.0.0/24`, and a single host (`10.0.2.119/32`) within the `10.0.0.0/16` network, but does not have access to `172.16.0.0/24` or any of the remaining hosts in the `10.0.0.0/16` network.
+ The engineering group can access the public internet, `172.16.0.0/24`, and `172.16.0.128/25`.
+ Any other user group, for example "admin group," can access the public internet, but not any other destination networks defined in the other rules.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS VPN. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
