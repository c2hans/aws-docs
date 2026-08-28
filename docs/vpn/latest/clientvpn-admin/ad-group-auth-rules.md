---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/ad-group-auth-rules.html
---

# Troubleshooting AWS Client VPN: Authorization rules for Active Directory groups not working as expected
<a name="ad-group-auth-rules"></a>

**Problem**
I have configured authorization rules for my Active Directory groups, but they are not working as I expected. I have added an authorization rule for `0.0.0.0/0` to authorize traffic for all networks, but traffic still fails for specific destination CIDRs.

**Cause**
Authorization rules are indexed on network CIDRs. Authorization rules must grant Active Directory groups access to specific network CIDRs. Authorization rules for `0.0.0.0/0` are handled as a special case, and are therefore evaluated last, regardless of the order in which the authorization rules are created.

For example, say that you create five authorization rules in the following order:
+ Rule 1: Group 1 access to `10.1.0.0/16`
+ Rule 2: Group 1 access to `0.0.0.0/0`
+ Rule 3: Group 2 access to `0.0.0.0/0`
+ Rule 4: Group 3 access to `0.0.0.0/0`
+ Rule 5: Group 2 access to `172.131.0.0/16`

In this example, Rule 2, Rule 3, and Rule 4 are evaluated last. Group 1 has access to `10.1.0.0/16` only, and Group 2 has access to `172.131.0.0/16` only. Group 3 does not have access to `10.1.0.0/16` or `172.131.0.0/16`, but it has access to all other networks. If you remove Rules 1 and 5, all three groups have access to all networks.

Client VPN uses longest prefix matching when evaluating authorization rules. See [Route priority](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html#route-tables-priority) in the *Amazon VPC User Guide* for more details.

**Solution**
Verify that you create authorization rules that explicitly grant Active Directory groups access to specific network CIDRs. If you add an authorization rule for `0.0.0.0/0`, keep in mind that it will be evaluated last, and that previous authorization rules may limit the networks to which it grants access.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS VPN. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
