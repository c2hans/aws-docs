---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_PivotOperation.html
---

# PivotOperation
<a name="API_PivotOperation"></a>

A transform operation that pivots data by converting row values into columns.

## Contents
<a name="API_PivotOperation_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Alias **   <a name="QS-Type-PivotOperation-Alias"></a>
Alias for this operation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** PivotConfiguration **   <a name="QS-Type-PivotOperation-PivotConfiguration"></a>
Configuration that specifies which labels to pivot and how to structure the resulting columns.
Type: [PivotConfiguration](API_PivotConfiguration.md) object
Required: Yes

 ** Source **   <a name="QS-Type-PivotOperation-Source"></a>
The source transform operation that provides input data for pivoting.
Type: [TransformOperationSource](API_TransformOperationSource.md) object
Required: Yes

 ** ValueColumnConfiguration **   <a name="QS-Type-PivotOperation-ValueColumnConfiguration"></a>
Configuration for how to aggregate values when multiple rows map to the same pivoted column.
Type: [ValueColumnConfiguration](API_ValueColumnConfiguration.md) object
Required: Yes

 ** GroupByColumnNames **   <a name="QS-Type-PivotOperation-GroupByColumnNames"></a>
The list of column names to group by when performing the pivot operation.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 128 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

## See Also
<a name="API_PivotOperation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/PivotOperation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/PivotOperation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/PivotOperation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
