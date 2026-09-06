---
source_url: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_IamRoleConfiguration.html
---

# IamRoleConfiguration
<a name="API_IamRoleConfiguration"></a>

The proposed access control configuration for an IAM role. You can propose a configuration for a new IAM role or an existing IAM role that you own by specifying the trust policy. If the configuration is for a new IAM role, you must specify the trust policy. If the configuration is for an existing IAM role that you own and you do not propose the trust policy, the access preview uses the existing trust policy for the role. The proposed trust policy cannot be an empty string. For more information about role trust policy limits, see [IAM and AWS STS quotas](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-quotas.html).

## Contents
<a name="API_IamRoleConfiguration_Contents"></a>

 ** trustPolicy **   <a name="accessanalyzer-Type-IamRoleConfiguration-trustPolicy"></a>
The proposed trust policy for the IAM role.
Type: String
Required: No

## See Also
<a name="API_IamRoleConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/IamRoleConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/IamRoleConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/IamRoleConfiguration)
