---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_CustomerAccountData.html
---

# CustomerAccountData

The customer information that you provide for a customer account, such as the company name, website, and address. We use these details to match the account to a customer.

## Contents
<a name="API_CustomerAccountData_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** CompanyName **   <a name="AWSPartnerCentral-Type-CustomerAccountData-CompanyName"></a>
The name of the customer company.
Type: String
Pattern: `(?s).{0,120}`
Required: Yes

 ** Address **   <a name="AWSPartnerCentral-Type-CustomerAccountData-Address"></a>
The address of the customer company.
Type: [Address](API_Address.md) object
Required: No

 ** Domain **   <a name="AWSPartnerCentral-Type-CustomerAccountData-Domain"></a>
The internet domain of the customer company, such as `example.com`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 253.
Required: No

 ** Duns **   <a name="AWSPartnerCentral-Type-CustomerAccountData-Duns"></a>
The Data Universal Numbering System (DUNS) number of the customer company.
Type: String
Pattern: `[0-9]{9}`
Required: No

 ** Industry **   <a name="AWSPartnerCentral-Type-CustomerAccountData-Industry"></a>
The industry of the customer company.
Type: String
Required: No

 ** OtherIndustry **   <a name="AWSPartnerCentral-Type-CustomerAccountData-OtherIndustry"></a>
A description of the industry, used when the industry is `Other`.
Type: String
Pattern: `(?s).{0,255}`
Required: No

 ** ParentCompanyName **   <a name="AWSPartnerCentral-Type-CustomerAccountData-ParentCompanyName"></a>
The name of the parent company of the customer company, if any.
Type: String
Pattern: `(?s).{0,120}`
Required: No

 ** WebsiteUrl **   <a name="AWSPartnerCentral-Type-CustomerAccountData-WebsiteUrl"></a>
The website URL of the customer company.
Type: String
Pattern: `(?s).{4,255}`
Required: No

## See Also
<a name="API_CustomerAccountData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/CustomerAccountData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/CustomerAccountData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/CustomerAccountData)
