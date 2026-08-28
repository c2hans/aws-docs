---
source_url: https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_AIAgentConfigurationData.html
---

# AIAgentConfigurationData
<a name="API_amazon-q-connect_AIAgentConfigurationData"></a>

A type that specifies the AI Agent ID configuration data when mapping an AI Agents to be used for an AI Agent type on a session or assistant.

## Contents
<a name="API_amazon-q-connect_AIAgentConfigurationData_Contents"></a>

 ** aiAgentId **   <a name="connect-Type-amazon-q-connect_AIAgentConfigurationData-aiAgentId"></a>
The ID of the AI Agent to be configured.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(:[A-Z0-9_$]+){0,1}`
Required: Yes

## See Also
<a name="API_amazon-q-connect_AIAgentConfigurationData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/AIAgentConfigurationData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/AIAgentConfigurationData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/AIAgentConfigurationData)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
