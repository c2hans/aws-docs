---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_CategoricalMeasureField.html
---

# CategoricalMeasureField
<a name="API_CategoricalMeasureField"></a>

The measure type field with categorical type columns.

## Contents
<a name="API_CategoricalMeasureField_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Column **   <a name="QS-Type-CategoricalMeasureField-Column"></a>
The column that is used in the `CategoricalMeasureField`.
Type: [ColumnIdentifier](API_ColumnIdentifier.md) object
Required: Yes

 ** FieldId **   <a name="QS-Type-CategoricalMeasureField-FieldId"></a>
The custom field ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: Yes

 ** AggregationFunction **   <a name="QS-Type-CategoricalMeasureField-AggregationFunction"></a>
The aggregation function of the measure field.
Type: String
Valid Values: `COUNT | DISTINCT_COUNT`
Required: No

 ** FormatConfiguration **   <a name="QS-Type-CategoricalMeasureField-FormatConfiguration"></a>
The format configuration of the field.
Type: [StringFormatConfiguration](API_StringFormatConfiguration.md) object
Required: No

## See Also
<a name="API_CategoricalMeasureField_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/CategoricalMeasureField)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/CategoricalMeasureField)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/CategoricalMeasureField)
