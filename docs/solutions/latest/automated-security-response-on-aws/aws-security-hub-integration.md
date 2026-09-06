---
source_url: https://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/aws-security-hub-integration.html
---

# AWS Security Hub integration
<a name="aws-security-hub-integration"></a>

Deploying the `automated-security-response-admin` stack creates integration with [AWS Security Hub CSPM’s](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html) custom action feature. When AWS Security Hub CSPM console users choose **Actions >** **Remediate with ASR**, the selected findings are sent to EventBridge and trigger the remediation workflow.

Cross-account permissions and AWS Systems Manager runbooks must be deployed to all AWS Security Hub accounts (admin and member) using the `automated-security-response-member.template` and `automated-security-response-member-roles.template` CloudFormation templates. For more information, refer to [Playbooks](playbooks.md). This template allows automated remediation in the target account.

Users can configure fully-automated remediations on a per-control basis using Amazon DynamoDB. This option activates fully automatic remediation of findings as soon as they are reported to AWS Security Hub. By default, automatic initiations are turned off. This option can be changed at any time after installation by modifying the [Remediation Configuration DynamoDB table](enable-fully-automated-remediations.md).
