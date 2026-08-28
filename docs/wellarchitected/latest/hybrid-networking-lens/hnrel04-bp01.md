---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnrel04-bp01.html
---

# HNREL04-BP01 Use physical location redundancy to host dedicated connections
<a name="hnrel04-bp01"></a>

 Design dedicated connections hosted at multiple geographically separated data centers or colocation facilities to provide physical location redundancy. This design ensures that your connectivity to cloud remains available even if one location is affected by an outage or disaster.

 **Desired outcome:** Maintain high availability and business continuity for hybrid connectivity, even in the event of a site-level failure.

 **Level of risk exposed if this best practice is not established:** High

 **Benefits of establishing this best practice:**
+  Minimizes the risk of a single point of failure
+  Enhance disaster recovery capabilities
+  Supports compliance and uptime requirements
+  Increases overall hybrid network resilience

## Implementation guidance
<a name="implementation-guidance-33"></a>
+  Deploy Direct Connect connections in at least two geographically distinct locations.
+  Route traffic dynamically between locations for failover.
+  Test failover scenarios regularly to validate resilience.

 **Resources:**
+  [AWS Direct Connect Resiliency Recommendations](https://aws.amazon.com/directconnect/resiliency-recommendation/)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
