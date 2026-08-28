---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DataSetStringFilterCondition.html
---

# DataSetStringFilterCondition
<a name="API_DataSetStringFilterCondition"></a>

A filter condition for string columns, supporting both comparison and list-based filtering.

## Contents
<a name="API_DataSetStringFilterCondition_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ColumnName **   <a name="QS-Type-DataSetStringFilterCondition-ColumnName"></a>
The name of the string column to filter.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** ComparisonFilterCondition **   <a name="QS-Type-DataSetStringFilterCondition-ComparisonFilterCondition"></a>
A comparison-based filter condition for the string column.
Type: [DataSetStringComparisonFilterCondition](API_DataSetStringComparisonFilterCondition.md) object
Required: No

 ** ListFilterCondition **   <a name="QS-Type-DataSetStringFilterCondition-ListFilterCondition"></a>
A list-based filter condition that includes or excludes values from a specified list.
Type: [DataSetStringListFilterCondition](API_DataSetStringListFilterCondition.md) object
Required: No

## See Also
<a name="API_DataSetStringFilterCondition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/DataSetStringFilterCondition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/DataSetStringFilterCondition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/DataSetStringFilterCondition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
