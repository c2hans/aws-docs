---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_ChallengeJavascriptSdkInjectionConfig.html
---

# ChallengeJavascriptSdkInjectionConfig
<a name="API_ChallengeJavascriptSdkInjectionConfig"></a>

Specifies whether the associated CloudFront distribution inserts the AWS WAF challenge JavaScript SDK into the HTML responses that it returns. The structure is empty: including it turns insertion on, and removing it turns insertion off.

This is used in the `ChallengeJavascriptSdkInjection` map of the `AssociationConfig` of the web ACL. The map key identifies the resource type and must be `CLOUDFRONT`.

JSON specification: `"CLOUDFRONT": {}`

## Contents
<a name="API_ChallengeJavascriptSdkInjectionConfig_Contents"></a>

The members of this exception structure are context-dependent.

## See Also
<a name="API_ChallengeJavascriptSdkInjectionConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/ChallengeJavascriptSdkInjectionConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/ChallengeJavascriptSdkInjectionConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/ChallengeJavascriptSdkInjectionConfig)
