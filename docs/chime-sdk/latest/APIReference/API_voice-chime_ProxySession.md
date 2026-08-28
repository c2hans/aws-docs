---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_ProxySession.html
---

# ProxySession
<a name="API_voice-chime_ProxySession"></a>

The proxy session for an Amazon Chime SDK Voice Connector.

## Contents
<a name="API_voice-chime_ProxySession_Contents"></a>

 ** Capabilities **   <a name="chimesdk-Type-voice-chime_ProxySession-Capabilities"></a>
The proxy session capabilities.
Type: Array of strings
Valid Values: `Voice | SMS`
Required: No

 ** CreatedTimestamp **   <a name="chimesdk-Type-voice-chime_ProxySession-CreatedTimestamp"></a>
The created time stamp, in ISO 8601 format.
Type: Timestamp
Required: No

 ** EndedTimestamp **   <a name="chimesdk-Type-voice-chime_ProxySession-EndedTimestamp"></a>
The ended time stamp, in ISO 8601 format.
Type: Timestamp
Required: No

 ** ExpiryMinutes **   <a name="chimesdk-Type-voice-chime_ProxySession-ExpiryMinutes"></a>
The number of minutes allowed for the proxy session.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** GeoMatchLevel **   <a name="chimesdk-Type-voice-chime_ProxySession-GeoMatchLevel"></a>
The preference for matching the country or area code of the proxy phone number with that of the first participant.
Type: String
Valid Values: `Country | AreaCode`
Required: No

 ** GeoMatchParams **   <a name="chimesdk-Type-voice-chime_ProxySession-GeoMatchParams"></a>
The country and area code for the proxy phone number.
Type: [GeoMatchParams](API_voice-chime_GeoMatchParams.md) object
Required: No

 ** Name **   <a name="chimesdk-Type-voice-chime_ProxySession-Name"></a>
The proxy session name.
Type: String
Length Constraints: Maximum length of 128.
Required: No

 ** NumberSelectionBehavior **   <a name="chimesdk-Type-voice-chime_ProxySession-NumberSelectionBehavior"></a>
The preference for proxy phone number reuse, or stickiness, between the same participants across sessions.
Type: String
Valid Values: `PreferSticky | AvoidSticky`
Required: No

 ** Participants **   <a name="chimesdk-Type-voice-chime_ProxySession-Participants"></a>
The proxy session participants.
Type: Array of [Participant](API_voice-chime_Participant.md) objects
Required: No

 ** ProxySessionId **   <a name="chimesdk-Type-voice-chime_ProxySession-ProxySessionId"></a>
The proxy session ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `.*\S.*`
Required: No

 ** Status **   <a name="chimesdk-Type-voice-chime_ProxySession-Status"></a>
The proxy session status.
Type: String
Valid Values: `Open | InProgress | Closed`
Required: No

 ** UpdatedTimestamp **   <a name="chimesdk-Type-voice-chime_ProxySession-UpdatedTimestamp"></a>
The updated time stamp, in ISO 8601 format.
Type: Timestamp
Required: No

 ** VoiceConnectorId **   <a name="chimesdk-Type-voice-chime_ProxySession-VoiceConnectorId"></a>
The Voice Connector ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_voice-chime_ProxySession_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-voice-2022-08-03/ProxySession)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-voice-2022-08-03/ProxySession)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-voice-2022-08-03/ProxySession)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
