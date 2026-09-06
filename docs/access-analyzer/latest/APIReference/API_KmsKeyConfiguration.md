---
source_url: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_KmsKeyConfiguration.html
---

# KmsKeyConfiguration
<a name="API_KmsKeyConfiguration"></a>

Proposed access control configuration for a KMS key. You can propose a configuration for a new KMS key or an existing KMS key that you own by specifying the key policy and AWS KMS grant configuration. If the configuration is for an existing key and you do not specify the key policy, the access preview uses the existing policy for the key. If the access preview is for a new resource and you do not specify the key policy, then the access preview uses the default key policy. The proposed key policy cannot be an empty string. For more information, see [Default key policy](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html#key-policy-default). For more information about key policy limits, see [Resource quotas](https://docs.aws.amazon.com/kms/latest/developerguide/resource-limits.html).

## Contents
<a name="API_KmsKeyConfiguration_Contents"></a>

 ** grants **   <a name="accessanalyzer-Type-KmsKeyConfiguration-grants"></a>
A list of proposed grant configurations for the KMS key. If the proposed grant configuration is for an existing key, the access preview uses the proposed list of grant configurations in place of the existing grants. Otherwise, the access preview uses the existing grants for the key.
Type: Array of [KmsGrantConfiguration](API_KmsGrantConfiguration.md) objects
Required: No

 ** keyPolicies **   <a name="accessanalyzer-Type-KmsKeyConfiguration-keyPolicies"></a>
Resource policy configuration for the KMS key. The only valid value for the name of the key policy is `default`. For more information, see [Default key policy](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html#key-policy-default).
Type: String to string map
Required: No

## See Also
<a name="API_KmsKeyConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/KmsKeyConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/KmsKeyConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/KmsKeyConfiguration)
