---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_TemplateVersion.html
---

# TemplateVersion
<a name="API_TemplateVersion"></a>

A version of a template.

## Contents
<a name="API_TemplateVersion_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** CreatedTime **   <a name="QS-Type-TemplateVersion-CreatedTime"></a>
The time that this template version was created.
Type: Timestamp
Required: No

 ** DataSetConfigurations **   <a name="QS-Type-TemplateVersion-DataSetConfigurations"></a>
Schema of the dataset identified by the placeholder. Any dashboard created from this template should be bound to new datasets matching the same schema described through this API operation.
Type: Array of [DataSetConfiguration](API_DataSetConfiguration.md) objects
Array Members: Maximum number of 30 items.
Required: No

 ** Description **   <a name="QS-Type-TemplateVersion-Description"></a>
The description of the template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

 ** Errors **   <a name="QS-Type-TemplateVersion-Errors"></a>
Errors associated with this template version.
Type: Array of [TemplateError](API_TemplateError.md) objects
Array Members: Minimum number of 1 item.
Required: No

 ** Sheets **   <a name="QS-Type-TemplateVersion-Sheets"></a>
A list of the associated sheets with the unique identifier and name of each sheet.
Type: Array of [Sheet](API_Sheet.md) objects
Array Members: Maximum number of 20 items.
Required: No

 ** SourceEntityArn **   <a name="QS-Type-TemplateVersion-SourceEntityArn"></a>
The Amazon Resource Name (ARN) of an analysis or template that was used to create this template.
Type: String
Required: No

 ** Status **   <a name="QS-Type-TemplateVersion-Status"></a>
The status that is associated with the template.
+  `CREATION_IN_PROGRESS`
+  `CREATION_SUCCESSFUL`
+  `CREATION_FAILED`
+  `UPDATE_IN_PROGRESS`
+  `UPDATE_SUCCESSFUL`
+  `UPDATE_FAILED`
+  `DELETED`
Type: String
Valid Values: `CREATION_IN_PROGRESS | CREATION_SUCCESSFUL | CREATION_FAILED | UPDATE_IN_PROGRESS | UPDATE_SUCCESSFUL | UPDATE_FAILED | DELETED`
Required: No

 ** ThemeArn **   <a name="QS-Type-TemplateVersion-ThemeArn"></a>
The ARN of the theme associated with this version of the template.
Type: String
Required: No

 ** TopicConfigurations **   <a name="QS-Type-TemplateVersion-TopicConfigurations"></a>
Schema of the topic identified by the placeholder. Any dashboard created from this template should be bound to new topics matching the same schema described through this API operation.
Type: Array of [TopicConfiguration](API_TopicConfiguration.md) objects
Array Members: Maximum number of 30 items.
Required: No

 ** VersionNumber **   <a name="QS-Type-TemplateVersion-VersionNumber"></a>
The version number of the template version.
Type: Long
Valid Range: Minimum value of 1.
Required: No

## See Also
<a name="API_TemplateVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/TemplateVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/TemplateVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/TemplateVersion)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
