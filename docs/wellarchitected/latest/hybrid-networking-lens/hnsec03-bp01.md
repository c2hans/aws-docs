---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnsec03-bp01.html
---

# HNSEC03-BP01 Implement network traffic monitoring and threat detection
<a name="hnsec03-bp01"></a>

 Monitor and implement an immediate response process that detects and reacts to any suspicious or malicious activity. Continuously monitoring workloads helps to identify security incidents faster. At a minimum, the metadata of logs should be captured for hybrid network connections with private connections.

 **Desired outcome:** Detect suspicious or unauthorized activity and improve security posture by capturing and analyzing network traffic logs.

 **Level of risk exposed if this best practice is not established:** High

 **Benefits of establishing this best practice:**
+  Enables early detection and response to security incidents
+  Provides visibility into hybrid network activity
+  Helps with forensic analysis and compliance reporting
+  Reduces risk of undetected malicious activity

## Implementation guidance
<a name="implementation-guidance-15"></a>
+  Enable flow logs on all relevant networks using services such as VPC Flow Logs and Transit Gateway Flow Logs
+  Enable continuous threat detection across network traffic and accounts. For example, you can achieve this with Amazon GuardDuty.
+  Review findings regularly and establish automated or manual incident response processes.
+  Store and analyze logs in a central location for correlation and investigation.

## Resources
<a name="resources-14"></a>
+  [Logging IP traffic using VPC Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html)
+  [AWS Transit Gateway Flow Logs](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-flow-logs.html)
+  [Amazon GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html)
+  [Centralized Logging with OpenSearch](https://aws.amazon.com/solutions/implementations/centralized-logging-with-opensearch/)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
