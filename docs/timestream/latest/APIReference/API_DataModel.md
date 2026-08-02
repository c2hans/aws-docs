---
source_url: https://docs.aws.amazon.com/timestream/latest/APIReference/API_DataModel.html
---

# DataModel
<a name="API_DataModel"></a>

Data model for a batch load task.

## Contents
<a name="API_DataModel_Contents"></a>

 ** DimensionMappings **   <a name="timestream-Type-DataModel-DimensionMappings"></a>
Source to target mappings for dimensions.
Type: Array of [DimensionMapping](API_DimensionMapping.md) objects
Array Members: Minimum number of 1 item.
Required: Yes

 ** MeasureNameColumn **   <a name="timestream-Type-DataModel-MeasureNameColumn"></a>

Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** MixedMeasureMappings **   <a name="timestream-Type-DataModel-MixedMeasureMappings"></a>
Source to target mappings for measures.
Type: Array of [MixedMeasureMapping](API_MixedMeasureMapping.md) objects
Array Members: Minimum number of 1 item.
Required: No

 ** MultiMeasureMappings **   <a name="timestream-Type-DataModel-MultiMeasureMappings"></a>
Source to target mappings for multi-measure records.
Type: [MultiMeasureMappings](API_MultiMeasureMappings.md) object
Required: No

 ** TimeColumn **   <a name="timestream-Type-DataModel-TimeColumn"></a>
Source column to be mapped to time.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** TimeUnit **   <a name="timestream-Type-DataModel-TimeUnit"></a>
 The granularity of the timestamp unit. It indicates if the time value is in seconds, milliseconds, nanoseconds, or other supported values. Default is `MILLISECONDS`.
Type: String
Valid Values: `MILLISECONDS | SECONDS | MICROSECONDS | NANOSECONDS`
Required: No

## See Also
<a name="API_DataModel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/timestream-write-2018-11-01/DataModel)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/timestream-write-2018-11-01/DataModel)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/timestream-write-2018-11-01/DataModel)
