---
source_url: https://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/aws-security-hub-integration.html
---

# AWS Security Hub integration
<a name="aws-security-hub-integration"></a>

Deploying the `automated-security-response-admin` stack creates integration with [AWS Security Hub CSPM’s](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html) custom action feature. When AWS Security Hub CSPM console users choose **Actions >** **Remediate with ASR**, the selected findings are sent to EventBridge and trigger the remediation workflow.

Cross-account permissions and AWS Systems Manager runbooks must be deployed to all AWS Security Hub accounts (admin and member) using the `automated-security-response-member.template` and `automated-security-response-member-roles.template` CloudFormation templates. For more information, refer to [Playbooks](playbooks.md). This template allows automated remediation in the target account.

You can configure fully automated remediation on a per-control basis. When it is enabled for a control, the solution remediates that control’s findings as soon as they are reported to AWS Security Hub. The setting is stored in the Remediation Configuration Amazon DynamoDB table and is turned off by default. You can change it at any time after installation from the Web UI **Controls** page, the MCP server, or the [Remediation Configuration DynamoDB table](enable-fully-automated-remediations.md).
