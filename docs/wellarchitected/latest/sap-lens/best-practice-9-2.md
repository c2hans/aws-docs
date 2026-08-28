---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/best-practice-9-2.html
---

# Best Practice 9.2 – Perform periodic tests for security bugs
<a name="best-practice-9-2"></a>

As described in the Well-Architected Framework Security Pillar incident response sections on simulations, assembling a runbook and conducting game days are recommended for all workloads, including those for SAP on AWS. This type of periodic testing can identify new attack vectors and vulnerabilities as well as prepare your SAP security resources for a rapid and effective response in the event of a security incident.

 Well-Architected Framework [Security]: [Incident Response – Simulation](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/simulate.html)

 **Suggestion 9.2.1 – Include SAP applications as targets in addition to standard security and penetration testing**

 Probative security testing is an important part of maintaining a secure environment. In addition to conducting standard penetration testing in AWS, make sure to include your SAP solution as an additional potential target for malicious activities. Keep in mind SAP-specific software solutions that often are publicly exposed in your architecture such as SAProuter, Web Dispatcher, Cloud Connector, and SAP Fiori.
+  AWS Documentation: [Penetration Testing](https://aws.amazon.com/security/penetration-testing/)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
