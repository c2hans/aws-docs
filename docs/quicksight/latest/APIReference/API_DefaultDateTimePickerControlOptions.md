---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DefaultDateTimePickerControlOptions.html
---

# DefaultDateTimePickerControlOptions
<a name="API_DefaultDateTimePickerControlOptions"></a>

The default options that correspond to the filter control type of a `DateTimePicker`.

## Contents
<a name="API_DefaultDateTimePickerControlOptions_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** CommitMode **   <a name="QS-Type-DefaultDateTimePickerControlOptions-CommitMode"></a>
The visibility configuration of the Apply button on a `DateTimePickerControl`.
Type: String
Valid Values: `AUTO | MANUAL`
Required: No

 ** DisplayOptions **   <a name="QS-Type-DefaultDateTimePickerControlOptions-DisplayOptions"></a>
The display options of a control.
Type: [DateTimePickerControlDisplayOptions](API_DateTimePickerControlDisplayOptions.md) object
Required: No

 ** Type **   <a name="QS-Type-DefaultDateTimePickerControlOptions-Type"></a>
The date time picker type of the `DefaultDateTimePickerControlOptions`. Choose one of the following options:
+  `SINGLE_VALUED`: The filter condition is a fixed date.
+  `DATE_RANGE`: The filter condition is a date time range.
Type: String
Valid Values: `SINGLE_VALUED | DATE_RANGE`
Required: No

## See Also
<a name="API_DefaultDateTimePickerControlOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/DefaultDateTimePickerControlOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/DefaultDateTimePickerControlOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/DefaultDateTimePickerControlOptions)
