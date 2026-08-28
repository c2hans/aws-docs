---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_TaskTemplateMetadata.html
---

# TaskTemplateMetadata
<a name="API_TaskTemplateMetadata"></a>

Contains summary information about the task template.

## Contents
<a name="API_TaskTemplateMetadata_Contents"></a>

 ** Arn **   <a name="connect-Type-TaskTemplateMetadata-Arn"></a>
The Amazon Resource Name (ARN) of the task template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: No

 ** CreatedTime **   <a name="connect-Type-TaskTemplateMetadata-CreatedTime"></a>
The timestamp when the task template was created.
Type: Timestamp
Required: No

 ** Description **   <a name="connect-Type-TaskTemplateMetadata-Description"></a>
The description of the task template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** Id **   <a name="connect-Type-TaskTemplateMetadata-Id"></a>
A unique identifier for the task template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: No

 ** LastModifiedTime **   <a name="connect-Type-TaskTemplateMetadata-LastModifiedTime"></a>
The timestamp when the task template was last modified.
Type: Timestamp
Required: No

 ** Name **   <a name="connect-Type-TaskTemplateMetadata-Name"></a>
The name of the task template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** Status **   <a name="connect-Type-TaskTemplateMetadata-Status"></a>
Marks a template as `ACTIVE` or `INACTIVE` for a task to refer to it. Tasks can only be created from `ACTIVE` templates. If a template is marked as `INACTIVE`, then a task that refers to this template cannot be created.
Type: String
Valid Values: `ACTIVE | INACTIVE`
Required: No

## See Also
<a name="API_TaskTemplateMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/TaskTemplateMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/TaskTemplateMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/TaskTemplateMetadata)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
