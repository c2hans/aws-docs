---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_PluginVisualFieldWell.html
---

# PluginVisualFieldWell
<a name="API_PluginVisualFieldWell"></a>

A collection of field wells for a plugin visual.

## Contents
<a name="API_PluginVisualFieldWell_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AxisName **   <a name="QS-Type-PluginVisualFieldWell-AxisName"></a>
The semantic axis name for the field well.
Type: String
Valid Values: `GROUP_BY | VALUE`
Required: No

 ** Dimensions **   <a name="QS-Type-PluginVisualFieldWell-Dimensions"></a>
A list of dimensions for the field well.
Type: Array of [DimensionField](API_DimensionField.md) objects
Array Members: Maximum number of 200 items.
Required: No

 ** Measures **   <a name="QS-Type-PluginVisualFieldWell-Measures"></a>
A list of measures that exist in the field well.
Type: Array of [MeasureField](API_MeasureField.md) objects
Array Members: Maximum number of 200 items.
Required: No

 ** Unaggregated **   <a name="QS-Type-PluginVisualFieldWell-Unaggregated"></a>
A list of unaggregated fields that exist in the field well.
Type: Array of [UnaggregatedField](API_UnaggregatedField.md) objects
Array Members: Maximum number of 200 items.
Required: No

## See Also
<a name="API_PluginVisualFieldWell_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/PluginVisualFieldWell)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/PluginVisualFieldWell)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/PluginVisualFieldWell)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
