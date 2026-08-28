---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnrel03-bp01.html
---

# HNREL03-BP01 Monitor the bandwidth and scale the bandwidth as needed
<a name="hnrel03-bp01"></a>

 Regularly monitor the bandwidth usage of your dedicated connection. If usage consistently approaches the connection limit, order additional dedicated connections and aggregate them into a LAG to increase bandwidth and resilience with minimal downtime.

 **Desired outcome:** Avoid service degradation or outages due to bandwidth limitations by proactively scaling your hybrid connectivity.

 **Level of risk exposed if this best practice is not established:** High

 **Benefits of establishing this best practice:**
+  Prevent performance bottlenecks and dropped traffic
+  Enables cost-effective scaling of hybrid network connectivity
+  Supports growth in hybrid workload demand
+  Ensures seamless failover and aggregation

## Implementation guidance
<a name="implementation-guidance-31"></a>
+  Monitor metrics for all dedicated connection and IPSec VPN links.
+  Create alarms for sustained high utilization.
+  Plan and implement LAG to aggregate bandwidth and connections.

## Resources
<a name="resources-27"></a>
+  [How can I migrate virtual Interfaces to Direct Connect connections or LAG bundles?](https://repost.aws/knowledge-center/migrate-virtual-interface-dx-lag)
+  [Direct Connect link aggregation groups (LAGs)](https://docs.aws.amazon.com/directconnect/latest/UserGuide/lags.html)
+  [Monitoring Direct Connect with CloudWatch](https://docs.aws.amazon.com/directconnect/latest/UserGuide/monitoring-cloudwatch.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
