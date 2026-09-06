---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_account_PartnerProfileSummary.html
---

# PartnerProfileSummary
<a name="API_account_PartnerProfileSummary"></a>

A summary view of a partner profile containing basic identifying information.

## Contents
<a name="API_account_PartnerProfileSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Id **   <a name="AWSPartnerCentral-Type-account_PartnerProfileSummary-Id"></a>
The unique identifier of the partner profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `pprofile-[A-Za-z0-9]{13}`
Required: Yes

 ** Name **   <a name="AWSPartnerCentral-Type-account_PartnerProfileSummary-Name"></a>
The display name of the partner.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 80.
Pattern: `[\u0020-\u007E\u00A0-\uD7FF\uE000-\uFFFD]+`
Required: Yes

## See Also
<a name="API_account_PartnerProfileSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-account-2025-04-04/PartnerProfileSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-account-2025-04-04/PartnerProfileSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-account-2025-04-04/PartnerProfileSummary)
