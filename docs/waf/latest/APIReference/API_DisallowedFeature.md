---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_DisallowedFeature.html
---

# DisallowedFeature
<a name="API_DisallowedFeature"></a>

A AWS WAF feature that is not supported by the CloudFront pricing plan associated with the web ACL.

## Contents
<a name="API_DisallowedFeature_Contents"></a>

 ** Feature **   <a name="WAF-Type-DisallowedFeature-Feature"></a>
The name of the disallowed AWS WAF feature.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[\w\-]+$`
Required: No

 ** RequiredPricingPlan **   <a name="WAF-Type-DisallowedFeature-RequiredPricingPlan"></a>
The name of the CloudFront pricing plan required to use the AWS WAF feature.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[\w\-]+$`
Required: No

## See Also
<a name="API_DisallowedFeature_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/DisallowedFeature)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/DisallowedFeature)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/DisallowedFeature)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
