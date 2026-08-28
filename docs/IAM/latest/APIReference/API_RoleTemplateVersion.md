---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_RoleTemplateVersion.html
---

# RoleTemplateVersion
<a name="API_RoleTemplateVersion"></a>

Contains information about a version of an IAM role template, including the configuration that is used to create roles with [AcquireRole](https://docs.aws.amazon.com/IAM/latest/APIReference/API_AcquireRole.html). This structure is returned as a response element by the [GetRoleTemplateVersion](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetRoleTemplateVersion.html) operation.

## Contents
<a name="API_RoleTemplateVersion_Contents"></a>

 ** AssumeRolePolicyDocumentTemplate **
The trust policy template that grants an entity permission to assume roles that you create from this template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 131072.
Pattern: `[\u0009\u000A\u000D\u0020-\u00FF]+`
Required: No

 ** CreateTimestamp **
The date and time, in [ISO 8601 date-time format](http://www.iso.org/iso/iso8601), when the role template version was created.
Type: Timestamp
Required: No

 ** DefaultMinorVersion **
The minor version that the service uses by default when you create a role from this template without specifying a minor version.
Type: Integer
Required: No

 ** Description **
The description of the role template.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `[\u0009\u000A\u000D\u0020-\u007E\u00A1-\u00FF]*`
Required: No

 ** Enabled **
Specifies whether the role template is enabled. When a template is disabled, you cannot create roles from it.
Type: Boolean
Required: No

 ** InlinePolicyTemplates.member.N **
A list of inline policy templates that the service embeds in roles that you create from this template.
Type: Array of [InlinePolicy](API_InlinePolicy.md) objects
Required: No

 ** MajorVersion **
The major version number of the role template.
Type: Integer
Required: No

 ** ManagedByType **
Indicates that the role template is managed by an AWS service.
Type: String
Valid Values: `Service`
Required: No

 ** ManagedByValue **
The identifier of the AWS service that manages the role template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** ManagedPolicyArns.member.N **
A list of the ARNs of the managed policies that the service attaches to roles that you create from this template.
Type: Array of strings
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: No

 ** MaxSessionDuration **
The maximum session duration (in seconds) for roles that are created from this template.
Type: Integer
Valid Range: Minimum value of 3600. Maximum value of 43200.
Required: No

 ** MinorVersion **
The minor version number of this role template version.
Type: Integer
Required: No

 ** ParametersDefinition.member.N **
A list of the parameters that are defined for this role template version. You supply values for these parameters when you create a role with [AcquireRole](https://docs.aws.amazon.com/IAM/latest/APIReference/API_AcquireRole.html).
Type: Array of [ParameterDefinition](API_ParameterDefinition.md) objects
Required: No

 ** PermissionBoundaryArn **
The ARN of the policy that sets the permissions boundary for roles that you create from this template.
For more information about ARNs, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference*.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: No

 ** RoleDescriptionPattern **
The pattern that is used to generate the description of a role that is created from this template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

 ** RoleNamePattern **
The pattern that is used to generate the name of a role that is created from this template. The pattern can include `@{parameter}` placeholders that are replaced with the values you supply in the `ReplacementValues` parameter of [AcquireRole](https://docs.aws.amazon.com/IAM/latest/APIReference/API_AcquireRole.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** RolePathPattern **
The pattern that is used to generate the path of a role that is created from this template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `/[\u0009\u000A\u000D\u0020-\u007E\u00A1-\u00FF]*/`
Required: No

 ** RoleTagsTemplate.member.N **
A list of tag templates that are applied to roles that are created from this template.
Type: Array of [TagTemplate](API_TagTemplate.md) objects
Array Members: Maximum number of 50 items.
Required: No

 ** TemplateArn **
The Amazon Resource Name (ARN) that identifies the role template.
For more information about ARNs, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference*.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: No

 ** TemplateName **
The friendly name that identifies the role template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w+=,.\-]+`
Required: No

 ** TemplateVersionId **
The identifier of the role template version.
Type: String
Length Constraints: Minimum length of 16. Maximum length of 128.
Pattern: `[\w]+`
Required: No

 ** UpdateTimestamp **
The date and time, in [ISO 8601 date-time format](http://www.iso.org/iso/iso8601), when the role template version was last updated.
Type: Timestamp
Required: No

 ** VersionEnabled **
Specifies whether this specific minor version of the role template is enabled.
Type: Boolean
Required: No

## See Also
<a name="API_RoleTemplateVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/RoleTemplateVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/RoleTemplateVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/RoleTemplateVersion)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Identity and Access Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query IAM` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
