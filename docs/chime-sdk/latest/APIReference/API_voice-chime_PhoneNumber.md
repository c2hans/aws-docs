---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_PhoneNumber.html
---

# PhoneNumber
<a name="API_voice-chime_PhoneNumber"></a>

A phone number used to call an Amazon Chime SDK Voice Connector.

## Contents
<a name="API_voice-chime_PhoneNumber_Contents"></a>

 ** Associations **   <a name="chimesdk-Type-voice-chime_PhoneNumber-Associations"></a>
The phone number's associations.
Type: Array of [PhoneNumberAssociation](API_voice-chime_PhoneNumberAssociation.md) objects
Required: No

 ** CallingName **   <a name="chimesdk-Type-voice-chime_PhoneNumber-CallingName"></a>
The outbound calling name associated with the phone number.
Type: String
Pattern: `^$|^[a-zA-Z0-9 ]{2,15}$`
Required: No

 ** CallingNameStatus **   <a name="chimesdk-Type-voice-chime_PhoneNumber-CallingNameStatus"></a>
The outbound calling name status.
Type: String
Valid Values: `Unassigned | UpdateInProgress | UpdateSucceeded | UpdateFailed`
Required: No

 ** Capabilities **   <a name="chimesdk-Type-voice-chime_PhoneNumber-Capabilities"></a>
The phone number's capabilities.
Type: [PhoneNumberCapabilities](API_voice-chime_PhoneNumberCapabilities.md) object
Required: No

 ** Country **   <a name="chimesdk-Type-voice-chime_PhoneNumber-Country"></a>
The phone number's country. Format: ISO 3166-1 alpha-2.
Type: String
Pattern: `[A-Z]{2}`
Required: No

 ** CreatedTimestamp **   <a name="chimesdk-Type-voice-chime_PhoneNumber-CreatedTimestamp"></a>
The phone number creation timestamp, in ISO 8601 format.
Type: Timestamp
Required: No

 ** DeletionTimestamp **   <a name="chimesdk-Type-voice-chime_PhoneNumber-DeletionTimestamp"></a>
The deleted phone number timestamp, in ISO 8601 format.
Type: Timestamp
Required: No

 ** E164PhoneNumber **   <a name="chimesdk-Type-voice-chime_PhoneNumber-E164PhoneNumber"></a>
The phone number, in E.164 format.
Type: String
Pattern: `^\+?[1-9]\d{1,14}$`
Required: No

 ** Name **   <a name="chimesdk-Type-voice-chime_PhoneNumber-Name"></a>
The name of the phone number.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `^$|^[a-zA-Z0-9\,\.\_\-]+(\s+[a-zA-Z0-9\,\.\_\-]+)*$`
Required: No

 ** OrderId **   <a name="chimesdk-Type-voice-chime_PhoneNumber-OrderId"></a>
The phone number's order ID.
Type: String
Pattern: `[a-fA-F0-9]{8}(?:-[a-fA-F0-9]{4}){3}-[a-fA-F0-9]{12}`
Required: No

 ** PhoneNumberId **   <a name="chimesdk-Type-voice-chime_PhoneNumber-PhoneNumberId"></a>
The phone number's ID.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ProductType **   <a name="chimesdk-Type-voice-chime_PhoneNumber-ProductType"></a>
The phone number's product type.
Type: String
Valid Values: `VoiceConnector | SipMediaApplicationDialIn`
Required: No

 ** Status **   <a name="chimesdk-Type-voice-chime_PhoneNumber-Status"></a>
The phone number's status.
Type: String
Valid Values: `Cancelled | PortinCancelRequested | PortinInProgress | AcquireInProgress | AcquireFailed | Unassigned | Assigned | ReleaseInProgress | DeleteInProgress | ReleaseFailed | DeleteFailed`
Required: No

 ** Type **   <a name="chimesdk-Type-voice-chime_PhoneNumber-Type"></a>
The phone number's type.
Type: String
Valid Values: `Local | TollFree`
Required: No

 ** UpdatedTimestamp **   <a name="chimesdk-Type-voice-chime_PhoneNumber-UpdatedTimestamp"></a>
The updated phone number timestamp, in ISO 8601 format.
Type: Timestamp
Required: No

## See Also
<a name="API_voice-chime_PhoneNumber_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-voice-2022-08-03/PhoneNumber)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-voice-2022-08-03/PhoneNumber)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-voice-2022-08-03/PhoneNumber)
