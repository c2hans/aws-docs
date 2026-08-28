---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnsec04-bp01.html
---

# HNSEC04-BP01 Control access to network resources
<a name="hnsec04-bp01"></a>

 Comprehensive network access control applied across both on-premises and cloud environments to create a unified security posture that addresses the unique challenges of hybrid infrastructures while maintaining compliance with regulatory requirements.

 **Desired outcome:** Protect hybrid network resources by controlling traffic from on-premises and cloud environments.

 **Level of risk exposed if this best practice is not established:** High

 **Benefits of establishing this best practice:**
+  Restrict network access to only approved sources
+  Minimizes risk of unauthorized or malicious traffic
+  Enables granular, instance-level security controls

## Implementation guidance
<a name="implementation-guidance-17"></a>
+  Define least-privilege inbound and outbound rules matching only approved network prefixes.
+  Regularly review and update rules for accuracy and compliance.

## Resources
<a name="resources-16"></a>
+  [Control traffic to your AWS resources using security groups](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html)
+  [Control subnet traffic with network access control lists](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
