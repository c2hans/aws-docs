---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_DifferentialPrivacyPreviewAggregation.html
---

# DifferentialPrivacyPreviewAggregation
<a name="API_DifferentialPrivacyPreviewAggregation"></a>

Provides an estimate of the number of aggregation functions that the member who can query can run given the epsilon and noise parameters.

## Contents
<a name="API_DifferentialPrivacyPreviewAggregation_Contents"></a>

 ** maxCount **   <a name="API-Type-DifferentialPrivacyPreviewAggregation-maxCount"></a>
The maximum number of aggregations that the member who can query can run given the epsilon and noise parameters.
Type: Integer
Valid Range: Minimum value of 0.
Required: Yes

 ** type **   <a name="API-Type-DifferentialPrivacyPreviewAggregation-type"></a>
The type of aggregation function.
Type: String
Valid Values: `AVG | COUNT | COUNT_DISTINCT | SUM | STDDEV`
Required: Yes

## See Also
<a name="API_DifferentialPrivacyPreviewAggregation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/DifferentialPrivacyPreviewAggregation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/DifferentialPrivacyPreviewAggregation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/DifferentialPrivacyPreviewAggregation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
