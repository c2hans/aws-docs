---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_ParticipantTokenCredentials.html
---

# ParticipantTokenCredentials
<a name="API_ParticipantTokenCredentials"></a>

The credentials used by the participant.

## Contents
<a name="API_ParticipantTokenCredentials_Contents"></a>

 ** Expiry **   <a name="connect-Type-ParticipantTokenCredentials-Expiry"></a>
The expiration of the token. It's specified in ISO 8601 format: yyyy-MM-ddThh:mm:ss.SSSZ. For example, 2019-11-08T02:41:28.172Z.
Type: String
Required: No

 ** ParticipantToken **   <a name="connect-Type-ParticipantTokenCredentials-ParticipantToken"></a>
The token used by the chat participant to call [CreateParticipantConnection](https://docs.aws.amazon.com/connect-participant/latest/APIReference/API_CreateParticipantConnection.html). The participant token is valid for the lifetime of a chat participant.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Required: No

## See Also
<a name="API_ParticipantTokenCredentials_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/ParticipantTokenCredentials)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/ParticipantTokenCredentials)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/ParticipantTokenCredentials)
