---
source_url: https://docs.aws.amazon.com/whitepapers/latest/securing-iot-with-aws/deploy-security-auditing-and-monitoring.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# 8. Deploy security auditing and monitoring mechanisms across your IoT environment and relevant IT systems.
<a name="deploy-security-auditing-and-monitoring"></a>

 As we’ve discussed, it’s important to ensure the proper configuration of IoT devices when they are put into production and that they are updated. But, it’s also important to monitor their behavior and security posture on an ongoing basis.
+  Deploy auditing and monitoring mechanisms to continuously collect and report activity metrics and logs.
+  Monitor on-device and related off-device activities such as network traffic and entry points, process implementation, and system interactions for any unexpected behavior.
+  Continuously check that your security controls and systems are intact by explicitly testing them.
+  Implement a monitoring solution to create a traffic baseline, and monitor anomalies and adherence to the baseline.
+  Collect security logs and analyze them in real time using automated tooling.
+  Monitor availability of your IoT devices in real time, where technically feasible.

## Supporting AWS resources
<a name="resources-8"></a>

 AWS provides the following capabilities and services to help you monitor your security at varying levels:
+  [AWS IoT Device Defender](https://aws.amazon.com/iot-device-defender/) – Monitors and audits your fleet of IoT devices.
+  [Monitor AWS IoT with CloudWatch Logs](https://docs.aws.amazon.com/iot/latest/developerguide/cloud-watch-logs.html) – Centralizes the logs from all of your systems, applications, and AWS services that you use, in a single, highly scalable service.
+  [Log AWS IoT API Calls with AWS CloudTrail](https://docs.aws.amazon.com/iot/latest/developerguide/iot-using-cloudtrail.html) – Provides a record of actions taken by a user, a role, or an AWS service in AWS IoT.
+  [Monitoring with AWS IoT Greengrass Logs](https://docs.aws.amazon.com/greengrass/v1/developerguide/greengrass-logs-overview.html)
+  [AWS Config](https://aws.amazon.com/config/) – Assess, audit, and evaluate the configurations of your AWS resources.
+  [Amazon GuardDuty](https://aws.amazon.com/guardduty/) – Continuously monitors for malicious activity and unauthorized behavior to protect your AWS accounts and workloads.
+  [AWS Security Hub CSPM](https://aws.amazon.com/security-hub/) – Automates AWS security checks and centralizes security alerts.
+  [Security Pillar of AWS Well-Architected](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html) and [IoT Lens](https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/welcome.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
