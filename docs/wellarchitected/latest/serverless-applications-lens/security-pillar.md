---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/security-pillar.html
---

# Security pillar
<a name="security-pillar"></a>

 The security pillar includes the ability to protect information, systems, and assets while delivering business value through risk assessments and mitigation strategies.

 There are five best practice areas for security in the cloud:
+ [Identity and access management](identity-and-access-management.md)
+ [Detective controls](detective-controls.md)
+  [Infrastructure protection](infrastructure-protection.md)
+ [Data protection](data-protection.md)
+ [Incident response](incident-response.md)

Serverless addresses some of today’s biggest security concerns because it removes infrastructure management tasks such as operating system patching and updating binaries. Although the attack surface is reduced compared to non-serverless architectures, the Open Web Application Security Project (OWASP) and application security best practices still apply.

 The questions in this section are designed to help you address specific ways an attacker could try to gain access to or exploit misconfigured permissions, which could lead to abuse. The practices described in this section strongly influence the security of your entire cloud platform and so they should be validated carefully and reviewed frequently.

 The [Incident response](incident-response.md) category will not be described in this document because the practices from the AWS Well-Architected Framework still apply.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
