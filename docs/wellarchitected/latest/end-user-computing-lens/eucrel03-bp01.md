---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucrel03-bp01.html
---

# EUCREL03-BP01 Add redundancy to networking connections
<a name="eucrel03-bp01"></a>

 Use a redundant networking architecture for Amazon WorkSpaces and WorkSpaces Applications, incorporating multiple Active Directory (AD) Controllers, AD connectors, DNS servers, gateways, VPNs, or AWS Direct Connect links. This approach supports continuous connectivity by providing alternative pathways for network traffic, reducing the risk of service disruptions due to network incidents and enhancing overall system resilience. Redundant networking helps mitigate the impact of network failures and supports uninterrupted access to WorkSpaces environments.

**Level of risk exposed if this best practice is not established:**High

## Implementation guidance
<a name="implementation-guidance-41"></a>

 Enhance the resilience of Amazon WorkSpaces and WorkSpaces Applications by configuring redundant networking components such as VPN connections or AWS Direct Connect links. This setup provides alternative paths for network traffic, mitigating the impact of network incidents and supporting continuous access to WorkSpaces environments. Verify that you have multiple AD controllers and connectors across multiple Availability Zones.

 Additionally, regularly monitor and test the redundant networking setup to check its effectiveness in maintaining continuous connectivity. Conduct failover tests and simulations to validate the redundancy configuration and identify any potential areas for improvement. By implementing redundant networking architecture, you can strengthen the resilience of your EUC environment and reduce the risk of downtime caused by network disruptions.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
