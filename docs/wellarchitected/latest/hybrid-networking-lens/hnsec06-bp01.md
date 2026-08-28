---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnsec06-bp01.html
---

# HNSEC06-BP01 Monitor your environment for malicious behavior
<a name="hnsec06-bp01"></a>

 Responding to any cyber incident requires the ability to detect threats and establish a baseline for normal operations in a hybrid environment. Continuously monitors your environment for malicious behavior to protect your accounts and workloads.

 **Desired outcome:** Quick detection of malicious activity enables fast containment and limits the impact of ransomware and other security incidents.

 **Level of risk exposed if this best practice is not established:** High

 **Benefits of establishing this best practice:**
+  Early identification of threats and abnormal behaviors
+  Reduces containment and remediation time
+  Enhances overall security posture with automated, continuous monitoring

## Implementation guidance
<a name="implementation-guidance-25"></a>
+  Monitor flow logs, API activity, and DNS logs for threats, such as using Amazon GuardDuty that monitors and reports findings from these sources.
+  Regularly review and baseline findings to distinguish normal from abnormal activity.

## Resources
<a name="resources-23"></a>
+  [Amazon GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
