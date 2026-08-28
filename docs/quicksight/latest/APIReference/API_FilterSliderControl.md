---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_FilterSliderControl.html
---

# FilterSliderControl
<a name="API_FilterSliderControl"></a>

A control to display a horizontal toggle bar. This is used to change a value by sliding the toggle.

## Contents
<a name="API_FilterSliderControl_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** FilterControlId **   <a name="QS-Type-FilterSliderControl-FilterControlId"></a>
The ID of the `FilterSliderControl`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: Yes

 ** MaximumValue **   <a name="QS-Type-FilterSliderControl-MaximumValue"></a>
The larger value that is displayed at the right of the slider.
Type: Double
Required: Yes

 ** MinimumValue **   <a name="QS-Type-FilterSliderControl-MinimumValue"></a>
The smaller value that is displayed at the left of the slider.
Type: Double
Required: Yes

 ** SourceFilterId **   <a name="QS-Type-FilterSliderControl-SourceFilterId"></a>
The source filter ID of the `FilterSliderControl`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: Yes

 ** StepSize **   <a name="QS-Type-FilterSliderControl-StepSize"></a>
The number of increments that the slider bar is divided into.
Type: Double
Required: Yes

 ** ControlTitleFormatText **   <a name="QS-Type-FilterSliderControl-ControlTitleFormatText"></a>
The title text format configuration for the control.
Type: [ControlTitleFormatText](API_ControlTitleFormatText.md) object
Required: No

 ** DisplayOptions **   <a name="QS-Type-FilterSliderControl-DisplayOptions"></a>
The display options of a control.
Type: [SliderControlDisplayOptions](API_SliderControlDisplayOptions.md) object
Required: No

 ** Title **   <a name="QS-Type-FilterSliderControl-Title"></a>
The title of the `FilterSliderControl`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

 ** Type **   <a name="QS-Type-FilterSliderControl-Type"></a>
The type of the `FilterSliderControl`. Choose one of the following options:
+  `SINGLE_POINT`: Filter against(equals) a single data point.
+  `RANGE`: Filter data that is in a specified range.
Type: String
Valid Values: `SINGLE_POINT | RANGE`
Required: No

## See Also
<a name="API_FilterSliderControl_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/FilterSliderControl)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/FilterSliderControl)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/FilterSliderControl)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
