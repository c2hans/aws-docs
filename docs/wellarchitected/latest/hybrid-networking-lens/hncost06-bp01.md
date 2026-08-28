---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hncost06-bp01.html
---

# HNCOST06-BP01 Implement QoS policies for traffic prioritization
<a name="hncost06-bp01"></a>

 Configure QoS rules on on-premises routers to prioritize latency-sensitive traffic such as voice and video over bulk transfers such as data syncs.

 **Desired outcome:** Guaranteed performance for critical workloads while optimizing bandwidth costs.

 **Level of risk exposed if this best practice is not established:** Medium

 **Benefits of establishing this best practice:**
+  Prevents costly performance degradation for high-priority traffic
+  Enables oversubscription of links without impacting critical workloads
+  Aligns network costs with business value

## Implementation guidance
<a name="implementation-guidance-56"></a>
+  Tag traffic with DSCP markers for on-premises traffic classification
+  Apply shapers or queues on on-premises routers

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
