---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/telco-lens/telcosec03.html
---

# External interface security
<a name="telcosec03"></a>

| TELCOSEC03: How do you maintain security on the external interfaces of your telco network? |
| --- |
|   |

 Telecom networks expose critical functionality through external interfaces that include APIs, control plane protocols, and data traffic. Maintaining robust security across these access points is essential to block unauthorized access and protect the network's integrity. This question explores how the organization implements security controls and updates mitigation measures to verify only authorized systems can interact with the network's external touchpoints.

**Topics**
+ [TELCOSEC03-BP01 Secure the APIs used to expose telco network functionality](telcosec03-bp01.md)
+ [TELSEC03-BP02 Deploy signaling firewall on the roaming and interconnecting interfaces with other telco networks](telsec03-bp02.md)
+ [TELSEC03-BP03 Perform regular penetration testing on each of the protocols implemented on the signaling layer](telsec03-bp03.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
