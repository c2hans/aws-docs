---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_NumericalMeasureField.html
---

# NumericalMeasureField
<a name="API_NumericalMeasureField"></a>

The measure type field with numerical type columns.

## Contents
<a name="API_NumericalMeasureField_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Column **   <a name="QS-Type-NumericalMeasureField-Column"></a>
The column that is used in the `NumericalMeasureField`.
Type: [ColumnIdentifier](API_ColumnIdentifier.md) object
Required: Yes

 ** FieldId **   <a name="QS-Type-NumericalMeasureField-FieldId"></a>
The custom field ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: Yes

 ** AggregationFunction **   <a name="QS-Type-NumericalMeasureField-AggregationFunction"></a>
The aggregation function of the measure field.
Type: [NumericalAggregationFunction](API_NumericalAggregationFunction.md) object
Required: No

 ** FormatConfiguration **   <a name="QS-Type-NumericalMeasureField-FormatConfiguration"></a>
The format configuration of the field.
Type: [NumberFormatConfiguration](API_NumberFormatConfiguration.md) object
Required: No

## See Also
<a name="API_NumericalMeasureField_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/NumericalMeasureField)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/NumericalMeasureField)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/NumericalMeasureField)
