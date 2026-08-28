---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DynamicDefaultValue.html
---

# DynamicDefaultValue
<a name="API_DynamicDefaultValue"></a>

Defines different defaults to the users or groups based on mapping.

## Contents
<a name="API_DynamicDefaultValue_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** DefaultValueColumn **   <a name="QS-Type-DynamicDefaultValue-DefaultValueColumn"></a>
The column that contains the default value of each user or group.
Type: [ColumnIdentifier](API_ColumnIdentifier.md) object
Required: Yes

 ** GroupNameColumn **   <a name="QS-Type-DynamicDefaultValue-GroupNameColumn"></a>
The column that contains the group name.
Type: [ColumnIdentifier](API_ColumnIdentifier.md) object
Required: No

 ** UserNameColumn **   <a name="QS-Type-DynamicDefaultValue-UserNameColumn"></a>
The column that contains the username.
Type: [ColumnIdentifier](API_ColumnIdentifier.md) object
Required: No

## See Also
<a name="API_DynamicDefaultValue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/DynamicDefaultValue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/DynamicDefaultValue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/DynamicDefaultValue)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
