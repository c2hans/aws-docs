---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/o.dip.3-implement-distributed-tracing-for-system-wide-request-tracking.html
---

# [O.DIP.3] Implement distributed tracing for system-wide request tracking
<a name="o.dip.3-implement-distributed-tracing-for-system-wide-request-tracking"></a>

 **Category:** RECOMMENDED

 Distributed tracing is a method to track requests as they move through distributed systems. It provides insights into system interactions across multiple services and applications, enabling quicker issue identification and resolution.

 Use a tracing solution that is scalable, provides real-time data collection, and supports comprehensive visualization of tracing data. Integrate this solution with the log and event aggregation tools to enhance system-wide visibility. This gives a comprehensive view of the entire system and its dependencies, facilitating quick identification and resolution of issues.

**Related information:**
+  [AWS Well-Architected Reliability Pillar: REL06-BP07 Monitor end-to-end tracing of requests through your system](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_monitor_aws_resources_end_to_end.html)
+  [Distributed Tracing System – AWS X-Ray](https://aws.amazon.com/xray/)
+  [Amazon CloudWatch ServiceLens](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ServiceLens.html)
+  [Amazon Managed Grafana](https://aws.amazon.com/grafana/)
+  [AWS X-Ray integration with Grafana](https://docs.aws.amazon.com/grafana/latest/userguide/x-ray-data-source.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
