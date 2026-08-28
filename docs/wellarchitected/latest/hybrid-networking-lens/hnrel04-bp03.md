---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnrel04-bp03.html
---

# HNREL04-BP03 Use dynamic routing for automatic failover
<a name="hnrel04-bp03"></a>

 Implement dynamically routing for dedicated connections and IPSec VPN connections using BGP to enable automatic load balancing and failover across redundant links.

 **Desired outcome:** Ensure seamless failover and traffic distribution across all available network paths, minimizing downtime and manual intervention.

 **Level of risk exposed if this best practice is not established:** High

 **Benefits of establishing this best practice:**
+  Enables automatic failover in the event of a connection failure
+  Balances network traffic for optimal performance
+  Reduces manual intervention and operational overhead
+  Increases resilience of hybrid connectivity

## Implementation guidance
<a name="implementation-guidance-35"></a>
+  Use BGP for dynamic routing between on-premises and cloud networks.
+  Regularly validate routing and failover with controlled tests.

## Resources
<a name="resources-28"></a>
+  [BGP Negotiation over AWS Site-to-Site VPN and Direct Connect: Troubleshooting Strategies for Efficient Networking](https://repost.aws/articles/ARIKYhXEYyQQqtO2ulKERrbw/bgp-negotiation-over-aws-site-to-site-vpn-and-direct-connect-troubleshooting-strategies-for-efficient-networking)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
