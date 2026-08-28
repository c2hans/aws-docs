---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_Recommendation.html
---

# Recommendation
<a name="API_Recommendation"></a>

A recommendation on how to remediate the issue identified in a finding.

## Contents
<a name="API_Recommendation_Contents"></a>

 ** Text **   <a name="securityhub-Type-Recommendation-Text"></a>
Describes the recommended steps to take to remediate an issue identified in a finding.
Length Constraints: Minimum of 1 length. Maximum of 512 length.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Url **   <a name="securityhub-Type-Recommendation-Url"></a>
A URL to a page or site that contains information about how to remediate a finding.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_Recommendation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/Recommendation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/Recommendation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/Recommendation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
