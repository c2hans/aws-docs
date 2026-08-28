---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hncost07-bp01.html
---

# HNCOST07-BP01 Use dedicated connection for high-volume predictable traffic
<a name="hncost07-bp01"></a>

 Deploy dedicated connection for production workloads requiring consistent, high-bandwidth connectivity between on-premises and cloud environments. Dedicated connection offers lower per-GB costs compared to IPSec VPN and avoids internet variability.

 **Desired outcome:** Predictable, reduced data transfer costs for mission-critical workloads.

 **Level of risk exposed if this best practice is not established:** Medium

 **Benefits of establishing this best practice:**
+  cost savings versus VPN for high-volume traffic
+  Improved performance and reliability

## Implementation guidance
<a name="implementation-guidance-58"></a>
+  Start with low bandwidth dedicated connections and scale up with high bandwidth connections or multiple connections with LAG

## Resources
<a name="resources-48"></a>
+  [AWS Direct Connect Pricing](https://aws.amazon.com/directconnect/pricing/)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
