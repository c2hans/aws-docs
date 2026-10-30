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

You can also use this to have your CloudFront distributions insert the AWS WAF challenge JavaScript SDK into the HTML responses that they return. For more information, see the `ChallengeJavascriptSdkInjection` setting.

## Contents
<a name="API_AssociationConfig_Contents"></a>

 ** ChallengeJavascriptSdkInjection **   <a name="WAF-Type-AssociationConfig-ChallengeJavascriptSdkInjection"></a>
Specifies the CloudFront distributions that insert the AWS WAF challenge JavaScript SDK into the HTML responses that they return. When you enable this setting for a distribution, you do not add the SDK to your web pages yourself.
You can configure this setting only for CloudFront distributions, using the `CLOUDFRONT` map key. AWS WAF rejects any other resource type, and the setting is not available for regional resources. To configure it, use the CloudFront scope.
Your web ACL must also contain at least one of the following qualifying managed rule groups. AWS WAF Bot Control qualifies only at the `TARGETED` inspection level, not at `COMMON`:
+ The AWS WAF Bot Control managed rule group `AWSManagedRulesBotControlRuleSet`, with the inspection level set to `TARGETED`.
+ The AWS WAF Fraud Control account takeover prevention (ATP) managed rule group `AWSManagedRulesATPRuleSet`.
+ The AWS WAF Fraud Control account creation fraud prevention (ACFP) managed rule group `AWSManagedRulesACFPRuleSet`.
If you remove the last qualifying managed rule group from the web ACL, or lower the AWS WAF Bot Control inspection level from `TARGETED` to `COMMON`, you must remove this setting in the same update. Otherwise, AWS WAF rejects the update.
Example JSON: ` { "CLOUDFRONT": {} }`
If you omit this setting, CloudFront does not insert the SDK. When you omit it from a web ACL that previously used it, cached HTML that already contains the SDK is still served until it expires, or until you invalidate the cache for that distribution. For more information, see [Automatic SDK integration for CloudFront distributions](https://docs.aws.amazon.com/waf/latest/developerguide/waf-challenge-javascript-sdk-injection.html) in the * AWS WAF Developer Guide*.
Type: String to [ChallengeJavascriptSdkInjectionConfig](API_ChallengeJavascriptSdkInjectionConfig.md) object map
Map Entries: Maximum number of items.
Valid Keys: `CLOUDFRONT | API_GATEWAY | COGNITO_USER_POOL | APP_RUNNER_SERVICE | VERIFIED_ACCESS_INSTANCE | AGENTCORE_GATEWAY`
Required: No

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
