---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DateMeasureField.html
---

# DateMeasureField
<a name="API_DateMeasureField"></a>

The measure type field with date type columns.

## Contents
<a name="API_DateMeasureField_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Column **   <a name="QS-Type-DateMeasureField-Column"></a>
The column that is used in the `DateMeasureField`.
Type: [ColumnIdentifier](API_ColumnIdentifier.md) object
Required: Yes

 ** FieldId **   <a name="QS-Type-DateMeasureField-FieldId"></a>
The custom field ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: Yes

 ** AggregationFunction **   <a name="QS-Type-DateMeasureField-AggregationFunction"></a>
The aggregation function of the measure field.
Type: String
Valid Values: `COUNT | DISTINCT_COUNT | MIN | MAX`
Required: No

 ** FormatConfiguration **   <a name="QS-Type-DateMeasureField-FormatConfiguration"></a>
The format configuration of the field.
Type: [DateTimeFormatConfiguration](API_DateTimeFormatConfiguration.md) object
Required: No

## See Also
<a name="API_DateMeasureField_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/DateMeasureField)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/DateMeasureField)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/DateMeasureField)
