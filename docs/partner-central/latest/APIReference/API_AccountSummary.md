---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_AccountSummary.html
---

# AccountSummary
<a name="API_AccountSummary"></a>

An object that contains an `Account`'s subset of fields.

## Contents
<a name="API_AccountSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** CompanyName **   <a name="AWSPartnerCentral-Type-AccountSummary-CompanyName"></a>
Specifies the end `Customer`'s company name associated with the `Opportunity`.
Type: String
Pattern: `(?s).{0,120}`
Required: Yes

 ** Address **   <a name="AWSPartnerCentral-Type-AccountSummary-Address"></a>
Specifies the end `Customer`'s address details associated with the `Opportunity`.
Type: [AddressSummary](API_AddressSummary.md) object
Required: No

 ** Industry **   <a name="AWSPartnerCentral-Type-AccountSummary-Industry"></a>
Specifies which industry the end `Customer` belongs to associated with the `Opportunity`. It refers to the category or sector that the customer's business operates in.
To submit a value outside the picklist, use `Other`.
Conditionally mandatory if `Other` is selected for Industry Vertical in LOVs.
Type: String
Valid Values: `Aerospace | Agriculture | Automotive | Computers and Electronics | Consumer Goods | Education | Energy - Oil and Gas | Energy - Power and Utilities | Financial Services | Gaming | Government | Healthcare | Hospitality | Life Sciences | Manufacturing | Marketing and Advertising | Media and Entertainment | Mining | Non-Profit Organization | Professional Services | Real Estate and Construction | Retail | Software and Internet | Telecommunications | Transportation and Logistics | Travel | Wholesale and Distribution | Other`
Required: No

 ** OtherIndustry **   <a name="AWSPartnerCentral-Type-AccountSummary-OtherIndustry"></a>
Specifies the end `Customer`'s industry associated with the ` Opportunity`, when the selected value in the `Industry` field is `Other`. This field is relevant when the customer's industry doesn't fall under the predefined picklist values and requires a custom description.
Type: String
Pattern: `(?s).{0,255}`
Required: No

 ** WebsiteUrl **   <a name="AWSPartnerCentral-Type-AccountSummary-WebsiteUrl"></a>
Specifies the end customer's company website URL associated with the `Opportunity`. This value is crucial to map the customer within the AWS CRM system.
Type: String
Pattern: `(?s).{4,255}`
Required: No

## See Also
<a name="API_AccountSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/AccountSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/AccountSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/AccountSummary)
