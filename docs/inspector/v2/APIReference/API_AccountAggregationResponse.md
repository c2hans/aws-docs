---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_AccountAggregationResponse.html
---

# AccountAggregationResponse
<a name="API_AccountAggregationResponse"></a>

An aggregation of findings by AWS account ID.

## Contents
<a name="API_AccountAggregationResponse_Contents"></a>

 ** accountId **   <a name="inspector2-Type-AccountAggregationResponse-accountId"></a>
The AWS account ID.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: No

 ** exploitAvailableCount **   <a name="inspector2-Type-AccountAggregationResponse-exploitAvailableCount"></a>
 The number of findings that have an exploit available.
Type: Long
Required: No

 ** fixAvailableCount **   <a name="inspector2-Type-AccountAggregationResponse-fixAvailableCount"></a>
 Details about the number of fixes.
Type: Long
Required: No

 ** severityCounts **   <a name="inspector2-Type-AccountAggregationResponse-severityCounts"></a>
The number of findings by severity.
Type: [SeverityCounts](API_SeverityCounts.md) object
Required: No

## See Also
<a name="API_AccountAggregationResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/AccountAggregationResponse)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/AccountAggregationResponse)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/AccountAggregationResponse)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Inspector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
