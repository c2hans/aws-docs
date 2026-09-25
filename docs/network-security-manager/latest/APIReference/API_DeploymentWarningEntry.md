---
source_url: https://docs.aws.amazon.com/network-security-manager/latest/APIReference/API_DeploymentWarningEntry.html
---

# DeploymentWarningEntry
<a name="API_DeploymentWarningEntry"></a>

A warning about a potential issue with a deployment.

## Contents
<a name="API_DeploymentWarningEntry_Contents"></a>

 ** code **   <a name="networksecuritymanager-Type-DeploymentWarningEntry-code"></a>
A code that identifies the type of warning.
Type: String
Required: Yes

 ** message **   <a name="networksecuritymanager-Type-DeploymentWarningEntry-message"></a>
A human-readable description of the warning.
Type: String
Required: Yes

 ** policyArn **   <a name="networksecuritymanager-Type-DeploymentWarningEntry-policyArn"></a>
The ARN of the policy that the warning relates to.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 1010.
Pattern: `arn(:[a-z0-9]+([.-][a-z0-9]+)*){2}(:([a-z0-9]+([.-][a-z0-9]+)*)?){2}:(.+)`
Required: Yes

## See Also
<a name="API_DeploymentWarningEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-security-manager-2025-10-30/DeploymentWarningEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-security-manager-2025-10-30/DeploymentWarningEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-security-manager-2025-10-30/DeploymentWarningEntry)
