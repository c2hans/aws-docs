---
source_url: https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_SigningConfiguration.html
---

# SigningConfiguration
<a name="API_SigningConfiguration"></a>

The signing configuration for a registry, which specifies rules for automatically signing images when pushed.

## Contents
<a name="API_SigningConfiguration_Contents"></a>

 ** rules **   <a name="ECR-Type-SigningConfiguration-rules"></a>
A list of signing rules. Each rule defines a signing profile and optional repository filters that determine which images are automatically signed. Maximum of 10 rules.
Type: Array of [SigningRule](API_SigningRule.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: Yes

## See Also
<a name="API_SigningConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-2015-09-21/SigningConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-2015-09-21/SigningConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-2015-09-21/SigningConfiguration)
