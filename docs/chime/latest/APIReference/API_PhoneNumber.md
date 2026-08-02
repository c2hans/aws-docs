---
source_url: https://docs.aws.amazon.com/chime/latest/APIReference/API_PhoneNumber.html
---

**End of support notice**: On February 20, 2026, AWS will end support for the Amazon Chime service. After February 20, 2026, you will no longer be able to access the Amazon Chime console or Amazon Chime application resources. For more information, visit the [blog post](https://aws.amazon.com/blogs/messaging-and-targeting/update-on-support-for-amazon-chime/). **Note:** This does not impact the availability of the [Amazon Chime SDK service](https://aws.amazon.com/chime/chime-sdk/).

# PhoneNumber
<a name="API_PhoneNumber"></a>

A phone number used for Amazon Chime Business Calling or an Amazon Chime Voice Connector.

## Contents
<a name="API_PhoneNumber_Contents"></a>

 ** Associations **   <a name="chime-Type-PhoneNumber-Associations"></a>
The phone number associations.
Type: Array of [PhoneNumberAssociation](API_PhoneNumberAssociation.md) objects
Required: No

 ** CallingName **   <a name="chime-Type-PhoneNumber-CallingName"></a>
The outbound calling name associated with the phone number.
Type: String
Pattern: `^$|^[a-zA-Z0-9 ]{2,15}$`
Required: No

 ** CallingNameStatus **   <a name="chime-Type-PhoneNumber-CallingNameStatus"></a>
The outbound calling name status.
Type: String
Valid Values: `Unassigned | UpdateInProgress | UpdateSucceeded | UpdateFailed`
Required: No

 ** Capabilities **   <a name="chime-Type-PhoneNumber-Capabilities"></a>
The phone number capabilities.
Type: [PhoneNumberCapabilities](API_PhoneNumberCapabilities.md) object
Required: No

 ** Country **   <a name="chime-Type-PhoneNumber-Country"></a>
The phone number country. Format: ISO 3166-1 alpha-2.
Type: String
Pattern: `[A-Z]{2}`
Required: No

 ** CreatedTimestamp **   <a name="chime-Type-PhoneNumber-CreatedTimestamp"></a>
The phone number creation timestamp, in ISO 8601 format.
Type: Timestamp
Required: No

 ** DeletionTimestamp **   <a name="chime-Type-PhoneNumber-DeletionTimestamp"></a>
The deleted phone number timestamp, in ISO 8601 format.
Type: Timestamp
Required: No

 ** E164PhoneNumber **   <a name="chime-Type-PhoneNumber-E164PhoneNumber"></a>
The phone number, in E.164 format.
Type: String
Pattern: `^\+?[1-9]\d{1,14}$`
Required: No

 ** PhoneNumberId **   <a name="chime-Type-PhoneNumber-PhoneNumberId"></a>
The phone number ID.
Type: String
Required: No

 ** ProductType **   <a name="chime-Type-PhoneNumber-ProductType"></a>
The phone number product type.
Type: String
Valid Values: `BusinessCalling | VoiceConnector | SipMediaApplicationDialIn`
Required: No

 ** Status **   <a name="chime-Type-PhoneNumber-Status"></a>
The phone number status.
Type: String
Valid Values: `AcquireInProgress | AcquireFailed | Unassigned | Assigned | ReleaseInProgress | DeleteInProgress | ReleaseFailed | DeleteFailed`
Required: No

 ** Type **   <a name="chime-Type-PhoneNumber-Type"></a>
The phone number type.
Type: String
Valid Values: `Local | TollFree`
Required: No

 ** UpdatedTimestamp **   <a name="chime-Type-PhoneNumber-UpdatedTimestamp"></a>
The updated phone number timestamp, in ISO 8601 format.
Type: Timestamp
Required: No

## See Also
<a name="API_PhoneNumber_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-2018-05-01/PhoneNumber)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-2018-05-01/PhoneNumber)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-2018-05-01/PhoneNumber)
