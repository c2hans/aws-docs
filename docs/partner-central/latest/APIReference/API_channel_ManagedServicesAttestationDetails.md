---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_channel_ManagedServicesAttestationDetails.html
---

# ManagedServicesAttestationDetails

Details specific to managed services attestation channel contracts. Applies only to managed services attestation channel contracts.

## Contents
<a name="API_channel_ManagedServicesAttestationDetails_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** endDate **   <a name="AWSPartnerCentral-Type-channel_ManagedServicesAttestationDetails-endDate"></a>
The end date of the managed services attestation.
Type: Timestamp
Required: Yes

 ** legalEntityName **   <a name="AWSPartnerCentral-Type-channel_ManagedServicesAttestationDetails-legalEntityName"></a>
The legal name of the end customer's legal entity.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Pattern: `[^\x00-\x1F\x7F]*`
Required: Yes

 ** programManagementAccountIdentifier **   <a name="AWSPartnerCentral-Type-channel_ManagedServicesAttestationDetails-programManagementAccountIdentifier"></a>
The identifier of the program management account.
Type: String
Length Constraints: Minimum length of 17. Maximum length of 1011.
Pattern: `(arn:[a-z-]+:partnercentral:[a-z0-9-]+:[0-9]{12}:catalog/[a-zA-Z]+/program-management-account/)?pma-[a-z0-9]{13}`
Required: Yes

 ** relationshipIdentifier **   <a name="AWSPartnerCentral-Type-channel_ManagedServicesAttestationDetails-relationshipIdentifier"></a>
The identifier of the relationship covered by the attestation.
Type: String
Length Constraints: Minimum length of 16. Maximum length of 1011.
Pattern: `(arn:[a-z-]+:partnercentral:[a-z0-9-]+:[0-9]{12}:catalog/[a-zA-Z]+/program-management-account/pma-[a-z0-9]{13}/relationship/)?rs-[a-z0-9]{13}`
Required: Yes

 ** signatoryEmail **   <a name="AWSPartnerCentral-Type-channel_ManagedServicesAttestationDetails-signatoryEmail"></a>
The email address of the signatory.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^\s@]+@[^\s@]+\.[^\s@]+`
Required: Yes

 ** signatoryName **   <a name="AWSPartnerCentral-Type-channel_ManagedServicesAttestationDetails-signatoryName"></a>
The name of the person who signs the attestation for the end customer.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^\x00-\x1F\x7F]*`
Required: Yes

 ** supportedServices **   <a name="AWSPartnerCentral-Type-channel_ManagedServicesAttestationDetails-supportedServices"></a>
The managed services that the partner provides to the end customer.
Type: Array of strings
Valid Values: `MONITORING | PATCHING | SECURITY | BACKUP_AND_DISASTER_RECOVERY | FINANCIAL_OPERATIONS | INFRASTRUCTURE_AS_CODE_AND_AUTOMATION | WELL_ARCHITECTED | ARTIFICIAL_INTELLIGENCE_AND_MACHINE_LEARNING_OPERATIONS`
Required: Yes

 ** legalEntityAddress **   <a name="AWSPartnerCentral-Type-channel_ManagedServicesAttestationDetails-legalEntityAddress"></a>
The address of the end customer's legal entity, if available.
Type: [Address](API_channel_Address.md) object
Required: No

 ** memberAccountIds **   <a name="AWSPartnerCentral-Type-channel_ManagedServicesAttestationDetails-memberAccountIds"></a>
The AWS account IDs of the end customer's member accounts covered by the managed services.
Type: Array of strings
Length Constraints: Fixed length of 12.
Pattern: `[0-9]*`
Required: No

## See Also
<a name="API_channel_ManagedServicesAttestationDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-channel-2024-03-18/ManagedServicesAttestationDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-channel-2024-03-18/ManagedServicesAttestationDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-channel-2024-03-18/ManagedServicesAttestationDetails)
