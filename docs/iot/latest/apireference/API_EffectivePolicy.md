---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_EffectivePolicy.html
---

# EffectivePolicy
<a name="API_EffectivePolicy"></a>

The policy that has the effect on the authorization results.

## Contents
<a name="API_EffectivePolicy_Contents"></a>

 ** policyArn **   <a name="iot-Type-EffectivePolicy-policyArn"></a>
The policy ARN.
Type: String
Required: No

 ** policyDocument **   <a name="iot-Type-EffectivePolicy-policyDocument"></a>
The IAM policy document.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 404600.
Pattern: `[\s\S]*`
Required: No

 ** policyName **   <a name="iot-Type-EffectivePolicy-policyName"></a>
The policy name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w+=,.@-]+`
Required: No

## See Also
<a name="API_EffectivePolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/EffectivePolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/EffectivePolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/EffectivePolicy)
