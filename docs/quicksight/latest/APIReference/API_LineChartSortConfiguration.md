---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_LineChartSortConfiguration.html
---

# LineChartSortConfiguration
<a name="API_LineChartSortConfiguration"></a>

The sort configuration of a line chart.

## Contents
<a name="API_LineChartSortConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** CategoryItemsLimitConfiguration **   <a name="QS-Type-LineChartSortConfiguration-CategoryItemsLimitConfiguration"></a>
The limit on the number of categories that are displayed in a line chart.
Type: [ItemsLimitConfiguration](API_ItemsLimitConfiguration.md) object
Required: No

 ** CategorySort **   <a name="QS-Type-LineChartSortConfiguration-CategorySort"></a>
The sort configuration of the category fields.
Type: Array of [FieldSortOptions](API_FieldSortOptions.md) objects
Array Members: Maximum number of 100 items.
Required: No

 ** ColorItemsLimitConfiguration **   <a name="QS-Type-LineChartSortConfiguration-ColorItemsLimitConfiguration"></a>
The limit on the number of lines that are displayed in a line chart.
Type: [ItemsLimitConfiguration](API_ItemsLimitConfiguration.md) object
Required: No

 ** SmallMultiplesLimitConfiguration **   <a name="QS-Type-LineChartSortConfiguration-SmallMultiplesLimitConfiguration"></a>
The limit on the number of small multiples panels that are displayed.
Type: [ItemsLimitConfiguration](API_ItemsLimitConfiguration.md) object
Required: No

 ** SmallMultiplesSort **   <a name="QS-Type-LineChartSortConfiguration-SmallMultiplesSort"></a>
The sort configuration of the small multiples field.
Type: Array of [FieldSortOptions](API_FieldSortOptions.md) objects
Array Members: Maximum number of 100 items.
Required: No

## See Also
<a name="API_LineChartSortConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/LineChartSortConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/LineChartSortConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/LineChartSortConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
