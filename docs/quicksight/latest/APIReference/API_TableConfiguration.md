---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_TableConfiguration.html
---

# TableConfiguration
<a name="API_TableConfiguration"></a>

The configuration for a `TableVisual`.

## Contents
<a name="API_TableConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** DashboardCustomizationVisualOptions **   <a name="QS-Type-TableConfiguration-DashboardCustomizationVisualOptions"></a>
The options that define customizations available to dashboard readers for a specific visual
Type: [DashboardCustomizationVisualOptions](API_DashboardCustomizationVisualOptions.md) object
Required: No

 ** FieldOptions **   <a name="QS-Type-TableConfiguration-FieldOptions"></a>
The field options for a table visual.
Type: [TableFieldOptions](API_TableFieldOptions.md) object
Required: No

 ** FieldWells **   <a name="QS-Type-TableConfiguration-FieldWells"></a>
The field wells of the visual.
Type: [TableFieldWells](API_TableFieldWells.md) object
Required: No

 ** Interactions **   <a name="QS-Type-TableConfiguration-Interactions"></a>
The general visual interactions setup for a visual.
Type: [VisualInteractionOptions](API_VisualInteractionOptions.md) object
Required: No

 ** PaginatedReportOptions **   <a name="QS-Type-TableConfiguration-PaginatedReportOptions"></a>
The paginated report options for a table visual.
Type: [TablePaginatedReportOptions](API_TablePaginatedReportOptions.md) object
Required: No

 ** SortConfiguration **   <a name="QS-Type-TableConfiguration-SortConfiguration"></a>
The sort configuration for a `TableVisual`.
Type: [TableSortConfiguration](API_TableSortConfiguration.md) object
Required: No

 ** TableInlineVisualizations **   <a name="QS-Type-TableConfiguration-TableInlineVisualizations"></a>
A collection of inline visualizations to display within a chart.
Type: Array of [TableInlineVisualization](API_TableInlineVisualization.md) objects
Array Members: Maximum number of 200 items.
Required: No

 ** TableOptions **   <a name="QS-Type-TableConfiguration-TableOptions"></a>
The table options for a table visual.
Type: [TableOptions](API_TableOptions.md) object
Required: No

 ** Tooltip **   <a name="QS-Type-TableConfiguration-Tooltip"></a>
The display options for the visual tooltip.
Type: [TooltipOptions](API_TooltipOptions.md) object
Required: No

 ** TotalOptions **   <a name="QS-Type-TableConfiguration-TotalOptions"></a>
The total options for a table visual.
Type: [TotalOptions](API_TotalOptions.md) object
Required: No

## See Also
<a name="API_TableConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/TableConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/TableConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/TableConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
