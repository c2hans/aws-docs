---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-voice-id_AuthenticationResult.html
---

# AuthenticationResult
<a name="API_connect-voice-id_AuthenticationResult"></a>

**Important**
End of support notice: On May 20, 2026, AWS will end support for Connect Customer Voice ID. After May 20, 2026, you will no longer be able to access Voice ID on the Connect Customer console, access Voice ID features on the Connect Customer admin website or Contact Control Panel, or access Voice ID resources. For more information, visit [ Connect Customer Voice ID end of support](https://docs.aws.amazon.com/connect/latest/adminguide/amazonconnect-voiceid-end-of-support.html).

The authentication result produced by Voice ID, processed against the current session state and streamed audio of the speaker.

## Contents
<a name="API_connect-voice-id_AuthenticationResult_Contents"></a>

 ** AudioAggregationEndedAt **   <a name="connect-Type-connect-voice-id_AuthenticationResult-AudioAggregationEndedAt"></a>
A timestamp of when audio aggregation ended for this authentication result.
Type: Timestamp
Required: No

 ** AudioAggregationStartedAt **   <a name="connect-Type-connect-voice-id_AuthenticationResult-AudioAggregationStartedAt"></a>
A timestamp of when audio aggregation started for this authentication result.
Type: Timestamp
Required: No

 ** AuthenticationResultId **   <a name="connect-Type-connect-voice-id_AuthenticationResult-AuthenticationResultId"></a>
The unique identifier for this authentication result. Because there can be multiple authentications for a given session, this field helps to identify if the returned result is from a previous streaming activity or a new result. Note that in absence of any new streaming activity, `AcceptanceThreshold` changes, or `SpeakerId` changes, Voice ID always returns cached Authentication Result for this API.
Type: String
Length Constraints: Fixed length of 22.
Pattern: `[a-zA-Z0-9]{22}`
Required: No

 ** Configuration **   <a name="connect-Type-connect-voice-id_AuthenticationResult-Configuration"></a>
The `AuthenticationConfiguration` used to generate this authentication result.
Type: [AuthenticationConfiguration](API_connect-voice-id_AuthenticationConfiguration.md) object
Required: No

 ** CustomerSpeakerId **   <a name="connect-Type-connect-voice-id_AuthenticationResult-CustomerSpeakerId"></a>
The client-provided identifier for the speaker whose authentication result is produced. Only present if a `SpeakerId` is provided for the session.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_-]*`
Required: No

 ** Decision **   <a name="connect-Type-connect-voice-id_AuthenticationResult-Decision"></a>
The authentication decision produced by Voice ID, processed against the current session state and streamed audio of the speaker.
Type: String
Valid Values: `ACCEPT | REJECT | NOT_ENOUGH_SPEECH | SPEAKER_NOT_ENROLLED | SPEAKER_OPTED_OUT | SPEAKER_ID_NOT_PROVIDED | SPEAKER_EXPIRED`
Required: No

 ** GeneratedSpeakerId **   <a name="connect-Type-connect-voice-id_AuthenticationResult-GeneratedSpeakerId"></a>
The service-generated identifier for the speaker whose authentication result is produced.
Type: String
Length Constraints: Fixed length of 25.
Pattern: `id#[a-zA-Z0-9]{22}`
Required: No

 ** Score **   <a name="connect-Type-connect-voice-id_AuthenticationResult-Score"></a>
The authentication score for the speaker whose authentication result is produced. This value is only present if the authentication decision is either `ACCEPT` or `REJECT`.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

## See Also
<a name="API_connect-voice-id_AuthenticationResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/voice-id-2021-09-27/AuthenticationResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/voice-id-2021-09-27/AuthenticationResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/voice-id-2021-09-27/AuthenticationResult)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
