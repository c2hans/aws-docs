---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_AWSConfiguration.html
---

# AWSConfiguration
<a name="API_AWSConfiguration"></a>

Configuration for AWS monitor account integration, allowing AIDevOps to monitor AWS resources.

## Contents
<a name="API_AWSConfiguration_Contents"></a>

 ** accountId **   <a name="devopsagent-Type-AWSConfiguration-accountId"></a>
AWS Account Id corresponding to provided resources.
Type: String
Pattern: `\d{12}`
Required: Yes

 ** accountType **   <a name="devopsagent-Type-AWSConfiguration-accountType"></a>
Account Type 'monitor' for AIDevOps monitoring.
Type: String
Valid Values: `monitor`
Required: Yes

 ** assumableRoleArn **   <a name="devopsagent-Type-AWSConfiguration-assumableRoleArn"></a>
Role ARN to be assumed by AIDevOps to operate on behalf of customer.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `arn:aws:iam::\d{12}:role/[a-zA-Z0-9+=,.@_/-]+`
Required: Yes

 ** agentElevatedRoleArn **   <a name="devopsagent-Type-AWSConfiguration-agentElevatedRoleArn"></a>
Optional IAM role ARN to be assumed by AIDevOps for elevated directed actions on behalf of the customer. Used for mutating operations gated by elevatedActionsEnabled on the AgentSpace. When not provided, only non-elevated directed actions are available for this AWS account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `arn:aws:iam::\d{12}:role/[a-zA-Z0-9+=,.@_/-]+`
Required: No

 ** agentElevatedRoleArnStatus **   <a name="devopsagent-Type-AWSConfiguration-agentElevatedRoleArnStatus"></a>
Validation status of the agentElevatedRoleArn. Updated asynchronously after the customer registers an elevated role. Possible values: PENDING\_CONFIRMATION (validation in progress), VALID (role validated), INVALID (validation failed).
Type: String
Valid Values: `valid | invalid | pending-confirmation`
Required: No

## See Also
<a name="API_AWSConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/AWSConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/AWSConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/AWSConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS DevOps Agent. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devopsagent` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
