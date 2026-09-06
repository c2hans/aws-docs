---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ChatResponseConfiguration.html
---

# ChatResponseConfiguration
<a name="API_ChatResponseConfiguration"></a>

Configuration details that define how Amazon Q Business generates and formats responses to user queries in chat interactions. This configuration allows administrators to customize response characteristics to meet specific organizational needs and communication standards.

## Contents
<a name="API_ChatResponseConfiguration_Contents"></a>

 ** chatResponseConfigurationArn **   <a name="qbusiness-Type-ChatResponseConfiguration-chatResponseConfigurationArn"></a>
The Amazon Resource Name (ARN) of the chat response configuration, which uniquely identifies the resource across all AWS services and accounts.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1284.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
Required: Yes

 ** chatResponseConfigurationId **   <a name="qbusiness-Type-ChatResponseConfiguration-chatResponseConfigurationId"></a>
A unique identifier for your chat response configuration settings, used to reference and manage the configuration within the Amazon Q Business service.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`
Required: Yes

 ** displayName **   <a name="qbusiness-Type-ChatResponseConfiguration-displayName"></a>
A human-readable name for the chat response configuration, making it easier to identify and manage multiple configurations within an organization.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** status **   <a name="qbusiness-Type-ChatResponseConfiguration-status"></a>
The current status of the chat response configuration, indicating whether it is active, pending, or in another state that affects its availability for use in chat interactions.
Type: String
Valid Values: `CREATING | UPDATING | FAILED | ACTIVE`
Required: Yes

 ** createdAt **   <a name="qbusiness-Type-ChatResponseConfiguration-createdAt"></a>
The timestamp indicating when the chat response configuration was initially created, useful for tracking the lifecycle of configuration resources.
Type: Timestamp
Required: No

 ** responseConfigurationSummary **   <a name="qbusiness-Type-ChatResponseConfiguration-responseConfigurationSummary"></a>
A summary of the response configuration settings, providing a concise overview of the key parameters that define how responses are generated and formatted.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Required: No

 ** updatedAt **   <a name="qbusiness-Type-ChatResponseConfiguration-updatedAt"></a>
The timestamp indicating when the chat response configuration was last modified, helping administrators track changes and maintain version awareness.
Type: Timestamp
Required: No

## See Also
<a name="API_ChatResponseConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/ChatResponseConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/ChatResponseConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/ChatResponseConfiguration)
