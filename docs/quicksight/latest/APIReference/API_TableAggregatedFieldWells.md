---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_TableAggregatedFieldWells.html
---

# TableAggregatedFieldWells
<a name="API_TableAggregatedFieldWells"></a>

The aggregated field well for the table.

## Contents
<a name="API_TableAggregatedFieldWells_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** GroupBy **   <a name="QS-Type-TableAggregatedFieldWells-GroupBy"></a>
The group by field well for a pivot table. Values are grouped by group by fields.
Type: Array of [DimensionField](API_DimensionField.md) objects
Array Members: Maximum number of 200 items.
Required: No

 ** Values **   <a name="QS-Type-TableAggregatedFieldWells-Values"></a>
The values field well for a pivot table. Values are aggregated based on group by fields.
Type: Array of [MeasureField](API_MeasureField.md) objects
Array Members: Maximum number of 200 items.
Required: No

## See Also
<a name="API_TableAggregatedFieldWells_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/TableAggregatedFieldWells)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/TableAggregatedFieldWells)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/TableAggregatedFieldWells)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
