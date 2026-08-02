---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsElbLbCookieStickinessPolicy.html
---

# AwsElbLbCookieStickinessPolicy
<a name="API_AwsElbLbCookieStickinessPolicy"></a>

Contains information about a stickiness policy that was created using `CreateLBCookieStickinessPolicy`.

## Contents
<a name="API_AwsElbLbCookieStickinessPolicy_Contents"></a>

 ** CookieExpirationPeriod **   <a name="securityhub-Type-AwsElbLbCookieStickinessPolicy-CookieExpirationPeriod"></a>
The amount of time, in seconds, after which the cookie is considered stale. If an expiration period is not specified, the stickiness session lasts for the duration of the browser session.
Type: Long
Required: No

 ** PolicyName **   <a name="securityhub-Type-AwsElbLbCookieStickinessPolicy-PolicyName"></a>
The name of the policy. The name must be unique within the set of policies for the load balancer.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsElbLbCookieStickinessPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsElbLbCookieStickinessPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsElbLbCookieStickinessPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsElbLbCookieStickinessPolicy)
