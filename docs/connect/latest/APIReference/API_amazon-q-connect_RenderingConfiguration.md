---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_RenderingConfiguration.html
---

# RenderingConfiguration
<a name="API_amazon-q-connect_RenderingConfiguration"></a>

Information about how to render the content.

## Contents
<a name="API_amazon-q-connect_RenderingConfiguration_Contents"></a>

 ** templateUri **   <a name="connect-Type-amazon-q-connect_RenderingConfiguration-templateUri"></a>
A URI template containing exactly one variable in `${variableName} `format. This can only be set for `EXTERNAL` knowledge bases. For Salesforce, ServiceNow, and Zendesk, the variable must be one of the following:
+ Salesforce: `Id`, `ArticleNumber`, `VersionNumber`, `Title`, `PublishStatus`, or `IsDeleted`
+ ServiceNow: `number`, `short_description`, `sys_mod_count`, `workflow_state`, or `active`
+ Zendesk: `id`, `title`, `updated_at`, or `draft`
The variable is replaced with the actual value for a piece of content when calling [GetContent](https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_GetContent.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

## See Also
<a name="API_amazon-q-connect_RenderingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/RenderingConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/RenderingConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/RenderingConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
