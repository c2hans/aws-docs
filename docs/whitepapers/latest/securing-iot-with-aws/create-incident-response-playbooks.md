---
source_url: https://docs.aws.amazon.com/whitepapers/latest/securing-iot-with-aws/create-incident-response-playbooks.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# 9. Create incident response playbooks, and build automation as your security response matures
<a name="create-incident-response-playbooks"></a>

 Management systems must build continuous health checks before the devices get shipped. It’s also important to create incident response playbooks for when those checks identify anomalies, and, as processes mature, automate the containing of events and returning to a known good state. Although it may seem daunting, this doesn’t have to happen all at the same time. This is a process that will continue throughout the lifecycle of the IoT environment, with the complexity and maturity of the program growing over time.
+  Maintain and regularly exercise a security incident response plan to test monitoring functionality.
+  Collect security logs and analyze them in real time using automated tooling. Build playbooks in response to unexpected findings.
+  Create an incident response playbook with clearly understood roles and responsibilities.
+  Test incident response procedures on a periodic basis.
+  As procedures become more stable, automate their implementation but maintain human interaction. As the automated procedures are validated, automate what triggers their implementation.

## Supporting AWS resources
<a name="resources-9"></a>

 AWS provides the following assets and services to help you monitor your security and create incident response playbooks:
+  [AWS Security Incident Response Guide](https://docs.aws.amazon.com/whitepapers/latest/aws-security-incident-response-guide/welcome.html)
+  [AWS Systems Manager](https://aws.amazon.com/systems-manager/) – Provides a centralized and consistent way to gather operational insights and carry out routine management tasks.
+  [Security Pillar of AWS Well-Architected](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html) and [https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/welcome.html](https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/welcome.html)
