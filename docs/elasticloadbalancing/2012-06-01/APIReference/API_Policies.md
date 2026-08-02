---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_Policies.html
---

# Policies
<a name="API_Policies"></a>

The policies for a load balancer.

## Contents
<a name="API_Policies_Contents"></a>

 ** AppCookieStickinessPolicies.member.N **
The stickiness policies created using [CreateAppCookieStickinessPolicy](API_CreateAppCookieStickinessPolicy.md).
Type: Array of [AppCookieStickinessPolicy](API_AppCookieStickinessPolicy.md) objects
Required: No

 ** LBCookieStickinessPolicies.member.N **
The stickiness policies created using [CreateLBCookieStickinessPolicy](API_CreateLBCookieStickinessPolicy.md).
Type: Array of [LBCookieStickinessPolicy](API_LBCookieStickinessPolicy.md) objects
Required: No

 ** OtherPolicies.member.N **
The policies other than the stickiness policies.
Type: Array of strings
Required: No

## See Also
<a name="API_Policies_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancing-2012-06-01/Policies)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancing-2012-06-01/Policies)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancing-2012-06-01/Policies)
