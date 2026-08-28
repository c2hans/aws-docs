---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_account_PartnerProfile.html
---

# PartnerProfile
<a name="API_account_PartnerProfile"></a>

Contains comprehensive profile information for a partner including public-facing details.

## Contents
<a name="API_account_PartnerProfile_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Description **   <a name="AWSPartnerCentral-Type-account_PartnerProfile-Description"></a>
A description of the partner's business, services, and capabilities.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 600.
Pattern: `[\u0020-\u007E\u00A0-\uD7FF\uE000-\uFFFD]+`
Required: Yes

 ** DisplayName **   <a name="AWSPartnerCentral-Type-account_PartnerProfile-DisplayName"></a>
The public display name for the partner organization.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 80.
Pattern: `[\u0020-\u007E\u00A0-\uD7FF\uE000-\uFFFD]+`
Required: Yes

 ** IndustrySegments **   <a name="AWSPartnerCentral-Type-account_PartnerProfile-IndustrySegments"></a>
The industry segments or verticals that the partner serves.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 3 items.
Valid Values: `AGRICULTURE_MINING | BIOTECHNOLOGY | BUSINESS_CONSUMER_SERVICES | BUSINESS_SERV | COMMUNICATIONS | COMPUTER_HARDWARE | COMPUTERS_ELECTRONICS | COMPUTER_SOFTWARE | CONSUMER_GOODS | CONSUMER_RELATED | EDUCATION | ENERGY_UTILITIES | FINANCIAL_SERVICES | GAMING | GOVERNMENT | GOVERNMENT_EDUCATION_PUBLIC_SERVICES | HEALTHCARE | HEALTHCARE_PHARMACEUTICALS_BIOTECH | INDUSTRIAL_ENERGY | INTERNET_SPECIFIC | LIFE_SCIENCES | MANUFACTURING | MEDIA_ENTERTAINMENT_LEISURE | MEDIA_ENTERTAINMENT | MEDICAL_HEALTH | NON_PROFIT_ORGANIZATION | OTHER | PROFESSIONAL_SERVICES | REAL_ESTATE_CONSTRUCTION | RETAIL | RETAIL_WHOLESALE_DISTRIBUTION | SEMICONDUCTOR_ELECTR | SOFTWARE_INTERNET | TELECOMMUNICATIONS | TRANSPORTATION_LOGISTICS | TRAVEL_HOSPITALITY | WHOLESALE_DISTRIBUTION`
Required: Yes

 ** LogoUrl **   <a name="AWSPartnerCentral-Type-account_PartnerProfile-LogoUrl"></a>
The URL to the partner's logo image.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `(https|HTTPS):\/\/[^\/\s]+(\/\S*)?`
Required: Yes

 ** PrimarySolutionType **   <a name="AWSPartnerCentral-Type-account_PartnerProfile-PrimarySolutionType"></a>
The primary type of solution or service the partner provides.
Type: String
Valid Values: `SOFTWARE_PRODUCTS | CONSULTING_SERVICES | PROFESSIONAL_SERVICES | MANAGED_SERVICES | HARDWARE_PRODUCTS | COMMUNICATION_SERVICES | VALUE_ADDED_RESALE_AWS_SERVICES | TRAINING_SERVICES`
Required: Yes

 ** TranslationSourceLocale **   <a name="AWSPartnerCentral-Type-account_PartnerProfile-TranslationSourceLocale"></a>
The source locale used for automatic translation of profile content.
Type: String
Pattern: `[a-z]{2}-[A-Z]{2}`
Required: Yes

 ** WebsiteUrl **   <a name="AWSPartnerCentral-Type-account_PartnerProfile-WebsiteUrl"></a>
The partner's primary website URL.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `(https|HTTPS):\/\/[^\/\s]+(\/\S*)?`
Required: Yes

 ** Headquarters **   <a name="AWSPartnerCentral-Type-account_PartnerProfile-Headquarters"></a>
The ISO 3166 country and subdivision codes for the partner's headquarters location. If no headquarters location is set, this field is not included in the response.
Type: [Headquarters](API_account_Headquarters.md) object
Required: No

 ** LocalizedContents **   <a name="AWSPartnerCentral-Type-account_PartnerProfile-LocalizedContents"></a>
A list of localized content versions for different languages and regions.
Type: Array of [LocalizedContent](API_account_LocalizedContent.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Required: No

 ** ProfileId **   <a name="AWSPartnerCentral-Type-account_PartnerProfile-ProfileId"></a>
The unique identifier of the partner profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `pprofile-[A-Za-z0-9]{13}`
Required: No

## See Also
<a name="API_account_PartnerProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-account-2025-04-04/PartnerProfile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-account-2025-04-04/PartnerProfile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-account-2025-04-04/PartnerProfile)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Partner Central. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query partner-central` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
