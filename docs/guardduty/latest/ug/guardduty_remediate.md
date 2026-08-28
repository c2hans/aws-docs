---
source_url: https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_remediate.html
---

# Remediating detected GuardDuty security findings
<a name="guardduty_remediate"></a>

Amazon GuardDuty generates [findings](guardduty_findings.md) that indicate potential security findings associated with GuardDuty foundational threat detection and dedicated protection plans. The following sections describe the recommended remediation steps for these scenarios. If there are alternative remediation scenarios, they will be described in the descriptions for each finding type. You can access the full information about a finding type by selecting it from the [Active findings types](guardduty_finding-types-active.md) table.

**Topics**
+ [Remediating a potentially compromised Amazon EC2 instance](compromised-ec2.md)
+ [Remediating a potentially compromised S3 bucket](compromised-s3.md)
+ [Remediating a potentially malicious S3 object](compromised-s3object-malware-protection-gdu.md)
+ [Remediating a potentially compromised EBS Snapshot](compromised-snapshot.md)
+ [Remediating a potentially compromised EC2 AMI](compromised-ami.md)
+ [Remediating a potentially compromised EC2 Recovery Point](compromised-ec2-recoverypoint.md)
+ [Remediating a potentially compromised S3 Recovery Point](compromised-s3-recoverypoint.md)
+ [Remediating a potentially compromised ECS cluster](compromised-ecs.md)
+ [Remediating potentially compromised AWS credentials](compromised-creds.md)
+ [Remediating a potentially compromised standalone container](remediate-compromised-standalone-container.md)
+ [Remediating EKS Protection findings](guardduty-remediate-kubernetes.md)
+ [Remediating Runtime Monitoring findings](guardduty-remediate-runtime-monitoring.md)
+ [Remediating a potentially compromised database](guardduty-remediate-compromised-database-rds.md)
+ [Remediating a potentially compromised Lambda function](remediate-lambda-protection-finding-types.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GuardDuty. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guardduty` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
