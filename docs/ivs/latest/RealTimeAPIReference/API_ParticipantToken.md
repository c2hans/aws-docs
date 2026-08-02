---
source_url: https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_ParticipantToken.html
---

# ParticipantToken
<a name="API_ParticipantToken"></a>

Object specifying a participant token in a stage.

 **Important**: Treat tokens as opaque; i.e., do not build functionality based on token contents. The format of tokens could change in the future.

## Contents
<a name="API_ParticipantToken_Contents"></a>

 ** attributes **   <a name="ivsrealtimeeapireference-Type-ParticipantToken-attributes"></a>
Application-provided attributes to encode into the token and attach to a stage. Map keys and values can contain UTF-8 encoded text. The maximum length of this field is 1 KB total. *This field is exposed to all stage participants and should not be used for personally identifying, confidential, or sensitive information.*
Type: String to string map
Required: No

 ** capabilities **   <a name="ivsrealtimeeapireference-Type-ParticipantToken-capabilities"></a>
Set of capabilities that the user is allowed to perform in the stage.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 2 items.
Valid Values: `PUBLISH | SUBSCRIBE`
Required: No

 ** duration **   <a name="ivsrealtimeeapireference-Type-ParticipantToken-duration"></a>
Duration (in minutes), after which the participant token expires. Default: 720 (12 hours).
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 20160.
Required: No

 ** expirationTime **   <a name="ivsrealtimeeapireference-Type-ParticipantToken-expirationTime"></a>
ISO 8601 timestamp (returned as a string) for when this token expires.
Type: Timestamp
Required: No

 ** participantId **   <a name="ivsrealtimeeapireference-Type-ParticipantToken-participantId"></a>
Unique identifier for this participant token, assigned by IVS.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `[a-zA-Z0-9-_]*`
Required: No

 ** token **   <a name="ivsrealtimeeapireference-Type-ParticipantToken-token"></a>
The issued client token, encrypted.
Type: String
Required: No

 ** userId **   <a name="ivsrealtimeeapireference-Type-ParticipantToken-userId"></a>
Customer-assigned name to help identify the token; this can be used to link a participant to a user in the customer’s own systems. This can be any UTF-8 encoded text. *This field is exposed to all stage participants and should not be used for personally identifying, confidential, or sensitive information.*
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Required: No

## See Also
<a name="API_ParticipantToken_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivs-realtime-2020-07-14/ParticipantToken)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivs-realtime-2020-07-14/ParticipantToken)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivs-realtime-2020-07-14/ParticipantToken)
