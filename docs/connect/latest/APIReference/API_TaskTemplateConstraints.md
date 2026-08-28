---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_TaskTemplateConstraints.html
---

# TaskTemplateConstraints
<a name="API_TaskTemplateConstraints"></a>

Describes constraints that apply to the template fields.

## Contents
<a name="API_TaskTemplateConstraints_Contents"></a>

 ** InvisibleFields **   <a name="connect-Type-TaskTemplateConstraints-InvisibleFields"></a>
Lists the fields that are invisible to agents.
Type: Array of [InvisibleFieldInfo](API_InvisibleFieldInfo.md) objects
Required: No

 ** ReadOnlyFields **   <a name="connect-Type-TaskTemplateConstraints-ReadOnlyFields"></a>
Lists the fields that are read-only to agents, and cannot be edited.
Type: Array of [ReadOnlyFieldInfo](API_ReadOnlyFieldInfo.md) objects
Required: No

 ** RequiredFields **   <a name="connect-Type-TaskTemplateConstraints-RequiredFields"></a>
Lists the fields that are required to be filled by agents.
Type: Array of [RequiredFieldInfo](API_RequiredFieldInfo.md) objects
Required: No

## See Also
<a name="API_TaskTemplateConstraints_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/TaskTemplateConstraints)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/TaskTemplateConstraints)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/TaskTemplateConstraints)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
