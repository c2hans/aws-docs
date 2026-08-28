---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_TitleAggregationResponse.html
---

# TitleAggregationResponse
<a name="API_TitleAggregationResponse"></a>

A response that contains details on the results of a finding aggregation by title.

## Contents
<a name="API_TitleAggregationResponse_Contents"></a>

 ** title **   <a name="inspector2-Type-TitleAggregationResponse-title"></a>
The title that the findings were aggregated on.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** accountId **   <a name="inspector2-Type-TitleAggregationResponse-accountId"></a>
The ID of the AWS account associated with the findings.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: No

 ** severityCounts **   <a name="inspector2-Type-TitleAggregationResponse-severityCounts"></a>
An object that represent the count of matched findings per severity.
Type: [SeverityCounts](API_SeverityCounts.md) object
Required: No

 ** vulnerabilityId **   <a name="inspector2-Type-TitleAggregationResponse-vulnerabilityId"></a>
The vulnerability ID of the finding.
Type: String
Required: No

## See Also
<a name="API_TitleAggregationResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/TitleAggregationResponse)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/TitleAggregationResponse)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/TitleAggregationResponse)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Inspector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
