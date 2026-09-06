---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_SourceAwsConfiguration.html
---

# SourceAwsConfiguration
<a name="API_SourceAwsConfiguration"></a>

Configuration for AWS source account integration. Setting the role ARNs on this configuration requires the caller to have at least the iam:PassRole permission (see assumableRoleArn).

## Contents
<a name="API_SourceAwsConfiguration_Contents"></a>

 ** accountId **   <a name="devopsagent-Type-SourceAwsConfiguration-accountId"></a>
AWS Account Id corresponding to provided resources.
Type: String
Pattern: `\d{12}`
Required: Yes

 ** accountType **   <a name="devopsagent-Type-SourceAwsConfiguration-accountType"></a>
Account Type 'source' for AIDevOps monitoring.
Type: String
Valid Values: `source`
Required: Yes

 ** assumableRoleArn **   <a name="devopsagent-Type-SourceAwsConfiguration-assumableRoleArn"></a>
Role ARN to be assumed by AIDevOps to operate on behalf of customer. To set this role ARN on AssociateService or UpdateAssociation, the caller must have at least the iam:PassRole permission on arn:aws:iam::<account-id>:role/\* in the caller's own account, with the condition iam:PassedToService set to aidevops.amazonaws.com. A broader iam:PassRole grant also satisfies this requirement.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `arn:aws:iam::\d{12}:role/[a-zA-Z0-9+=,.@_/-]+`
Required: Yes

 ** agentElevatedRoleArn **   <a name="devopsagent-Type-SourceAwsConfiguration-agentElevatedRoleArn"></a>
Optional IAM role ARN to be assumed by AIDevOps for elevated directed actions on behalf of the customer. Used for mutating operations gated by elevatedActionsEnabled on the AgentSpace. When not provided, only non-elevated directed actions are available for this AWS account. Setting this role is subject to the same minimum iam:PassRole requirement described on assumableRoleArn.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `arn:aws:iam::\d{12}:role/[a-zA-Z0-9+=,.@_/-]+`
Required: No

 ** agentElevatedRoleArnStatus **   <a name="devopsagent-Type-SourceAwsConfiguration-agentElevatedRoleArnStatus"></a>
Validation status of the agentElevatedRoleArn. Updated asynchronously after the customer registers an elevated role. Possible values: PENDING\_CONFIRMATION (validation in progress), VALID (role validated), INVALID (validation failed).
Type: String
Valid Values: `valid | invalid | pending-confirmation`
Required: No

 ** externalId **   <a name="devopsagent-Type-SourceAwsConfiguration-externalId"></a>
External ID for additional security when assuming the role. Used to prevent the confused deputy problem.
Type: String
Required: No

## See Also
<a name="API_SourceAwsConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/SourceAwsConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/SourceAwsConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/SourceAwsConfiguration)
