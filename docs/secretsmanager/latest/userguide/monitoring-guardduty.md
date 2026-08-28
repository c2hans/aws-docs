---
source_url: https://docs.aws.amazon.com/secretsmanager/latest/userguide/monitoring-guardduty.html
---

# Detect threats with Amazon GuardDuty
<a name="monitoring-guardduty"></a>

Amazon GuardDuty is a threat detection service that helps you protect your accounts, containers, workloads, and the data with your AWS environment. By using machine learning (ML) models and anomaly and threat detection capabilities, GuardDuty continuously monitors different log sources to identify and prioritize potential security risks and malicious activities in your environment. For example, GuardDuty will detect potential threats such as unusual or suspicious access to secrets, and credential exfiltration in case it detects credentials that were created exclusively for an Amazon EC2 instance through an instance launch role but are being used from another account within AWS. For more information, see the [Amazon GuardDuty User Guide](https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html).

Another example use-case for detection is anomalous behavior. For example, if AWS Secrets Manager typically gets `create-secret`, `get-secret-value`, `describe-secret`, and `list-secrets` calls from an entity using the Java SDK, and then a different entity begins calling `batch-get-secret-value` and `get-secret-value` using the AWS CLI from outside of the VPN, GuardDuty can report a finding that the second entity is anomalously invoking APIs. For more information, see [GuardDuty IAM finding type CredentialAccess:IAMUser/AnomalousBehavior](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-iam.html#credentialaccess-iam-anomalousbehavior).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Secrets Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query secretsmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
