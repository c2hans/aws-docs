---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_account_PartnerSummary.html
---

# PartnerSummary
<a name="API_account_PartnerSummary"></a>

A summary view of a partner account containing basic information for listing purposes.

## Contents
<a name="API_account_PartnerSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Arn **   <a name="AWSPartnerCentral-Type-account_PartnerSummary-Arn"></a>
The Amazon Resource Name (ARN) of the partner account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `arn:[a-z-]+:partnercentral:[a-z0-9-]+:[0-9]{12}:catalog/[A-Za-z-_]+/partner/partner-[A-Za-z0-9]{13}`
Required: Yes

 ** Catalog **   <a name="AWSPartnerCentral-Type-account_PartnerSummary-Catalog"></a>
The catalog identifier for the partner account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9-]+`
Required: Yes

 ** CreatedAt **   <a name="AWSPartnerCentral-Type-account_PartnerSummary-CreatedAt"></a>
The timestamp when the partner account was created.
Type: Timestamp
Required: Yes

 ** Id **   <a name="AWSPartnerCentral-Type-account_PartnerSummary-Id"></a>
The unique identifier of the partner account.
Type: String
Pattern: `partner-[A-Za-z0-9]{13}`
Required: Yes

 ** LegalName **   <a name="AWSPartnerCentral-Type-account_PartnerSummary-LegalName"></a>
The legal name of the partner organization.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 80.
Pattern: `[\u0020-\u007E\u00A0-\uD7FF\uE000-\uFFFD]+`
Required: Yes

## See Also
<a name="API_account_PartnerSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-account-2025-04-04/PartnerSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-account-2025-04-04/PartnerSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-account-2025-04-04/PartnerSummary)
