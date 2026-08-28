---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsElbLoadBalancerPolicies.html
---

# AwsElbLoadBalancerPolicies
<a name="API_AwsElbLoadBalancerPolicies"></a>

Contains information about the policies for a load balancer.

## Contents
<a name="API_AwsElbLoadBalancerPolicies_Contents"></a>

 ** AppCookieStickinessPolicies **   <a name="securityhub-Type-AwsElbLoadBalancerPolicies-AppCookieStickinessPolicies"></a>
The stickiness policies that are created using `CreateAppCookieStickinessPolicy`.
Type: Array of [AwsElbAppCookieStickinessPolicy](API_AwsElbAppCookieStickinessPolicy.md) objects
Required: No

 ** LbCookieStickinessPolicies **   <a name="securityhub-Type-AwsElbLoadBalancerPolicies-LbCookieStickinessPolicies"></a>
The stickiness policies that are created using `CreateLBCookieStickinessPolicy`.
Type: Array of [AwsElbLbCookieStickinessPolicy](API_AwsElbLbCookieStickinessPolicy.md) objects
Required: No

 ** OtherPolicies **   <a name="securityhub-Type-AwsElbLoadBalancerPolicies-OtherPolicies"></a>
The policies other than the stickiness policies.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsElbLoadBalancerPolicies_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsElbLoadBalancerPolicies)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsElbLoadBalancerPolicies)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsElbLoadBalancerPolicies)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
