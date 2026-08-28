---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_LogicalTable.html
---

# LogicalTable
<a name="API_LogicalTable"></a>

A *logical table* is a unit that joins and that data transformations operate on. A logical table has a source, which can be either a physical table or result of a join. When a logical table points to a physical table, the logical table acts as a mutable copy of that physical table through transform operations.

## Contents
<a name="API_LogicalTable_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Alias **   <a name="QS-Type-LogicalTable-Alias"></a>
A display name for the logical table.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** Source **   <a name="QS-Type-LogicalTable-Source"></a>
Source of this logical table.
Type: [LogicalTableSource](API_LogicalTableSource.md) object
Required: Yes

 ** DataTransforms **   <a name="QS-Type-LogicalTable-DataTransforms"></a>
Transform operations that act on this logical table. For this structure to be valid, only one of the attributes can be non-null.
Type: Array of [TransformOperation](API_TransformOperation.md) objects
Array Members: Minimum number of 1 item. Maximum number of 2048 items.
Required: No

## See Also
<a name="API_LogicalTable_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/LogicalTable)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/LogicalTable)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/LogicalTable)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
