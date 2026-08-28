---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_TableFieldOptions.html
---

# TableFieldOptions
<a name="API_TableFieldOptions"></a>

The field options of a table visual.

## Contents
<a name="API_TableFieldOptions_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Order **   <a name="QS-Type-TableFieldOptions-Order"></a>
The order of the field IDs that are configured as field options for a table visual.
Type: Array of strings
Array Members: Maximum number of 200 items.
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

 ** PinnedFieldOptions **   <a name="QS-Type-TableFieldOptions-PinnedFieldOptions"></a>
The settings for the pinned columns of a table visual.
Type: [TablePinnedFieldOptions](API_TablePinnedFieldOptions.md) object
Required: No

 ** SelectedFieldOptions **   <a name="QS-Type-TableFieldOptions-SelectedFieldOptions"></a>
The field options to be configured to a table.
Type: Array of [TableFieldOption](API_TableFieldOption.md) objects
Array Members: Maximum number of 201 items.
Required: No

 ** TransposedTableOptions **   <a name="QS-Type-TableFieldOptions-TransposedTableOptions"></a>
The `TableOptions` of a transposed table.
Type: Array of [TransposedTableOption](API_TransposedTableOption.md) objects
Array Members: Maximum number of 10001 items.
Required: No

## See Also
<a name="API_TableFieldOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/TableFieldOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/TableFieldOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/TableFieldOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
