---
source_url: https://docs.aws.amazon.com/chime/latest/APIReference/API_PhoneNumberAssociation.html
---

**End of support notice**: On February 20, 2026, AWS will end support for the Amazon Chime service. After February 20, 2026, you will no longer be able to access the Amazon Chime console or Amazon Chime application resources. For more information, visit the [blog post](https://aws.amazon.com/blogs/messaging-and-targeting/update-on-support-for-amazon-chime/). **Note:** This does not impact the availability of the [Amazon Chime SDK service](https://aws.amazon.com/chime/chime-sdk/).

# PhoneNumberAssociation
<a name="API_PhoneNumberAssociation"></a>

The phone number associations, such as Amazon Chime account ID, Amazon Chime user ID, Amazon Chime Voice Connector ID, or Amazon Chime Voice Connector group ID.

## Contents
<a name="API_PhoneNumberAssociation_Contents"></a>

 ** AssociatedTimestamp **   <a name="chime-Type-PhoneNumberAssociation-AssociatedTimestamp"></a>
The timestamp of the phone number association, in ISO 8601 format.
Type: Timestamp
Required: No

 ** Name **   <a name="chime-Type-PhoneNumberAssociation-Name"></a>
Defines the association with an Amazon Chime account ID, user ID, Amazon Chime Voice Connector ID, or Amazon Chime Voice Connector group ID.
Type: String
Valid Values: `AccountId | UserId | VoiceConnectorId | VoiceConnectorGroupId | SipRuleId`
Required: No

 ** Value **   <a name="chime-Type-PhoneNumberAssociation-Value"></a>
Contains the ID for the entity specified in Name.
Type: String
Required: No

## See Also
<a name="API_PhoneNumberAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-2018-05-01/PhoneNumberAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-2018-05-01/PhoneNumberAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-2018-05-01/PhoneNumberAssociation)
