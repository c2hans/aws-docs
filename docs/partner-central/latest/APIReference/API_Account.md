---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_Account.html
---

# Account
<a name="API_Account"></a>

Specifies the `Customer`'s account details associated with the `Opportunity`.

## Contents
<a name="API_Account_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** CompanyName **   <a name="AWSPartnerCentral-Type-Account-CompanyName"></a>
Specifies the end `Customer`'s company name associated with the `Opportunity`.
Type: String
Pattern: `(?s).{0,120}`
Required: Yes

 ** Address **   <a name="AWSPartnerCentral-Type-Account-Address"></a>
Specifies the end `Customer`'s address details associated with the `Opportunity`.
Type: [Address](API_Address.md) object
Required: No

 ** AwsAccountId **   <a name="AWSPartnerCentral-Type-Account-AwsAccountId"></a>
Specifies the `Customer` AWS account ID associated with the `Opportunity`.
Type: String
Pattern: `([0-9]{12}|\w{1,12})`
Required: No

 ** Duns **   <a name="AWSPartnerCentral-Type-Account-Duns"></a>
Indicates the `Customer` DUNS number, if available.
Type: String
Pattern: `[0-9]{9}`
Required: No

 ** Industry **   <a name="AWSPartnerCentral-Type-Account-Industry"></a>
Specifies the industry the end `Customer` belongs to that's associated with the `Opportunity`. It refers to the category or sector where the customer's business operates. This is a required field.
Type: String
Valid Values: `Aerospace | Agriculture | Automotive | Computers and Electronics | Consumer Goods | Education | Energy - Oil and Gas | Energy - Power and Utilities | Financial Services | Gaming | Government | Healthcare | Hospitality | Life Sciences | Manufacturing | Marketing and Advertising | Media and Entertainment | Mining | Non-Profit Organization | Professional Services | Real Estate and Construction | Retail | Software and Internet | Telecommunications | Transportation and Logistics | Travel | Wholesale and Distribution | Other`
Required: No

 ** OtherIndustry **   <a name="AWSPartnerCentral-Type-Account-OtherIndustry"></a>
Specifies the end `Customer`'s industry associated with the `Opportunity`, when the selected value in the `Industry` field is `Other`.
Type: String
Pattern: `(?s).{0,255}`
Required: No

 ** WebsiteUrl **   <a name="AWSPartnerCentral-Type-Account-WebsiteUrl"></a>
Specifies the end customer's company website URL associated with the `Opportunity`. This value is crucial to map the customer within the AWS CRM system. This field is required in all cases except when the opportunity is related to national security.
Type: String
Pattern: `(?s).{4,255}`
Required: No

## See Also
<a name="API_Account_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/Account)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/Account)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/Account)
