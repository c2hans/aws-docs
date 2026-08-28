---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_TimeSeriesDataPointFormInput.html
---

# TimeSeriesDataPointFormInput
<a name="API_TimeSeriesDataPointFormInput"></a>

The time series data points form.

## Contents
<a name="API_TimeSeriesDataPointFormInput_Contents"></a>

 ** formName **   <a name="datazone-Type-TimeSeriesDataPointFormInput-formName"></a>
The name of the time series data points form.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** timestamp **   <a name="datazone-Type-TimeSeriesDataPointFormInput-timestamp"></a>
The timestamp of the time series data points form.
Type: Timestamp
Required: Yes

 ** typeIdentifier **   <a name="datazone-Type-TimeSeriesDataPointFormInput-typeIdentifier"></a>
The ID of the type of the time series data points form.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 385.
Pattern: `(?!\.)[\w\.]*\w`
Required: Yes

 ** content **   <a name="datazone-Type-TimeSeriesDataPointFormInput-content"></a>
The content of the time series data points form.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500000.
Required: No

 ** typeRevision **   <a name="datazone-Type-TimeSeriesDataPointFormInput-typeRevision"></a>
The revision type of the time series data points form.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

## See Also
<a name="API_TimeSeriesDataPointFormInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/TimeSeriesDataPointFormInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/TimeSeriesDataPointFormInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/TimeSeriesDataPointFormInput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
