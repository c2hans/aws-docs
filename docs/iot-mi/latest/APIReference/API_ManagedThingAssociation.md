---
source_url: https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_ManagedThingAssociation.html
---

# ManagedThingAssociation
<a name="API_ManagedThingAssociation"></a>

Structure representing an association between a managed thing and an account association, which connects a device to a third-party account.

## Contents
<a name="API_ManagedThingAssociation_Contents"></a>

 ** AccountAssociationId **   <a name="managedintegrations-Type-ManagedThingAssociation-AccountAssociationId"></a>
The identifier of the account association in the association.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-zA-Z]+`
Required: No

 ** ManagedThingAssociationStatus **   <a name="managedintegrations-Type-ManagedThingAssociation-ManagedThingAssociationStatus"></a>
The status of the registration between the managed thing and the account association. Indicates whether the device is pre-associated or fully associated with the account association.
Type: String
Valid Values: `PRE_ASSOCIATED | ASSOCIATED`
Required: No

 ** ManagedThingId **   <a name="managedintegrations-Type-ManagedThingAssociation-ManagedThingId"></a>
The identifier of the managed thing in the association.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9:_-]*`
Required: No

## See Also
<a name="API_ManagedThingAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-managed-integrations-2025-03-03/ManagedThingAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-managed-integrations-2025-03-03/ManagedThingAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-managed-integrations-2025-03-03/ManagedThingAssociation)
