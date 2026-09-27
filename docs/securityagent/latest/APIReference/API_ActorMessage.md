---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_ActorMessage.html
---

# ActorMessage
<a name="API_ActorMessage"></a>

A message received at an actor's server-generated email MFA address.

## Contents
<a name="API_ActorMessage_Contents"></a>

 ** body **   <a name="securityagent-Type-ActorMessage-body"></a>
The plain-text body of the message, containing the MFA code or verification link.
Type: String
Required: No

 ** receivedAt **   <a name="securityagent-Type-ActorMessage-receivedAt"></a>
The time the message was received.
Type: Timestamp
Required: No

 ** sender **   <a name="securityagent-Type-ActorMessage-sender"></a>
The address the message was sent from.
Type: String
Required: No

 ** subject **   <a name="securityagent-Type-ActorMessage-subject"></a>
The subject line of the message.
Type: String
Required: No

## See Also
<a name="API_ActorMessage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/ActorMessage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/ActorMessage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/ActorMessage)
