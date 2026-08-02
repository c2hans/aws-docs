---
source_url: https://docs.aws.amazon.com/b2bi/latest/APIReference/API_PartnershipSummary.html
---

# PartnershipSummary
<a name="API_PartnershipSummary"></a>

A structure that contains the details for a partnership. A partnership represents the connection between you and your trading partner. It ties together a profile and one or more trading capabilities.

## Contents
<a name="API_PartnershipSummary_Contents"></a>

 ** createdAt **   <a name="b2bi-Type-PartnershipSummary-createdAt"></a>
Returns a timestamp for creation date and time of the partnership.
Type: Timestamp
Required: Yes

 ** partnershipId **   <a name="b2bi-Type-PartnershipSummary-partnershipId"></a>
Returns the unique, system-generated identifier for a partnership.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

 ** profileId **   <a name="b2bi-Type-PartnershipSummary-profileId"></a>
Returns the unique, system-generated identifier for the profile connected to this partnership.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

 ** capabilities **   <a name="b2bi-Type-PartnershipSummary-capabilities"></a>
Returns one or more capabilities associated with this partnership.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`
Required: No

 ** capabilityOptions **   <a name="b2bi-Type-PartnershipSummary-capabilityOptions"></a>
Contains the details for an Outbound EDI capability.
Type: [CapabilityOptions](API_CapabilityOptions.md) object
Required: No

 ** modifiedAt **   <a name="b2bi-Type-PartnershipSummary-modifiedAt"></a>
Returns a timestamp that identifies the most recent date and time that the partnership was modified.
Type: Timestamp
Required: No

 ** name **   <a name="b2bi-Type-PartnershipSummary-name"></a>
Returns the name of the partnership.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 254.
Required: No

 ** tradingPartnerId **   <a name="b2bi-Type-PartnershipSummary-tradingPartnerId"></a>
Returns the unique, system-generated identifier for a trading partner.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`
Required: No

## See Also
<a name="API_PartnershipSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/b2bi-2022-06-23/PartnershipSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/b2bi-2022-06-23/PartnershipSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/b2bi-2022-06-23/PartnershipSummary)
