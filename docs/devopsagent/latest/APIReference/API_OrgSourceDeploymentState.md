---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_OrgSourceDeploymentState.html
---

# OrgSourceDeploymentState

Describes the current rollout state of an AWS Organization source configuration, including the number of accounts that have been deployed to and any issues encountered during deployment.

## Contents
<a name="API_OrgSourceDeploymentState_Contents"></a>

 ** deployedAccountCount **   <a name="devopsagent-Type-OrgSourceDeploymentState-deployedAccountCount"></a>
The number of accounts in the targeted AWS Organization or organizational unit that have successfully been deployed to.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** issues **   <a name="devopsagent-Type-OrgSourceDeploymentState-issues"></a>
The issues encountered while deploying the source configuration across the accounts in the AWS Organization.
Type: Array of [OrgSourceIssue](API_OrgSourceIssue.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Required: No

 ** lastEvaluatedAt **   <a name="devopsagent-Type-OrgSourceDeploymentState-lastEvaluatedAt"></a>
The timestamp of the most recent evaluation of the organization-wide deployment state.
Type: Timestamp
Required: No

## See Also
<a name="API_OrgSourceDeploymentState_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/OrgSourceDeploymentState)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/OrgSourceDeploymentState)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/OrgSourceDeploymentState)
