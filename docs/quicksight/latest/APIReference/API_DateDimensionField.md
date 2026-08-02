---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DateDimensionField.html
---

# DateDimensionField
<a name="API_DateDimensionField"></a>

The dimension type field with date type columns.

## Contents
<a name="API_DateDimensionField_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Column **   <a name="QS-Type-DateDimensionField-Column"></a>
The column that is used in the `DateDimensionField`.
Type: [ColumnIdentifier](API_ColumnIdentifier.md) object
Required: Yes

 ** FieldId **   <a name="QS-Type-DateDimensionField-FieldId"></a>
The custom field ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: Yes

 ** DateGranularity **   <a name="QS-Type-DateDimensionField-DateGranularity"></a>
The date granularity of the `DateDimensionField`. Choose one of the following options:
+  `YEAR`
+  `QUARTER`
+  `MONTH`
+  `WEEK`
+  `DAY`
+  `HOUR`
+  `MINUTE`
+  `SECOND`
+  `MILLISECOND`
Type: String
Valid Values: `YEAR | QUARTER | MONTH | WEEK | DAY | HOUR | MINUTE | SECOND | MILLISECOND`
Required: No

 ** FormatConfiguration **   <a name="QS-Type-DateDimensionField-FormatConfiguration"></a>
The format configuration of the field.
Type: [DateTimeFormatConfiguration](API_DateTimeFormatConfiguration.md) object
Required: No

 ** HierarchyId **   <a name="QS-Type-DateDimensionField-HierarchyId"></a>
The custom hierarchy ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

## See Also
<a name="API_DateDimensionField_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/DateDimensionField)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/DateDimensionField)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/DateDimensionField)
