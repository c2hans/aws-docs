---
source_url: https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_WhatsAppBusinessAccountEventDestination.html
---

# WhatsAppBusinessAccountEventDestination
<a name="API_WhatsAppBusinessAccountEventDestination"></a>

Contains information on the event destination.

## Contents
<a name="API_WhatsAppBusinessAccountEventDestination_Contents"></a>

 ** eventDestinationArn **   <a name="Social-Type-WhatsAppBusinessAccountEventDestination-eventDestinationArn"></a>
The ARN of the event destination.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:.*:[a-z-]+([/:](.*))?`
Required: Yes

 ** roleArn **   <a name="Social-Type-WhatsAppBusinessAccountEventDestination-roleArn"></a>
The Amazon Resource Name (ARN) of an AWS Identity and Access Management role that is able to import phone numbers and write events.
Type: String
Pattern: `arn:.*:iam::\d{12}:role\/[a-zA-Z0-9+=,.@\-_]+`
Required: No

## See Also
<a name="API_WhatsAppBusinessAccountEventDestination_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/socialmessaging-2024-01-01/WhatsAppBusinessAccountEventDestination)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/socialmessaging-2024-01-01/WhatsAppBusinessAccountEventDestination)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/socialmessaging-2024-01-01/WhatsAppBusinessAccountEventDestination)
