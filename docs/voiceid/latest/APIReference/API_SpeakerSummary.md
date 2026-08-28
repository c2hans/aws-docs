---
source_url: https://docs.aws.amazon.com/voiceid/latest/APIReference/API_SpeakerSummary.html
---

# SpeakerSummary
<a name="API_connect-voice-id_SpeakerSummary"></a>

**Important**
End of support notice: On May 20, 2026, AWS will end support for Connect Customer Voice ID. After May 20, 2026, you will no longer be able to access Voice ID on the Connect Customer console, access Voice ID features on the Connect Customer admin website or Contact Control Panel, or access Voice ID resources. For more information, visit [ Connect Customer Voice ID end of support](https://docs.aws.amazon.com/connect/latest/adminguide/amazonconnect-voiceid-end-of-support.html).

Contains a summary of information about a speaker.

## Contents
<a name="API_connect-voice-id_SpeakerSummary_Contents"></a>

 ** CreatedAt **   <a name="connect-Type-connect-voice-id_SpeakerSummary-CreatedAt"></a>
A timestamp showing the speaker's creation time.
Type: Timestamp
Required: No

 ** CustomerSpeakerId **   <a name="connect-Type-connect-voice-id_SpeakerSummary-CustomerSpeakerId"></a>
The client-provided identifier for the speaker.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_-]*`
Required: No

 ** DomainId **   <a name="connect-Type-connect-voice-id_SpeakerSummary-DomainId"></a>
The identifier of the domain that contains the speaker.
Type: String
Length Constraints: Fixed length of 22.
Pattern: `[a-zA-Z0-9]{22}`
Required: No

 ** GeneratedSpeakerId **   <a name="connect-Type-connect-voice-id_SpeakerSummary-GeneratedSpeakerId"></a>
The service-generated identifier for the speaker.
Type: String
Length Constraints: Fixed length of 25.
Pattern: `id#[a-zA-Z0-9]{22}`
Required: No

 ** LastAccessedAt **   <a name="connect-Type-connect-voice-id_SpeakerSummary-LastAccessedAt"></a>
The timestamp when the speaker was last accessed for enrollment, re-enrollment or a successful authentication. This timestamp is accurate to one hour.
Type: Timestamp
Required: No

 ** Status **   <a name="connect-Type-connect-voice-id_SpeakerSummary-Status"></a>
The current status of the speaker.
Type: String
Valid Values: `ENROLLED | EXPIRED | OPTED_OUT | PENDING`
Required: No

 ** UpdatedAt **   <a name="connect-Type-connect-voice-id_SpeakerSummary-UpdatedAt"></a>
A timestamp showing the speaker's last update.
Type: Timestamp
Required: No

## See Also
<a name="API_connect-voice-id_SpeakerSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/voice-id-2021-09-27/SpeakerSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/voice-id-2021-09-27/SpeakerSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/voice-id-2021-09-27/SpeakerSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
