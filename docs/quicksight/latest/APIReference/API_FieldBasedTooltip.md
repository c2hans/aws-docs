---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_FieldBasedTooltip.html
---

# FieldBasedTooltip
<a name="API_FieldBasedTooltip"></a>

The setup for the detailed tooltip.

## Contents
<a name="API_FieldBasedTooltip_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AggregationVisibility **   <a name="QS-Type-FieldBasedTooltip-AggregationVisibility"></a>
The visibility of `Show aggregations`.
Type: String
Valid Values: `HIDDEN | VISIBLE`
Required: No

 ** TooltipFields **   <a name="QS-Type-FieldBasedTooltip-TooltipFields"></a>
The fields configuration in the tooltip.
Type: Array of [TooltipItem](API_TooltipItem.md) objects
Array Members: Maximum number of 100 items.
Required: No

 ** TooltipTitleType **   <a name="QS-Type-FieldBasedTooltip-TooltipTitleType"></a>
The type for the >tooltip title. Choose one of the following options:
+  `NONE`: Doesn't use the primary value as the title.
+  `PRIMARY_VALUE`: Uses primary value as the title.
Type: String
Valid Values: `NONE | PRIMARY_VALUE`
Required: No

## See Also
<a name="API_FieldBasedTooltip_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/FieldBasedTooltip)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/FieldBasedTooltip)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/FieldBasedTooltip)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
