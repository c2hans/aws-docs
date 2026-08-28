---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DefaultSliderControlOptions.html
---

# DefaultSliderControlOptions
<a name="API_DefaultSliderControlOptions"></a>

The default options that correspond to the `Slider` filter control type.

## Contents
<a name="API_DefaultSliderControlOptions_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** MaximumValue **   <a name="QS-Type-DefaultSliderControlOptions-MaximumValue"></a>
The larger value that is displayed at the right of the slider.
Type: Double
Required: Yes

 ** MinimumValue **   <a name="QS-Type-DefaultSliderControlOptions-MinimumValue"></a>
The smaller value that is displayed at the left of the slider.
Type: Double
Required: Yes

 ** StepSize **   <a name="QS-Type-DefaultSliderControlOptions-StepSize"></a>
The number of increments that the slider bar is divided into.
Type: Double
Required: Yes

 ** DisplayOptions **   <a name="QS-Type-DefaultSliderControlOptions-DisplayOptions"></a>
The display options of a control.
Type: [SliderControlDisplayOptions](API_SliderControlDisplayOptions.md) object
Required: No

 ** Type **   <a name="QS-Type-DefaultSliderControlOptions-Type"></a>
The type of the `DefaultSliderControlOptions`. Choose one of the following options:
+  `SINGLE_POINT`: Filter against(equals) a single data point.
+  `RANGE`: Filter data that is in a specified range.
Type: String
Valid Values: `SINGLE_POINT | RANGE`
Required: No

## See Also
<a name="API_DefaultSliderControlOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/DefaultSliderControlOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/DefaultSliderControlOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/DefaultSliderControlOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
