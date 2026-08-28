---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_FilterOperationSelectedFieldsConfiguration.html
---

# FilterOperationSelectedFieldsConfiguration
<a name="API_FilterOperationSelectedFieldsConfiguration"></a>

The configuration of selected fields in the`CustomActionFilterOperation`.

This is a union type structure. For this structure to be valid, only one of the attributes can be defined.

## Contents
<a name="API_FilterOperationSelectedFieldsConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** SelectedColumns **   <a name="QS-Type-FilterOperationSelectedFieldsConfiguration-SelectedColumns"></a>
The selected columns of a dataset.
Type: Array of [ColumnIdentifier](API_ColumnIdentifier.md) objects
Array Members: Maximum number of 10 items.
Required: No

 ** SelectedFieldOptions **   <a name="QS-Type-FilterOperationSelectedFieldsConfiguration-SelectedFieldOptions"></a>
A structure that contains the options that choose which fields are filtered in the `CustomActionFilterOperation`.
Valid values are defined as follows:
+  `ALL_FIELDS`: Applies the filter operation to all fields.
Type: String
Valid Values: `ALL_FIELDS`
Required: No

 ** SelectedFields **   <a name="QS-Type-FilterOperationSelectedFieldsConfiguration-SelectedFields"></a>
Chooses the fields that are filtered in `CustomActionFilterOperation`.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

## See Also
<a name="API_FilterOperationSelectedFieldsConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/FilterOperationSelectedFieldsConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/FilterOperationSelectedFieldsConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/FilterOperationSelectedFieldsConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
