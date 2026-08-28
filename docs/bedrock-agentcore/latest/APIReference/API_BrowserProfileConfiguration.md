---
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_BrowserProfileConfiguration.html
---

# BrowserProfileConfiguration
<a name="API_BrowserProfileConfiguration"></a>

The configuration for a browser profile in Amazon Bedrock AgentCore. A browser profile contains persistent browser data such as cookies and local storage that can be saved from one browser session and reused in subsequent sessions. Browser profiles enable continuity for tasks that require authentication, maintain user preferences, or depend on previously stored browser state.

## Contents
<a name="API_BrowserProfileConfiguration_Contents"></a>

 ** profileIdentifier **   <a name="BedrockAgentCore-Type-BrowserProfileConfiguration-profileIdentifier"></a>
The unique identifier of the browser profile. This identifier is used to reference the profile when starting new browser sessions or saving session data to the profile.
Type: String
Pattern: `[a-zA-Z][a-zA-Z0-9_]{0,47}-[a-zA-Z0-9]{10}`
Required: Yes

## See Also
<a name="API_BrowserProfileConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/BrowserProfileConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/BrowserProfileConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/BrowserProfileConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock AgentCore Data Plane. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock-agentcore` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
