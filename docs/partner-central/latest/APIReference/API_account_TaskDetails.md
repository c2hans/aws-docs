---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_account_TaskDetails.html
---

# TaskDetails
<a name="API_account_TaskDetails"></a>

Contains detailed information about a profile update task including the changes to be made.

## Contents
<a name="API_account_TaskDetails_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Description **   <a name="AWSPartnerCentral-Type-account_TaskDetails-Description"></a>
The updated description for the partner profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 600.
Pattern: `[\u0020-\u007E\u00A0-\uD7FF\uE000-\uFFFD]+`
Required: Yes

 ** DisplayName **   <a name="AWSPartnerCentral-Type-account_TaskDetails-DisplayName"></a>
The updated display name for the partner profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 80.
Pattern: `[\u0020-\u007E\u00A0-\uD7FF\uE000-\uFFFD]+`
Required: Yes

 ** IndustrySegments **   <a name="AWSPartnerCentral-Type-account_TaskDetails-IndustrySegments"></a>
The updated industry segments for the partner profile.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 3 items.
Valid Values: `AGRICULTURE_MINING | BIOTECHNOLOGY | BUSINESS_CONSUMER_SERVICES | BUSINESS_SERV | COMMUNICATIONS | COMPUTER_HARDWARE | COMPUTERS_ELECTRONICS | COMPUTER_SOFTWARE | CONSUMER_GOODS | CONSUMER_RELATED | EDUCATION | ENERGY_UTILITIES | FINANCIAL_SERVICES | GAMING | GOVERNMENT | GOVERNMENT_EDUCATION_PUBLIC_SERVICES | HEALTHCARE | HEALTHCARE_PHARMACEUTICALS_BIOTECH | INDUSTRIAL_ENERGY | INTERNET_SPECIFIC | LIFE_SCIENCES | MANUFACTURING | MEDIA_ENTERTAINMENT_LEISURE | MEDIA_ENTERTAINMENT | MEDICAL_HEALTH | NON_PROFIT_ORGANIZATION | OTHER | PROFESSIONAL_SERVICES | REAL_ESTATE_CONSTRUCTION | RETAIL | RETAIL_WHOLESALE_DISTRIBUTION | SEMICONDUCTOR_ELECTR | SOFTWARE_INTERNET | TELECOMMUNICATIONS | TRANSPORTATION_LOGISTICS | TRAVEL_HOSPITALITY | WHOLESALE_DISTRIBUTION`
Required: Yes

 ** LogoUrl **   <a name="AWSPartnerCentral-Type-account_TaskDetails-LogoUrl"></a>
The updated logo URL for the partner profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `(https|HTTPS):\/\/[^\/\s]+(\/\S*)?`
Required: Yes

 ** PrimarySolutionType **   <a name="AWSPartnerCentral-Type-account_TaskDetails-PrimarySolutionType"></a>
The updated primary solution type for the partner profile.
Type: String
Valid Values: `SOFTWARE_PRODUCTS | CONSULTING_SERVICES | PROFESSIONAL_SERVICES | MANAGED_SERVICES | HARDWARE_PRODUCTS | COMMUNICATION_SERVICES | VALUE_ADDED_RESALE_AWS_SERVICES | TRAINING_SERVICES`
Required: Yes

 ** TranslationSourceLocale **   <a name="AWSPartnerCentral-Type-account_TaskDetails-TranslationSourceLocale"></a>
The updated translation source locale for the partner profile.
Type: String
Pattern: `[a-z]{2}-[A-Z]{2}`
Required: Yes

 ** WebsiteUrl **   <a name="AWSPartnerCentral-Type-account_TaskDetails-WebsiteUrl"></a>
The updated website URL for the partner profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `(https|HTTPS):\/\/[^\/\s]+(\/\S*)?`
Required: Yes

 ** Headquarters **   <a name="AWSPartnerCentral-Type-account_TaskDetails-Headquarters"></a>
The ISO 3166 country and subdivision codes for the partner's headquarters location. If you omit this field, the service retains the existing headquarters value.
Type: [Headquarters](API_account_Headquarters.md) object
Required: No

 ** LocalizedContents **   <a name="AWSPartnerCentral-Type-account_TaskDetails-LocalizedContents"></a>
The updated localized content for the partner profile.
Type: Array of [LocalizedContent](API_account_LocalizedContent.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Required: No

## See Also
<a name="API_account_TaskDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-account-2025-04-04/TaskDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-account-2025-04-04/TaskDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-account-2025-04-04/TaskDetails)
