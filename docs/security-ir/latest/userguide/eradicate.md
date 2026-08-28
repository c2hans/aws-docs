---
source_url: https://docs.aws.amazon.com/security-ir/latest/userguide/eradicate.html
---

# Eradicate
<a name="eradicate"></a>

 During the eradication phase, it is important to identify and address all affected accounts, resources, and instances - such as by deleting malware, removing compromised user accounts, and mitigating any discovered vulnerabilities - to apply uniform remediation across the environment.

 It is a best practice to use a phased approach to eradication and recovery, and to prioritize remediation steps. The purpose of the early phases is to increase the overall security quickly (days to weeks) with high-value changes to prevent future events. The later phases can focus on longer-term changes (for example, infrastructure changes), and ongoing work to keep the enterprise as secure as possible. Each case is unique and AWS Security Incident Response engineers will work with you to assess necessary actions.

 Consider the following:
+  Can you re-image the system and harden it with patches or other countermeasures to prevent or reduce the risk of attacks?
+  Can you replace the infected system with a new instance or resource, enabling a clean baseline while terminating the infected item?
+  Have you removed all malware and other artifacts left behind by the unauthorized use, and hardened the affected systems against further attacks?
+  Is there a requirement for forensics on the impacted resources?

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Security Incident Response. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query security-ir` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
