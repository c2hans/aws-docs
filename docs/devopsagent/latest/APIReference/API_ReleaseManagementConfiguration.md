---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_ReleaseManagementConfiguration.html
---

# ReleaseManagementConfiguration
<a name="API_ReleaseManagementConfiguration"></a>

Configuration for a release management environment.

## Contents
<a name="API_ReleaseManagementConfiguration_Contents"></a>

 ** name **   <a name="devopsagent-Type-ReleaseManagementConfiguration-name"></a>
The name for this release management environment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\p{L}\p{N}\p{P}\p{S}\p{Z}]+`
Required: Yes

 ** networkAccess **   <a name="devopsagent-Type-ReleaseManagementConfiguration-networkAccess"></a>
Specifies how AWS DevOps Agent reaches your application using a Release Management Environment
Type: [NetworkAccessConfiguration](API_NetworkAccessConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

## See Also
<a name="API_ReleaseManagementConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/ReleaseManagementConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/ReleaseManagementConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/ReleaseManagementConfiguration)
