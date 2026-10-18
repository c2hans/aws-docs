---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_PrivateNetworkAccess.html
---

# PrivateNetworkAccess
<a name="API_PrivateNetworkAccess"></a>

Private network access to the resource inside a VPC, using a private connection.

## Contents
<a name="API_PrivateNetworkAccess_Contents"></a>

 ** privateConnectionName **   <a name="devopsagent-Type-PrivateNetworkAccess-privateConnectionName"></a>
Name of the private connection that supplies the VPC configuration for this release management environment.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 30.
Pattern: `[a-z0-9]([a-z0-9-]*[a-z0-9])?`
Required: Yes

 ** runtimeRoleArn **   <a name="devopsagent-Type-PrivateNetworkAccess-runtimeRoleArn"></a>
Role ARN that AWS DevOps Agent assumes at runtime to connect to your VPC.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `arn:(aws|aws-cn|aws-us-gov):iam::\d{12}:role/[a-zA-Z0-9+=,.@_/-]+`
Required: Yes

## See Also
<a name="API_PrivateNetworkAccess_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/PrivateNetworkAccess)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/PrivateNetworkAccess)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/PrivateNetworkAccess)
