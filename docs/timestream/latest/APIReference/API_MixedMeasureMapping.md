---
source_url: https://docs.aws.amazon.com/timestream/latest/APIReference/API_MixedMeasureMapping.html
---

# MixedMeasureMapping
<a name="API_MixedMeasureMapping"></a>

## Contents
<a name="API_MixedMeasureMapping_Contents"></a>

 ** MeasureValueType **   <a name="timestream-Type-MixedMeasureMapping-MeasureValueType"></a>

Type: String
Valid Values: `DOUBLE | BIGINT | VARCHAR | BOOLEAN | TIMESTAMP | MULTI`
Required: Yes

 ** MeasureName **   <a name="timestream-Type-MixedMeasureMapping-MeasureName"></a>

Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** MultiMeasureAttributeMappings **   <a name="timestream-Type-MixedMeasureMapping-MultiMeasureAttributeMappings"></a>

Type: Array of [MultiMeasureAttributeMapping](API_MultiMeasureAttributeMapping.md) objects
Array Members: Minimum number of 1 item.
Required: No

 ** SourceColumn **   <a name="timestream-Type-MixedMeasureMapping-SourceColumn"></a>

Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** TargetMeasureName **   <a name="timestream-Type-MixedMeasureMapping-TargetMeasureName"></a>

Type: String
Length Constraints: Minimum length of 1.
Required: No

## See Also
<a name="API_MixedMeasureMapping_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/timestream-write-2018-11-01/MixedMeasureMapping)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/timestream-write-2018-11-01/MixedMeasureMapping)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/timestream-write-2018-11-01/MixedMeasureMapping)
