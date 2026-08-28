---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnsec06-bp02.html
---

# HNSEC06-BP02 Automate incident response
<a name="hnsec06-bp02"></a>

 Implement automated response capabilities to enhance incident containment speed and reliability while reducing manual intervention requirements. This approach ensures consistent execution of response procedures while minimizing human error during critical security events.

 **Desired outcome:** Faster, more reliable containment and recovery from incidents with reduced operational burden.

 **Level of risk exposed if this best practice is not established:** High

 **Benefits of establishing this best practice:**
+  Shortens response times and limits damage
+  Reduces alert fatigue and manual workload
+  Ensures consistent, repeatable incident handling

## Implementation guidance
<a name="implementation-guidance-26"></a>
+  Automate incident response by configuring security findings with response actions. For example, you can achieve this by integrating AWS Security Hub CSPM findings with AWS Lambda for automated actions.
+  Test and tune automation playbooks in non-production environments.

## Resources
<a name="resources-24"></a>
+  [Using EventBridge for automated response and remediation PDF RSS](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-cloudwatch-events.html)
+  [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/automating-security-responses.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
