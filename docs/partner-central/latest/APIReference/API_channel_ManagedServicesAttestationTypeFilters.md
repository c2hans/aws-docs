---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_channel_ManagedServicesAttestationTypeFilters.html
---

# ManagedServicesAttestationTypeFilters

Filters specific to managed services attestation channel contracts. Applies only to managed services attestation channel contracts.

## Contents
<a name="API_channel_ManagedServicesAttestationTypeFilters_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** legalEntityNames **   <a name="AWSPartnerCentral-Type-channel_ManagedServicesAttestationTypeFilters-legalEntityNames"></a>
Filter by legal entity names.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 300.
Pattern: `[^\x00-\x1F\x7F]*`
Required: No

 ** relationshipIdentifiers **   <a name="AWSPartnerCentral-Type-channel_ManagedServicesAttestationTypeFilters-relationshipIdentifiers"></a>
Filter by relationship identifiers.
Type: Array of strings
Length Constraints: Minimum length of 16. Maximum length of 1011.
Pattern: `(arn:[a-z-]+:partnercentral:[a-z0-9-]+:[0-9]{12}:catalog/[a-zA-Z]+/program-management-account/pma-[a-z0-9]{13}/relationship/)?rs-[a-z0-9]{13}`
Required: No

## See Also
<a name="API_channel_ManagedServicesAttestationTypeFilters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-channel-2024-03-18/ManagedServicesAttestationTypeFilters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-channel-2024-03-18/ManagedServicesAttestationTypeFilters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-channel-2024-03-18/ManagedServicesAttestationTypeFilters)
