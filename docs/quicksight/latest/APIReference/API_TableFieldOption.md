---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_TableFieldOption.html
---

# TableFieldOption
<a name="API_TableFieldOption"></a>

The options for a table field.

## Contents
<a name="API_TableFieldOption_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** FieldId **   <a name="QS-Type-TableFieldOption-FieldId"></a>
The field ID for a table field.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: Yes

 ** CustomLabel **   <a name="QS-Type-TableFieldOption-CustomLabel"></a>
The custom label for a table field.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** URLStyling **   <a name="QS-Type-TableFieldOption-URLStyling"></a>
The URL configuration for a table field.
Type: [TableFieldURLConfiguration](API_TableFieldURLConfiguration.md) object
Required: No

 ** Visibility **   <a name="QS-Type-TableFieldOption-Visibility"></a>
The visibility of a table field.
Type: String
Valid Values: `HIDDEN | VISIBLE`
Required: No

 ** Width **   <a name="QS-Type-TableFieldOption-Width"></a>
The width for a table field.
Type: String
Required: No

## See Also
<a name="API_TableFieldOption_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/TableFieldOption)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/TableFieldOption)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/TableFieldOption)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
