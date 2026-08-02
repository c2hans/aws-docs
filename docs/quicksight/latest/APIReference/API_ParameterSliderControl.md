---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ParameterSliderControl.html
---

# ParameterSliderControl
<a name="API_ParameterSliderControl"></a>

A control to display a horizontal toggle bar. This is used to change a value by sliding the toggle.

## Contents
<a name="API_ParameterSliderControl_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** MaximumValue **   <a name="QS-Type-ParameterSliderControl-MaximumValue"></a>
The larger value that is displayed at the right of the slider.
Type: Double
Required: Yes

 ** MinimumValue **   <a name="QS-Type-ParameterSliderControl-MinimumValue"></a>
The smaller value that is displayed at the left of the slider.
Type: Double
Required: Yes

 ** ParameterControlId **   <a name="QS-Type-ParameterSliderControl-ParameterControlId"></a>
The ID of the `ParameterSliderControl`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: Yes

 ** SourceParameterName **   <a name="QS-Type-ParameterSliderControl-SourceParameterName"></a>
The source parameter name of the `ParameterSliderControl`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^[a-zA-Z0-9]+$`
Required: Yes

 ** StepSize **   <a name="QS-Type-ParameterSliderControl-StepSize"></a>
The number of increments that the slider bar is divided into.
Type: Double
Required: Yes

 ** ControlTitleFormatText **   <a name="QS-Type-ParameterSliderControl-ControlTitleFormatText"></a>
The title text format configuration for the control.
Type: [ControlTitleFormatText](API_ControlTitleFormatText.md) object
Required: No

 ** DisplayOptions **   <a name="QS-Type-ParameterSliderControl-DisplayOptions"></a>
The display options of a control.
Type: [SliderControlDisplayOptions](API_SliderControlDisplayOptions.md) object
Required: No

 ** Title **   <a name="QS-Type-ParameterSliderControl-Title"></a>
The title of the `ParameterSliderControl`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

## See Also
<a name="API_ParameterSliderControl_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/ParameterSliderControl)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/ParameterSliderControl)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/ParameterSliderControl)
