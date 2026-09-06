---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_TimeSeriesDataPointFormOutput.html
---

# TimeSeriesDataPointFormOutput
<a name="API_TimeSeriesDataPointFormOutput"></a>

The time series data points form.

## Contents
<a name="API_TimeSeriesDataPointFormOutput_Contents"></a>

 ** formName **   <a name="datazone-Type-TimeSeriesDataPointFormOutput-formName"></a>
The name of the time series data points form.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** timestamp **   <a name="datazone-Type-TimeSeriesDataPointFormOutput-timestamp"></a>
The timestamp of the time series data points form.
Type: Timestamp
Required: Yes

 ** typeIdentifier **   <a name="datazone-Type-TimeSeriesDataPointFormOutput-typeIdentifier"></a>
The ID of the type of the time series data points form.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 385.
Pattern: `(?!\.)[\w\.]*\w`
Required: Yes

 ** content **   <a name="datazone-Type-TimeSeriesDataPointFormOutput-content"></a>
The content of the time series data points form.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500000.
Required: No

 ** id **   <a name="datazone-Type-TimeSeriesDataPointFormOutput-id"></a>
The ID of the time series data points form.
Type: String
Pattern: `[a-zA-Z0-9_-]{0,36}`
Required: No

 ** typeRevision **   <a name="datazone-Type-TimeSeriesDataPointFormOutput-typeRevision"></a>
The revision type of the time series data points form.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

## See Also
<a name="API_TimeSeriesDataPointFormOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/TimeSeriesDataPointFormOutput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/TimeSeriesDataPointFormOutput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/TimeSeriesDataPointFormOutput)
