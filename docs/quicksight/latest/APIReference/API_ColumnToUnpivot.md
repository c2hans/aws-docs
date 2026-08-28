---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ColumnToUnpivot.html
---

# ColumnToUnpivot
<a name="API_ColumnToUnpivot"></a>

Specifies a column to be unpivoted, transforming it from a column into rows with associated values.

## Contents
<a name="API_ColumnToUnpivot_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ColumnName **   <a name="QS-Type-ColumnToUnpivot-ColumnName"></a>
The name of the column to unpivot from the source data.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** NewValue **   <a name="QS-Type-ColumnToUnpivot-NewValue"></a>
The value to assign to this column in the unpivoted result, typically the column name or a descriptive label.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2047.
Required: No

## See Also
<a name="API_ColumnToUnpivot_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/ColumnToUnpivot)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/ColumnToUnpivot)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/ColumnToUnpivot)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
