---
source_url: https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_InsightSelector.html
---

# InsightSelector
<a name="API_InsightSelector"></a>

A JSON string that contains a list of Insights types that are logged on a trail or event data store.

## Contents
<a name="API_InsightSelector_Contents"></a>

 ** EventCategories **   <a name="awscloudtrail-Type-InsightSelector-EventCategories"></a>
Select the event category on which Insights should be enabled.
+ If EventCategories is not provided, the specified Insights types are enabled on management API calls by default.
+ If EventCategories is provided, the given event categories will overwrite the existing ones. For example, if a trail already has Insights enabled on management events, and then a PutInsightSelectors request is made with only data events specified in EventCategories, Insights on management events will be disabled.
Type: Array of strings
Valid Values: `Management | Data`
Required: No

 ** InsightType **   <a name="awscloudtrail-Type-InsightSelector-InsightType"></a>
The type of Insights events to log on a trail or event data store. `ApiCallRateInsight` and `ApiErrorRateInsight` are valid Insight types.
The `ApiCallRateInsight` Insights type analyzes write-only management API calls or read and write data API calls that are aggregated per minute against a baseline API call volume.
The `ApiErrorRateInsight` Insights type analyzes management and data API calls that result in error codes. The error is shown if the API call is unsuccessful.
Type: String
Valid Values: `ApiCallRateInsight | ApiErrorRateInsight`
Required: No

## See Also
<a name="API_InsightSelector_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/InsightSelector)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/InsightSelector)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/InsightSelector)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudTrail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query awscloudtrail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
