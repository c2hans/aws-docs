---
source_url: https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_ToolConfiguration.html
---

# ToolConfiguration
<a name="API_amazon-q-connect_ToolConfiguration"></a>

Configuration settings for a tool used by AI Agents.

## Contents
<a name="API_amazon-q-connect_ToolConfiguration_Contents"></a>

 ** toolName **   <a name="connect-Type-amazon-q-connect_ToolConfiguration-toolName"></a>
The name of the tool.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: Yes

 ** toolType **   <a name="connect-Type-amazon-q-connect_ToolConfiguration-toolType"></a>
The type of the tool.
Type: String
Valid Values: `MODEL_CONTEXT_PROTOCOL | RETURN_TO_CONTROL | CONSTANT`
Required: Yes

 ** annotations **   <a name="connect-Type-amazon-q-connect_ToolConfiguration-annotations"></a>
Annotations for the tool configuration.
Type: [Annotation](API_amazon-q-connect_Annotation.md) object
Required: No

 ** description **   <a name="connect-Type-amazon-q-connect_ToolConfiguration-description"></a>
The description of the tool configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

 ** inputSchema **   <a name="connect-Type-amazon-q-connect_ToolConfiguration-inputSchema"></a>
The input schema for the tool configuration.
Type: JSON value
Required: No

 ** instruction **   <a name="connect-Type-amazon-q-connect_ToolConfiguration-instruction"></a>
Instructions for using the tool.
Type: [ToolInstruction](API_amazon-q-connect_ToolInstruction.md) object
Required: No

 ** outputFilters **   <a name="connect-Type-amazon-q-connect_ToolConfiguration-outputFilters"></a>
Output filters applies to the tool result.
Type: Array of [ToolOutputFilter](API_amazon-q-connect_ToolOutputFilter.md) objects
Required: No

 ** outputSchema **   <a name="connect-Type-amazon-q-connect_ToolConfiguration-outputSchema"></a>
The output schema for the tool configuration.
Type: JSON value
Required: No

 ** overrideInputValues **   <a name="connect-Type-amazon-q-connect_ToolConfiguration-overrideInputValues"></a>
Override input values for the tool configuration.
Type: Array of [ToolOverrideInputValue](API_amazon-q-connect_ToolOverrideInputValue.md) objects
Required: No

 ** title **   <a name="connect-Type-amazon-q-connect_ToolConfiguration-title"></a>
The title of the tool configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

 ** toolId **   <a name="connect-Type-amazon-q-connect_ToolConfiguration-toolId"></a>
The identifier of the tool, for example toolName from Model Context Provider server.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

 ** userInteractionConfiguration **   <a name="connect-Type-amazon-q-connect_ToolConfiguration-userInteractionConfiguration"></a>
Configuration for user interaction with the tool.
Type: [UserInteractionConfiguration](API_amazon-q-connect_UserInteractionConfiguration.md) object
Required: No

## See Also
<a name="API_amazon-q-connect_ToolConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/ToolConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/ToolConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/ToolConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
