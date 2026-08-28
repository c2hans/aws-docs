---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_TimeSeriesDataPointSummaryFormOutput.html
---

# TimeSeriesDataPointSummaryFormOutput
<a name="API_TimeSeriesDataPointSummaryFormOutput"></a>

The summary of the time series data points form.

## Contents
<a name="API_TimeSeriesDataPointSummaryFormOutput_Contents"></a>

 ** formName **   <a name="datazone-Type-TimeSeriesDataPointSummaryFormOutput-formName"></a>
The name of the time series data points summary form.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** timestamp **   <a name="datazone-Type-TimeSeriesDataPointSummaryFormOutput-timestamp"></a>
The timestamp of the time series data points summary form.
Type: Timestamp
Required: Yes

 ** typeIdentifier **   <a name="datazone-Type-TimeSeriesDataPointSummaryFormOutput-typeIdentifier"></a>
The type ID of the time series data points summary form.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 385.
Pattern: `(?!\.)[\w\.]*\w`
Required: Yes

 ** contentSummary **   <a name="datazone-Type-TimeSeriesDataPointSummaryFormOutput-contentSummary"></a>
The content of the summary of the time series data points form.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 20000.
Required: No

 ** id **   <a name="datazone-Type-TimeSeriesDataPointSummaryFormOutput-id"></a>
The ID of the time series data points summary form.
Type: String
Pattern: `[a-zA-Z0-9_-]{0,36}`
Required: No

 ** typeRevision **   <a name="datazone-Type-TimeSeriesDataPointSummaryFormOutput-typeRevision"></a>
The type revision of the time series data points summary form.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

## See Also
<a name="API_TimeSeriesDataPointSummaryFormOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/TimeSeriesDataPointSummaryFormOutput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/TimeSeriesDataPointSummaryFormOutput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/TimeSeriesDataPointSummaryFormOutput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
