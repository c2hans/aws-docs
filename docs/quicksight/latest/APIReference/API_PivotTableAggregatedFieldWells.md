---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_PivotTableAggregatedFieldWells.html
---

# PivotTableAggregatedFieldWells
<a name="API_PivotTableAggregatedFieldWells"></a>

The aggregated field well for the pivot table.

## Contents
<a name="API_PivotTableAggregatedFieldWells_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Columns **   <a name="QS-Type-PivotTableAggregatedFieldWells-Columns"></a>
The columns field well for a pivot table. Values are grouped by columns fields.
Type: Array of [DimensionField](API_DimensionField.md) objects
Array Members: Maximum number of 40 items.
Required: No

 ** Rows **   <a name="QS-Type-PivotTableAggregatedFieldWells-Rows"></a>
The rows field well for a pivot table. Values are grouped by rows fields.
Type: Array of [DimensionField](API_DimensionField.md) objects
Array Members: Maximum number of 40 items.
Required: No

 ** Values **   <a name="QS-Type-PivotTableAggregatedFieldWells-Values"></a>
The values field well for a pivot table. Values are aggregated based on rows and columns fields.
Type: Array of [MeasureField](API_MeasureField.md) objects
Array Members: Maximum number of 40 items.
Required: No

## See Also
<a name="API_PivotTableAggregatedFieldWells_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/PivotTableAggregatedFieldWells)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/PivotTableAggregatedFieldWells)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/PivotTableAggregatedFieldWells)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
