---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_SupportedAssociation.html
---

# SupportedAssociation
<a name="API_SupportedAssociation"></a>

The processing rules for when a registration can be associated with an origination identity and disassociated from an origination identity.

## Contents
<a name="API_SupportedAssociation_Contents"></a>

 ** AssociationBehavior **   <a name="pinpoint-Type-SupportedAssociation-AssociationBehavior"></a>
The association behavior.
+  `ASSOCIATE_BEFORE_SUBMIT` The origination identity has to be supplied when creating a registration.
+  `ASSOCIATE_ON_APPROVAL` This applies to all sender ID registrations. The sender ID will be automatically provisioned once the registration is approved.
+  `ASSOCIATE_AFTER_COMPLETE` This applies to phone number registrations when you must complete a registration first, then associate one or more phone numbers later. For example 10DLC campaigns and long codes.
Type: String
Valid Values: `ASSOCIATE_BEFORE_SUBMIT | ASSOCIATE_ON_APPROVAL | ASSOCIATE_AFTER_COMPLETE`
Required: Yes

 ** DisassociationBehavior **   <a name="pinpoint-Type-SupportedAssociation-DisassociationBehavior"></a>
The disassociation behavior.
+  `DISASSOCIATE_ALL_CLOSES_REGISTRATION` All origination identities must be disassociated from the registration before the registration can be closed.
+  `DISASSOCIATE_ALL_ALLOWS_DELETE_REGISTRATION` All origination identities must be disassociated from the registration before the registration can be deleted.
+  `DELETE_REGISTRATION_DISASSOCIATES` The registration can be deleted and all origination identities will be disasscoiated.
Type: String
Valid Values: `DISASSOCIATE_ALL_CLOSES_REGISTRATION | DISASSOCIATE_ALL_ALLOWS_DELETE_REGISTRATION | DELETE_REGISTRATION_DISASSOCIATES`
Required: Yes

 ** ResourceType **   <a name="pinpoint-Type-SupportedAssociation-ResourceType"></a>
Defines the behavior of when an origination identity and registration can be associated with each other.
Type: String
Required: Yes

 ** IsoCountryCode **   <a name="pinpoint-Type-SupportedAssociation-IsoCountryCode"></a>
The two-character code, in ISO 3166-1 alpha-2 format, for the country or region.
Type: String
Length Constraints: Fixed length of 2.
Pattern: `[A-Z]{2}`
Required: No

## See Also
<a name="API_SupportedAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/SupportedAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/SupportedAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/SupportedAssociation)
