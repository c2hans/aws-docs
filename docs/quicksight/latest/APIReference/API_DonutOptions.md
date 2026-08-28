---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DonutOptions.html
---

# DonutOptions
<a name="API_DonutOptions"></a>

The options for configuring a donut chart or pie chart.

## Contents
<a name="API_DonutOptions_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ArcOptions **   <a name="QS-Type-DonutOptions-ArcOptions"></a>
The option for define the arc of the chart shape. Valid values are as follows:
+  `WHOLE` - A pie chart
+  `SMALL`- A small-sized donut chart
+  `MEDIUM`- A medium-sized donut chart
+  `LARGE`- A large-sized donut chart
Type: [ArcOptions](API_ArcOptions.md) object
Required: No

 ** DonutCenterOptions **   <a name="QS-Type-DonutOptions-DonutCenterOptions"></a>
The label options of the label that is displayed in the center of a donut chart. This option isn't available for pie charts.
Type: [DonutCenterOptions](API_DonutCenterOptions.md) object
Required: No

## See Also
<a name="API_DonutOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/DonutOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/DonutOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/DonutOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
