---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_FixedResponseActionConfig.html
---

# FixedResponseActionConfig
<a name="API_FixedResponseActionConfig"></a>

Information about an action that returns a custom HTTP response.

## Contents
<a name="API_FixedResponseActionConfig_Contents"></a>

 ** StatusCode **
The HTTP response code (2XX, 4XX, or 5XX).
Type: String
Pattern: `^(2|4|5)\d\d$`
Required: Yes

 ** ContentType **
The content type.
Valid Values: text/plain \| text/css \| text/html \| application/javascript \| application/json
Type: String
Length Constraints: Minimum length of 0. Maximum length of 32.
Required: No

 ** MessageBody **
The message.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

## See Also
<a name="API_FixedResponseActionConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancingv2-2015-12-01/FixedResponseActionConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancingv2-2015-12-01/FixedResponseActionConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancingv2-2015-12-01/FixedResponseActionConfig)
