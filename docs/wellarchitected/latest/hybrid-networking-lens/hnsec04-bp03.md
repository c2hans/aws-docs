---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnsec04-bp03.html
---

# HNSEC04-BP03 Implement network traffic security inspection
<a name="hnsec04-bp03"></a>

 Network traffic security inspection provides a layered security approach to ensure traffic between your cloud and on-premises resources is properly monitored and protected against threats.

 **Desired outcome:** Deploy inspection and security enforcement on ingress and egress network paths as needed.

 **Level of risk exposed if this best practice is not established:** High

 **Benefits of establishing this best practice:**
+  Enables deep packet inspection
+  Provides scalable firewall for hybrid network traffic
+  Enables advanced rule sets for protocol, domain, and threat filtering
+  Simplifies compliance with perimeter defense requirements

## Implementation guidance
<a name="implementation-guidance-19"></a>
+  Route traffic through the firewall appliances
+  Define and maintain firewall rule groups for hybrid traffic.
+  Monitor firewall activity and adapt rules as threats evolve.

## Resources
<a name="resources-18"></a>
+  [Gateway Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/gateway/introduction.html)
+  [Centralized Traffic Inspection with Gateway Load Balancer on AWS](https://aws.amazon.com/blogs/apn/centralized-traffic-inspection-with-gateway-load-balancer-on-aws/)
+  [AWS Network Firewall Documentation](https://docs.aws.amazon.com/network-firewall/latest/developerguide/)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
