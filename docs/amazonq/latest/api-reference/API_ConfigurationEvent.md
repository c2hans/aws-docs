---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ConfigurationEvent.html
---

# ConfigurationEvent
<a name="API_ConfigurationEvent"></a>

A configuration event activated by an end user request to select a specific chat mode.

## Contents
<a name="API_ConfigurationEvent_Contents"></a>

 ** attributeFilter **   <a name="qbusiness-Type-ConfigurationEvent-attributeFilter"></a>
Enables filtering of responses based on document attributes or metadata fields.
Type: [AttributeFilter](API_AttributeFilter.md) object
Required: No

 ** chatMode **   <a name="qbusiness-Type-ConfigurationEvent-chatMode"></a>
The chat modes available to an Amazon Q Business end user.
+  `RETRIEVAL_MODE` - The default chat mode for an Amazon Q Business application. When this mode is enabled, Amazon Q Business generates responses only from data sources connected to an Amazon Q Business application.
+  `CREATOR_MODE` - By selecting this mode, users can choose to generate responses only from the LLM knowledge, without consulting connected data sources, for a chat request.
+  `PLUGIN_MODE` - By selecting this mode, users can choose to use plugins in chat.
For more information, see [Admin controls and guardrails](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/guardrails.html), [Plugins](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/plugins.html), and [Conversation settings](https://docs.aws.amazon.com/amazonq/latest/business-use-dg/using-web-experience.html#chat-source-scope).
Type: String
Valid Values: `RETRIEVAL_MODE | CREATOR_MODE | PLUGIN_MODE`
Required: No

 ** chatModeConfiguration **   <a name="qbusiness-Type-ConfigurationEvent-chatModeConfiguration"></a>
Configuration information for Amazon Q Business conversation modes.
For more information, see [Admin controls and guardrails](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/guardrails.html) and [Conversation settings](https://docs.aws.amazon.com/amazonq/latest/business-use-dg/using-web-experience.html#chat-source-scope).
Type: [ChatModeConfiguration](API_ChatModeConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## See Also
<a name="API_ConfigurationEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/ConfigurationEvent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/ConfigurationEvent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/ConfigurationEvent)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q Business. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
