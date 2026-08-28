---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_GeospatialGradientColor.html
---

# GeospatialGradientColor
<a name="API_GeospatialGradientColor"></a>

The definition for a gradient color.

## Contents
<a name="API_GeospatialGradientColor_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** StepColors **   <a name="QS-Type-GeospatialGradientColor-StepColors"></a>
A list of gradient step colors for the gradient.
Type: Array of [GeospatialGradientStepColor](API_GeospatialGradientStepColor.md) objects
Array Members: Minimum number of 2 items. Maximum number of 3 items.
Required: Yes

 ** DefaultOpacity **   <a name="QS-Type-GeospatialGradientColor-DefaultOpacity"></a>
The default opacity for the gradient color.
Type: Double
Valid Range: Minimum value of 0. Maximum value of 1.
Required: No

 ** NullDataSettings **   <a name="QS-Type-GeospatialGradientColor-NullDataSettings"></a>
The null data visualization settings.
Type: [GeospatialNullDataSettings](API_GeospatialNullDataSettings.md) object
Required: No

 ** NullDataVisibility **   <a name="QS-Type-GeospatialGradientColor-NullDataVisibility"></a>
The state of visibility for null data.
Type: String
Valid Values: `HIDDEN | VISIBLE`
Required: No

## See Also
<a name="API_GeospatialGradientColor_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/GeospatialGradientColor)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/GeospatialGradientColor)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/GeospatialGradientColor)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
