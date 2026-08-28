---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/sec_securely_operate_updated_threats.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# SEC01-BP04 Keep up-to-date with security threats
<a name="sec_securely_operate_updated_threats"></a>

 To help you define and implement appropriate controls, recognize attack vectors by staying up to date with the latest security threats. Consume AWS Managed Services to make it easier to receive notification of unexpected or unusual behavior in your AWS accounts. Investigate using AWS Partner tools or third-party threat information feeds as part of your security information flow. The [Common Vulnerabilities and Exposures (CVE) List ](https://cve.mitre.org/) list contains publicly disclosed cyber security vulnerabilities that you can use to stay up to date.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>
+  Subscribe to threat intelligence sources: Regularly review threat intelligence information from multiple sources that are relevant to the technologies used in your workload.
  +  [Common Vulnerabilities and Exposures List ](https://cve.mitre.org/)
+  Consider [AWS Shield Advanced](https://aws.amazon.com/shield/?whats-new-cards.sort-by=item.additionalFields.postDateTime&whats-new-cards.sort-order=desc) service: It provides near real-time visibility into intelligence sources, if your workload is internet accessible.

## Resources
<a name="resources"></a>

 **Related documents:**
+ [AWS Security Audit Guidelines](https://docs.aws.amazon.com/general/latest/gr/aws-security-audit-guide.html)
+  [AWS Shield](https://aws.amazon.com/shield/)
+ [ Security Bulletins](https://aws.amazon.com/security/security-bulletins/)

 **Related videos:**
+ [Security Best Practices the Well-Architected Way ](https://youtu.be/u6BCVkXkPnM)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
