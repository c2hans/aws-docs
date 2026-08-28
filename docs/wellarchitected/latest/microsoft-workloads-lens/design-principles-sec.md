---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/design-principles-sec.html
---

# Design principles
<a name="design-principles-sec"></a>

 Refer to design principles in the Well-Architected Framework Security Pillar for core security concepts. Additionally, consider these Microsoft-specific security aspects:
+  **Microsoft-specific security configurations:** Use Microsoft security baselines, Active Directory Group Policies, and Windows-specific security features like Windows Defender, AppLocker, and BitLocker for enhanced workload protection.
+  **Identity integration patterns:** Implement proper integration between AWS IAM and Microsoft Active Directory services (either AWS Managed Microsoft AD or self-managed AD) for secure authentication across hybrid environments.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
