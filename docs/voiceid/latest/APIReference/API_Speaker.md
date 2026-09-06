---
source_url: https://docs.aws.amazon.com/voiceid/latest/APIReference/API_Speaker.html
---

# Speaker
<a name="API_connect-voice-id_Speaker"></a>

**Important**
End of support notice: On May 20, 2026, AWS will end support for Connect Customer Voice ID. After May 20, 2026, you will no longer be able to access Voice ID on the Connect Customer console, access Voice ID features on the Connect Customer admin website or Contact Control Panel, or access Voice ID resources. For more information, visit [ Connect Customer Voice ID end of support](https://docs.aws.amazon.com/connect/latest/adminguide/amazonconnect-voiceid-end-of-support.html).

Contains all the information about a speaker.

## Contents
<a name="API_connect-voice-id_Speaker_Contents"></a>

 ** CreatedAt **   <a name="connect-Type-connect-voice-id_Speaker-CreatedAt"></a>
A timestamp of when the speaker was created.
Type: Timestamp
Required: No

 ** CustomerSpeakerId **   <a name="connect-Type-connect-voice-id_Speaker-CustomerSpeakerId"></a>
The client-provided identifier for the speaker.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_-]*`
Required: No

 ** DomainId **   <a name="connect-Type-connect-voice-id_Speaker-DomainId"></a>
The identifier of the domain that contains the speaker.
Type: String
Length Constraints: Fixed length of 22.
Pattern: `[a-zA-Z0-9]{22}`
Required: No

 ** GeneratedSpeakerId **   <a name="connect-Type-connect-voice-id_Speaker-GeneratedSpeakerId"></a>
The service-generated identifier for the speaker.
Type: String
Length Constraints: Fixed length of 25.
Pattern: `id#[a-zA-Z0-9]{22}`
Required: No

 ** LastAccessedAt **   <a name="connect-Type-connect-voice-id_Speaker-LastAccessedAt"></a>
The timestamp of when the speaker was last accessed for enrollment, re-enrollment or a successful authentication. This timestamp is accurate to one hour.
Type: Timestamp
Required: No

 ** Status **   <a name="connect-Type-connect-voice-id_Speaker-Status"></a>
The current status of the speaker.
Type: String
Valid Values: `ENROLLED | EXPIRED | OPTED_OUT | PENDING`
Required: No

 ** UpdatedAt **   <a name="connect-Type-connect-voice-id_Speaker-UpdatedAt"></a>
A timestamp of the speaker's last update.
Type: Timestamp
Required: No

## See Also
<a name="API_connect-voice-id_Speaker_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/voice-id-2021-09-27/Speaker)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/voice-id-2021-09-27/Speaker)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/voice-id-2021-09-27/Speaker)
