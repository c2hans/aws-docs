---
source_url: https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_RecommendationResourceExclusion.html
---

# RecommendationResourceExclusion
<a name="API_RecommendationResourceExclusion"></a>

The request entry for Recommendation Resource exclusion. Each entry is a combination of Recommendation Resource ARN and corresponding exclusion status

## Contents
<a name="API_RecommendationResourceExclusion_Contents"></a>

 ** arn **   <a name="ta-Type-RecommendationResourceExclusion-arn"></a>
The ARN of the Recommendation Resource
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[\w-]+:trustedadvisor::\d{12}:recommendation-resource\/[\w-]+\/[\w-]+`
Required: Yes

 ** isExcluded **   <a name="ta-Type-RecommendationResourceExclusion-isExcluded"></a>
The exclusion status
Type: Boolean
Required: Yes

## See Also
<a name="API_RecommendationResourceExclusion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/trustedadvisor-2022-09-15/RecommendationResourceExclusion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/trustedadvisor-2022-09-15/RecommendationResourceExclusion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/trustedadvisor-2022-09-15/RecommendationResourceExclusion)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Trusted Advisor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query trustedadvisor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
