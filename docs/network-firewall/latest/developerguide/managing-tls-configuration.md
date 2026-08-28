---
source_url: https://docs.aws.amazon.com/network-firewall/latest/developerguide/managing-tls-configuration.html
---

# Managing your TLS inspection configuration in Network Firewall
<a name="managing-tls-configuration"></a>

This section describes how to create, update, and delete a TLS inspection configuration in Network Firewall. To turn on TLS inspection for your firewall, create a TLS inspection configuration, add the TLS inspection configuration to a firewall policy, then associate the firewall policy with your firewall.

You can only add a TLS inspection configuration to a new policy, not to an existing policy. However, you can replace an existing TLS inspection configuration with another TLS inspection configuration in a firewall policy. To add a TLS inspection configuration to a firewall policy or update an existing TLS inspection configuration, see [Managing your firewall policy](firewall-policy-managing.md).

**Note**
A TLS inspection configuration is only available for use by the account that you use to create it. It can't be shared across accounts.

**Topics**
+ [Creating a TLS inspection configuration in Network Firewall](creating-tls-configuration.md)
+ [Updating a TLS inspection configuration in Network Firewall](updating-tls-configuration.md)
+ [Deleting a TLS inspection configuration in Network Firewall](deleting-tls-configuration.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Network Firewall. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query network-firewall` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
