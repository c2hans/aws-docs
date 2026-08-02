---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_account_LocalizedContent.html
---

# LocalizedContent
<a name="API_account_LocalizedContent"></a>

Contains localized content for a partner profile in a specific language or locale.

## Contents
<a name="API_account_LocalizedContent_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Description **   <a name="AWSPartnerCentral-Type-account_LocalizedContent-Description"></a>
The localized description of the partner's business and services.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 600.
Pattern: `[\u0020-\u007E\u00A0-\uD7FF\uE000-\uFFFD]+`
Required: Yes

 ** DisplayName **   <a name="AWSPartnerCentral-Type-account_LocalizedContent-DisplayName"></a>
The localized display name for the partner.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 80.
Pattern: `[\u0020-\u007E\u00A0-\uD7FF\uE000-\uFFFD]+`
Required: Yes

 ** Locale **   <a name="AWSPartnerCentral-Type-account_LocalizedContent-Locale"></a>
The locale or language code for the localized content.
Type: String
Pattern: `[a-z]{2}-[A-Z]{2}`
Required: Yes

 ** LogoUrl **   <a name="AWSPartnerCentral-Type-account_LocalizedContent-LogoUrl"></a>
The URL to the partner's logo image for this locale.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `(https|HTTPS):\/\/[^\/\s]+(\/\S*)?`
Required: Yes

 ** WebsiteUrl **   <a name="AWSPartnerCentral-Type-account_LocalizedContent-WebsiteUrl"></a>
The localized website URL for the partner.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `(https|HTTPS):\/\/[^\/\s]+(\/\S*)?`
Required: Yes

## See Also
<a name="API_account_LocalizedContent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-account-2025-04-04/LocalizedContent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-account-2025-04-04/LocalizedContent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-account-2025-04-04/LocalizedContent)
