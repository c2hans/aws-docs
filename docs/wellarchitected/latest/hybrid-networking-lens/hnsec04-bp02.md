---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnsec04-bp02.html
---

# HNSEC04-BP02 Implement routing controls for network segments
<a name="hnsec04-bp02"></a>

 Implementing routing controls for network segments involves strategically managing traffic flow between different parts of your network infrastructure. This includes setting up route tables to direct traffic based on security policies. These controls should enforce the principle of least privilege, ensuring network components can only communicate with authorized segments.

 **Desired outcome:** Enable centralized, flexible, and secure traffic routing between cloud and on-premises networks.

 **Level of risk exposed if this best practice is not established:** High

 **Benefits of establishing this best practice:**
+  Provides centralized control of network paths
+  Allows for segmentation and isolation using null routes
+  Prevents unauthorized or misrouted hybrid traffic

## Implementation guidance
<a name="implementation-guidance-18"></a>
+  Design route tables to segment environments and block unnecessary paths.
+  Use null routes to block specific destinations when needed.
+  Periodically review and simulate route changes before deployment.

## Resources
<a name="resources-17"></a>
+  [Transit gateway route tables in AWS Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-route-tables.html)
+  [Core network policy versions in AWS Cloud WAN](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-create-policy-version.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
