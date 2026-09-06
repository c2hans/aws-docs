---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_PhoneNumberAssociation.html
---

# PhoneNumberAssociation
<a name="API_voice-chime_PhoneNumberAssociation"></a>

The phone number associations, such as an Amazon Chime SDK account ID, user ID, Voice Connector ID, or Voice Connector group ID.

## Contents
<a name="API_voice-chime_PhoneNumberAssociation_Contents"></a>

 ** AssociatedTimestamp **   <a name="chimesdk-Type-voice-chime_PhoneNumberAssociation-AssociatedTimestamp"></a>
The timestamp of the phone number association, in ISO 8601 format.
Type: Timestamp
Required: No

 ** Name **   <a name="chimesdk-Type-voice-chime_PhoneNumberAssociation-Name"></a>
Defines the association with an Amazon Chime SDK account ID, user ID, Voice Connector ID, or Voice Connector group ID.
Type: String
Valid Values: `VoiceConnectorId | VoiceConnectorGroupId | SipRuleId`
Required: No

 ** Value **   <a name="chimesdk-Type-voice-chime_PhoneNumberAssociation-Value"></a>
Contains the ID for the entity specified in Name.
Type: String
Required: No

## See Also
<a name="API_voice-chime_PhoneNumberAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-voice-2022-08-03/PhoneNumberAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-voice-2022-08-03/PhoneNumberAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-voice-2022-08-03/PhoneNumberAssociation)
