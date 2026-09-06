---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_AssociationConfig.html
---

# AssociationConfig
<a name="API_AssociationConfig"></a>

Specifies custom configurations for the associations between the web ACL and protected resources.

Use this to customize the maximum size of the request body that your protected resources forward to AWS WAF for inspection. You can customize this setting for CloudFront, API Gateway, Amazon Cognito, App Runner, or Verified Access resources. The default setting is 16 KB (16,384 bytes).

**Note**
You are charged additional fees when your protected resources forward body sizes that are larger than the default. For more information, see [AWS WAF Pricing](http://aws.amazon.com/waf/pricing/).

For Application Load Balancer and AWS AppSync, the limit is fixed at 8 KB (8,192 bytes).

## Contents
<a name="API_AssociationConfig_Contents"></a>

 ** RequestBody **   <a name="WAF-Type-AssociationConfig-RequestBody"></a>
Customizes the maximum size of the request body that your protected CloudFront, API Gateway, Amazon Cognito, App Runner, and Verified Access resources forward to AWS WAF for inspection. The default size is 16 KB (16,384 bytes). You can change the setting for any of the available resource types.
You are charged additional fees when your protected resources forward body sizes that are larger than the default. For more information, see [AWS WAF Pricing](http://aws.amazon.com/waf/pricing/).
Example JSON: ` { "API_GATEWAY": "KB_48", "APP_RUNNER_SERVICE": "KB_32" }`
For Application Load Balancer and AWS AppSync, the limit is fixed at 8 KB (8,192 bytes).
Type: String to [RequestBodyAssociatedResourceTypeConfig](API_RequestBodyAssociatedResourceTypeConfig.md) object map
Valid Keys: `CLOUDFRONT | API_GATEWAY | COGNITO_USER_POOL | APP_RUNNER_SERVICE | VERIFIED_ACCESS_INSTANCE | AGENTCORE_GATEWAY`
Required: No

## See Also
<a name="API_AssociationConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/AssociationConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/AssociationConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/AssociationConfig)
