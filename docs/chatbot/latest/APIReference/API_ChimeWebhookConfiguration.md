---
source_url: https://docs.aws.amazon.com/chatbot/latest/APIReference/API_ChimeWebhookConfiguration.html
---

# ChimeWebhookConfiguration
<a name="API_ChimeWebhookConfiguration"></a>

An Amazon Q Developer configuration for Amazon Chime.

## Contents
<a name="API_ChimeWebhookConfiguration_Contents"></a>

 ** ChatConfigurationArn **   <a name="qdevinchatapps-Type-ChimeWebhookConfiguration-ChatConfigurationArn"></a>
The Amazon Resource Name (ARN) of the ChimeWebhookConfiguration.
Type: String
Length Constraints: Minimum length of 19. Maximum length of 1169.
Pattern: `arn:aws:(wheatley|chatbot):[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,1023}`
Required: Yes

 ** IamRoleArn **   <a name="qdevinchatapps-Type-ChimeWebhookConfiguration-IamRoleArn"></a>
A user-defined role that Amazon Q Developer assumes. This is not the service-linked role.
For more information, see [IAM policies for Amazon Q Developer](https://docs.aws.amazon.com/chatbot/latest/adminguide/chatbot-iam-policies.html) in the * Amazon Q Developer Administrator Guide*.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 1224.
Pattern: `arn:aws:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,1023}`
Required: Yes

 ** SnsTopicArns **   <a name="qdevinchatapps-Type-ChimeWebhookConfiguration-SnsTopicArns"></a>
The Amazon Resource Names (ARNs) of the SNS topics that deliver notifications to Amazon Q Developer.
Type: Array of strings
Length Constraints: Minimum length of 12. Maximum length of 1224.
Pattern: `arn:aws:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,1023}`
Required: Yes

 ** WebhookDescription **   <a name="qdevinchatapps-Type-ChimeWebhookConfiguration-WebhookDescription"></a>
A description of the webhook. We recommend using the convention `RoomName/WebhookName`.
For more information, see [Tutorial: Get started with Amazon Chime](https://docs.aws.amazon.com/chatbot/latest/adminguide/chime-setup.html) in the * Amazon Q Developer Administrator Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** ConfigurationName **   <a name="qdevinchatapps-Type-ChimeWebhookConfiguration-ConfigurationName"></a>
The name of the configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[A-Za-z0-9-_]+`
Required: No

 ** LoggingLevel **   <a name="qdevinchatapps-Type-ChimeWebhookConfiguration-LoggingLevel"></a>
Logging levels include `ERROR`, `INFO`, or `NONE`.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 5.
Pattern: `(ERROR|INFO|NONE)`
Required: No

 ** State **   <a name="qdevinchatapps-Type-ChimeWebhookConfiguration-State"></a>
Either `ENABLED` or `DISABLED`. The resource returns `DISABLED` if the organization's Amazon Q Developer policy has explicitly denied that configuration. For example, if Amazon Chime is disabled.
Type: String
Pattern: `(ENABLED|DISABLED)`
Required: No

 ** StateReason **   <a name="qdevinchatapps-Type-ChimeWebhookConfiguration-StateReason"></a>
Provided if State is `DISABLED`. Provides context as to why the resource is disabled.
Type: String
Required: No

 ** Tags **   <a name="qdevinchatapps-Type-ChimeWebhookConfiguration-Tags"></a>
A map of tags assigned to a resource. A tag is a string-to-string map of key-value pairs.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## See Also
<a name="API_ChimeWebhookConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chatbot-2017-10-11/ChimeWebhookConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chatbot-2017-10-11/ChimeWebhookConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chatbot-2017-10-11/ChimeWebhookConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q Developer in chat applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chatbot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
