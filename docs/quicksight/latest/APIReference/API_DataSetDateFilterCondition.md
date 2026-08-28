---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DataSetDateFilterCondition.html
---

# DataSetDateFilterCondition
<a name="API_DataSetDateFilterCondition"></a>

A filter condition for date columns, supporting both comparison and range-based filtering.

## Contents
<a name="API_DataSetDateFilterCondition_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ColumnName **   <a name="QS-Type-DataSetDateFilterCondition-ColumnName"></a>
The name of the date column to filter.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** ComparisonFilterCondition **   <a name="QS-Type-DataSetDateFilterCondition-ComparisonFilterCondition"></a>
A comparison-based filter condition for the date column.
Type: [DataSetDateComparisonFilterCondition](API_DataSetDateComparisonFilterCondition.md) object
Required: No

 ** RangeFilterCondition **   <a name="QS-Type-DataSetDateFilterCondition-RangeFilterCondition"></a>
A range-based filter condition for the date column, filtering values between minimum and maximum dates.
Type: [DataSetDateRangeFilterCondition](API_DataSetDateRangeFilterCondition.md) object
Required: No

## See Also
<a name="API_DataSetDateFilterCondition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/DataSetDateFilterCondition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/DataSetDateFilterCondition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/DataSetDateFilterCondition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
