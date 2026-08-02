---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_account_PartnerDomain.html
---

# PartnerDomain
<a name="API_account_PartnerDomain"></a>

Represents a verified domain associated with a partner account.

## Contents
<a name="API_account_PartnerDomain_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** DomainName **   <a name="AWSPartnerCentral-Type-account_PartnerDomain-DomainName"></a>
The domain name that has been verified for the partner account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 253.
Pattern: `[a-zA-Z0-9]([a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(\.[a-zA-Z0-9]([a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*`
Required: Yes

 ** RegisteredAt **   <a name="AWSPartnerCentral-Type-account_PartnerDomain-RegisteredAt"></a>
The timestamp when the domain was registered and verified for the partner account.
Type: Timestamp
Required: Yes

## See Also
<a name="API_account_PartnerDomain_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-account-2025-04-04/PartnerDomain)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-account-2025-04-04/PartnerDomain)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-account-2025-04-04/PartnerDomain)
