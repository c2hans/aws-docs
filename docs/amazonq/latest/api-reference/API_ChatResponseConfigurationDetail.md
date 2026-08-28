---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ChatResponseConfigurationDetail.html
---

# ChatResponseConfigurationDetail
<a name="API_ChatResponseConfigurationDetail"></a>

Detailed information about a chat response configuration, including comprehensive settings and parameters that define how Amazon Q Business generates and formats responses.

## Contents
<a name="API_ChatResponseConfigurationDetail_Contents"></a>

 ** error **   <a name="qbusiness-Type-ChatResponseConfigurationDetail-error"></a>
Provides information about a Amazon Q Business request error.
Type: [ErrorDetail](API_ErrorDetail.md) object
Required: No

 ** responseConfigurations **   <a name="qbusiness-Type-ChatResponseConfigurationDetail-responseConfigurations"></a>
A collection of specific response configuration settings that collectively define how responses are generated, formatted, and presented to users in chat interactions.
Type: String to [ResponseConfiguration](API_ResponseConfiguration.md) object map
Map Entries: Maximum number of 1 item.
Valid Keys: `ALL`
Required: No

 ** responseConfigurationSummary **   <a name="qbusiness-Type-ChatResponseConfigurationDetail-responseConfigurationSummary"></a>
A summary of the response configuration details, providing a concise overview of the key parameters and settings that define the response generation behavior.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** status **   <a name="qbusiness-Type-ChatResponseConfigurationDetail-status"></a>
The current status of the chat response configuration, indicating whether it is active, pending, or in another state that affects its availability for use.
Type: String
Valid Values: `CREATING | UPDATING | FAILED | ACTIVE`
Required: No

 ** updatedAt **   <a name="qbusiness-Type-ChatResponseConfigurationDetail-updatedAt"></a>
The timestamp indicating when the detailed chat response configuration was last modified, helping administrators track changes and maintain version awareness.
Type: Timestamp
Required: No

## See Also
<a name="API_ChatResponseConfigurationDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/ChatResponseConfigurationDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/ChatResponseConfigurationDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/ChatResponseConfigurationDetail)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q Business. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
