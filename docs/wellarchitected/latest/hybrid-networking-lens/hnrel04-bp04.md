---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnrel04-bp04.html
---

# HNREL04-BP04 Provision sufficient network capacity
<a name="hnrel04-bp04"></a>

 Provision enough network capacity so that the failure of a single network connection does not overwhelm or degrade the remaining redundant connections.

 **Desired outcome:** Maintain performance and service levels during network outages or planned maintenance by ensuring available bandwidth meets business needs.

 **Level of risk exposed if this best practice is not established:** High

 **Benefits of establishing this best practice:**
+  Avoids performance bottlenecks during failover
+  Ensure sufficient capacity for critical workloads at all times
+  Supports scalability and growth in hybrid environments
+  Enhances customer and user experience

## Implementation guidance
<a name="implementation-guidance-36"></a>
+  Analyze peak and average bandwidth requirements for hybrid workloads.
+  Size redundant connections so any one connection can handle the full load if others fail.
+  Monitor bandwidth usage and adjust capacity proactively.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
